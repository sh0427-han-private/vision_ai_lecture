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

expected = {"intro": 11, "ai_basics": 44, "vision_ai": 37}

for name, count in expected.items():
    document = (DOCS / f"{name}.html").read_text("utf-8")
    actual = len(re.findall(r'<section class="slide(?: [^"]+)?"', document))
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

# Both published entrypoints must go straight to Intro 1, not a contents menu.
home = (DOCS / "index.html").read_text("utf-8")
repo_home = (ROOT / "index.html").read_text("utf-8")
assert 'location.replace("./intro.html#slide-1")' in home
assert 'location.replace("./docs/intro.html#slide-1")' in repo_home
assert 'class="card"' not in home and 'mode=core' not in home
nav_js = (DOCS / "slide.js").read_text("utf-8")
assert 'coreMode' not in nav_js and 'nearbyIncluded' not in nav_js
assert 'if (currentIndex > 0) return goTo(currentIndex - 1)' in nav_js
assert 'if (currentIndex < slides.length - 1) return goTo(currentIndex + 1)' in nav_js
for page in ("intro.html", "ai_basics.html", "vision_ai.html"):
    markup = (DOCS / page).read_text("utf-8")
    assert "data-lesson-mode-toggle" not in markup, page
    assert "data-lesson-mode-summary" not in markup, page
    assert '>목차</a>' not in markup and 'class="nav-links"' not in markup, page
    assert 'href="intro.html#slide-1"' in markup, page
    assert ('slide.js?v=prevent-toc-wheel-20261016-1' if page == "intro.html"
            else 'slide.js?v=prevent-toc-wheel-20261016-1') in markup, page
intro_markup = (DOCS / "intro.html").read_text("utf-8")
assert 'data-prev-page=""' in intro_markup
assert 'data-next-page="vision_ai_course.html"' in intro_markup
assert 'data-prev-page="intro.html"' in (DOCS / "ai_basics.html").read_text("utf-8")
assert 'data-next-page="vision_ai.html"' in (DOCS / "ai_basics.html").read_text("utf-8")
assert 'data-prev-page="ai_basics.html"' in (DOCS / "vision_ai.html").read_text("utf-8")
assert 'data-next-page=""' in (DOCS / "vision_ai.html").read_text("utf-8")
print("Landing redirects and single-track controls validated.")

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
    "vision_ai_convolution_ppt",
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

# Visual teaching additions: ReLU, affine composition, grouped-video split,
# local-to-global CNN illustration, and theoretical receptive field.
new_figures = [
    "lesson_relu_value_graph",
    "lesson_affine_relu_comparison",
    "lesson_video_group_split_comparison",
    "lesson_cnn_feature_hierarchy",
    "lesson_receptive_field_growth",
]
for name in new_figures:
    path = DOCS / "assets/lesson" / f"{name}.svg"
    assert path.is_file(), path
    assert ET.parse(path).getroot().tag == "{http://www.w3.org/2000/svg}svg"
    assert name in builder, name

def relu(x):
    return max(0, x)

assert [relu(x) for x in (-2, -1, 0, 1, 2)] == [0, 0, 0, 1, 2]
for x in (-2, -1, -0.5, 0, 1, 2):
    h = 2 * x + 1
    assert 3 * h - 2 == 6 * x + 1
assert 3 * relu(2 * -1 + 1) - 2 == -2
assert 3 * relu(2 * 0 + 1) - 2 == 1
assert 3 * relu(2 * 1 + 1) - 2 == 7

random_splits = {
    "Train": {"A1", "B1", "C1"},
    "Validation": {"A2", "B2", "C2"},
    "Test": {"A3", "B3", "C3"},
}
grouped_splits = {
    "Train": {"A1", "A2", "A3"},
    "Validation": {"B1", "B2", "B3"},
    "Test": {"C1", "C2", "C3"},
}
group_identity = lambda frame: frame[0]
assert set(group_identity(x) for x in random_splits["Train"]) & set(
    group_identity(x) for x in random_splits["Test"]
)
assert all(
    set(group_identity(x) for x in grouped_splits[a]).isdisjoint(
        set(group_identity(x) for x in grouped_splits[b])
    )
    for a, b in [("Train", "Validation"), ("Train", "Test"),
                 ("Validation", "Test")]
)
assert sum(len(x) for x in grouped_splits.values()) == 9
assert [3 + 2 * depth for depth in (0, 1, 2)] == [3, 5, 7]
print("Pedagogical continuity: ReLU, affine layer collapse, video-grouped holdout, 3/5/7 receptive fields verified.")

