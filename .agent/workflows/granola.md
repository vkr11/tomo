---
description: Access and manage Granola meeting transcripts
---

To use the Granola tool, you can ask for any of the following:

1. **List all meetings (with dates)**: "List my Granola talks" or "Show my recent meetings"
   // turbo
   `python3 app/granola_tool.py list`

2. **Search for a meeting**: "Find my meetings with [Name]"
   // turbo
   `python3 app/granola_tool.py search "[Name]"`

3. **Get a transcript**: "Show me the transcript for the meeting [Meeting ID]" or "What did I discuss with [Name] today?"
   // turbo
   `python3 app/granola_tool.py transcript [Meeting ID]`

The data is sourced from `users/vikash/episodes/cache-v3.json` in this workspace.
