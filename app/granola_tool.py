import json
import os
import sys
from datetime import datetime

# Default user for now, could be made dynamic
USER_NAME = "vikash"
BASE_DIR = f"/Users/vikashrungta/code/tomo/users/{USER_NAME}"
EPISODES_DIR = f"{BASE_DIR}/episodes"
CACHE_FILE = f"{EPISODES_DIR}/cache-v3.json"

def load_data():
    if not os.path.exists(CACHE_FILE):
        print(f"Error: {CACHE_FILE} not found.")
        sys.exit(1)
    
    with open(CACHE_FILE, 'r') as f:
        data = json.load(f)
    
    # Granola's cache is nested: {"cache": "{\"state\": ...}"}
    if "cache" in data:
        return json.loads(data["cache"])
    return data

def list_meetings():
    state = load_data().get("state", {})
    meetings = state.get("meetingsMetadata", {})
    transcripts = state.get("transcripts", {})
    
    results = []
    for meeting_id, meta in meetings.items():
        if meeting_id in transcripts:
            results.append({
                "id": meeting_id,
                "title": meta.get("title", "Untitled"),
                "date": meta.get("created_at", "Unknown")
            })
    
    # Sort by date descending
    results.sort(key=lambda x: x["date"], reverse=True)
    
    print(f"{'ID':<40} | {'Date':<20} | {'Title'}")
    print("-" * 100)
    for r in results:
        # Parse and format date
        try:
            dt = datetime.fromisoformat(r['date'].replace('Z', '+00:00'))
            date_str = dt.strftime("%Y-%m-%d %H:%M")
        except:
            date_str = r['date'][:16]
        print(f"{r['id']:<40} | {date_str:<20} | {r['title']}")

def get_transcript(meeting_id):
    state = load_data().get("state", {})
    transcripts = state.get("transcripts", {})
    metadata = state.get("meetingsMetadata", {})
    
    if meeting_id not in transcripts:
        print(f"Error: No transcript found for ID {meeting_id}")
        return

    meta = metadata.get(meeting_id, {})
    print(f"Transcript for: {meta.get('title', 'Unknown')}")
    print(f"Date: {meta.get('created_at', 'Unknown')}")
    print("-" * 50)
    
    entries = transcripts[meeting_id]
    
    # Format the transcript nicely
    for entry in entries:
        source = entry.get("source", "unknown")
        text = entry.get("text", "")
        # source "microphone" is usually the user, "system" is others
        speaker = "Me" if source == "microphone" else "Others"
        print(f"[{speaker}]: {text}")

def search_meetings(query):
    state = load_data().get("state", {})
    meetings = state.get("meetingsMetadata", {})
    transcripts = state.get("transcripts", {})
    
    query = query.lower()
    results = []
    for meeting_id, meta in meetings.items():
        title = meta.get("title", "").lower()
        if query in title and meeting_id in transcripts:
            results.append({
                "id": meeting_id,
                "title": meta.get("title", "Untitled"),
                "date": meta.get("created_at", "Unknown")
            })
    
    if not results:
        print(f"No meetings found matching '{query}'")
        return

    print(f"Found {len(results)} meetings:")
    for r in results:
        print(f"- {r['title']} (ID: {r['id']})")

def generate_dashboard():
    if not os.path.exists(CACHE_FILE):
        print(f"Error: {CACHE_FILE} not found.")
        return

    # Load and re-dump JSON to ensure it's safely escaped for the script tag
    try:
        with open(CACHE_FILE, 'r') as f:
            data = json.load(f)
        data_json = json.dumps(data)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return
    
    html_file = f"{EPISODES_DIR}/granola_dashboard.html"
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found. Please create it first.")
        return

    with open(html_file, 'r') as f:
        html_content = f.read()

    # Inject the data into the script tag
    # Use string replacement instead of re.sub to avoid backslash escaping issues
    start_marker = '<script id="granolaData" type="application/json">'
    end_marker = '</script>'
    
    start_idx = html_content.find(start_marker)
    end_idx = html_content.find(end_marker, start_idx)
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not find script markers in HTML.")
        return

    # Escape any </script> sequences in the JSON to avoid breaking the script tag
    safe_json = data_json.replace('</script>', '<\\/script>')
    
    updated_content = (
        html_content[:start_idx + len(start_marker)] + 
        safe_json + 
        html_content[end_idx:]
    )

    with open(html_file, 'w') as f:
        f.write(updated_content)
    
    print(f"Dashboard updated successfully: {html_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python granola_tool.py [list|transcript <id>|search <query>|dashboard]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "list":
        list_meetings()
    elif cmd == "transcript" and len(sys.argv) > 2:
        get_transcript(sys.argv[2])
    elif cmd == "search" and len(sys.argv) > 2:
        search_meetings(sys.argv[2])
    elif cmd == "dashboard":
        generate_dashboard()
    else:
        print("Unknown command or missing arguments.")
