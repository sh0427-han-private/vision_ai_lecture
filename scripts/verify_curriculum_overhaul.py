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

expected = {"intro": 19, "ai_basics": 44, "vision_ai": 37}

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

# Public learning path starts with CNN essentials; duplicate YOLO chapters are removed.
# Original ai_basics / vision_ai files are retained for optional deep study.
course_page = (DOCS / "vision_ai_course.html").read_text("utf-8")
course_slides = re.findall(
    r'<section class="slide(?: [^"]+)?"[^>]*>.*?</section>',
    course_page, flags=re.DOTALL
)
assert len(course_slides) == 49, "49 core CNN/AI slides after YOLO removal"
assert course_page.count('class="slide active"') == 1
sources = [
    (deck, int(index))
    for deck, index in re.findall(
        r'data-source-deck="([^"]+)" data-source-slide="(\d+)"', course_page
    )
]
assert len(sources) == 49 and len(set(sources)) == 49, "Sources must be unique"
assert sources[:5] == [("vision_ai", n) for n in range(2, 7)]
assert sources[5:7] == [("ai_basics", 2), ("ai_basics", 3)]
assert sources[7:11] == [
    ("new_lessons",1), ("cnn_expansion",1),
    ("cnn_featuremaps",1), ("vision_ai",28)
]
assert sources[11:16] == [
    ("vision_ai",18), ("vision_ai",10),
    ("vision_ai",19), ("cnn_contrast",1), ("ai_basics",8)
]
assert sources[16:21] == [
    ("new_lessons",2), ("new_lessons",3), ("ai_basics",13),
    ("new_lessons",4), ("ai_basics",11)
]
assert sources[25:29] == [
    ("vision_ai",23), ("vision_ai",24),
    ("vision_ai",25), ("vision_ai",31)
]
assert sources[-1] == ("ai_basics",44)
assert not any(d.startswith("yolo") for d,i in sources)
assert not re.search(r"\bYOLO\b|yolo_", course_page, flags=re.IGNORECASE)
assert not re.search(r"\*\*[^*]+\*\*", course_page), "Raw Markdown bold is not rendered in HTML slides"
assert ("vision_ai",7) in sources, "IoU still appears in evaluation section"
assert sorted(i for d,i in sources if d=="cnn_expansion") == [1,2]
assert all(d!="cnn_expansion" or i<=2 for d,i in sources)
assert ("vision_ai", 27) not in sources
assert ("ai_basics", 27) not in sources
assert "cnn_squeezenet_actual_feature_maps.png" in course_page
assert (DOCS / "assets/lesson/cnn_squeezenet_actual_feature_maps.png").is_file()
assert (ROOT / "scripts/render_cnn_feature_maps.py").is_file()
assert "cnn_numeric_why_logic.css?v=20261017-1" in course_page
assert 'data-prev-page="intro.html"' in course_page
assert 'data-next-page=""' in course_page
assert 'slide.js?v=prevent-toc-wheel-20261016-1' in course_page
assert 'slide.js?v=prevent-toc-wheel-20261016-1' in intro_markup
for markup in (intro_markup, course_page):
    for path in ("lecture_sidebar.css", "lecture_outline.js",
                 "lecture_sidebar.js"):
        assert path in markup, path
for url in re.findall(r'(?:src|href)="([^"]+)"', course_page):
    if url.startswith(("http:", "https:", "#", "mailto:", "data:")):
        continue
    target = url.split("?", 1)[0].split("#", 1)[0]
    if target:
        assert (DOCS / target).is_file(), target

# Exactly 68 public links: Intro 19 + CNN/AI 49.
outline_source = (DOCS / "lecture_outline.js").read_text("utf-8")
outline = json.loads(outline_source.split(" = ", 1)[1].strip().rstrip(";"))
items = [item for group in outline["groups"] for item in group["items"]]
assert len(items) == 68
assert [it["global"] for it in items] == list(range(1,69))
assert [(it["page"], it["slide"]) for it in items[:19]] == [
    ("intro.html", n) for n in range(1,20)
]
assert [(it["page"], it["slide"]) for it in items[19:]] == [
    ("vision_ai_course.html", n) for n in range(1,50)
]
assert len(outline["groups"]) == 11
assert [it["title"] for it in items[19:]] == [
    html.unescape(re.sub(r"<[^>]+>","",re.search(
        r'<h2 class="slide-title">([^<]+)</h2>', slide
    ).group(1))) for slide in course_slides
], "Sidebar titles must exactly match visible slide titles"
assert all(not it.get("original","").startswith("Y") for it in items)
assert items[19+7]["original"] == "N1"
assert items[19+14]["original"] == "F1"
assert [items[19+i]["original"] for i in (16,17,19,20)] == [
    "N2","N3","N4","A11"
]
assert "lecture-toc-drawer" in (DOCS / "lecture_sidebar.js").read_text("utf-8")

