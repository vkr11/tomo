# Apify Model Context Protocol (MCP) Server

This is a Model Context Protocol (MCP) server for **Apify**. It allows your AI assistants (like Claude Desktop, Cursor, or VS Code extensions) to run scrapers, crawlers, and automation tools on the Apify platform, monitor runs, and extract scraped results using standard tools.

---

## Features

* **Run Actors:** Run any Actor from the Apify Store or your personal account (e.g. Google Maps Scraper, Instagram Scraper, Website Content Crawler).
* **Smart Waiting:** Optionally block until a run completes and get the dataset results immediately in a single prompt loop.
* **Retrieve Datasets:** Fetch output items from Apify datasets with optional auto-cleaning of internal system metadata (saves token context!).
* **Fetch Key-Value Stores:** Retrieve output files or direct JSON records from Actor runs.
* **Monitor Runs & Actors:** List recent runs, retrieve status details, and search custom actors.

---

## Setup Instructions

### 1. Requirements
* Python 3.10+ (The project is set up with Python 3.11).
* An Apify API Token (obtain one from the [Apify Console integrations page](https://console.apify.com/account/integrations)).

### 2. Quick Install
All packages are installed inside the local `.venv` environment in this folder. To run the server, we use the `run.sh` wrapper script.

Ensure `run.sh` is executable:
```bash
chmod +x run.sh
```

---

## Configuration

You can configure your MCP client (such as Claude Desktop or Cursor) to communicate with this server using the standard `stdio` transport.

### 1. Environment Configuration (Optional)
If you'd like to configure the token locally, create a file named `.env` in this directory:
```env
APIFY_TOKEN=your_apify_api_token_here
```

### 2. Client Setup

#### A. Claude Desktop
Add the server definition to your Claude Desktop configuration file (typically located at `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "apify": {
      "command": "/Users/vikashrungta/code/tomo/.agents/skills/apify_mcp/scripts/run.sh",
      "env": {
        "APIFY_TOKEN": "your_apify_api_token_here"
      }
    }
  }
}
```
*(Replace `your_apify_api_token_here` with your actual token. If you specify `APIFY_TOKEN` in the `"env"` object in the config, you do not need a `.env` file.)*

#### B. Cursor (Settings -> Features -> MCP)
1. Add a new MCP server.
2. Set **Name** to `apify`.
3. Set **Type** to `command`.
4. Set **Command** to `/Users/vikashrungta/code/tomo/.agents/skills/apify_mcp/scripts/run.sh`.
5. *(Make sure `APIFY_TOKEN` is defined in a `.env` file in the `/Users/vikashrungta/code/tomo/.agents/skills/apify_mcp/scripts` directory so that the wrapper loads it automatically.)*

---

## Tools Reference

The server exposes the following tools to the AI assistant:

### `run_actor`
Runs a specific Actor and waits for completion.
* **Arguments:**
  * `actor_id` (string, required): The ID or username/name of the Actor (e.g. `apify/web-scraper` or `apify/hello-world`).
  * `run_input` (object, optional): Input JSON schema configuration for the Actor.
  * `wait_limit_seconds` (integer, optional, default: `300`): Maximum time to wait. Set to `0` to run asynchronously.
* **Behavior:** If it completes within the wait limit, it returns the run details and up to 100 dataset items.

### `get_dataset_items`
Retrieves items from a dataset.
* **Arguments:**
  * `dataset_id` (string, required): The ID of the dataset.
  * `limit` (integer, optional, default: `100`): Max number of items to return.
  * `offset` (integer, optional, default: `0`): Pagination offset.
  * `clean` (boolean, optional, default: `true`): Strips out internal metadata keys (columns starting with `#`) to reduce token consumption.

### `get_run_status`
Checks the status of an active or past Actor run.
* **Arguments:**
  * `run_id` (string, required): The run ID.

### `get_key_value_store_record`
Retrieves a record value from a Key-Value Store.
* **Arguments:**
  * `store_id` (string, required): Key-Value store ID.
  * `key` (string, optional, default: `OUTPUT`): The record key.

### `list_actors`
Lists the custom Actors configured in your account.

### `list_runs`
Lists recent Actor runs in your account.

---

## Example Prompts

Here are some prompts you can use to interact with Apify through your AI assistant:

* *"Can you list the recent runs in my Apify account?"*
* *"Start a run of `apify/hello-world` with the input message 'Hello from MCP' and show me the results."*
* *"Find the status of the Apify run with ID `xyz`."*
* *"Retrieve the latest 20 items from the dataset `abc`."*
