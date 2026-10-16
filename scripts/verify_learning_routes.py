"""Browser QA: Intro -> integrated Vision/AI course plus retractable sidebar."""
from __future__ import annotations

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = os.getenv("AUDIT_BASE_URL","http://127.0.0.1:8765")
OUT = Path(__file__).resolve().parents[1] / "visual_audit_output"
DECKS = (("intro",19),("vision_ai_course",48))


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
        position(page, "vision_ai_course", 9, 48)
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
        check(page.locator(".lecture-toc-link").count() == 67,
              "TOC must list all 67 slides")
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
        position(page,"vision_ai_course",3,48)
        check("Detection · 위치와 종류 찾기" in page.locator(".slide.active").inner_text(),
              "Expected object detection before general AI")
        check(page.locator(".slide.active").get_attribute("data-source-deck") == "vision_ai",
              "Vision content did not come first")
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-unit").nth(2).locator("summary").click()
        page.locator('.lecture-toc-link[href="vision_ai_course.html#slide-7"]').click()
        position(page,"vision_ai_course",7,48)
        check(page.locator(".slide.active").get_attribute("data-source-deck") == "ai_basics",
              "AI theory is not interleaved after vision tasks")
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-sections").hover(position={"x": 100, "y": 170})
        page.mouse.wheel(0, 630)
        position(page,"vision_ai_course",7,48)
        page.locator(".lecture-toc-close").click()
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded") == "false",
              "TOC close button failed")

        # All 67 published slides are reachable by next, no AI chapter detour.
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
        position(page,"vision_ai_course",1,48)
        page.click("[data-slide-prev]")
        position(page,"intro",19,19)
        page.goto(BASE+"/vision_ai_course.html#slide-48")
        check(page.locator("[data-slide-next]").is_disabled(),
              "Final slide must end course")

        # Slide content follows why-CNN -> convolution -> XOR -> numeric operations.
        for index,title in (
            (8,"왜 이미지에 CNN을 사용할까?"),
            (9,"CNN 전체 구조와 특징 추출"),
            (10,"실제 Feature Map"),
            (11,"Feature Visualization"),
            (18,"AND는 직선으로 구분, XOR는 불가능"),
            (19,"선형 Layer만 쌓으면 결국 하나의 Layer"),
            (20,"ReLU로 XOR를 표현하는 신경망"),
        ):
            page.goto(BASE+f"/vision_ai_course.html#slide-{index}")
            position(page,"vision_ai_course",index,48)
            check(title in page.locator(".slide.active").inner_text(),
                  f"Missing lecture content at slide {index}: {title}")

        def displayed_grids():
            return [[int(v) for v in matrix.locator(".cnn-cell").all_text_contents()]
                    for matrix in page.locator(".slide.active .cnn-number-grid").all()]

        page.goto(BASE+"/vision_ai_course.html#slide-25")
        position(page,"vision_ai_course",25,48)
        mats=displayed_grids()
        check(len(mats)==3,"Stride input and both outputs must be visible")
        check(mats[1]==[7,8,9,12,13,14,17,18,19],"Stride1 values")
        check(mats[2]==[7,9,17,19],"Stride2 values")

        page.goto(BASE+"/vision_ai_course.html#slide-26")
        position(page,"vision_ai_course",26,48)
        mats=displayed_grids()
        check(len(mats)==4,"Padding input, no pad, padded input and output")
        check(mats[1]==[45],"Without padding 3x3 sum should be 45")
        check(mats[2][:5]==[0]*5,"Padding zero border")
        check(mats[3]==[12,21,16,27,45,33,24,39,28],
              "Padding1 output does not match 3x3 kernel sum")

        page.goto(BASE+"/vision_ai_course.html#slide-27")
        position(page,"vision_ai_course",27,48)
        mats=displayed_grids()
        check(len(mats)==2 and mats[1]==[6,8,3,4],"2x2 Max Pooling")

        page.goto(BASE+"/vision_ai_course.html#slide-20")
        position(page,"vision_ai_course",20,48)
        rows=page.locator(".slide.active .cnn-truth-table tbody tr")
        check(rows.count()==4,"ReLU XOR requires four binary input cases")
        check([int(row.locator("td").last.inner_text()) for row in rows.all()]
              ==[0,1,1,0],"XOR output from two ReLU hidden units")
        check(page.locator('.slide[data-source-deck="yolo_intro"]').count()==0,
              "Redundant YOLO slides remain in public course")

        # Old query strings must not activate the removed core-only feature.
        page.goto(BASE+"/vision_ai_course.html?mode=core#slide-21")
        position(page,"vision_ai_course",21,48)
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
        print("VISION_FIRST_NAV_QA_PASSED: Intro19 -> integrated Vision+CNN48 = 67")
        print("RETRACTABLE_TOC_QA_PASSED: 67 links, click, close, outside and Escape")


if __name__ == "__main__":
    main()
