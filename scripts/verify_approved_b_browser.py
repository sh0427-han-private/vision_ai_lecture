"""Chromium QA for approved B P14-P18 (both presentation viewports).

Requires local HTTP server rooted at docs and playwright Chromium.
The educational photos and figures are illustrative, not model predictions.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = os.getenv("AUDIT_BASE_URL", "http://127.0.0.1:8765")
MANIFEST = json.loads((ROOT / "docs/two_hour_manifest.json").read_text())
COURSE = {
    item["concept"]: item["slide"]
    for item in MANIFEST["decks"]["vision_ai_course"]
}
OUT = ROOT / "visual_audit_output" / "approved_b"
OUT.mkdir(parents=True, exist_ok=True)


def is_loaded(page, selector: str) -> bool:
    return page.locator(selector).evaluate_all(
        "(els) => els.length > 0 && "
        "els.every(el => el.complete && el.naturalWidth > 0)"
    )


def check_figure(page, concept: str) -> dict:
    slide_no = COURSE[concept]
    page.goto(
        f"{BASE_URL}/vision_ai_course.html#slide-{slide_no}",
        wait_until="networkidle",
    )
    page.locator(".slide.active").wait_for()
    assert page.locator(".slide.active").get_attribute("data-concept") == concept
    slide = page.locator(".slide.active")
    summary = {"slide": slide_no, "concept": concept}
    assert page.locator(".slide.active .slide-title").count() == 1

    if concept == "task":
        assert slide.locator(".b55-tasks article").count() == 3
        assert slide.locator("svg").count() == 3
        assert "정답(GT)" in slide.inner_text()
    elif concept == "rules":
        assert slide.locator(".rl-python-rule").count() == 1
        code = slide.locator(".rl-python-code").inner_text()
        scope = {}
        exec(code, scope)
        assert scope["add"](1, 1) == 2
        assert scope["add"](2, 1) == 3
    elif concept == "rules-image":
        assert slide.locator(".rl-pane").count() == 2
        assert slide.locator(".b55-example").count() == 6
        assert slide.locator(".b55-model").count() == 1
        assert slide.locator(".b55-training").count() == 1
        assert slide.locator(".b55-inference").count() == 1
        assert slide.locator(".b55-prediction").count() == 1
        assert is_loaded(page, ".slide.active .b55-example img")
        assert is_loaded(page, ".slide.active .b55-new-photo img")
        pairs = page.evaluate(
            """() => {
                const panes = [...document.querySelectorAll(
                    '.slide.active .b55-panel'
                )];
                return [0, 1, 2].map(i => {
                    const a = panes[0].querySelectorAll('.b55-example')[i];
                    const b = panes[1].querySelectorAll('.b55-example')[i];
                    const ia = a.querySelector('img');
                    const ib = b.querySelector('img');
                    const ra = a.getBoundingClientRect();
                    const rb = b.getBoundingClientRect();
                    return {
                        labels: [a.innerText, b.innerText],
                        images: [ia.getAttribute('src'), ib.getAttribute('src')],
                        filters: [getComputedStyle(ia).filter,
                                  getComputedStyle(ib).filter],
                        heightDelta: Math.abs(ra.height - rb.height),
                        yDelta: Math.abs(ra.y - rb.y)
                    };
                });
            }"""
        )
        for pair in pairs:
            assert pair["labels"][0] == pair["labels"][1], pair
            assert pair["images"][0] == pair["images"][1], pair
            assert pair["filters"][0] == pair["filters"][1], pair
            assert pair["heightDelta"] < 3, pair
            assert pair["yDelta"] < 9, pair
        fonts = slide.locator(".b55-ml-path .b55-step strong").evaluate_all(
            "(els) => els.map(e => parseFloat(getComputedStyle(e).fontSize))"
        )
        assert fonts and min(fonts) >= 16, fonts
        shared = page.evaluate(
            """() => {
                const q = selector => document.querySelector(
                    '.slide.active ' + selector
                ).getBoundingClientRect();
                const t = q('.b55-training');
                const m = q('.b55-model');
                const i = q('.b55-inference');
                return {modelTop: m.top, trainTop: t.top,
                        modelBottom: m.bottom, inferBottom: i.bottom};
            }"""
        )
        assert shared["modelTop"] <= shared["trainTop"] + 3, shared
        assert shared["modelBottom"] >= shared["inferBottom"] - 3, shared
        summary["minimum_model_label_px"] = min(fonts)
        summary["matched_cases"] = 3
    elif concept == "model-choice":
        assert slide.locator(".b55-choice-row").count() == 3
        assert slide.locator(".b55-gate").count() == 3
        assert "사과 객체 인식 ≠ 결함 판정" in slide.inner_text()
    elif concept == "task-model-data":
        assert slide.locator(".b55-label-row").count() == 3
        assert slide.locator(".b55-label-gt").count() == 3
        assert "Mask" in slide.inner_text()

    return summary


def main() -> None:
    concepts = ["task", "rules", "rules-image", "model-choice",
                "task-model-data"]
    report = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True, args=["--no-sandbox"]
        )
        for width, height in [(1920, 1080), (1366, 768)]:
            page = browser.new_page(viewport={"width": width, "height": height})
            exceptions = []
            page.on("pageerror", lambda e: exceptions.append(str(e)))
            for concept in concepts:
                result = check_figure(page, concept)
                result["viewport"] = f"{width}x{height}"
                page.screenshot(
                    path=str(OUT / f"{result['viewport']}_{concept}.png"),
                    full_page=False,
                )
                report.append(result)
            assert not exceptions, exceptions
            page.close()
        browser.close()
    (OUT / "checks.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("APPROVED_B_BROWSER_QA_PASSED", json.dumps(
        {"renders": len(report), "concepts": concepts},
        ensure_ascii=False,
    ))


if __name__ == "__main__":
    main()
