import os
import sys
import time
import asyncio
import logging
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from apify_client import ApifyClientAsync
from dotenv import load_dotenv

# Load env variables from .env if present
load_dotenv()

# Configure logging to go to stderr so it doesn't pollute stdout (which is used for JSON-RPC)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr
)
logger = logging.getLogger("apify-mcp")

# Initialize FastMCP
mcp = FastMCP("Apify")

def get_client() -> ApifyClientAsync:
    """Retrieve and initialize the ApifyClientAsync with the API token."""
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        logger.error("APIFY_TOKEN is missing from the environment.")
        raise ValueError(
            "APIFY_TOKEN environment variable is not set. Please set it in your environment or a local .env file. "
            "You can generate/retrieve your token from your Apify Console: https://console.apify.com/account/integrations"
        )
    return ApifyClientAsync(token)

@mcp.tool()
async def run_actor(
    actor_id: str,
    run_input: Optional[Dict[str, Any]] = None,
    wait_limit_seconds: int = 300
) -> Dict[str, Any]:
    """
    Run an Apify Actor and wait for it to complete (up to wait_limit_seconds).
    
    Args:
        actor_id: The ID or name of the actor to run (e.g., 'apify/web-scraper', 'apify/google-maps-scraper').
        run_input: A dictionary of configuration options (input payload) for the actor.
        wait_limit_seconds: Max seconds to wait for the run to complete. Default is 300. Set to 0 to run asynchronously and return immediately.
        
    Returns:
        A dictionary containing the status of the run, and if completed successfully, the dataset items.
    """
    logger.info(f"Starting actor '{actor_id}'...")
    client = get_client()
    
    # 1. Start the Actor run
    try:
        run = await client.actor(actor_id).start(run_input=run_input)
    except Exception as e:
        logger.exception(f"Failed to start actor '{actor_id}'")
        return {
            "success": False,
            "error": f"Failed to start actor '{actor_id}': {str(e)}"
        }
        
    run_id = run.get("id")
    dataset_id = run.get("defaultDatasetId")
    logger.info(f"Actor run started. Run ID: {run_id}, Default Dataset ID: {dataset_id}")
    
    if wait_limit_seconds <= 0:
        return {
            "success": True,
            "status": run.get("status"),
            "run_id": run_id,
            "dataset_id": dataset_id,
            "message": "Actor run started asynchronously."
        }
        
    # 2. Poll for completion
    start_time = time.time()
    logger.info(f"Waiting for run '{run_id}' to complete (timeout: {wait_limit_seconds}s)...")
    while True:
        try:
            run_status = await client.run(run_id).get()
        except Exception as e:
            logger.exception(f"Error checking status for run '{run_id}'")
            return {
                "success": False,
                "error": f"Failed to fetch status for run '{run_id}': {str(e)}",
                "run_id": run_id,
                "dataset_id": dataset_id
            }
            
        if not run_status:
            return {
                "success": False,
                "error": f"Run '{run_id}' not found.",
                "run_id": run_id,
                "dataset_id": dataset_id
            }
            
        status = run_status.get("status")
        logger.info(f"Run '{run_id}' is in status: {status}")
        
        if status in ["SUCCEEDED", "FAILED", "TIMED-OUT", "ABORTED"]:
            break
            
        elapsed = time.time() - start_time
        if elapsed >= wait_limit_seconds:
            logger.warning(f"Run '{run_id}' did not complete within {wait_limit_seconds}s.")
            return {
                "success": True,
                "status": status,
                "run_id": run_id,
                "dataset_id": dataset_id,
                "message": f"Actor run is still in status '{status}' after waiting {wait_limit_seconds} seconds. You can retrieve results later."
            }
            
        # Poll interval: wait 5 seconds
        await asyncio.sleep(5)
        
    # 3. Handle results
    if status == "SUCCEEDED":
        logger.info(f"Run '{run_id}' succeeded. Fetching dataset items...")
        try:
            dataset_list = await client.dataset(dataset_id).list_items(limit=100)
            items = dataset_list.items
            return {
                "success": True,
                "status": status,
                "run_id": run_id,
                "dataset_id": dataset_id,
                "item_count": len(items),
                "items": items
            }
        except Exception as e:
            logger.exception(f"Error fetching dataset '{dataset_id}' for run '{run_id}'")
            return {
                "success": True,
                "status": status,
                "run_id": run_id,
                "dataset_id": dataset_id,
                "error_fetching_dataset": str(e),
                "message": "Actor run succeeded, but failed to retrieve dataset items."
            }
    else:
        logger.error(f"Run '{run_id}' finished with non-successful status: {status}")
        return {
            "success": False,
            "status": status,
            "run_id": run_id,
            "dataset_id": dataset_id,
            "message": f"Actor run finished with status '{status}'."
        }

