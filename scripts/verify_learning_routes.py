"""Browser QA for core/full navigation, including deep links and chapter handoffs."""
from __future__ import annotations

import os
from playwright.sync_api import sync_playwright

BASE = os.getenv("AUDIT_BASE_URL", "http://127.0.0.1:8765")
DECKS = {"ai_basics": (44, 36), "vision_ai": (40, 28)}


def check(flag: bool, message: str) -> None:
    if not flag:
        raise AssertionError(message)


def wait_slide(page, number: int) -> None:
    page.wait_for_function(
        "(n) => location.hash === '#slide-' + n && "
        "document.querySelector('.slide.active') !== null", arg=number
    )


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = browser.new_page(viewport={"width": 1366, "height": 768})
        page.goto(f"{BASE}/index.html")
        check(page.locator('a[href="intro.html?mode=core#slide-1"]').count() == 1,
              "homepage core route missing")
        check(page.locator('a[href="intro.html#slide-1"]').count() == 1,
              "homepage full route missing")

        # Core path begins with Intro (all Intro slides are essential).
        page.goto(f"{BASE}/intro.html?mode=core#slide-15")
        page.click("[data-slide-next]")
        page.wait_for_url("**/ai_basics.html?mode=core#slide-1")
        check(page.locator("[data-slide-total]").inner_text() == "36",
              "Intro to AI Basics core handoff lost route")
        check(page.locator("[data-lesson-mode-toggle]").get_attribute("aria-pressed") == "true",
              "AI core toggle not active")
        check("mode=core" in page.locator('.nav-links a[href^="vision_ai.html"]').get_attribute("href"),
              "chapter header link lost selected core route")

        for deck, (full, core) in DECKS.items():
            page.goto(f"{BASE}/{deck}.html?mode=core#slide-1")
            check(page.locator("[data-slide-total]").inner_text() == str(core),
                  f"{deck}: unexpected core length")
            check(page.locator("[data-lesson-mode-toggle]").count() == 1,
                  f"{deck}: core/full toggle missing")
            page.screenshot(
                path=str(__import__("pathlib").Path(__file__).resolve().parents[1]
                         / "visual_audit_output" / f"learning_route_{deck}_core.jpg"),
                type="jpeg", quality=80
            )
            for i in range(core):
                level = page.locator(".slide.active").get_attribute("data-level")
                check(level != "detail", f"{deck}: detail visited in core mode")
                check(page.locator("[data-slide-current]").inner_text() == str(i + 1),
                      f"{deck}: progress counter mismatch")
                if i < core - 1:
                    page.click("[data-slide-next]")
            # The last essential slide should be the last physical slide.
            check(page.url.endswith(f"#slide-{full}"),
                  f"{deck}: did not arrive at final slide")
            page.click("[data-lesson-mode-toggle]")
            check(page.locator("[data-slide-total]").inner_text() == str(full),
                  f"{deck}: full mode not restored")
            check("mode=core" not in page.url, f"{deck}: URL core flag retained")
            check("mode=core" not in page.locator('.nav-links a[href^="intro.html"]').get_attribute("href"),
                  f"{deck}: chapter header link retained core flag")
            page.click("[data-lesson-mode-toggle]")
            check(page.locator("[data-slide-total]").inner_text() == str(core),
                  f"{deck}: core mode toggle failed")

        # A deep link to an advanced slide in core mode resolves to the next
        # essential slide. For AI Basics, physical slide 5 is "detail".
        page.goto(f"{BASE}/ai_basics.html?mode=core#slide-5")
        wait_slide(page, 6)
        check(page.locator(".slide.active").get_attribute("data-level") == "basic",
              "advanced deep link should resolve to next essential slide")
        page.click("[data-lesson-mode-toggle]")
        page.click("[data-slide-prev]")
        wait_slide(page, 5)
        check(page.locator(".slide.active").get_attribute("data-level") == "detail",
              "full path must preserve detailed slide")
        page.goto(f"{BASE}/ai_basics.html?mode=core#slide-44")
        page.click("[data-slide-next]")
        page.wait_for_url("**/vision_ai.html?mode=core#slide-1")
        check(page.locator("[data-slide-total]").inner_text() == "28",
              "core mode lost at AI -> Vision handoff")

        browser.close()
        print("CORE_FULL_LEARNING_ROUTE_QA_PASSED: Intro15 + AI36 + Vision28 = 79")
        print("FULL_ROUTE_LENGTH: Intro15 + AI44 + Vision40 = 99")


if __name__ == "__main__":
    main()
