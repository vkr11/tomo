---
name: apify_mcp
description: Model Context Protocol (MCP) server for Apify. Run scrapers, crawlers, and automation tools on Apify, monitor runs, and extract dataset results. Use when you need to run web scrapers, crawlers, or APIs hosted on Apify.
---

# Apify Model Context Protocol (MCP) Server

An MCP server allowing AI assistants (like Claude Desktop or Cursor) to run scrapers, crawlers, and automation tools on the Apify platform, monitor runs, and extract scraped results.

## Location
All server scripts and environments are located at:
`/Users/vikashrungta/code/tomo/.agents/skills/apify_mcp/scripts/`

## Setup & Run Instructions

### 1. Requirements
* Python 3.10+ (The project is set up with Python 3.11).
* Apify API Token.

### 2. Client Setup

#### A. Claude Desktop
Add to your `claude_desktop_config.json`:
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

#### B. Cursor (Settings -> Features -> MCP)
1. Add a new MCP server.
2. Set **Name** to `apify`.
3. Set **Type** to `command`.
4. Set **Command** to `/Users/vikashrungta/code/tomo/.agents/skills/apify_mcp/scripts/run.sh`.
5. *(Make sure `APIFY_TOKEN` is defined in a `.env` file in the `/Users/vikashrungta/code/tomo/.agents/skills/apify_mcp/scripts` directory so that the wrapper loads it automatically.)*

---

## Tools Reference

The server exposes the following tools:

* **`run_actor`**: Runs a specific Actor and waits for completion.
* **`get_dataset_items`**: Retrieves items from a dataset.
* **`get_run_status`**: Checks the status of an active or past Actor run.
* **`get_key_value_store_record`**: Retrieves a record value from a Key-Value Store.
* **`list_actors`**: Lists the custom Actors configured in your account.
* **`list_runs`**: Lists recent Actor runs in your account.
