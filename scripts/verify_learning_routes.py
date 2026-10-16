"""Browser QA: 67-slide Intro -> CNN-first course, numeric tensors and sidebar."""
from __future__ import annotations

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = os.getenv("AUDIT_BASE_URL", "http://127.0.0.1:8765")
OUT = Path(__file__).resolve().parents[1] / "visual_audit_output"
DECKS = (("intro",19),("vision_ai_course",48))


def check(ok, why):
    if not ok:
        raise AssertionError(why)


def position(page, deck, slide, total):
    page.wait_for_url(f"**/{deck}.html#slide-{slide}")
    page.wait_for_function(
        "n => document.querySelector('[data-slide-current]')?.textContent.trim() === String(n)",
        arg=slide
    )
    check(page.locator(".slide.active").count() == 1, "exactly one active slide")
    check(page.locator("[data-slide-total]").inner_text() == str(total),
          f"{deck}: expected total {total}")


def main():
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True,
            args=["--no-sandbox","--disable-dev-shm-usage"])
        page = browser.new_page(viewport={"width":1366,"height":768})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(BASE+"/index.html")
        position(page,"intro",1,19)
        check(page.locator("[data-slide-prev]").is_disabled(), "Intro must start at 1")
        check(page.locator(".lecture-toc-toggle").is_visible(), "TOC toggle missing")
        check(page.locator("#lecture-toc-drawer").get_attribute("aria-hidden")=="true",
              "Sidebar must start closed")
        page.click(".lecture-toc-toggle")
        check(page.locator(".lecture-toc-link").count()==67, "Sidebar should show 67 slides")
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded")=="true",
              "TOC not opened")
        toc = page.locator(".lecture-toc-sections")
        toc.evaluate("(el) => el.scrollTop=0")
        toc.hover(position={"x":90,"y":170})
        page.mouse.wheel(0,450)
        page.wait_for_function(
            "() => document.querySelector('.lecture-toc-sections').scrollTop > 0"
        )
        position(page,"intro",1,19)
        page.keyboard.press("PageDown")
        position(page,"intro",1,19)
        page.locator('.lecture-toc-link[href="intro.html#slide-3"]').click()
        position(page,"intro",3,19)
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded")=="false",
              "TOC should close after selection")
        page.click(".lecture-toc-toggle")
        page.keyboard.press("Escape")
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded")=="false",
              "Escape should close TOC")
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-backdrop").click(position={"x":850,"y":220})
        check(page.locator(".lecture-toc-toggle").get_attribute("aria-expanded")=="false",
              "Backdrop click should close TOC")

        # Direct-link across topic chapters, without introducing YOLO repeats.
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-unit").nth(1).locator("summary").click()
        page.locator('.lecture-toc-link[href="vision_ai_course.html#slide-3"]').click()
        position(page,"vision_ai_course",3,48)
        check("Detection" in page.locator(".slide.active").inner_text(),
              "Detection content must precede CNN concepts")
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-unit").nth(2).locator("summary").click()
        page.locator('.lecture-toc-link[href="vision_ai_course.html#slide-7"]').click()
        position(page,"vision_ai_course",7,48)
        check(page.locator(".slide.active").get_attribute("data-source-deck")=="ai_basics",
              "AI fundamentals not interleaved")
        page.click(".lecture-toc-toggle")
        page.locator(".lecture-toc-close").click()

        for deck,total in DECKS:
            page.goto(f"{BASE}/{deck}.html#slide-1")
            position(page,deck,1,total)
            for idx in range(2,total+1):
                page.click("[data-slide-next]")
                position(page,deck,idx,total)
        page.goto(BASE+"/intro.html#slide-19")
        page.click("[data-slide-next]")
        position(page,"vision_ai_course",1,48)
        page.click("[data-slide-prev]")
        position(page,"intro",19,19)
        page.goto(BASE+"/vision_ai_course.html#slide-48")
        check(page.locator("[data-slide-next]").is_disabled(), "Last slide must end course")

        # CNN comes with the WHY, not merely another structure diagram.
        expected_titles = {
            8:"CNN을 쓰는 이유",
            9:"CNN 전체 구조",
            18:"AND는 직선",
            19:"ReLU · XOR",
            20:"비선형성이 없으면",
            25:"Stride",
            26:"Padding",
            27:"Max Pooling",
        }
        for idx,title in expected_titles.items():
            page.goto(BASE+f"/vision_ai_course.html#slide-{idx}")
            position(page,"vision_ai_course",idx,48)
            check(title in page.locator(".slide.active").inner_text(),
                  f"Wrong course concept at {idx}: {title}")
        page.goto(BASE+"/vision_ai_course.html#slide-18")
        check(page.locator(".slide.active svg").count()==2,
              "AND/XOR must have two separate decision diagrams")
        page.goto(BASE+"/vision_ai_course.html#slide-19")
        trs = page.locator(".slide.active .logic-table tbody tr")
        check(trs.count()==4,"XOR must show all 4 input combinations")
        for i,v in enumerate((0,1,1,0)):
            check(trs.nth(i).locator("td").last.inner_text()==str(v),
                  f"XOR truth table mismatch at {i}")
        page.goto(BASE+"/vision_ai_course.html#slide-20")
        check("W₂(W₁x+b₁)+b₂" in page.locator(".slide.active").inner_text(),
              "Affine composition equation missing")

        def matrices(idx):
            page.goto(BASE+f"/vision_ai_course.html#slide-{idx}")
            position(page,"vision_ai_course",idx,48)
            return [[int(t.inner_text()) for t in a.locator("span").all()]
                    for a in page.locator(".slide.active .matrix-grid").all()]

        check(matrices(25)==[
            list(range(1,26)),[7,8,9,12,13,14,17,18,19],[7,9,17,19]
        ],"Stride 1 vs 2 values incorrect")
        check(matrices(26)==[
            list(range(1,10)),
            [0,0,0,0,0,0,1,2,3,0,0,4,5,6,0,0,7,8,9,0,0,0,0,0,0],
            [12,21,16,27,45,33,24,39,28]
        ],"Zero padding values incorrect")
        check(matrices(27)==[
            [1,3,2,4,5,8,7,6,2,1,9,0,3,4,5,6],[8,7,4,9]
        ],"2x2 Max Pooling values incorrect")

        page.goto(BASE+"/vision_ai_course.html?mode=core#slide-24")
        position(page,"vision_ai_course",24,48)
        check("mode=core" not in page.url,"Legacy mode query must be ignored")
        page.click("header a.brand")
        position(page,"intro",1,19)
        check(not errors, "JS errors: "+repr(errors))
        page.screenshot(path=str(OUT/"cnn_and_spatial_lecture_navigation.jpg"),
                        type="jpeg",quality=80)
        browser.close()
        print("VISION_FIRST_NAV_QA_PASSED: Intro19 + Vision CNN fundamentals48 = 67")
        print("RETRACTABLE_TOC_QA_PASSED: 67 links and direct chapter navigation")
        print("CNN_XOR_SPATIAL_VALUES_QA_PASSED: AND, XOR, Stride, Padding, Pooling")


if __name__ == "__main__":
    main()
