"""Audit visible SVG figure text for overlapping labels and clipping.

Run a local HTTP server on port 8765 with docs/ as root. Requires Playwright.
The audit inspects rendered SVG text geometry in Chromium, including nested
transforms. It excludes intentional clipping at the image canvas boundary.
"""
from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE_URL = os.getenv("AUDIT_BASE_URL", "http://127.0.0.1:8765")
OUTPUT = ROOT / "visual_audit_output"
OUTPUT.mkdir(exist_ok=True)
DECKS = ("intro", "ai_basics", "vision_ai")


def listed_assets() -> dict[str, list[str]]:
    result: dict[str, list[str]] = defaultdict(list)
    for deck in DECKS:
        content = (DOCS / f"{deck}.html").read_text(encoding="utf-8")
        sections = re.findall(
            r'<section class="slide(?: [^"]+)?"[^>]*>.*?</section>',
            content,
            flags=re.DOTALL,
        )
        for number, section in enumerate(sections, 1):
            for source in re.findall(r'(?:href|src)="([^"]+)"', section):
                path = unquote(urlsplit(source).path)
                if not path.lower().endswith(".svg"):
                    continue
                if not (DOCS / path).is_file():
                    continue
                reference = f"{deck}#{number}"
                if reference not in result[path]:
                    result[path].append(reference)
    return result


JS_GEOMETRY = r"""() => {
  const svg = document.querySelector('svg');
  if (!svg) return {error:'no SVG root'};
  const frame = svg.getBoundingClientRect();
  const visible = [...svg.querySelectorAll('text')]
    .filter(el => el.textContent.trim().length > 0
      && getComputedStyle(el).display !== 'none'
      && getComputedStyle(el).visibility !== 'hidden')
    .map((el, index) => {
      const r = el.getBoundingClientRect();
      return {
        index, text:el.textContent.trim().replace(/\s+/g,' ').slice(0,75),
        x:r.left-frame.left, y:r.top-frame.top,
        right:r.right-frame.left, bottom:r.bottom-frame.top,
        width:r.width, height:r.height
      };
    }).filter(t=>t.width>1 && t.height>1);
  const overlaps=[];
  const clipped=[];
  for(let i=0;i<visible.length;i++) {
    const a=visible[i];
    if(a.x < -4 || a.y < -4 ||
       a.right > frame.width+4 || a.bottom > frame.height+4) {
      clipped.push({label:a.text,
        x:+a.x.toFixed(1),y:+a.y.toFixed(1)});
    }
    for(let j=i+1;j<visible.length;j++){
      const b=visible[j];
      const dx=Math.min(a.right,b.right)-Math.max(a.x,b.x);
      const dy=Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y);
      if(dx<=3 || dy<=3) continue;
      const ratio=dx*dy/Math.min(a.width*a.height,b.width*b.height);
      if(ratio<.12)continue;
      overlaps.push({
        a:a.text,b:b.text,
        overlapX:+dx.toFixed(1),overlapY:+dy.toFixed(1),
        ratio:+ratio.toFixed(2)
      });
    }
  }
  return {
    texts:visible.length,width:+frame.width.toFixed(1),
    height:+frame.height.toFixed(1),overlaps,clipped
  };
}"""


def main() -> None:
    assets = listed_assets()
    records = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        for asset, references in sorted(assets.items()):
            page.goto(f"{BASE_URL}/{asset}", wait_until="load", timeout=30000)
            page.evaluate("document.fonts.ready")
            data = page.evaluate(JS_GEOMETRY)
            records.append({"asset": asset, "slides": references, **data})
        browser.close()

    output = OUTPUT / "svg_text_layout.json"
    output.write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    suspect = [
        item for item in records
        if item.get("overlaps") or item.get("clipped") or item.get("error")
    ]
    print("SVG_TEXT_AUDIT", json.dumps({
        "assets": len(assets),
        "text_nodes": sum(item.get("texts", 0) for item in records),
        "suspect_assets": len(suspect),
        "text_pairs": sum(len(item.get("overlaps", [])) for item in records),
        "clipped_labels": sum(len(item.get("clipped", [])) for item in records),
    }, ensure_ascii=False))
    for item in suspect:
        print("SVG_TEXT_ISSUE", json.dumps({
            "asset": item["asset"], "slides": item["slides"],
            "overlaps": item.get("overlaps", [])[:12],
            "clipped": item.get("clipped", [])[:8],
        }, ensure_ascii=False))
    if suspect:
        raise SystemExit(f"SVG figure label issues remain in {len(suspect)} assets")


if __name__ == "__main__":
    main()
