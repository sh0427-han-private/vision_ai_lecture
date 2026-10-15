"""Browser QA for a single continuous Intro -> AI Basics -> Vision AI course."""
from __future__ import annotations

import os
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = os.getenv("AUDIT_BASE_URL", "http://127.0.0.1:8765")
DECKS = (("intro", 19), ("ai_basics", 44), ("vision_ai", 37))
OUT = Path(__file__).resolve().parents[1] / "visual_audit_output"


def check(flag: bool, message: str) -> None:
    if not flag:
        raise AssertionError(message)


def verify_position(page, deck: str, current: int, total: int) -> None:
    page.wait_for_url(f"**/{deck}.html#slide-{current}")
    check(page.locator(".slide.active").count() == 1,
          f"{deck} slide {current}: one active slide expected")
    check(page.locator("[data-slide-current]").inner_text() == str(current),
          f"{deck} slide {current}: current page counter incorrect")
    check(page.locator("[data-slide-total]").inner_text() == str(total),
          f"{deck} slide {current}: total page counter incorrect")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = browser.new_page(viewport={"width": 1366, "height": 768})

        # The former contents page now redirects immediately to Intro 1.
        page.goto(f"{BASE}/index.html")
        verify_position(page, "intro", 1, 19)
        check("AI는 세상을 어떻게 볼까?" in page.locator(".slide.active").inner_text(),
              "homepage did not open the original Intro first slide")
        check(page.locator("[data-slide-prev]").is_disabled(),
              "Intro 1 must be the beginning of the course")

        # There is no contents page, chapter picker, or basic/advanced mode.
        for deck, total in DECKS:
            page.goto(f"{BASE}/{deck}.html#slide-1")
            verify_position(page, deck, 1, total)
            check(page.locator(".nav-links").count() == 0,
                  f"{deck}: contents/chapter shortcut navigation still present")
            check(page.locator('[data-lesson-mode-toggle]').count() == 0,
                  f"{deck}: core-only toggle still present")
            check(page.locator('[data-lesson-mode-summary]').count() == 0,
                  f"{deck}: obsolete route label still present")
            check(page.locator('a:has-text("목차")').count() == 0,
                  f"{deck}: contents link still present")
            for i in range(1, total):
                page.click("[data-slide-next]")
                verify_position(page, deck, i + 1, total)
            # Previously skipped detail slides must be included.
            check(page.locator(".slide.active").count() == 1,
                  f"{deck}: final slide missing")

        # Both chapter boundaries work in either direction, without a menu.
        for src, src_total, dst, dst_total in (
            ("intro", 19, "ai_basics", 44),
            ("ai_basics", 44, "vision_ai", 37),
        ):
            page.goto(f"{BASE}/{src}.html#slide-{src_total}")
            page.click("[data-slide-next]")
            verify_position(page, dst, 1, dst_total)
            page.click("[data-slide-prev]")
            verify_position(page, src, src_total, src_total)

        page.goto(f"{BASE}/vision_ai.html#slide-37")
        check(page.locator("[data-slide-next]").is_disabled(),
              "Vision AI 37 should be the final slide")

        # Old bookmarks with ?mode=core must not filter any slides.
        for deck, slide_number, total in (
            ("ai_basics", 5, 44),
            ("vision_ai", 32, 37),
        ):
            page.goto(f"{BASE}/{deck}.html?mode=core#slide-{slide_number}")
            verify_position(page, deck, slide_number, total)
            check("mode=core" not in page.url,
                  f"{deck}: removed mode parameter persists")
            check(page.locator(".slide.active").get_attribute("data-level") == "detail",
                  f"{deck}: existing deep link to detail slide must work")

        # Site branding always returns to the first Intro slide.
        page.goto(f"{BASE}/vision_ai.html#slide-4")
        page.click("header a.brand")
        verify_position(page, "intro", 1, 19)
        page.screenshot(path=str(OUT / "learning_route_single_track.jpg"),
                        type="jpeg", quality=80)

        browser.close()
        print("SINGLE_TRACK_NAVIGATION_QA_PASSED: Intro19 -> AI44 -> Vision37 = 100")
        print("NO_CONTENTS_OR_CORE_MODE_QA_PASSED: old core links show full lesson")


if __name__ == "__main__":
    main()
