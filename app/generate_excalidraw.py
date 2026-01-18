import json
import time

def create_rect(id_val, x, y, width, height, bg_color):
    return {
        "id": id_val,
        "type": "rectangle",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "angle": 0,
        "strokeColor": "#000000",
        "backgroundColor": bg_color,
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "roundness": {"type": 3},
        "seed": int(time.time() * 1000) % 100000,
        "version": 1,
        "versionNonce": 0,
        "isDeleted": False,
        "boundElements": [],
        "updated": int(time.time() * 1000),
        "link": None,
        "locked": False,
    }

def create_text(id_val, x, y, width, height, text, font_size=16):
     return {
        "id": id_val,
        "type": "text",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "angle": 0,
        "strokeColor": "#000000",
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "roundness": None,
        "seed": int(time.time() * 1000) % 100000,
        "version": 1,
        "versionNonce": 0,
        "isDeleted": False,
        "boundElements": [],
        "updated": int(time.time() * 1000),
        "link": None,
        "locked": False,
        "text": text,
        "fontSize": font_size,
        "fontFamily": 1,
        "textAlign": "center",
        "verticalAlign": "middle",
        "baseline": 18,
        "containerId": None,
        "originalText": text,
    }

elements = []

# Top Row Columns
cols = [
    ("STRATEGY", ["What's vision?", "How launch?", "Build or buy?", "How defend?", "What to kill?"], "#dbeafe"),
    ("SENSE", ["Design X", "Improve Y", "Pick top 3", "Kill or keep?", "Who's user?"], "#dcfce7"),
    ("EXECUTION", ["How ship?", "Who owns?", "How align XFN?", "What's risk?", "Why delayed?"], "#f3f4f6"),
    ("TECHNICAL", ["Design system", "Which DB?", "Scale 10x?", "Build or buy?", "Where bottleneck?"], "#fee2e2")
]

start_x = 50
start_y = 100
col_w = 260
col_h = 240
gap = 20

for i, (title, items, color) in enumerate(cols):
    x = start_x + i * (col_w + gap)
    y = start_y
    # Box
    rect_id = f"rect_{i}"
    elements.append(create_rect(rect_id, x, y, col_w, col_h, color))
    # Title
    elements.append(create_text(f"title_{i}", x + 10, y + 10, col_w - 20, 30, title, 20))
    # Items
    item_y = y + 50
    for j, item in enumerate(items):
        elements.append(create_text(f"item_{i}_{j}", x + 10, item_y, col_w - 20, 20, f"• {item}", 16))
        item_y += 35

# Bottom Rows
rows = [
    ("DOMAIN", "Ads  ·  AI/ML  ·  Infra  ·  Trust & Safety  ·  Payments", "#ffedd5"),
    ("METRICS & EXPERIMENTATION", "Define metric?  ·  Why dropped?  ·  Design A/B?  ·  Counter-metric?  ·  Tradeoff?", "#fef9c3"),
    ("LEADERSHIP & ORG DESIGN", "How re-org?  ·  How hire?  ·  Resolve conflict?  ·  Influence w/o power?", "#f3e8ff"),
    ("BEHAVIORAL", "Tell me about…  ·  Biggest failure?  ·  Disagree & commit?  ·  How communicate?", "#fce7f3")
]

row_w = (col_w * 4) + (gap * 3)
row_h = 100
row_start_y = start_y + col_h + gap

for k, (title, items, color) in enumerate(rows):
    x = start_x
    y = row_start_y + k * (row_h + gap)
    rect_id = f"rect_row_{k}"
    elements.append(create_rect(rect_id, x, y, row_w, row_h, color))
    elements.append(create_text(f"title_row_{k}", x + 10, y + 15, row_w - 20, 30, title, 20))
    elements.append(create_text(f"item_row_{k}", x + 10, y + 55, row_w - 20, 20, items, 16))

# Main Title
elements.append(create_text("main_title", start_x, 30, row_w, 40, "IC7 / D1 INTERVIEW PREP FRAMEWORK", 36))

output = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "viewBackgroundColor": "#ffffff",
        "gridSize": None
    },
    "files": {}
}

print(json.dumps(output, indent=2))
