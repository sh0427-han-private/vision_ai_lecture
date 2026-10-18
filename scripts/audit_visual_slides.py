"""Render the 3 lecture decks at two presentation resolutions.

Produces complete per-slide screenshots/contact sheets plus machine-readable
layout issues. This script audits the ACTUAL Chromium layout, not HTML guesses.
"""
from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "visual_audit_output"
OUTPUT.mkdir(exist_ok=True)
BASE_URL = os.getenv("AUDIT_BASE_URL", "http://127.0.0.1:8765")
DECKS = {name: len(entries) for name, entries in json.loads(
    (ROOT / "docs/two_hour_manifest.json").read_text()
)["decks"].items()}
VIEWPORTS = [(1920, 1080), (1366, 768)]


def inspect_slide(page):
    """Return observable sizes, overlaps, asset loading and legibility risk."""
    return page.evaluate(
        r"""() => {
          const slide = document.querySelector('.slide.active');
          if (!slide) return {error:'no active slide'};
          const inner = slide.querySelector('.slide-inner');
          const sr = slide.getBoundingClientRect();
          const ir = inner.getBoundingClientRect();
          const fit = Number(slide.dataset.fitScale || '1');
          const style = getComputedStyle(slide);
          const availableBottom = sr.bottom - parseFloat(style.paddingBottom);
          const availableRight = sr.right - parseFloat(style.paddingRight);
          const title = slide.querySelector('.slide-title');
          const titleText = title?.innerText?.trim() || '';
          const rect = node => {
            const r=node.getBoundingClientRect();
            return {x:r.x,y:r.y,right:r.right,bottom:r.bottom,
                    width:r.width,height:r.height};
          };
          const nodes = [...slide.querySelectorAll(
            '.slide-title,.slide-subtitle,.lesson-meta,.lesson-figure,' +
            '.lesson-takeaway,.figure,.callout,.sensor-life-trio,' +
            '.apple-variation-grid,.generalization-visual,' +
            '.intro-visual,.visual-panel,.lesson-reference,' +
            '.th-panes,.th-cnn-flow,.th-case-table,.th-note,' +
            '.nb-main-figure,.nb-network-numbers,.nb-derivation,' +
            '.concept-equation,.nb-takeaway,.nb-activation-charts,' +
            '.gate-geometry-layout,.principle-figure,.pf-pipeline,' +
            '.pf-workflow,.pf-apple-row,.pf-parallel,.pf-dataset,' +
            '.pf-evaluation-layout,.pf-static-confusion,.pf-caption,.pf-teaching-note,' +
            '.vm-grid,.vm-showcase,.vm-blueprint,.vm-training-figure,.vm-intro-message,' +
            '.lf-gate-figure,.lf-pad-shared,.lf-pad-compare,.lf-augment-grid,' +
            '.lf-simple-photo-grid,.lf-training-story,.lf-transfer-flow,.lf-cnn-architecture'
          )].filter(x => x.getBoundingClientRect().height > 1);
          // Visually hidden accessibility-only content has no visual overlap.
          const visuallyPresent = nodes.filter(node => {
            if (node.closest('.ppt-screenreader-only,[aria-hidden="true"]'))
              return false;
            const cs = getComputedStyle(node);
            return cs.display !== 'none' && cs.visibility !== 'hidden' &&
              cs.opacity !== '0';
          });
          const visibleNodes = visuallyPresent.filter(x =>
            !visuallyPresent.some(y => y !== x && y.contains(x)));
          const elements = visibleNodes.map(node => ({
            name: node.className || node.tagName, bounds:rect(node)
          }));
          const overlaps=[];
          for(let i=0;i<elements.length;i++){
            for(let j=i+1;j<elements.length;j++){
              const a=elements[i].bounds,b=elements[j].bounds;
              const overlapX=Math.min(a.right,b.right)-Math.max(a.x,b.x);
              const overlapY=Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y);
              if(overlapX>12 && overlapY>12)
                overlaps.push([elements[i].name,elements[j].name,
                               Math.round(overlapX),Math.round(overlapY)]);
            }
          }
          const imgs=[...slide.querySelectorAll('img')].map(img=>{
             const r=img.getBoundingClientRect();
             return {src:img.getAttribute('src'),loaded:img.complete&&img.naturalWidth>0,
                     naturalW:img.naturalWidth,naturalH:img.naturalHeight,
                     renderW:Math.round(r.width),renderH:Math.round(r.height)};
          });
          const fontPx=title?parseFloat(getComputedStyle(title).fontSize)*fit:0;
          return {
            title:titleText,fitScale:fit,titleFontPx:Number(fontPx.toFixed(1)),
            slideHeight:Math.round(sr.height),
            contentHeight:Math.round(ir.height),
            contentBottomOverflow:Math.max(0,Math.round(ir.bottom-availableBottom)),
            contentRightOverflow:Math.max(0,Math.round(ir.right-availableRight)),
            browserHorizontalOverflow:document.documentElement.scrollWidth-innerWidth,
            overlaps,images:imgs,elements
          };
        }"""
    )


