"""
Headless Web Capture Tool
─────────────────────────
A production-grade Playwright-based scraper that fetches a webpage headlessly
and extracts its content in multiple formats:

  • Screenshot (PNG/JPEG) — full-page visual capture
  • HTML             — fully rendered DOM after JS execution
  • Markdown         — clean, LLM-ready text extracted from the page body
  • Metadata (JSON)  — title, description, OG tags, canonical URL, images

All outputs are optional and can be combined in a single run.
"""

import asyncio
import argparse
import json
import os
import re
import sys
from urllib.parse import urljoin

from playwright.async_api import async_playwright

# ---------------------------------------------------------------------------
# Markdown conversion (best-effort with available libs)
# ---------------------------------------------------------------------------

def _strip_noise_tags(html_string):
    """Pre-process HTML to fully remove noise tags (script, style, nav, etc.)."""
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_string, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "noscript", "iframe", "svg"]):
            tag.decompose()
        return str(soup)
    except ImportError:
        return html_string


def _html_to_markdown(html_string, base_url=""):
    """Convert an HTML string to clean Markdown.

    Pre-cleans the HTML with BeautifulSoup (if available) to decompose noise
    tags, then converts using markdownify → html2text → bs4 plain text.
    """
    cleaned = _strip_noise_tags(html_string)

    try:
        import markdownify
        md = markdownify.markdownify(cleaned, heading_style="ATX")
        return _clean_markdown(md)
    except ImportError:
        pass

    try:
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.body_width = 0  # no wrapping
        h.ignore_emphasis = False
        return _clean_markdown(h.handle(cleaned))
    except ImportError:
        pass

    # Last resort: plain text
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(cleaned, "html.parser")
        return soup.get_text(separator="\n", strip=True)
    except ImportError:
        return "(Could not convert to Markdown — install markdownify, html2text, or bs4)"


