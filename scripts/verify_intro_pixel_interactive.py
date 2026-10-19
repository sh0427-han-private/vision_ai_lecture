"""Browser QA for the interactive grayscale and RGB concept slides.

Usage: run a local server with docs/ as root on port 8765, then execute
python scripts/verify_intro_pixel_interactive.py (requires Playwright Chromium).
"""
from __future__ import annotations

import math
import os
import json
from pathlib import Path
import re

from playwright.sync_api import sync_playwright


BASE_URL = os.getenv("AUDIT_BASE_URL", "http://127.0.0.1:8765") + "/intro.html"
MANIFEST = json.loads((Path(__file__).resolve().parents[1] / "docs/two_hour_manifest.json").read_text())
INTRO = {entry["concept"]: entry["slide"] for entry in MANIFEST["decks"]["intro"]}


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

        page.goto(BASE_URL + f"#slide-{INTRO['start']}", wait_until="networkidle")
        assert "Vision AI란 무엇인가?" in page.locator(".slide.active").inner_text()
        page.goto(BASE_URL + f"#slide-{INTRO['ai-ml-dl-cv']}", wait_until="networkidle")
        assert "Computer Vision" in page.locator(".slide.active").inner_text()
        page.goto(BASE_URL + f"#slide-{INTRO['photo-numbers']}", wait_until="networkidle")
        page.wait_for_function(
            "() => document.querySelector('[data-apple-matrix-bridge]')"
            "?.dataset.appleMatrixReady === 'true'"
        )
        bridge = page.evaluate("""() => {
            const root = document.querySelector('[data-apple-matrix-bridge]');
            const img = root.querySelector('[data-apple-matrix-source]');
            const grid = root.querySelector('[data-apple-matrix-grid]');
            const canvas = document.createElement('canvas');
            canvas.width = 12;
            canvas.height = 8;
            const context = canvas.getContext('2d');
            context.imageSmoothingEnabled = true;
            context.imageSmoothingQuality = 'high';
            context.drawImage(img, 0, 0, 12, 8);
            const pixels = context.getImageData(0,0,12,8).data;
            const expected = [];
            for (let i = 0; i < 96; i++) {
                const j = i * 4;
                expected.push(Math.round(
                    .299*pixels[j] + .587*pixels[j+1] + .114*pixels[j+2]
                ));
            }
            return {
                src: img.getAttribute('src'),
                dims: [img.naturalWidth,img.naturalHeight],
                mode: root.dataset.appleMatrixReady,
                count: grid.children.length,
                actual: [...grid.children].map(el=>Number(el.textContent)),
                expected,
            };
        }""")
        assert bridge["dims"] == [960, 640], bridge
        assert page.locator(".meaning-speech").all_text_contents() == [
            "사람이 얻은 의미 · 사과", "컴퓨터가 받은 입력 · 숫자 배열"
        ]
        assert bridge["count"] == 96, bridge
        assert bridge["actual"] == bridge["expected"], bridge
        assert len(set(bridge["actual"])) > 10, bridge
        assert all(0 <= x <= 255 for x in bridge["actual"]), bridge
        page.goto(BASE_URL + f"#slide-{INTRO['gray']}", wait_until="networkidle")
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

        page.goto(BASE_URL + f"#slide-{INTRO['rgb']}", wait_until="networkidle")
        page.wait_for_function(
            "() => document.querySelector('[data-rgb-shape]').textContent"
            ".includes('× 3')"
        )
        # Match the live JPEG dimensions with H x W x RGB channel order.
        image_shape = page.locator("[data-rgb-shape]").inner_text()
        assert "640" in image_shape and "960" in image_shape, image_shape
        image = page.locator("[data-rgb-photo]")
        dimensions = image.evaluate(
            "(el) => [el.naturalWidth, el.naturalHeight]"
        )
        assert dimensions == [960, 640], dimensions
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
        # Same source image must generate three real output rasters.
        page.goto(BASE_URL + f"#slide-{INTRO['hwc']}", wait_until="networkidle")
        assert "1,843,200" in page.locator(".slide.active").inner_text()
        assert page.locator(".intro-rgb-data-figure img").count() == 1
        assert page.locator(".slide.active .callout").count() == 0
        page.goto(BASE_URL + f"#slide-{INTRO['resolution']}", wait_until="networkidle")
        page.wait_for_function(
            "() => document.querySelector('[data-resolution-comparison]')"
            "?.dataset.resolutionReady === 'true'",
            timeout=20000,
        )
        data = page.evaluate("""() => {
            const root = document.querySelector('[data-resolution-comparison]');
            const values = [90, 180, 360].map(p => {
                const card = root.querySelector('[data-resolution-p="' + p + '"]');
                const full = card.querySelector('[data-resolution-full]');
                const zoom = card.querySelector('[data-resolution-zoom]');
                const z = zoom.getContext('2d').getImageData(
                    0, 0, zoom.width, zoom.height).data;
                let colored = 0;
                let signature = 0;
                for (let i = 0; i < z.length; i += 4) {
                    if (z[i] || z[i+1] || z[i+2]) colored++;
                    if (i % 160 === 0) signature +=
                        z[i]*3 + z[i+1]*5 + z[i+2]*7;
                }
                return {
                    p, size:[full.width,full.height],
                    zoomSize:[zoom.width,zoom.height],
                    colored, signature,
                    locator:card.querySelector('[data-resolution-locator]')
                        .getBoundingClientRect().width,
                };
            });
            return {
                src:[Number(root.dataset.sourceWidth),
                     Number(root.dataset.sourceHeight)],
                values
            };
        }""")
        assert data["src"] == [960,640], data
        assert all(v["size"][0] <= 960 and v["size"][1] <= 540 for v in data["values"]), data
        assert [v["size"] for v in data["values"]] == [
            [160, 90], [320, 180], [640, 360]
        ], data
        assert all(v["colored"] > 0 and v["locator"] > 0
                   for v in data["values"]), data
        assert len(set(v["signature"] for v in data["values"])) > 1, data
        assert not errors, errors
        browser.close()

    print("Intro interactive QA passed: actual 12x8 apple number matrix, photo-to-numbers continuity, region click, matching 6x6 cells, "
          "brightness arithmetic, reset, true RGB sampling, "
          "and 160×90/320×180/640×360 downsampling comparison.")


if __name__ == "__main__":
    main()