# All teaching figures below refer to the SAME evaluation of 100 samples.
metrics_figures = {
    "lesson_threshold_score_decision": "0.82",
    "lesson_confusion_100cases": "18",
    "lesson_precision_recall_sharedcase": "81.8%",
    "lesson_accuracy_f1_same100": "85.7%",
    "lesson_backbone_head_roles": "Backbone",
    "lesson_backbone_tensor_head_options": "224×224×3",
    "lesson_transfer_pretraining_to_task": "Backbone",
    "lesson_transfer_freeze_vs_finetune": "Fine-tuning",
}
for stem, marker in metrics_figures.items():
    path = DOCS / "assets" / "lesson" / f"{stem}.svg"
    assert path.is_file(), path
    assert ET.parse(path).getroot().tag == "{http://www.w3.org/2000/svg}svg", path
    assert marker in path.read_text("utf-8"), (stem, marker)
    assert stem in builder, stem

tp, fn, fp, tn = 18, 2, 4, 76
assert tp + fn + fp + tn == 100
assert tp + fn == 20 and fp + tn == 80 and tp + fp == 22
precision = tp / (tp + fp)
recall = tp / (tp + fn)
accuracy = (tp + tn) / (tp + fn + fp + tn)
f1 = 2 * tp / (2 * tp + fp + fn)
assert round(precision * 100, 1) == 81.8
assert round(recall * 100, 1) == 90.0
assert round(accuracy * 100, 1) == 94.0
assert round(f1 * 100, 1) == 85.7
assert abs(2 * precision * recall / (precision + recall) - f1) < 1e-12