def capture_contact_sheets(folder: Path, prefix: str, viewport: tuple[int,int]):
    files = sorted(folder.glob("*.jpg"))
    if not files:
        return
    width, height = viewport
    thumb_w = 390
    thumb_h = round(height * thumb_w / width)
    cols, rows = 4, 4
    cell_w, cell_h = thumb_w + 20, thumb_h + 43
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 17
    )
    for start in range(0, len(files), cols * rows):
        batch = files[start:start+cols*rows]
        sheet = Image.new("RGB", (cols*cell_w, rows*cell_h), "#f4f7f9")
        draw = ImageDraw.Draw(sheet)
        for k, file in enumerate(batch):
            image = Image.open(file).convert("RGB")
            image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            x = (k % cols)*cell_w+10
            y = (k // cols)*cell_h+10
            sheet.paste(image, (x, y))
            draw.text((x, y + thumb_h+5), file.stem, fill="#1a3347", font=font)
        target = OUTPUT / f"{prefix}_contact_{start//(cols*rows)+1:02d}.jpg"
        sheet.save(target, quality=82, optimize=True)


def main():
    findings = []
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        for width, height in VIEWPORTS:
            page = browser.new_page(
                viewport={"width":width,"height":height},
                device_scale_factor=1
            )
            for deck, expected in DECKS.items():
                shots = OUTPUT / f"{deck}_{width}x{height}"
                shots.mkdir(exist_ok=True)
                page.goto(f"{BASE_URL}/{deck}.html#slide-1",
                          wait_until="load", timeout=45000)
                page.evaluate("document.fonts.ready")
                actual = page.locator(".slide").count()
                if actual != expected:
                    findings.append({
                       "deck":deck,"viewport":f"{width}x{height}",
                       "severity":"critical","kind":"count",
                       "expected":expected,"actual":actual
                    })
                for index in range(1,actual+1):
                    page.evaluate("(n)=>{location.hash='#slide-'+n;}",index)
                    page.wait_for_function(
                        "(n)=>document.querySelector('.slide.active')"
                        " && Number(location.hash.replace('#slide-',''))===n",
                        arg=index, timeout=8000
                    )
                    page.evaluate(
                        "() => new Promise(resolve => requestAnimationFrame("
                        "()=>requestAnimationFrame(resolve)))"
                    )
                    page.wait_for_timeout(75)
                    info = inspect_slide(page)
                    record = {
                        "deck":deck,"slide":index,
                        "viewport":f"{width}x{height}",
                        **info
                    }
                    findings.append(record)
                    page.screenshot(
                        path=str(shots/f"{index:03d}.jpg"),
                        type="jpeg", quality=64,
                        animations="disabled", full_page=False
                    )
                capture_contact_sheets(
                    shots,f"{deck}_{width}x{height}",(width,height)
                )
            page.close()
        browser.close()

    (OUTPUT/"report.json").write_text(
        json.dumps(findings,ensure_ascii=False,indent=2),encoding="utf-8"
    )
    summary = []
    for row in findings:
        if "slide" not in row:
            continue
        issues=[]
        if row["contentBottomOverflow"] > 6:
            issues.append("bottom_overflow")
        if row["contentRightOverflow"] > 6:
            issues.append("right_overflow")
        if row["fitScale"] < 0.78:
            issues.append("heavy_shrink")
        elif row["fitScale"] < 0.9:
            issues.append("shrink")
        if row["overlaps"]:
            issues.append("overlap")
        if any(not x["loaded"] for x in row["images"]):
            issues.append("broken_image")
        if issues:
            summary.append({
                "deck":row["deck"],"slide":row["slide"],
                "viewport":row["viewport"],"title":row["title"],
                "fit":row["fitScale"],"bottom":row["contentBottomOverflow"],
                "right":row["contentRightOverflow"],
                "overlaps":row["overlaps"][:3],"issues":issues
            })

    (OUTPUT/"issues.json").write_text(
        json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8"
    )
    print("VISUAL_AUDIT_OVERVIEW",json.dumps({
        "rendered":len([x for x in findings if "slide" in x]),
        "issue_records":len(summary),
        "categories":dict(Counter(t for r in summary for t in r["issues"])),
        "min_fit":min((x["fitScale"] for x in findings
                        if "slide" in x),default=None),
    },ensure_ascii=False))
    for entry in sorted(summary,key=lambda x: (
            x["fit"],-x["bottom"]))[:55]:
        print("VISUAL_ISSUE",json.dumps(entry,ensure_ascii=False))
    print("VISUAL_AUDIT_COMPLETE",OUTPUT)


if __name__ == "__main__":
    main()
