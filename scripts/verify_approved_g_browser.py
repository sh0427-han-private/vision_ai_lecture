"""Browser-level re-review for G P48-P52 at two presentation resolutions.

Run with a local server: python -m http.server 8765 --directory docs
Then: python scripts/verify_approved_g_browser.py

Images, checks and observed layout are written to visual_audit_output/approved_g/.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_visual_slides import inspect_slide  # noqa: E402

BASE_URL = os.getenv("AUDIT_BASE_URL", "http://127.0.0.1:8765")
OUT = ROOT / "visual_audit_output" / "approved_g"
OUT.mkdir(parents=True, exist_ok=True)
MANIFEST = json.loads(
    (ROOT / "docs/two_hour_manifest.json").read_text(encoding="utf-8")
)
COURSE = {
    item["concept"]: item["slide"]
    for item in MANIFEST["decks"]["vision_ai_course"]
}
CONCEPTS = ("threshold", "confusion", "imbalance", "metrics", "iou")
VIEWPORTS = ((1920, 1080), (1366, 768))
EXPECTED = {
    "0.3": ((20, 0, 30, 50), "Precision 40.0% · Recall 100.0%"),
    "0.5": ((18, 2, 4, 76), "Precision 81.8% · Recall 90.0%"),
    "0.7": ((11, 9, 2, 78), "Precision 84.6% · Recall 55.0%"),
}
EXPECTED_BINS = {
    2: (0, 50), 4: (2, 26), 6: (7, 2), 8: (11, 2),
}
REPORT = {"screens": [], "interactions": [], "console_errors": [],
          "page_errors": [], "issues": []}


def check_counts(page, value: str) -> None:
    root = page.locator(".slide.active [data-project-evaluation]")
    assert root.get_attribute("data-ready") == "true"
    assert root.get_attribute("data-threshold") == value
    expected_counts, result = EXPECTED[value]
    for name, number in zip(("tp", "fn", "fp", "tn"), expected_counts):
        assert root.locator(f"[data-project-{name}]").inner_text() == str(number)
    assert root.locator("[data-project-result]").inner_text() == result
    for name, number in zip(("fn", "fp"),
                            (expected_counts[1], expected_counts[2])):
        bar = root.locator(f"[data-project-{name}-bar]")
        label = root.locator(f"[data-project-{name}-label]")
        assert int(bar.get_attribute("value")) == number
        assert label.inner_text() == f"{number}건"
    svg = root.locator("[data-score-histogram]")
    assert float(svg.locator("[data-threshold-line]").get_attribute(
        "data-threshold-line"
    )) == float(value)
    path = svg.locator("[data-threshold-line]").get_attribute("d")
    x = float(re.search(r"M([0-9.]+)", path).group(1))
    assert abs(x - (58 + 490 * float(value))) < 0.01, (x, value)
    REPORT["interactions"].append({"threshold": value,
                                   "counts": expected_counts, "result": result})


def check_bins(page) -> None:
    bins = page.locator(".slide.active [data-score-bin]").evaluate_all(
        """els => els.map(el => ({
            bin:Number(el.dataset.scoreBin),
            pos:Number(el.dataset.positive),
            neg:Number(el.dataset.negative),
            rectangles:[...el.querySelectorAll('rect')].map(r => ({
                y:Number(r.getAttribute('y')),
                height:Number(r.getAttribute('height'))
            }))
        }))"""
    )
    assert len(bins) == 10, bins
    for b in bins:
        assert (b["pos"], b["neg"]) == EXPECTED_BINS.get(
            b["bin"], (0, 0)
        ), b
        for rect in b["rectangles"]:
            assert rect["y"] >= 31.9, rect
            assert rect["y"] + rect["height"] <= 192.1, rect
    assert sum(b["pos"] for b in bins) == 20
    assert sum(b["neg"] for b in bins) == 80
    assert sum(b["pos"] + b["neg"] for b in bins) == 100
    svg_text = page.locator(
        ".slide.active [data-score-histogram]"
    ).text_content()
    assert "50" in svg_text, svg_text


def check_threshold_interactions(page) -> None:
    root = page.locator(".slide.active [data-project-evaluation]")
    select = root.locator("[data-project-threshold]")
    check_bins(page)
    check_counts(page, "0.5")
    select.select_option("0.3")
    check_counts(page, "0.3")
    select.select_option("0.7")
    check_counts(page, "0.7")
    select.focus()
    page.keyboard.press("Home")
    check_counts(page, "0.3")
    page.keyboard.press("End")
    check_counts(page, "0.7")
    button = root.locator("[data-project-reset]")
    button.focus()
    page.keyboard.press("Enter")
    assert select.input_value() == "0.5"
    check_counts(page, "0.5")
    select.select_option("0.3")
    button.click()
    check_counts(page, "0.5")
    check_bins(page)


def check_iou(page, blue: str) -> None:
    slide = page.locator(".slide.active")
    gt = slide.locator(".g55-iou svg rect[stroke='#187c9a']")
    assert gt.count() == 2, gt.count()
    assert slide.locator(
        ".g55-iou [data-iou-box='gt']"
    ).get_attribute("data-xyxy") == "1,1,6,7"
    assert slide.locator(
        ".g55-iou [data-iou-box='prediction']"
    ).get_attribute("data-xyxy") == "1,3,6,9"
    assert slide.locator(".g55-iou svg rect[stroke='#c17b27']").count() == 2
    legend = slide.locator(".g55-iou .g55-pos")
    assert legend.evaluate(
        "el => getComputedStyle(el).color"
    ) == blue
    image_ok = slide.locator(".g55-iou image").evaluate_all(
        """async images => Promise.all(images.map(async image => {
            const img = new Image();
            img.src = image.href.baseVal;
            try { await img.decode(); return img.naturalWidth > 0; }
            catch { return false; }
        }))"""
    )
    assert image_ok and all(image_ok), image_ok
    assert "IoU = 20 / (30+30−20) = 0.5" in slide.inner_text()


def check_slide(page, concept: str, viewport: str) -> None:
    no = COURSE[concept]
    page.goto(f"{BASE_URL}/vision_ai_course.html#slide-{no}",
              wait_until="load")
    page.wait_for_function(
        "(c) => document.querySelector('.slide.active')?.dataset.concept === c",
        arg=concept,
    )
    slide = page.locator(".slide.active")
    assert slide.locator(".slide-title").count() == 1
    if concept == "threshold":
        page.locator(
            ".slide.active [data-project-evaluation][data-ready='true']"
        ).wait_for()
        check_threshold_interactions(page)
    elif concept == "confusion":
        assert "TP" in slide.inner_text() and "FN" in slide.inner_text()
        assert "Threshold 0.50" in slide.inner_text()
        assert all(slide.locator(f".pf-{name} b").first.inner_text() == str(n)
                   for name, n in (("tp", 18), ("fn", 2),
                                   ("fp", 4), ("tn", 76)))
    elif concept == "imbalance":
        assert slide.locator(".pf-tilegrid span").count() == 100
        assert slide.locator(".pf-tilegrid .pf-miss").count() == 20
    elif concept == "metrics":
        assert slide.locator(".pf-card").count() == 2
        assert slide.locator(".pf-card").nth(0).locator(
            ".pf-metric-dots span"
        ).count() == 22
        assert slide.locator(".pf-card").nth(1).locator(
            ".pf-metric-dots span"
        ).count() == 20
    elif concept == "iou":
        check_iou(page, "rgb(24, 124, 154)")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(180)
    audit = inspect_slide(page)
    audit.update({"concept": concept, "viewport": viewport})
    screenshot = f"{viewport}_{concept}.png"
    page.screenshot(path=str(OUT / screenshot), animations="disabled")
    audit["screenshot"] = screenshot
    REPORT["screens"].append(audit)
    failures = {
        key: audit.get(key, 0)
        for key in ("contentBottomOverflow", "contentRightOverflow",
                    "browserHorizontalOverflow")
        if audit.get(key, 0) > 6
    }
    if failures or audit.get("overlaps") or audit.get("error"):
        REPORT["issues"].append(
            {"concept": concept, "viewport": viewport, "failures": failures,
             "overlaps": audit.get("overlaps", []),
             "error": audit.get("error")}
        )


def main() -> None:
    REPORT["head"] = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"])
        for width, height in VIEWPORTS:
            viewport = f"{width}x{height}"
            page = browser.new_page(
                viewport={"width": width, "height": height}
            )
            page.on("pageerror", lambda e: REPORT["page_errors"].append(str(e)))
            page.on("console", lambda m: REPORT["console_errors"].append(
                m.text) if m.type == "error" else None)
            # P14 reference figure, not an extra screenshot.
            page.goto(f"{BASE_URL}/vision_ai_course.html#slide-{COURSE['task']}",
                      wait_until="load")
            assert page.locator(
                ".slide.active svg [stroke='#187c9a']"
            ).count() >= 1
            for concept in CONCEPTS:
                check_slide(page, concept, viewport)
            page.close()
        browser.close()
    (OUT / "report.json").write_text(
        json.dumps(REPORT, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    assert len(REPORT["screens"]) == 10
    assert not REPORT["issues"], REPORT["issues"]
    assert not REPORT["page_errors"], REPORT["page_errors"]
    assert not REPORT["console_errors"], REPORT["console_errors"]
    print("APPROVED_G_BROWSER_QA_PASSED",
          json.dumps({"head": REPORT["head"], "screens": 10,
                      "interactive_checks": len(REPORT["interactions"])},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
