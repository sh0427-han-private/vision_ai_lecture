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

# Pedagogical continuity: the feature map must preserve all values from
# the immediately preceding CNN-style cross-correlation calculation.
i = [[1, 2, 3, 0, 1], [4, 5, 6, 1, 0], [7, 8, 9, 2, 1],
     [0, 1, 2, 3, 1], [1, 0, 1, 2, 3]]
k = [[1, 0, -1]] * 3
expected = [[-6, 12, 16], [-6, 8, 15], [-4, 2, 7]]
calculated = [
    [sum(i[y + dy][x + dx] * k[dy][dx]
         for dy in range(3) for dx in range(3))
     for x in range(3)]
    for y in range(3)
]
assert calculated == expected, calculated

content_conv = (DOCS / "assets/lesson/lesson_convolution_calculated.svg").read_text("utf-8")
content_map = (DOCS / "assets/lesson/lesson_featuremap_numeric_continuation.svg").read_text("utf-8")
for number in (-6, 12, 16, 8, 15, -4, 2, 7):
    # Values are embedded in readable SVG text, including negative responses.
    needle = f">{number}</text>"
    assert needle in content_conv and needle in content_map, number

for ident in (
    "lesson_perceptron_numeric_flow",
    "lesson_and_xor_separability",
    "lesson_convolution_calculated",
    "lesson_featuremap_numeric_continuation",
    "lesson_multichannel_filter_to_maps",
):
    assert ident in builder, ident

assert abs(0.5 * 0.2 + 1.0 * 0.8 - 0.6 - 0.3) < 1e-12
assert [(u, v, int(u and v), int(bool(u) != bool(v)))
        for u in (0, 1) for v in (0, 1)] == [
        (0, 0, 0, 0), (0, 1, 0, 1), (1, 0, 0, 1), (1, 1, 1, 0)
]
assert 64 * 3 * 3 * 3 == 1728
assert 1728 + 64 == 1792
assert (224 + 2 * 1 - 3) // 1 + 1 == 224
print("Pedagogical continuity: perceptron, AND/XOR, convolution → feature-map and 64-channel shapes verified.")