@mcp.tool()
async def get_dataset_items(
    dataset_id: str,
    limit: int = 100,
    offset: int = 0,
    clean: bool = True
) -> Dict[str, Any]:
    """
    Retrieve items from an Apify dataset.
    
    Args:
        dataset_id: The ID of the dataset to fetch.
        limit: The maximum number of items to retrieve (default: 100).
        offset: The number of items to skip (default: 0).
        clean: If True, cleans up internal Apify metadata fields (starting with '#') to save context space.
        
    Returns:
        A dictionary with the items and pagination metadata.
    """
    logger.info(f"Fetching dataset items for dataset '{dataset_id}' (limit={limit}, offset={offset})...")
    client = get_client()
    try:
        page = await client.dataset(dataset_id).list_items(limit=limit, offset=offset)
        items = page.items
        
        if clean:
            cleaned_items = []
            for item in items:
                # Remove keys starting with '#'
                cleaned_item = {k: v for k, v in item.items() if not k.startswith('#')}
                cleaned_item.pop('__metadata__', None)
                cleaned_items.append(cleaned_item)
            items = cleaned_items
            
        return {
            "success": True,
            "items": items,
            "count": page.count,
            "total": page.total,
            "offset": page.offset,
            "limit": page.limit
        }
    except Exception as e:
        logger.exception(f"Failed to retrieve dataset items from '{dataset_id}'")
        return {
            "success": False,
            "error": f"Failed to retrieve dataset items: {str(e)}"
        }

@mcp.tool()
async def get_run_status(run_id: str) -> Dict[str, Any]:
    """
    Check the status and metadata of a specific Actor run.
    
    Args:
        run_id: The ID of the run to check.
        
    Returns:
        Run metadata including current status, start/finish times, usage, and associated resource IDs.
    """
    logger.info(f"Fetching run status for run '{run_id}'...")
    client = get_client()
    try:
        run = await client.run(run_id).get()
        if not run:
            return {"success": False, "error": f"Run '{run_id}' not found."}
            
        return {
            "success": True,
            "run_id": run.get("id"),
            "actor_id": run.get("actId"),
            "status": run.get("status"),
            "started_at": run.get("startedAt"),
            "finished_at": run.get("finishedAt"),
            "default_dataset_id": run.get("defaultDatasetId"),
            "default_key_value_store_id": run.get("defaultKeyValueStoreId"),
            "usage_usd": run.get("usageUsd"),
            "build_id": run.get("buildId"),
            "exit_code": run.get("exitCode")
        }
    except Exception as e:
        logger.exception(f"Failed to get run status for run '{run_id}'")
        return {
            "success": False,
            "error": f"Failed to get run status: {str(e)}"
        }

@mcp.tool()
async def get_key_value_store_record(
    store_id: str,
    key: str = "OUTPUT"
) -> Dict[str, Any]:
    """
    Retrieve a specific record (such as OUTPUT) from an Apify Key-Value Store.
    
    Args:
        store_id: The ID of the Key-Value Store.
        key: The key of the record to retrieve. Default is 'OUTPUT'.
        
    Returns:
        The record metadata and value content.
    """
    logger.info(f"Fetching Key-Value store record for store '{store_id}' with key '{key}'...")
    client = get_client()
    try:
        record = await client.key_value_store(store_id).get_record(key)
        if not record:
            return {
                "success": False,
                "error": f"Record with key '{key}' not found in store '{store_id}'."
            }
            
        return {
            "success": True,
            "key": record.get("key"),
            "content_type": record.get("contentType"),
            "value": record.get("value")
        }
    except Exception as e:
        logger.exception(f"Failed to fetch record '{key}' from store '{store_id}'")
        return {
            "success": False,
            "error": f"Failed to fetch Key-Value store record: {str(e)}"
        }

@mcp.tool()
async def list_actors(limit: int = 20, desc: bool = True) -> Dict[str, Any]:
    """
    List the custom Actors defined in the authenticated Apify account.
    
    Args:
        limit: Maximum number of actors to return (default: 20).
        desc: Sort by creation date descending (default: True).
        
    Returns:
        A list of Actors.
    """
    logger.info(f"Listing actors (limit={limit})...")
    client = get_client()
    try:
        page = await client.actors().list(limit=limit, desc=desc)
        actors = []
        for actor in page.items:
            actors.append({
                "id": actor.get("id"),
                "name": actor.get("name"),
                "username": actor.get("username"),
                "created_at": actor.get("createdAt"),
                "modified_at": actor.get("modifiedAt"),
                "description": actor.get("description")
            })
        return {
            "success": True,
            "actors": actors,
            "count": page.count,
            "total": page.total
        }
    except Exception as e:
        logger.exception("Failed to list actors")
        return {
            "success": False,
            "error": f"Failed to list actors: {str(e)}"
        }

@mcp.tool()
async def list_runs(limit: int = 20, desc: bool = True) -> Dict[str, Any]:
    """
    List the recent Actor runs in the authenticated Apify account.
    
    Args:
        limit: Maximum number of runs to return (default: 20).
        desc: Sort by start time descending (default: True).
        
    Returns:
        A list of recent runs.
    """
    logger.info(f"Listing runs (limit={limit})...")
    client = get_client()
    try:
        page = await client.runs().list(limit=limit, desc=desc)
        runs = []
        for run in page.items:
            runs.append({
                "id": run.get("id"),
                "actor_id": run.get("actId"),
                "status": run.get("status"),
                "started_at": run.get("startedAt"),
                "finished_at": run.get("finishedAt"),
                "default_dataset_id": run.get("defaultDatasetId"),
                "usage_usd": run.get("usageUsd")
            })
        return {
            "success": True,
            "runs": runs,
            "count": page.count,
            "total": page.total
        }
    except Exception as e:
        logger.exception("Failed to list runs")
        return {
            "success": False,
            "error": f"Failed to list runs: {str(e)}"
        }

if __name__ == "__main__":
    logger.info("Starting Apify MCP server...")
    mcp.run()