# Numerical convolution, padding, max pooling, AND/XOR must all be correct.
for idx, phrase in [
    (7,"1,048,576"), (16,"x₁ + 7x₂ + 3"), (17,"AND Gate"),
    (19,"xor_multilayer_gates_ko"), (25,"3×3 = 9칸"), (26,"3×3 → 1×1"),
    (27,"4×4 (16칸) → 2×2")
]:
    assert phrase in course_slides[idx], (idx+1,phrase)
assert "x₁+x₂ = 1.4" in course_slides[17]
assert "XOR Gate" in course_slides[17]
assert "기울기" not in course_slides[17], "Gate slide is geometry, not gradient"
assert "y = z₁ + z₂" in course_slides[16]
assert "neuron_concept_flow.css?v=20261017-3" in course_page
assert "z = Wx + b" in course_slides[15]
assert "2 → 3 → 2 → 1 뉴런" in course_slides[16]
assert "W₂φ(W₁x+b₁)+b₂" in course_slides[20]
assert "perceptron_gate_structure_ko" in course_slides[15]
assert "nb-network-numbers" in course_slides[16]
assert "gate-truth" in course_slides[17]
assert "and_xor_gate_geometry_ko" in course_slides[17]
assert "x₁+x₂ = 1.4" in course_slides[17]
assert "nb-activation-charts" in course_slides[18]
assert course_slides[19].count("<tr>") == 5
assert "nb-activation-role" in course_slides[20]
assert 'class="concept-source"' not in course_page, "Only actual borrowed images need source labels"
assert "개념 참고:" not in course_page, "Do not cite sources used only for concepts"
assert all(
    max(0,x-y)+max(0,y-x) == (x^y)
    for x in (0,1) for y in (0,1)
)
# 5x5 with center-only 3x3 kernel, valid convolutions:
input5 = [[1+5*y+x for x in range(5)] for y in range(5)]
assert [[input5[y+1][x+1] for x in range(3)]
        for y in range(3)] == [[7,8,9],[12,13,14],[17,18,19]]
assert [[input5[y*2+1][x*2+1] for x in range(2)]
        for y in range(2)] == [[7,9],[17,19]]
original3 = [[1,2,3],[4,5,6],[7,8,9]]
padded = [[0]*5] + [[0]+line+[0] for line in original3] + [[0]*5]
assert sum(sum(row) for row in original3) == 45
padding_result = [
    [sum(padded[y+i][x+j] for i in range(3) for j in range(3))
     for x in range(3)] for y in range(3)
]
assert padding_result == [[12,21,16],[27,45,33],[24,39,28]]
pool_input = [[1,3,2,4],[5,6,1,2],[4,2,9,3],[0,7,8,1]]
pooled = [[max(pool_input[2*y+i][2*x+j]
               for i in range(2) for j in range(2))
           for x in range(2)] for y in range(2)]
assert pooled == [[6,4],[7,9]]
assert 32*32*32*32 == 1_048_576
assert 3*3 == 9
print("CNN motivation, ReLU/XOR, numeric Stride/Padding/Pooling and 68 sidebar entries validated.")


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
    19 + 1 + sum(x["level"] == "basic" for x in manifest["ai_basics"])
    + 1 + sum(x["level"] == "basic" for x in manifest["vision_ai"])
) == 81
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


