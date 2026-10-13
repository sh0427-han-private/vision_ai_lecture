"""Pure-standard-library verification for the public Vision AI lecture deck."""
from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
manifest = json.loads((DOCS / "assets/lesson/manifest.json").read_text("utf-8"))

expected = {"intro": 15, "ai_basics": 44, "vision_ai": 40}

for name, count in expected.items():
    document = (DOCS / f"{name}.html").read_text("utf-8")
    actual = len(re.findall(r'<section class="slide(?: active)?"', document))
    assert actual == count, (name, actual, count)
    assert document.count('class="slide active"') == 1, name

    if name in manifest:
        entries = manifest[name]
        assert len(entries) + 1 == actual, (name, "manifest vs slides")
        titles = [
            html.unescape(value) for value in re.findall(
                r'<h2 class="slide-title">([^<]+)</h2>', document
            )
        ]
        assert titles == [entry["title"] for entry in entries], name
        assert [entry["number"] for entry in entries] == list(
            range(1, len(entries) + 1)
        )
        for item in entries:
            assert (DOCS / item["asset"]).is_file(), item["asset"]

    local_urls = re.findall(r'(?:src|href)="([^"]+)"', document)
    for url in local_urls:
        if url.startswith(("https:", "http:", "#", "mailto:", "data:")):
            continue
        target = url.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        assert (DOCS / target).is_file(), (name, target)

    print(f"{name}: {actual} slides and local resources verified")

home = (DOCS / "index.html").read_text("utf-8")
assert home.count('class="card"') == 3, "course landing page"
for page in ("intro.html", "ai_basics.html", "vision_ai.html"):
    assert f'href="{page}"' in home

figures = sorted((DOCS / "assets/lesson").glob("lecture_*.svg"))
assert len(figures) >= 9, "missing new lesson illustrations"
figures.append(DOCS / "assets/lesson/task_labels_three_outputs.svg")
figures.append(DOCS / "assets/intro_grayscale_crop_6x6.svg")
for path in figures:
    tree = ET.parse(path)
    assert tree.getroot().tag == "{http://www.w3.org/2000/svg}svg", path

values = [[98, 101, 99], [102, 255, 100], [101, 98, 99]]
flat = [value for row in values for value in row]
assert sum(flat) == 1053
assert sum(flat) / 9 == 117
assert sorted(flat)[4] == 100
weights = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
assert sum(values[r][c] * weights[r][c]
           for r in range(3) for c in range(3)) == 2219
assert 2219 / 16 == 138.6875
kernel_grid = [
    [96, 98, 100, 100, 99],
    [97, 98, 101, 99, 100],
    [98, 102, 255, 100, 101],
]
expected_sums = [1045, 1053, 1055]
assert [sum(kernel_grid[r][c] for r in range(3)
            for c in range(x, x + 3)) for x in range(3)] == expected_sums

builder = (ROOT / "scripts/build_lesson_revision.py").read_text("utf-8")
compile(builder, str(ROOT / "scripts/build_lesson_revision.py"), "exec")
for marker in (
    "task_labels_three_outputs",
    "lecture_filter_to_cnn_bridge",
    "lecture_point_neighborhood",
):
    assert marker in builder, marker

print("SVG XML, kernel arithmetic, Python syntax, source registry verified.")
