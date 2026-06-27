---
name: web_capture
description: Fetch a webpage without opening a browser and convert its full page content (including images, styles, and dynamically rendered content) into an image file (screenshot) using Playwright. Use whenever you need to capture visual evidence of a website, save references of visual layouts, or when the user asks to "convert a page to an image" or "take a headless screenshot".
---

# Headless Web Capture

A production-grade Playwright-based tool that headlessly fetches any URL and extracts its content in **four output formats** — all from a single page load:

| Format | Flag | Best for |
|:---|:---|:---|
| **Screenshot** (PNG/JPEG) | `-i` | Visual proof, layout verification, UX review |
| **HTML** | `-H` | Full DOM preservation, re-rendering, scraping |
| **Markdown** | `-m` | LLM consumption, article extraction, search indexing |
| **Metadata** (JSON) | `-M` | Title, OG tags, canonical URL, image inventory |

## Setup Requirements

1. Python 3 with `playwright` installed (`pip install playwright && playwright install chromium`).
2. For best Markdown output, have `markdownify` installed (falls back to `html2text`, then `bs4` plain-text).

## How to Use

Invoke the script via `run_command`. You must supply **at least one** output flag.

### Syntax

```bash
python3 <SKILL_DIR>/scripts/capture.py <URL> [output flags] [options]
```

Where `<SKILL_DIR>` is `/Users/vikashrungta/code/tomo/.agents/skills/_tools/web_capture`.

### Examples

```bash
SKILL=/Users/vikashrungta/code/tomo/.agents/skills/_tools/web_capture/scripts/capture.py

# Screenshot only
python3 $SKILL "https://example.com" -i screenshot.png

# Full capture — image + HTML + Markdown + metadata
python3 $SKILL "https://example.com" -i shot.png -H page.html -m page.md -M meta.json

# LLM-ready markdown only (fastest — no image rendering)
python3 $SKILL "https://example.com" -m article.md

# Mobile device emulation
python3 $SKILL "https://example.com" -i mobile.png --device "iPhone 14 Pro"

# Custom viewport and extended timeout for slow pages
python3 $SKILL "https://example.com" -i wide.png --viewport_width 1920 --timeout 60000
```

## Output Flags Reference

| Short | Long | Description |
|:---|:---|:---|
| `-i` | `--image_output` | Save a full-page screenshot (PNG or JPEG, by extension) |
| `-H` | `--html_output` | Save the fully rendered DOM after JS execution |
| `-m` | `--markdown_output` | Save clean Markdown (scripts, nav, footers stripped) |
| `-M` | `--metadata_output` | Save JSON metadata (title, description, OG tags, images) |

## Capture Options

| Option | Default | Description |
|:---|:---|:---|
| `--viewport_width` | 1440 | Browser viewport width in pixels |
| `--viewport_height` | 900 | Browser viewport height in pixels |
| `--device` | — | Playwright device name for mobile emulation (e.g. `"iPhone 14 Pro"`) |
| `--timeout` | 30000 | Navigation timeout in milliseconds |
| `--wait` | 2000 | Extra milliseconds to wait after load for dynamic rendering |
| `--no-full-page` | off | Capture viewport only (not the full scrollable page) |
| `--no-scroll` | off | Skip auto-scrolling (disables lazy-load image triggering) |
| `--no-dismiss` | off | Skip auto-dismissing cookie/consent popups |
| `--user-agent` | — | Custom User-Agent string |

## Smart Behaviors

1. **Lazy-load scrolling** — Automatically scrolls the page to trigger lazy-loaded images and infinite scroll content before capturing.
2. **Cookie/consent auto-dismiss** — Detects and clicks common "Accept cookies" banners so they don't obstruct the screenshot.
3. **Anti-detection** — Disables Chromium's `AutomationControlled` flag for better compatibility with protected pages.
4. **Graceful Markdown fallback** — Tries `markdownify` → `html2text` → `bs4` text extraction, so it always produces output regardless of installed libraries.

## When to Use

- **"Capture this page"** — User wants a visual snapshot or content dump.
- **Research pipelines** — Feed Markdown output directly to LLMs for summarization, extraction, or Q&A.
- **Scraping JS-heavy sites** — Pages that require JavaScript execution (SPAs, React apps) where `curl` fails.
- **Mobile testing** — Use `--device` to emulate phones and check responsive layouts.
- **Visual regression** — Store screenshots as reference images for UI audits.
