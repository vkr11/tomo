#!/bin/bash

# Determine the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Navigate to the script's directory
cd "$DIR"

# Load local .env file if it exists
if [ -f .env ]; then
  # Export variables while ignoring comments
  export $(grep -v '^#' .env | xargs)
fi

# Run the MCP server using the virtual environment's python
exec "$DIR/.venv/bin/python" "$DIR/server.py"