def _clean_markdown(text):
    """Remove excessive blank lines and trailing whitespace."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(lines).strip() + "\n"


# ---------------------------------------------------------------------------
# Metadata extraction (runs inside Playwright page context)
# ---------------------------------------------------------------------------

async def _extract_metadata(page, url):
    """Pull structured metadata from the live page."""
    meta = await page.evaluate("""() => {
        const get = (sel) => {
            const el = document.querySelector(sel);
            return el ? (el.content || el.textContent || '').trim() : '';
        };
        const getAllMeta = (prefix) => {
            const result = {};
            document.querySelectorAll(`meta[property^="${prefix}"]`).forEach(el => {
                const key = el.getAttribute('property') || el.getAttribute('name');
                if (key) result[key] = (el.content || '').trim();
            });
            return result;
        };
        const images = Array.from(document.querySelectorAll('img[src]'))
            .map(img => ({
                src: img.src,
                alt: img.alt || '',
                width: img.naturalWidth || img.width || 0,
                height: img.naturalHeight || img.height || 0,
            }))
            .filter(img => img.width >= 50 && img.height >= 50);

        return {
            title: document.title || '',
            description: get('meta[name="description"]') || get('meta[property="og:description"]'),
            canonical: get('link[rel="canonical"]') || '',
            og: getAllMeta('og:'),
            images: images.slice(0, 30),
            h1: Array.from(document.querySelectorAll('h1')).map(el => el.textContent.trim()).slice(0, 5),
        };
    }""")
    meta["url"] = url
    return meta


# ---------------------------------------------------------------------------
# Cookie-banner / popup auto-dismissal
# ---------------------------------------------------------------------------

async def _dismiss_popups(page):
    """Best-effort click on common cookie/consent banners."""
    selectors = [
        # Common cookie-consent buttons
        "button:has-text('Accept')",
        "button:has-text('Accept all')",
        "button:has-text('Accept All')",
        "button:has-text('I agree')",
        "button:has-text('Got it')",
        "button:has-text('OK')",
        "[id*='cookie'] button",
        "[class*='cookie'] button",
        "[id*='consent'] button",
        "[class*='consent'] button",
    ]
    for sel in selectors:
        try:
            btn = page.locator(sel).first
            if await btn.is_visible(timeout=300):
                await btn.click(timeout=500)
                await page.wait_for_timeout(300)
                return
        except Exception:
            continue


# ---------------------------------------------------------------------------
# Scroll-to-bottom for lazy-loaded content
# ---------------------------------------------------------------------------

async def _scroll_to_load(page, max_scrolls=15, pause_ms=400):
    """Incrementally scroll the page to trigger lazy-loading images/content."""
    prev_height = 0
    for _ in range(max_scrolls):
        curr_height = await page.evaluate("document.body.scrollHeight")
        if curr_height == prev_height:
            break
        prev_height = curr_height
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(pause_ms)
    # Scroll back to top for a clean screenshot
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(300)


# ---------------------------------------------------------------------------
# Main capture logic
# ---------------------------------------------------------------------------

async def capture(
    url,
    image_output=None,
    html_output=None,
    markdown_output=None,
    metadata_output=None,
    viewport_width=1440,
    viewport_height=900,
    device=None,
    timeout=30000,
    wait_after_load=2000,
    full_page=True,
    scroll=True,
    dismiss_cookies=True,
    user_agent=None,
):
    if not any([image_output, html_output, markdown_output, metadata_output]):
        print("Error: Must provide at least one output flag.", file=sys.stderr)
        sys.exit(1)

    print(f"🌐  Capturing {url}")
    async with async_playwright() as p:
        try:
            launch_args = ["--disable-blink-features=AutomationControlled"]
            browser = await p.chromium.launch(headless=True, args=launch_args)

            # Device emulation or custom viewport
            context_opts = {}
            if device and device in p.devices:
                context_opts = {**p.devices[device]}
                print(f"📱  Emulating device: {device}")
            else:
                context_opts["viewport"] = {"width": viewport_width, "height": viewport_height}

            if user_agent:
                context_opts["user_agent"] = user_agent

            context = await browser.new_context(**context_opts)
            page = await context.new_page()

            # Navigate
            print("   ⏳ Loading page …")
            await page.goto(url, timeout=timeout, wait_until="networkidle")

            # Dismiss cookie banners
            if dismiss_cookies:
                await _dismiss_popups(page)

            # Scroll to trigger lazy-loaded content
            if scroll:
                print("   📜 Scrolling to load lazy content …")
                await _scroll_to_load(page)

            # Wait for dynamic rendering to settle
            await page.wait_for_timeout(wait_after_load)

            # ── Metadata ──────────────────────────────────────────
            if metadata_output:
                print(f"   📋 Extracting metadata → {metadata_output}")
                meta = await _extract_metadata(page, url)
                with open(metadata_output, "w", encoding="utf-8") as f:
                    json.dump(meta, f, indent=2, ensure_ascii=False)

            # ── HTML ──────────────────────────────────────────────
            html_content = await page.content()
            if html_output:
                print(f"   📄 Saving HTML → {html_output}")
                with open(html_output, "w", encoding="utf-8") as f:
                    f.write(html_content)

            # ── Markdown ──────────────────────────────────────────
            if markdown_output:
                print(f"   📝 Converting to Markdown → {markdown_output}")
                md = _html_to_markdown(html_content, base_url=url)
                with open(markdown_output, "w", encoding="utf-8") as f:
                    f.write(md)

            # ── Screenshot ────────────────────────────────────────
            if image_output:
                print(f"   📸 Screenshot → {image_output}")
                await page.screenshot(path=image_output, full_page=full_page)

            await context.close()
            await browser.close()
            print("✅  Capture complete.")

        except Exception as e:
            print(f"❌  Error: {e}", file=sys.stderr)
            sys.exit(1)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Headless web capture: screenshot, HTML, Markdown, and metadata extraction.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Screenshot only
  %(prog)s https://example.com -i screenshot.png

  # Full capture — image + HTML + Markdown + metadata
  %(prog)s https://example.com -i shot.png -H page.html -m page.md -M meta.json

  # Mobile device emulation
  %(prog)s https://example.com -i mobile.png --device "iPhone 14 Pro"

  # LLM-ready markdown only (fastest, no image rendering overhead)
  %(prog)s https://example.com -m article.md
""",
    )
    parser.add_argument("url", help="URL to capture")

    out = parser.add_argument_group("Output formats (at least one required)")
    out.add_argument("-i", "--image_output",    help="Save full-page screenshot (PNG/JPEG)")
    out.add_argument("-H", "--html_output",     help="Save fully rendered HTML DOM")
    out.add_argument("-m", "--markdown_output",  help="Save clean Markdown (LLM-ready)")
    out.add_argument("-M", "--metadata_output",  help="Save page metadata as JSON (title, OG tags, images)")

    opts = parser.add_argument_group("Capture options")
    opts.add_argument("--viewport_width",  type=int, default=1440,  help="Viewport width (default: 1440)")
    opts.add_argument("--viewport_height", type=int, default=900,   help="Viewport height (default: 900)")
    opts.add_argument("--device",          type=str, default=None,  help="Playwright device name for emulation (e.g. 'iPhone 14 Pro')")
    opts.add_argument("--timeout",         type=int, default=30000, help="Navigation timeout in ms (default: 30000)")
    opts.add_argument("--wait",            type=int, default=2000,  help="Extra ms to wait after load (default: 2000)")
    opts.add_argument("--no-full-page",    action="store_true",     help="Capture only the viewport, not the full scrollable page")
    opts.add_argument("--no-scroll",       action="store_true",     help="Skip scrolling (disables lazy-load triggering)")
    opts.add_argument("--no-dismiss",      action="store_true",     help="Skip auto-dismissing cookie/consent popups")
    opts.add_argument("--user-agent",      type=str, default=None,  help="Custom User-Agent string")

    args = parser.parse_args()

    asyncio.run(capture(
        url=args.url,
        image_output=args.image_output,
        html_output=args.html_output,
        markdown_output=args.markdown_output,
        metadata_output=args.metadata_output,
        viewport_width=args.viewport_width,
        viewport_height=args.viewport_height,
        device=args.device,
        timeout=args.timeout,
        wait_after_load=args.wait,
        full_page=not args.no_full_page,
        scroll=not args.no_scroll,
        dismiss_cookies=not args.no_dismiss,
        user_agent=args.user_agent,
    ))


if __name__ == "__main__":
    main()