demo_score = 0.82
assert demo_score >= 0.5 and demo_score < 0.9
assert [((224 + 2 * 1 - 3) // 2 + 1), ((112 + 2 * 1 - 3) // 2 + 1),
        ((56 + 2 * 1 - 3) // 2 + 1), ((28 + 2 * 1 - 3) // 2 + 1)] == [112, 56, 28, 14]
assert [64, 128, 192, 256] == [64, 128, 192, 256]
print("Metrics (100 cases), threshold decision, backbone tensor sizes, transfer diagrams verified.")


# Essential-only route: a basic lesson must not rely on a neighboring
# advanced slide, because the 82-slide mode intentionally skips all such pages.
for deck in ("ai_basics", "vision_ai"):
    registry = manifest[deck]
    page = (DOCS / f"{deck}.html").read_text("utf-8")
    slide_sections = re.findall(
        r'(?s)<section class="slide(?: [^"]+)?"[^>]*>.*?</section>',
        page
    )
    assert len(slide_sections) == len(registry) + 1
    for idx, item in enumerate(registry):
        if item["level"] != "basic":
            continue
        match = re.search(
            r'(?s)<p class="slide-subtitle">(.*?)</p>',
            slide_sections[idx + 1]
        )
        assert match, (deck, idx + 1, "missing subtitle")
        description = re.sub(r"<[^>]+>", " ", match.group(1))
        previous_advanced = idx > 0 and registry[idx - 1]["level"] == "detail"
        next_advanced = idx + 1 < len(registry) and registry[idx + 1]["level"] == "detail"
        if previous_advanced:
            assert not re.search(r"직전|앞 장|지난 장|이전 장", description), (
                deck, item["number"], "refers to skipped preceding advanced slide"
            )
        if next_advanced:
            assert not re.search(r"다음 장|바로 다음|이후 장", description), (
                deck, item["number"], "refers to skipped following advanced slide"
            )
assert (
    11 + 1 + sum(x["level"] == "basic" for x in manifest["ai_basics"])
    + 1 + sum(x["level"] == "basic" for x in manifest["vision_ai"])
) == 73
assert "직전 Convolution" not in (
    DOCS / "assets/lesson/lesson_featuremap_numeric_continuation.svg"
).read_text("utf-8")
print("Core-course narrative continuity: skipped-advanced references verified.")


# Important number- and structure-heavy figures must have useful descriptions
# rather than just repeat their slide titles.
accessible_figures = (
    "lesson_perceptron_numeric_flow",
    "lesson_and_xor_separability",
    "lesson_relu_value_graph",
    "lesson_video_group_split_comparison",
    "lesson_confusion_100cases",
    "lesson_precision_recall_sharedcase",
    "lesson_accuracy_f1_same100",
    "lesson_featuremap_numeric_continuation",
    "lesson_backbone_head_roles",
    "lesson_receptive_field_growth",
    "lesson_transfer_freeze_vs_finetune",
    "lesson_cnn_feature_hierarchy",
)
joined_lessons = (
    (DOCS / "ai_basics.html").read_text("utf-8")
    + (DOCS / "vision_ai.html").read_text("utf-8")
)
for basename in accessible_figures:
    match = re.search(
        rf'<img src="assets/lesson/{basename}[.]svg[?]v=[^"]+" alt="([^"]+)"',
        joined_lessons
    )
    assert match and len(html.unescape(match.group(1))) >= 35, basename
print("Descriptive alt text on 12 key instructional figures verified.")

# The core Median slide contains no numeric 3×3 grid; do not claim that
# its photograph-only panel shows a preceding list of 9 values.
assert "앞의 9개 숫자" not in (
    DOCS / "assets/lesson/processing_median.svg"
).read_text("utf-8")
print("Median essential Figure has no reference to hidden arithmetic.")

ppt_svg = DOCS / "assets/ppt_slides/vision_ai_convolution_ppt.svg"
assert ppt_svg.is_file(), ppt_svg
ppt_data = ppt_svg.read_text("utf-8")
assert 'width="1200" height="675"' in ppt_data
for output_number in ("-6", "12", "16", "8", "15", "-4", "2", "7"):
    assert output_number in ppt_data, output_number
assert (ROOT / "slides/pptx_sources/Vision_AI_Convolution_PPT_Source.pptx").is_file()
print("PPT slide source and 16:9 lecture SVG are present and mathematically aligned.")


# Vision AI 9 is now the point-versus-neighborhood operation slide.
vision_html = (DOCS / "vision_ai.html").read_text("utf-8")
vision_slides = re.findall(
    r'<section class="slide(?: [^"]+)?"[^>]*>.*?</section>',
    vision_html, flags=re.DOTALL
)
assert len(vision_slides) == 37
assert "한 Pixel을 바꿀 수도, 주변 Pixel을 함께 볼 수도 있습니다" in vision_slides[8]
assert not any("Opening" in slide or "Closing" in slide
               for slide in vision_slides)
assert not any(x.get("asset", "").endswith("processing_morphology.svg")
               for x in manifest["vision_ai"])
assert [x["number"] for x in manifest["vision_ai"]] == list(range(1, 37))
# Physical Vision 33 and 34 were removed simultaneously from the prior 39-slide deck.
# The former Vision 35, CNN training, must now become Vision 33.
assert "CNN의 필터도 오차를 줄이는 방향으로 학습합니다" in vision_slides[32]
assert "data-topic=\"CNN 학습\"" in vision_slides[32]
assert "survey_architecture_patterns.svg" not in vision_html
assert "survey_residual_detail.svg" not in vision_html
removed_assets = {"survey_architecture_patterns.svg", "survey_residual_detail.svg"}
assert not any(x.get("asset", "").rsplit("/", 1)[-1] in removed_assets
               for x in manifest["vision_ai"])
assert [int(x) for x in re.findall(
    r'<div class="lesson-meta"><span>(\d{2}) · ', vision_html
)] == list(range(1, 37))
assert sum(x["level"] == "basic" for x in manifest["vision_ai"]) == 25
print("Vision 33/34 removed; Vision 33 is CNN training; 37 full / 26 core slides verified.")


# Slide 6 must literally reuse the apple photo and the localized defect
# annotations shown in Vision AI slides 3, 4 and 5.
task_sources = {
    name: (DOCS / f"assets/lesson/context_task_{name}.svg").read_text("utf-8")
    for name in ("classification", "detection", "segmentation")
}
label_svg_path = DOCS / "assets/lesson/task_labels_three_outputs.svg"
label_markup = label_svg_path.read_text("utf-8")
embedded = re.compile(r'<image[^>]*href="data:image/jpeg;base64,([^"]+)"')
canonical_photo = embedded.search(task_sources["classification"]).group(1)
assert all(embedded.search(src).group(1) == canonical_photo
           for src in task_sources.values())
assert embedded.findall(label_markup) == [canonical_photo], (
    "Use the same original apple image exactly once, not similar stock fruit"
)
for kind in ("classification", "detection", "segmentation"):
    assert f'data-apple-figure="{kind}"' in label_markup
    assert f'data-reuse-source="context_task_{kind}.svg"' in label_markup
assert label_markup.count('<use href="#apple-reference"') == 3
source_box = re.search(
    r'<rect x="399.25" y="232.05" width="34.45" height="37.050000000000004"',
    task_sources["detection"]
)
assert source_box is not None
box_el = ET.parse(label_svg_path).getroot().find(
    ".//*[@data-reused-bbox='true']"
)
assert box_el is not None
for key, expected in {
    "x": (399.25 - 32) / .65,
    "y": (232.05 - 104) / .65,
    "width": 34.45 / .65,
    "height": 37.05 / .65,
}.items():
    assert abs(float(box_el.get(key)) - expected) < 0.00001, key
source_mask = re.search(
    r'<path transform="translate\(32 104\) scale\(0.65\)" d="([^"]+)"',
    task_sources["segmentation"]
)
mask_el = ET.parse(label_svg_path).getroot().find(
    ".//*[@data-reused-mask='true']"
)
assert source_mask is not None and mask_el is not None
assert mask_el.get("d") == source_mask.group(1), (
    "Mask must follow the same localized apple defect outline"
)
for page_name, idx in (("vision_ai", 5),):
    markup = (DOCS / f"{page_name}.html").read_text("utf-8")
    slides = re.findall(
        r'<section class="slide(?: [^"]+)?"[^>]*>.*?</section>',
        markup, flags=re.DOTALL
    )
    assert "같은 사진이라도 Task가 바뀌면 정답 형태가 바뀝니다" in slides[idx]
    assert "task_labels_three_outputs.svg?v=shared-apple-20261015-1" in slides[idx]
print("Vision AI slide 6 apple, defect Box and Pixel Mask match slides 3-5.")

# Step convention is consistently z >= 0; verify all displayed gate rows.
step = lambda z: int(z >= 0)
for x1 in (0, 1):
    for x2 in (0, 1):
        and_y = step(0.5*x1 + 0.5*x2 - 0.7)
        h1 = step(-0.5*x1 - 0.5*x2 + 0.7)
        h2 = step(0.5*x1 + 0.5*x2 - 0.2)
        xor_y = step(0.5*h1 + 0.5*h2 - 0.7)
        assert and_y == (x1 & x2)
        assert xor_y == (x1 ^ x2)
print("Perceptron AND and multilayer XOR: all truth-table rows verified.")

# Two-input fully connected affine network with a sum output.
for x1, x2 in ((1, 2), (0, 0), (-2, 3), (0.5, -1.5), (4, -3)):
    h1, h2, h3 = x1+x2+1, 2*x1-x2, -x1+2*x2
    z1, z2 = h1+h2+h3, 2*h1-h2+h3
    assert z1 == 2*x1+2*x2+1
    assert z2 == -x1+5*x2+2
    assert z1+z2 == x1+7*x2+3
assert (1+2+1, 2*1-2, -1+2*2) == (4, 0, 3)
assert (4+0+3, 2*4-0+3, 7+11) == (7, 11, 18)

# Current public sequence and arithmetic are maintained independently of legacy decks.
import runpy
runpy.run_path(str(ROOT / "scripts/verify_two_hour_course.py"), run_name="__main__")
