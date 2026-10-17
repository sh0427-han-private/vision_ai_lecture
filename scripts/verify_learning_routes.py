"""Browser QA: Intro -> integrated Vision/AI course plus retractable sidebar."""
from __future__ import annotations

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = os.getenv("AUDIT_BASE_URL","http://127.0.0.1:8765")
OUT = Path(__file__).resolve().parents[1] / "visual_audit_output"
DECKS = (("intro",19),("vision_ai_course",49))


def check(flag, why):
    if not flag:
        raise AssertionError(why)


def position(page, deck, slide, total):
    page.wait_for_url(f"**/{deck}.html#slide-{slide}")
    # A TOC anchor changes the hash before the browser fires hashchange;
    # wait for the actual slide render rather than only URL navigation.
    page.wait_for_function(
        "n => document.querySelector('[data-slide-current]')?.textContent"
        ".trim() === String(n)", arg=slide
    )
    check(page.locator(".slide.active").count() == 1, "active slide count")
    check(page.locator("[data-slide-current]").inner_text() == str(slide),
          f"{deck} current {slide}")
    check(page.locator("[data-slide-total]").inner_text() == str(total),
          f"{deck} expected {total}")


def main():
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page(viewport={"width":1366,"height":768})
        errors = []
        page.on("pageerror",lambda e: errors.append(str(e)))

        # Legacy URLs previously shared as /docs/*.html should redirect to
        # the Pages root while preserving slide numbers and search parameters.
        page.goto(BASE + "/docs/vision_ai_course.html#slide-9")
        position(page, "vision_ai_course", 9, 49)
        check("/docs/" not in page.url, "Legacy course URL not normalized")
        page.goto(BASE + "/docs/vision_ai_course.html?from=legacy#slide-9")
        page.wait_for_url("**/vision_ai_course.html?from=legacy#slide-9")
        check(page.locator("[data-slide-current]").inner_text() == "9",
              "Legacy course query/hash not retained")
        page.goto(BASE + "/docs/intro.html#slide-7")
        position(page, "intro", 7, 19)
        check("/docs/" not in page.url, "Legacy Intro URL not normalized")
        page.goto(BASE + "/docs/")
        position(page, "intro", 1, 19)

        page.goto(BASE + "/index.html")
        position(page,"intro",1,19)
        check(page.locator("[data-slide-prev]").is_disabled(),
              "Intro 1 previous button not disabled")
        check(page.locator(".lecture-toc-toggle").is_visible(),
              "Intro sidebar toggle is missing")
        check(page.locator("#lecture-toc-drawer").get_attribute("aria-hidden") == "true",
              "Sidebar should initially be closed")

        # Toggle open, select a different slide, and return via both controls.
        page.click(".lecture-toc-toggle")
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded") == "true",
              "TOC toggle did not open")
        check(page.locator("#lecture-toc-drawer").get_attribute("aria-hidden") == "false",
              "TOC drawer is not accessible when open")
        check(page.locator(".lecture-toc-link").count() == 68,
              "TOC must list all 68 slides")
        # Wheel scrolls the outline contents, but never advances the lecture.
        toc = page.locator(".lecture-toc-sections")
        toc.evaluate("(el) => { el.scrollTop = 0; }")
        check(toc.evaluate("(el) => el.scrollHeight > el.clientHeight"),
              "TOC should have scrollable contents")
        toc.hover(position={"x": 100, "y": 170})
        page.mouse.wheel(0, 540)
        page.wait_for_function(
            "() => document.querySelector('.lecture-toc-sections').scrollTop > 0"
        )
        position(page,"intro",1,19)
        page.mouse.wheel(0, -260)
        position(page,"intro",1,19)
        page.mouse.move(800, 260)
        page.mouse.wheel(0, 400)
        position(page,"intro",1,19)
        page.keyboard.press("PageDown")
        position(page,"intro",1,19)
        check(page.locator('.lecture-toc-link[aria-current="page"]').count() == 1,
              "TOC active link missing")
        page.locator('.lecture-toc-link[href="intro.html#slide-3"]').click()
        position(page,"intro",3,19)
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded") == "false",
              "Selecting slide should close sidebar")
        page.click(".lecture-toc-toggle")
        page.keyboard.press("Escape")
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded") == "false",
              "Escape did not dismiss TOC")
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-backdrop").click(position={"x":800,"y":200})
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded") == "false",
              "Outside click did not dismiss TOC")

        # Vision tasks must come before the AI theory section.
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-unit").nth(1).locator("summary").click()
        page.locator('.lecture-toc-link[href="vision_ai_course.html#slide-3"]').click()
        position(page,"vision_ai_course",3,49)
        check("Detection · 위치와 종류 찾기" in page.locator(".slide.active").inner_text(),
              "Expected object detection before general AI")
        check(page.locator(".slide.active").get_attribute("data-source-deck") == "vision_ai",
              "Vision content did not come first")
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-unit").nth(2).locator("summary").click()
        page.locator('.lecture-toc-link[href="vision_ai_course.html#slide-7"]').click()
        position(page,"vision_ai_course",7,49)
        check(page.locator(".slide.active").get_attribute("data-source-deck") == "ai_basics",
              "AI theory is not interleaved after vision tasks")
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-sections").hover(position={"x": 100, "y": 170})
        page.mouse.wheel(0, 630)
        position(page,"vision_ai_course",7,49)
        page.locator(".lecture-toc-close").click()
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded") == "false",
              "TOC close button failed")

        # All 68 published slides are reachable by next, no AI chapter detour.
        for deck,total in DECKS:
            page.goto(f"{BASE}/{deck}.html#slide-1")
            position(page,deck,1,total)
            check(page.locator("[data-lesson-mode-toggle]").count() == 0,
                  "Removed core mode came back")
            for i in range(2,total+1):
                page.click("[data-slide-next]")
                position(page,deck,i,total)
        page.goto(BASE+"/intro.html#slide-19")
        page.click("[data-slide-next]")
        position(page,"vision_ai_course",1,49)
        page.click("[data-slide-prev]")
        position(page,"intro",19,19)
        page.goto(BASE+"/vision_ai_course.html#slide-49")
        check(page.locator("[data-slide-next]").is_disabled(),
              "Final slide must end course")

        # New pedagogical sequence with numerically faithful before/after grids.
        for slide_number, phrase in (
            (8,"왜 CNN을 사용할까?"),
            (16,"퍼셉트론"),
            (17,"활성화 함수가 없으면"),
            (18,"AND와 XOR"),
            (19,"ReLU"),
            (20,"XOR 계산"),
            (21,"선형 변환 사이"),
            (26,"Stride"),
            (27,"Padding"),
            (28,"Max Pooling"),
        ):
            page.goto(BASE + f"/vision_ai_course.html#slide-{slide_number}")
            position(page,"vision_ai_course",slide_number,49)
            check(phrase in page.locator(".slide.active").inner_text(),
                  f"Pedagogical slide {slide_number} missing")
        check(page.locator(".slide.active .concept-matrix").count() == 2,
              "Max Pooling must show both before/after numeric matrices")
        page.click(".lecture-toc-toggle")
        check(page.locator(".lecture-toc-link").count() == 68,
              "Sidebar should reflect updated 68-slide course")
        page.locator(".lecture-toc-close").click()

        # Sequence: whole CNN first, then real maps, learned features and Kernel.
        page.goto(BASE + "/vision_ai_course.html#slide-9")
        position(page,"vision_ai_course",9,49)
        check("CNN 전체 구조" in page.locator(".slide.active").inner_text(),
              "CNN architecture must precede Kernel arithmetic")
        page.goto(BASE + "/vision_ai_course.html#slide-13")
        position(page,"vision_ai_course",13,49)
        check("Kernel" in page.locator(".slide.active").inner_text(),
              "Kernel concept must follow CNN overview")
        page.goto(BASE + "/vision_ai_course.html#slide-15")
        position(page,"vision_ai_course",15,49)
        check(page.locator(".slide.active .kernel-optional-images").count()==1,
              "Fixed-filter examples must be optional")
        # Two distinct explanations: actual activation maps vs. learned patterns.
        page.goto(BASE + "/vision_ai_course.html#slide-10")
        position(page,"vision_ai_course",10,49)
        check("SqueezeNet" in page.locator(".slide.active").inner_text(),
              "Actual CNN map slide missing")
        check(page.locator(".slide.active .cnn-real-image img").count() == 1,
              "Real feature map figure missing")
        page.goto(BASE + "/vision_ai_course.html#slide-11")
        position(page,"vision_ai_course",11,49)
        check("VGG-16" in page.locator(".slide.active").inner_text(),
              "CS231n visualisation should follow actual feature maps")

        # Old query strings must not activate the removed core-only feature.
        page.goto(BASE+"/vision_ai_course.html?mode=core#slide-21")
        position(page,"vision_ai_course",21,49)
        check("mode=core" not in page.url,"Legacy core param persists")
        check(page.locator(".slide.active").get_attribute("data-level") in ("basic","detail"),
              "Legacy core mode cannot hide content")
        page.goto(BASE+"/vision_ai_course.html#slide-18")
        page.click("header a.brand")
        position(page,"intro",1,19)
        check(not errors,"Browser JS errors: "+repr(errors))
        page.screenshot(path=str(OUT/"vision_first_sidebar_navigation.jpg"),
                        type="jpeg",quality=80)
        browser.close()
        print("VISION_FIRST_NAV_QA_PASSED: Intro19 -> integrated Vision+CNN49 = 68")
        print("RETRACTABLE_TOC_QA_PASSED: 68 links, click, close, outside and Escape")


if __name__ == "__main__":
    main()
