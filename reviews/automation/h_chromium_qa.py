"""Independent pinned-H Chromium geometry, image, canvas and navigation QA.

Runs on review branch created directly from 4469656244e55476b2c0e8ca2a1344a9710a29db.
No builder sources are changed. Screenshots are evaluated by a reviewer separately.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get("AUDIT_BASE_URL", "http://127.0.0.1:8766")
OUT = Path("reviews/evidence/h-4469656-browser")
OUT.mkdir(parents=True, exist_ok=True)
SHA = "4469656244e55476b2c0e8ca2a1344a9710a29db"
TARGETS = [
    (40, "workflow", "P53"),
    (41, "project-iterate", "P54"),
    (42, "project-check", "P55"),
]
SIZES = [(1920, 1080), (1366, 768)]


def inspect(page):
    return page.evaluate("""() => {
      const section = document.querySelector('.slide.active');
      const inner = section.querySelector('.slide-inner');
      const outer = section.getBoundingClientRect();
      const rect = inner.getBoundingClientRect();
      const style = getComputedStyle(section);
      const padB = parseFloat(style.paddingBottom);
      const padR = parseFloat(style.paddingRight);
      const headings = [...inner.querySelectorAll('h2,h3')].map(el => {
        const r = el.getBoundingClientRect();
        return {text: el.textContent.trim(), x:r.x, y:r.y,
                bottom:r.bottom, right:r.right};
      });
      const photoUrls=[...section.querySelectorAll('svg image')]
        .map(x=>x.getAttribute('href'));
      const canvas=[...section.querySelectorAll('[data-h-review-resolution]')]
        .map(c=>{
          const pixels=c.getContext('2d').getImageData(0,0,c.width,c.height).data;
          let count=0, min=255, max=0;
          for(let i=0;i<pixels.length;i+=4){
            if(pixels[i+3]>0)count++;
            min=Math.min(min,pixels[i],pixels[i+1],pixels[i+2]);
            max=Math.max(max,pixels[i],pixels[i+1],pixels[i+2]);
          }
          return {nominal:+c.dataset.hReviewResolution, width:c.width,height:c.height,
                  ready:c.dataset.ready||null, nonTransparent:count, min,max};
        });
      const answerIds=[...section.querySelectorAll('[data-review-answer]')]
        .map(x=>x.dataset.reviewAnswer);
      return {
        concept:section.dataset.concept, fit:+(section.dataset.fitScale||1),
        title:section.querySelector('.slide-title')?.textContent.trim(),
        viewport:{width:innerWidth,height:innerHeight}, headings,
        contentBottomOverflow:Math.max(0,Math.round(rect.bottom-outer.bottom+padB)),
        contentRightOverflow:Math.max(0,Math.round(rect.right-outer.right+padR)),
        browserHorizontalOverflow:document.documentElement.scrollWidth-innerWidth,
        photoUrls,canvas,answerIds,
        figureSvgs:section.querySelectorAll('svg').length,
        questionLines:section.querySelectorAll('[data-question-node]').length,
        workflowNodes:section.querySelectorAll('[data-review-node]').length,
        resourceStatus:performance.getEntriesByType('resource').filter(x=>
          x.name.includes('vision_task_apple_reference.jpg'))
          .map(x=>({name:x.name,bytes:x.transferSize,duration:x.duration}))
      };
    }""")


def verify(row, expected):
    assert row["concept"] == expected, row
    assert row["fit"] >= 0.90, ("excessive zoom", row)
    assert row["contentBottomOverflow"] <= 6, ("bottom overflow", row)
    assert row["contentRightOverflow"] <= 6, ("right overflow", row)
    assert row["browserHorizontalOverflow"] <= 1, ("horizontal scroll", row)
    assert len(row["photoUrls"]) >= 1, ("missing source photo", row)
    assert all(url == "assets/vision_task_apple_reference.jpg"
               for url in row["photoUrls"]), row["photoUrls"]
    if expected == "workflow":
        assert row["workflowNodes"] == 5 and row["questionLines"] == 4, row
    if expected == "project-iterate":
        assert {x["nominal"] for x in row["canvas"]} == {240,24}, row
        assert all(x["ready"] == "true"
                   and x["width"] == x["height"] == x["nominal"]
                   and x["nonTransparent"] == x["width"] ** 2
                   and x["max"] > x["min"] for x in row["canvas"]), row
    if expected == "project-check":
        assert row["answerIds"] == ["pixel", "feature", "learn", "evaluate"], row


def main():
    results = {"fixed_source": SHA, "screens": [], "page_errors": [],
               "navigation": [], "details": [], "failures": []}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        for width,height in SIZES:
            page = browser.new_page(viewport={"width":width,"height":height},
                                    device_scale_factor=1)
            page.on("pageerror",lambda err:results["page_errors"].append(str(err)))
            for number,concept,plan in TARGETS:
                page.goto(f"{BASE_URL}/vision_ai_course.html#slide-{number}",
                          wait_until="load",timeout=45000)
                page.evaluate("document.fonts.ready")
                page.wait_for_function(
                  "(name)=>document.querySelector('.slide.active')?.dataset.concept===name",
                  arg=concept,timeout=12000)
                if concept=="project-iterate":
                    page.wait_for_function(
                      "()=>[...document.querySelectorAll('[data-h-review-resolution]')]"
                      ".length===2&&[...document.querySelectorAll("
                      "'[data-h-review-resolution]')].every(x=>x.dataset.ready==='true')",
                      timeout=12000)
                page.wait_for_timeout(250)
                row=inspect(page)
                row.update({"plan":plan,"viewport":f"{width}x{height}"})
                results["screens"].append(row)
                try: verify(row,concept)
                except Exception as exc:
                    results["failures"].append(f"{plan} {width}x{height}: {exc}")
                page.screenshot(path=str(OUT/f"{plan}-{width}x{height}.png"),
                                animations="disabled",full_page=False)
                if number == 42:
                    page.locator("details.project-answer summary").click()
                    opened=page.locator("details.project-answer").evaluate(
                        "(x)=>x.open")
                    results["details"].append({"viewport":f"{width}x{height}",
                                               "opened":opened})
                    if not opened:results["failures"].append("P55 details did not open")
                    page.locator("details.project-answer summary").click()
                    closed=not page.locator("details.project-answer").evaluate(
                        "(x)=>x.open")
                    if not closed:results["failures"].append("P55 details did not close")
                    page.locator("body").click(position={"x":50,"y":120})
                    page.keyboard.press("ArrowLeft")
                    page.wait_for_function("()=>location.hash==='#slide-41'")
                    page.keyboard.press("ArrowRight")
                    page.wait_for_function("()=>location.hash==='#slide-42'")
                    results["navigation"].append({"viewport":f"{width}x{height}",
                                                  "keyboard":"42→41→42 PASS"})
            page.close()
        browser.close()
    (OUT/"report.json").write_text(
        json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    overview={"source":SHA,"screens":len(results["screens"]),
              "page_errors":results["page_errors"],"failures":results["failures"],
              "min_fit":min((x["fit"] for x in results["screens"]),default=None),
              "canvas":[{"viewport":r["viewport"],"data":r["canvas"]}
                        for r in results["screens"] if r["canvas"]]}
    print("REVIEW_H_CHROMIUM_OVERVIEW",json.dumps(overview,ensure_ascii=False))
    assert not results["page_errors"] and not results["failures"], overview


if __name__=="__main__":
    main()