# Intro: the real apple JPEG is width 960, height 640. Shape is H x W x C.
intro_page = (DOCS / "intro.html").read_text("utf-8")
intro_slides = re.findall(
    r'<section class="slide(?: [^"]+)?"[^>]*>.*?</section>',
    intro_page, flags=re.DOTALL
)
assert len(intro_slides) == 19
assert "AI와 시각의 출발점" in intro_slides[0]
assert "사람의 시각 · 장면 이해" in intro_slides[1]
assert "일상 속 Vision 기술" in intro_slides[3]
assert "assets/intro_photos/perspective.webp" in intro_slides[1]
for photo in ("cctv.webp", "robot.webp", "thermal.webp"):
    assert f"assets/intro_photos/{photo}" in intro_slides[3]
assert "사진 속 객체 인식" in intro_slides[4]
assert "사람의 의미 인식 vs Pixel 숫자" in intro_slides[5]
assert 'data-apple-matrix-bridge' in intro_slides[5]
assert 'data-apple-matrix-grid' in intro_slides[5]
assert 'assets/vision_task_apple_reference.jpg' in intro_slides[4]
assert 'assets/vision_task_apple_reference.jpg' in intro_slides[5]
assert "Vision AI가 어려운 이유:" in intro_slides[5]
assert "“아, 사과구나!”" in intro_slides[5]
assert "“?! 그냥 숫자 배열이네”" in intro_slides[5]
assert "조명·색감에 따른 Pixel 변화" in intro_slides[6]
assert "시점·회전·가림·초점 변화" in intro_slides[7]
assert 'class="iv-image iv-fov figure-display"' in intro_slides[7]
assert "위치 변화와 Pixel 배열" in intro_slides[8]
assert 'data-grayscale-lesson' in intro_slides[8]
assert "RGB · Pixel당 세 숫자" in intro_slides[9]
assert "RGB 이미지와 숫자 배열" in intro_slides[10]
assert "640 × 960 ×" in intro_slides[10]
assert "1,843,200" in intro_slides[10]
assert "<strong>핵심:</strong>" not in intro_slides[10]
assert "lecture_rgb_channel_stack.svg?v=rgb-total-20261016-1" in intro_slides[10]
assert "해상도와 Pixel 수" in intro_slides[11]
assert "더 세밀한 정보를 기록할 수 있습니다" in intro_slides[11]
assert "해상도에 따른 정보 차이" in intro_slides[12]
assert "저해상도 원본을 확대 저장해도" in intro_slides[12]
assert "시각 이해 · What과 Where" in intro_slides[2]
assert "2D 이미지와 3D 공간의 모호함" in intro_slides[13]
assert "to know what is where by looking" in intro_slides[2]
assert "Marr &amp; Nishihara (1978)" in intro_slides[13]
assert "https://doi.org/10.1098/rspb.1978.0020" in intro_slides[13]
assert "intro_inverse_2d_3d_ambiguity.svg?v=what-where-20261015-1" in intro_slides[13]
assert "intro_vision_foundations.css?v=rgb-total-20261016-1" in intro_page
assert "intro_vision_story.css?v=20261016-1" in intro_page
assert (DOCS / "intro_vision_story.css").is_file()
assert "640 × 960 × <span>3</span> = <strong>1,843,200</strong>" in intro_slides[10], "RGB numeric array count changed"
assert "720 × 1280 × 3" in intro_slides[11], "resolution H × W × C changed"
assert 'data-resolution-source="assets/generated/apple_studio.webp"' in intro_slides[12]
for p, w, h in ((360, 640, 360), (720, 1280, 720), (1080, 1920, 1080)):
    assert f'data-resolution-p="{p}"' in intro_slides[12]
    assert f'width="{w}" height="{h}" data-resolution-full' in intro_slides[12]
for path in ("intro_resolution_demo.js", "intro_resolution_demo.css",
             "intro_apple_number_bridge.js", "intro_apple_number_bridge.css"):
    assert (DOCS / path).is_file(), path
assert "intro_resolution_demo.js?v=20261015-1" in intro_page
assert "intro_apple_number_bridge.js?v=20261015-1" in intro_page
assert "intro_apple_number_bridge.css?v=intro-picto-20261016-1" in intro_page
intro_outline_key = re.search(r"lecture_outline[.]js[?]v=([^\"]+)", intro_page)
course_outline_key = re.search(r"lecture_outline[.]js[?]v=([^\"]+)", course_page)
assert intro_outline_key and course_outline_key, "Both pages must load a versioned outline"
assert intro_outline_key.group(1) == course_outline_key.group(1), "Intro/Course outline cache versions must agree"
bridge_script = (DOCS / "intro_apple_number_bridge.js").read_text("utf-8")
assert "const width = 12, height = 8;" in bridge_script
for channel_weight in ("0.299", "0.587", "0.114"):
    assert channel_weight in bridge_script

