"""Browser QA for the interactive grayscale and RGB concept slides.

Usage: run a local server with docs/ as root on port 8765, then execute
python scripts/verify_intro_pixel_interactive.py (requires Playwright Chromium).
"""
from __future__ import annotations

import math
import re

from playwright.sync_api import sync_playwright


BASE_URL = "http://127.0.0.1:8765/intro.html"


def numbers(page, selector: str) -> list[int]:
    return [
        int(text)
        for text in page.locator(f"{selector} span").all_text_contents()
    ]


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1366, "height": 768})
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))

        page.goto(BASE_URL + "#slide-3", wait_until="networkidle")
        page.locator("[data-gray-coordinate]").wait_for()
        page.wait_for_function(
            "() => document.querySelector('[data-gray-values]')"
            ".children.length === 36"
        )
        initial = numbers(page, "[data-gray-values]")
        assert len(initial) == 36
        assert initial == numbers(page, "[data-gray-tones]")
        assert all(0 <= value <= 255 for value in initial)

        photo = page.locator("[data-gray-photo]")
        photo.click(position={"x": 48, "y": 48})
        first_coordinate = page.locator("[data-gray-coordinate]").inner_text()
        first_values = numbers(page, "[data-gray-values]")
        photo.click(position={"x": 275, "y": 165})
        second_coordinate = page.locator("[data-gray-coordinate]").inner_text()
        second_values = numbers(page, "[data-gray-values]")
        assert first_coordinate != second_coordinate
        assert first_values != second_values

        page.locator("[data-gray-brightness]").evaluate(
            """element => {
                element.value = '1.5';
                element.dispatchEvent(new Event('input', {bubbles:true}));
            }"""
        )
        brighter = numbers(page, "[data-gray-values]")
        assert brighter == [
            min(255, math.floor(value * 1.5 + 0.5))
            for value in second_values
        ]
        assert brighter == numbers(page, "[data-gray-tones]")
        page.locator("[data-gray-reset]").click()
        assert numbers(page, "[data-gray-values]") == second_values

        page.goto(BASE_URL + "#slide-5", wait_until="networkidle")
        page.wait_for_function(
            "() => document.querySelector('[data-rgb-shape]').textContent"
            ".includes('× 3')"
        )
        image = page.locator("[data-rgb-photo]")
        image.click(position={"x": 180, "y": 130})
        selected = page.locator("[data-rgb-coordinate]").inner_text()
        match = re.fullmatch(r"image\[y=(\d+), x=(\d+)\]", selected)
        assert match, selected
        selected_y, selected_x = map(int, match.groups())
        expected = image.evaluate(
            """(element, position) => {
                const canvas = document.createElement('canvas');
                canvas.width = element.naturalWidth;
                canvas.height = element.naturalHeight;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(element, 0, 0);
                return Array.from(ctx.getImageData(
                    position.x, position.y, 1, 1).data).slice(0, 3);
            }""",
            {"x": selected_x, "y": selected_y},
        )
        result = [
            int(page.locator(f"[data-rgb-{color}]").inner_text())
            for color in ("r", "g", "b")
        ]
        assert result == expected, (result, expected)
        assert not errors, errors
        browser.close()

    print("Intro interactive QA passed: region click, matching 6x6 cells, "
          "brightness arithmetic, reset, and true RGB sampling.")


if __name__ == "__main__":
    main()