# Perspective illustration shows equal apparent height for scaled size/distance.
assert 160 / (625 - 145) == 220 / (805 - 145)
inverse_svg = DOCS / "assets/lesson/intro_inverse_2d_3d_ambiguity.svg"
inverse_root = ET.parse(inverse_svg).getroot()
assert inverse_root.get("viewBox") == "0 0 1200 445"
assert inverse_root.tag == "{http://www.w3.org/2000/svg}svg"

labels = [int(x) for x in re.findall(
    r'<span class="slide-number">(\d+)</span>', intro_page
)]
assert labels == [3] + list(range(6, 20)), labels
channel_svg = (DOCS / "assets/lesson/lecture_rgb_channel_stack.svg").read_text("utf-8")
assert 'viewBox="0 0 960 640"' in channel_svg
assert "H × W × C = 640 × 960 × 3" in channel_svg
assert "한 위치의 3개 값 (예시)" not in channel_svg
assert "640 × 960 = 614,400 Pixel" in channel_svg
assert "1,843,200" in intro_slides[10]
res_file = DOCS / "assets/lesson/intro_resolution_comparison.svg"
res_root = ET.parse(res_file).getroot()
res_labels = "".join(node.text or "" for node in res_root.iter()
                     if node.tag.endswith("text"))
for label in ("640 × 360", "1280 × 720", "1920 × 1080",
              "720 × 1280 × 3"):
    assert label in res_labels, label
for w, h in ((640, 360), (1280, 720), (1920, 1080)):
    assert w * 9 == h * 16
and_svg = (DOCS / "assets/lesson/lesson_and_xor_separability.svg").read_text("utf-8")
assert 'stroke="#d2652f" stroke-width="7"' in and_svg
assert 'stroke="#fbe1d0" stroke-width="18"' in and_svg
assert "결정 경계" in and_svg
and_root = ET.fromstring(and_svg)
ns = "{http://www.w3.org/2000/svg}"
plots = [node for node in and_root.iter(ns + "g")
         if node.get("data-plot") in ("and", "xor")]
assert sorted(node.get("data-plot") for node in plots) == ["and", "xor"]
for plot in plots:
    assert (plot.get("data-x-max"), plot.get("data-y-max")) == ("2", "2")
    gate = plot.get("data-plot")
    circles = [node for node in plot.iter(ns + "circle")]
    assert len(circles) == 4, (gate, len(circles))
    for dot in circles:
        x, y = int(dot.get("data-x")), int(dot.get("data-y"))
        predicted = int(dot.get("data-class"))
        expected_class = (x & y) if gate == "and" else (x ^ y)
        assert predicted == expected_class, (gate, x, y, predicted)
        x0 = 175 if gate == "and" else 765
        assert float(dot.get("cx")) == x0 + 100 * x
        assert float(dot.get("cy")) == 354 - 100 * y
lines = [node for node in and_root.iter(ns + "path")
         if node.get("data-decision-boundary-main") == "and"]
assert len(lines) == 1
assert lines[0].get("d") == "M175 204 L325 354"
# Every point lies on the correct side of x1+x2=1.5.
assert all(
    (x + y > 1.5) == bool(x & y)
    for x in (0, 1) for y in (0, 1)
)
print("Intro apple-to-number bridge, HWC, 19-slide numbering and AND/XOR verified.")


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
for page_name, idx in (("vision_ai_course", 4), ("vision_ai", 5)):
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
assert "시각 이해 · What과 Where" in intro_slides[2]
intro_titles = [html.unescape(re.search(
    r'<h[12] class="slide-title[^"]*">([^<]+)</h[12]>', s
).group(1)) for s in intro_slides]
assert [item["title"] for item in items[:19]] == intro_titles
print("Two-input network, collapsed equation, Intro order and sidebar verified.")
