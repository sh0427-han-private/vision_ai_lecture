"""Build exact SVG teaching figures and beginner/detail slide sequences.

Requires lxml, numpy and Pillow. Run from any directory; output stays in this repo.
All numeric figures are calculated here rather than painted by image generation.
"""

from __future__ import annotations

import html
import json
import base64
from pathlib import Path

import numpy as np
from lxml import etree

from build_loss_optimizer_figures import build_loss_optimizer_figures
from build_survey_figures import build_survey_figures
from build_image_processing_figures import build_image_processing_figures, SECTIONS as PROCESSING_SECTIONS


FIGURE_ALT_DESCRIPTIONS = {
  "lesson_perceptron_numeric_flow": "두 입력 0.5와 1.0에 가중치 0.2와 0.8을 곱한 뒤 Bias −0.6을 더해 0.3을 얻고, 임계값 0 이상이므로 1로 판정하는 흐름",
  "lesson_and_xor_separability": "AND는 (1,1)만 출력 1이므로 직선으로 구분되지만 XOR는 (0,1)과 (1,0)이 출력 1이라 직선 하나로 구분되지 않는 좌표 비교",
  "lesson_relu_value_graph": "ReLU 함수는 입력 −2, −1, 0을 0으로 바꾸고 1, 2는 그대로 내보내며 원점에서 꺾이는 그래프",
  "lesson_video_group_split_comparison": "9개 프레임을 무작위로 나누면 영상 A B C가 Train Validation Test에 중복되지만 영상별 Group Split에서는 원본 영상이 서로 겹치지 않는 비교",
  "lesson_confusion_100cases": "총 100건에서 실제 불량 20건의 TP 18 FN 2와 실제 정상 80건의 FP 4 TN 76을 배치한 2×2 혼동행렬",
  "lesson_precision_recall_sharedcase": "정밀도는 TP 18개를 불량 판정 22개로 나눠 81.8%, 재현율은 TP 18개를 실제 불량 20개로 나눠 90%가 되는 비교",
  "lesson_accuracy_f1_same100": "혼동행렬 TP18 FP4 FN2 TN76으로 Accuracy는 94/100=94%, F1은 36/42=85.7%가 되는 계산",
  "lesson_featuremap_numeric_continuation": "5×5 입력에 3×3 필터를 이동해 얻은 3×3 반응값을 같은 위치에 놓아 Feature Map이 되며 음수와 양수의 차이도 보여주는 격자",
  "lesson_backbone_head_roles": "사과 사진 입력에서 Backbone이 공통 특징을 추출하고 분류 Head는 Class 점수, 검출 Head는 Box, 분할 Head는 Pixel Mask를 출력하는 선택형 구조",
  "lesson_receptive_field_growth": "동일한 7×7 입력 격자 위에서 3×3 합성곱 층이 1개 2개 3개 쌓일 때 이론적 수용영역이 3×3, 5×5, 7×7로 커지는 비교",
  "lesson_transfer_freeze_vs_finetune": "Freeze에서는 사전학습 Backbone을 고정하고 Head만 학습하며 Fine-tuning에서는 선택한 Backbone 가중치도 함께 업데이트하는 구조",
  "lesson_cnn_feature_hierarchy": "사과 사진에서 작은 경계 반응이 곡선과 형태의 단서로 조합되는 CNN 특징 계층 개념도이며 실제 모델 Feature Map 측정 결과는 아님"
}

REPO_DIR = Path(__file__).resolve().parents[1]
ASSET_DIR = REPO_DIR / "docs/assets/lesson"
VERSION = "professional-20261006-2"
BLUE = "#275879"
GREEN = "#36756f"
ORANGE = "#b2773d"
INK = "#17243b"
MUTED = "#64748b"
FONT_FAMILY = "'Noto Sans CJK KR', 'Malgun Gothic', sans-serif"
SVG_NS = "http://www.w3.org/2000/svg"
SURVEY_URL = "https://link.springer.com/article/10.1186/s40537-021-00444-8"
SURVEY_REFERENCES = {
    "survey_feature_learning": ("Fig. 3 · 특징 학습", "https://www.nature.com/articles/nature14539", "LeCun et al. (2015)"),
    "survey_classification_loss": ("CNN layers · Loss", "https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html", "PyTorch CrossEntropyLoss"),
    "survey_regularization": ("Regularization", "https://jmlr.org/papers/v15/srivastava14a.html", "Dropout 원 논문"),
    "survey_class_imbalance": ("Imbalanced data", "https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html", "클래스별 Loss 가중치"),
    "survey_cnn_pipeline": ("Fig. 7 · CNN layers", "https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html", "PyTorch Conv2d"),
    "survey_architecture_patterns": ("CNN architectures", "https://arxiv.org/abs/1409.1556", "VGG 원 논문"),
    "survey_residual_detail": ("Fig. 20 · ResNet", "https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html", "ResNet 원 논문"),
}
ASSET_DIR.mkdir(parents=True, exist_ok=True)


def text(x, y, value, size=28, color=INK, anchor="middle", bold=False):
    """Draw one text line; coordinates describe its baseline and anchor."""
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
        f'text-anchor="{anchor}" font-weight="{700 if bold else 400}">'
        f'{html.escape(str(value))}</text>'
    )


def rect(x, y, w, h, fill="#f8fafc", stroke="#cbd5e1", radius=4):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>')


def arrow(x1, y1, x2, y2, color=BLUE, dashed=False):
    dash = ' stroke-dasharray="8 6"' if dashed else ""
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" '
            f'stroke-width="2.5" fill="none" marker-end="url(#arrow-{color[1:]})"{dash}/>')


def svg(name, content, height=500):
    markers = "".join(
        f'<marker id="arrow-{c[1:]}" markerWidth="8" markerHeight="8" '
        f'refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="{c}"/></marker>'
        for c in [BLUE, GREEN, ORANGE, MUTED]
    )
    if '#lesson-photo' in content:
        markers += f'<image id="lesson-photo" width="960" height="640" xlink:href="{PHOTO_DATA}"/>'
    result = (f'<svg xmlns="{SVG_NS}" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1200 {height}" '
              f'font-family="{html.escape(FONT_FAMILY, quote=True)}">'
              f'<defs>{markers}</defs><rect width="1200" height="{height}" '
              f'fill="white"/>{content}</svg>\n')
    etree.fromstring(result.encode())
    (ASSET_DIR / f"{name}.svg").write_text(result, encoding="utf-8")
    return f"assets/lesson/{name}.svg"


def card(x, title, lines, color=BLUE, y=70, w=330, h=350):
    out = rect(x, y, w, h) + text(x + w / 2, y + 48, title, 30, color, bold=True)
    for i, line in enumerate(lines):
        out += text(x + w / 2, y + 118 + i * 52, line, 27)
    return out


def fruit(x, y, kind="apple", scale=1):
    """Place generated photographic examples instead of symbolic fruit drawings."""
    size = 88 * scale
    data = GENERATED_DATA[kind]
    return (f'<image x="{x-size/2}" y="{y-size/2}" width="{size}" '
            f'height="{size}" xlink:href="{data}" preserveAspectRatio="xMidYMid meet"/>')


def grid(x, y, values, cell=48, highlights=(), pale=False):
    out = ""
    for iy, row in enumerate(values):
        for ix, value in enumerate(row):
            fill = "#e5edf3" if (iy, ix) in highlights else "#f8fafc"
            if pale:
                shade = int(245 - float(value) * 20)
                fill = f"rgb({shade},{shade},{shade})"
            out += rect(x+ix*cell, y+iy*cell, cell, cell, fill, radius=0)
            out += text(x+(ix+.5)*cell, y+(iy+.65)*cell, value, min(27, cell*.48))
    return out


def heatmap(x, y, values, cell=40):
    values = np.asarray(values, dtype=float)
    lo, hi = values.min(), values.max()
    out = ""
    for iy, row in enumerate(values):
        for ix, value in enumerate(row):
            ratio = (value-lo)/(hi-lo) if hi != lo else .1
            c = tuple(int(a+(b-a)*ratio) for a, b in zip((239,246,255),(37,99,235)))
            out += rect(x+ix*cell, y+iy*cell, cell, cell, f"rgb{c}", "white", 0)
    return out


def pipeline(name, items, note=""):
    out = ""
    width = (1080 - 40*(len(items)-1))/len(items)
    for i, (title, lines) in enumerate(items):
        x = 60+i*(width+40)
        out += card(x, title, lines, y=85, w=width, h=300)
        if i < len(items)-1:
            out += arrow(x+width+5, 235, x+width+33, 235)
    if note:
        out += text(600, 455, note, 25, MUTED)
    return svg(name, out)


photo_root = etree.parse(str(REPO_DIR / "docs/assets/task_classification.svg"))
PHOTO_DATA = photo_root.find(f".//{{{SVG_NS}}}image").get("href")
GENERATED_DIR = REPO_DIR / "docs/assets/generated"
GENERATED_DATA = {
    name: "data:image/png;base64," + base64.b64encode(
        (GENERATED_DIR / f"{name}_studio_preview.png").read_bytes()
    ).decode("ascii")
    for name in ["apple", "orange"]
}
DEFECT_PATH = "M581 201 C595 200 605 209 609 221 C614 234 606 244 594 246 C580 247 572 236 571 224 C568 213 574 204 581 201Z"


def photo(x, y, w=240, mode="plain"):
    scale = w / 960
    out = (f'<use xlink:href="#lesson-photo" transform="translate({x} {y}) scale({scale})"/>')
    if mode == "box":
        out += rect(x+565*scale, y+197*scale, 53*scale, 57*scale, "none", BLUE, 0)
    if mode == "mask":
        out += (f'<path transform="translate({x} {y}) scale({scale})" '
                f'd="{DEFECT_PATH}" fill="#38bdf8" fill-opacity=".75" '
                f'stroke="{BLUE}" stroke-width="4"/>')
    return out


def build_professional_figures():
    """Use generated photography as examples, with exact native annotations."""
    out = text(185,65,"입력 이미지",28,BLUE,bold=True)
    out += fruit(185,230,"apple",3.4)
    stages = [(420,"국소 패턴",["명암 변화 · 경계","작은 수용영역"]),
              (675,"패턴 조합",["부분 형태 · 질감","이전 층의 반응 조합"]),
              (930,"Task 표현",["분류에 유용한 특징","더 넓은 입력 범위"]) ]
    for x, label, lines in stages:
        out += rect(x,95,235,255) + text(x+117.5,143,label,27,BLUE,bold=True)
        for j,line in enumerate(lines):
            out += text(x+117.5,218+j*52,line,22)
    out += arrow(345,230,410,230)
    out += arrow(660,230,670,230)+arrow(915,230,925,230)
    out += text(600,415,"계층적 표현: 국소 연산의 반복 → 넓은 문맥의 특징 조합",27,MUTED)
    out += text(600,460,"설명용 구조이며 실제 Feature Map을 관찰한 결과는 아닙니다",22,MUTED)
    svg("hierarchy_professional",out)

    out = text(285,55,"학습 데이터의 상관관계",29,BLUE,bold=True)
    out += text(915,55,"촬영 환경이 바뀐 데이터",29,GREEN,bold=True)
    for x, kind, fill, label in [(55,"apple","#e5edf3","Class: 사과"),
                                  (315,"orange","#f2e9dc","Class: 오렌지"),
                                  (685,"apple","#f2e9dc","Class: 사과"),
                                  (945,"orange","#e5edf3","Class: 오렌지")]:
        out += rect(x,105,200,235,fill,fill)
        out += fruit(x+100,205,kind,1.9)+text(x+100,375,label,25)
    out += arrow(530,225,660,225,MUTED)
    out += text(285,425,"Class와 배경색이 항상 함께 반복",25,BLUE)
    out += text(915,425,"물체는 유지, 배경색의 관계는 변경",25,GREEN)
    out += text(600,478,"배경만으로 맞춘 모델은 새로운 조건에서 실패할 수 있습니다",25,MUTED)
    svg("shortcut_professional",out)

    plate = "data:image/jpeg;base64," + base64.b64encode(
        (GENERATED_DIR / "capture_conditions.jpg").read_bytes()
    ).decode("ascii")
    out = f'<image x="35" y="85" width="1130" height="280" xlink:href="{plate}" preserveAspectRatio="xMidYMid meet"/>'
    for x,label in [(220,"기준 촬영"),(600,"측면 조명 · 저조도"),(980,"초점 변화")]:
        out += text(x,55,label,29,BLUE,bold=True)
        out += text(x,410,"정답 Class: 사과",26,GREEN)
    out += text(600,468,"촬영 조건을 다양하게 포함하고, Label 기준을 일관되게 관리",26,MUTED)
    svg("capture_conditions",out)


def build_figures():
    build_professional_figures()
    # Labels precede abstract feature-space plots.
    out = rect(30, 35, 550, 430) + rect(620, 35, 550, 430)
    out += text(305, 80, "지도학습: 입력–Label 관계 학습", 29, BLUE, bold=True)
    out += text(895, 80, "비지도학습: 데이터 구조 탐색", 29, GREEN, bold=True)
    for i, kind in enumerate(["apple", "orange", "apple"]):
        x=135+i*165
        out += fruit(x, 160, kind) + text(x, 220, "사과" if kind=="apple" else "오렌지", 25)
    out += arrow(305, 250, 305, 315) + text(305, 365, "새 이미지의 Class 예측", 28)
    out += rect(675, 115, 190, 235, "#f4f7fa", "#a9bfcc")
    out += rect(930, 115, 190, 235, "#fff7ed", "#fdba74")
    for x,y,k in [(725,165,"apple"),(815,230,"apple"),(745,295,"apple"),
                  (975,170,"orange"),(1060,235,"orange"),(990,295,"orange")]:
        out += fruit(x,y,k,.75)
    out += text(895, 405, "Label 없이 유사한 데이터 군집 탐색", 27)
    svg("learning_basic", out)

    out = ""
    for x, title in [(60,"Label을 이용해 경계 학습"),(650,"거리로 군집 탐색")]:
        out += rect(x, 40, 490, 410) + text(x+245, 85, title, 29, BLUE, bold=True)
        out += arrow(x+65, 370, x+435, 370, MUTED) + arrow(x+65, 370, x+65, 120, MUTED)
        out += text(x+270, 415, "특징 1", 23, MUTED) + text(x+68, 110,"특징 2",23,MUTED)
    for px,py,label in [(160,320,0),(210,280,0),(245,335,0),(300,300,0),
                        (365,180,1),(410,210,1),(450,160,1),(400,270,1)]:
        out += f'<circle cx="{px}" cy="{py}" r="12" fill="{BLUE if label==0 else ORANGE}"/>'
    out += '<path d="M320 130 L320 360" stroke="#334155" stroke-width="3" stroke-dasharray="8 6"/>'
    for cx,cy,color in [(790,290,BLUE),(990,205,ORANGE)]:
        out += f'<ellipse cx="{cx}" cy="{cy}" rx="75" ry="58" fill="none" stroke="{color}" stroke-width="3"/>'
        for dx,dy in [(-30,-8),(0,20),(28,-18)]:
            out += f'<circle cx="{cx+dx}" cy="{cy+dy}" r="12" fill="#64748b"/>'
    svg("learning_detail", out)

    out=rect(45,45,1110,185)+rect(45,270,1110,185)
    out+=text(180,95,"분류",31,BLUE,bold=True)+photo(80,115,200)
    out+=arrow(310,145,470,145)+rect(490,100,230,100,"#f4f7fa")
    out+=text(605,160,"모델",30,BLUE)+arrow(730,145,850,145)
    out+=text(985,145,"사과",34,GREEN,bold=True)+text(985,195,"범주 이름",27)
    out+=text(180,320,"회귀",31,BLUE,bold=True)+text(180,395,"입력 x = 2",30)
    out+=arrow(310,370,470,370)+rect(490,325,230,100,"#f4f7fa")
    out+=text(605,385,"모델",30,BLUE)+arrow(730,370,850,370)
    out+=text(985,370,"예측값 3.6",34,GREEN,bold=True)+text(985,420,"연속적인 숫자",27)
    svg("classification_basic",out)

    out=""
    for x,title,rows in [(45,"Binary: 2개 Class",[("정상",.18),("불량",.82)]),
                         (655,"Multi-class: 3개 이상",[("정상",.10),("Case A",.75),("Case B",.15)])]:
        out+=rect(x,35,500,430)+text(x+250,85,title,29,BLUE,bold=True)
        for i,(label,score) in enumerate(rows):
            y=150+i*100
            out+=text(x+30,y+30,label,26,INK,anchor="start")
            out+=rect(x+135,y,240,40,"#f4f7fa","none",3)
            out+=rect(x+135,y,240*score,40,BLUE,"none",3)
            out+=text(x+435,y+30,f"{score:.2f}",28,BLUE,bold=True)
    svg("classification_outputs",out)

    out = card(40,"입력 x = 2",["정답 y = 4","예측: ŷ = w × x","Bias는 0으로 고정"],w=330)
    out += card(435,"처음: w = 1",["ŷ = 1 × 2 = 2","정답보다 2 작음","Loss = (2 − 4)² = 4"],w=330)
    out += card(830,"수정 후: w = 1.8",["ŷ = 1.8 × 2 = 3.6","정답보다 0.4 작음","Loss = 0.16"],color=GREEN,w=330)
    out += arrow(375,240,425,240) + arrow(770,240,820,240)
    svg("learning_update",out)

    out = rect(80,55,1040,360)
    out += text(600,105,"오차를 보고 계산 기준을 바꿉니다",31,BLUE,bold=True)
    for x,v,label,color in [(245,4,"정답",INK),(510,2,"처음 예측",ORANGE),(810,3.6,"수정 후 예측",GREEN)]:
        out += text(x,165,label,27,color,bold=True)
        out += rect(x-40,340-v*34,80,v*34,"#e5edf3" if color==INK else "#e4efec" if color==GREEN else "#ffedd5",color,0)
        out += text(x,385,f"{v}",34,color,bold=True)
    out += text(600,465,"같은 입력 2 → 정답 4에 가까워지는 예측",28)
    svg("loss_basic",out)

    out = card(40,"입력",["밝기 x₁ = 0.5","모양 x₂ = 1.0"],w=300)
    out += card(450,"가중합",["0.2 × 0.5", "+ 0.8 × 1.0", "− 0.6 = 0.3"],w=300)
    out += card(860,"판정",["합계 0.3 ≥ 0","사과로 판정","예시 규칙"],color=GREEN,w=300)
    out += arrow(350,240,440,240) + arrow(760,240,850,240)
    svg("perceptron_basic",out)
    out = ""
    for y,label in [(150,"x₁ = 0.5"),(300,"x₂ = 1.0")]:
        out += rect(45,y-40,210,80,"#f4f7fa") + text(150,y+10,label,30)
    out += arrow(260,150,445,220) + arrow(260,300,445,240)
    out += text(330,145,"w₁ = 0.2",25,BLUE) + text(330,340,"w₂ = 0.8",25,BLUE)
    out += rect(455,175,310,120,"#f2f7f5")
    out += text(610,220,"z = Σ wᵢxᵢ + b",32,GREEN,bold=True)
    out += text(610,265,"z = 0.3",30)
    out += text(610,125,"b = −0.6",28,GREEN) + arrow(610,135,610,170,GREEN)
    out += arrow(775,235,850,235) + rect(860,175,300,120,"#f4f7fa")
    out += text(1010,220,"y = 1 if z ≥ 0",29,BLUE,bold=True)
    out += text(1010,265,"y = 0 if z < 0",29)
    out += text(600,430,"하나의 임계값 판정을 사용하는 퍼셉트론 예시",27,MUTED)
    svg("perceptron_detail",out)

    out = ""
    for x,gate in [(50,"AND"),(650,"XOR")]:
        out += rect(x,35,500,430) + text(x+250,80,gate,32,BLUE,bold=True)
        for a,b in [(0,0),(0,1),(1,0),(1,1)]:
            yes=(a and b) if gate=="AND" else a!=b
            px=x+135+a*240; py=350-b*200
            out += f'<circle cx="{px}" cy="{py}" r="18" fill="{BLUE if yes else "white"}" stroke="#334155" stroke-width="2"/>'
            out += text(px,py+45,f"({a}, {b})",23)
        if gate=="AND":
            # x1+x2=1.5 maps to a line sloping down in SVG coordinates.
            out += f'<path d="M{x+255} 150 L{x+375} 250" stroke="{GREEN}" stroke-width="4"/>'
            out += text(x+250,435,"직선 하나로 파란 점 분리",26,GREEN)
        else:
            out += text(x+250,435,"직선 하나로 파란 점 분리 불가",25,ORANGE)
    svg("and_xor",out)

    out = ""
    out += fruit(160,245,"apple",1.8) + text(160,370,"입력 이미지",27)
    for cx in [465,750]:
        for cy in [135,245,355]:
            out += f'<circle cx="{cx}" cy="{cy}" r="27" fill="#f4f7fa" stroke="{BLUE}" stroke-width="3"/>'
    for cy in [205,245,285]:
        for dy in [135,245,355]: out += arrow(205,cy,435,dy,MUTED)
    for sy in [135,245,355]:
        for dy in [135,245,355]:
            out += f'<path d="M492 {sy} L722 {dy}" stroke="#cbd5e1" stroke-width="2"/>'
    out += arrow(785,245,900,245) + card(915,"출력",["사과 점수","오렌지 점수"],y=130,w=240,h=245)
    out += text(465,440,"Layer 1",27,BLUE) + text(750,440,"Layer 2",27,BLUE)
    svg("network_basic",out)

    # Gradient: one parameter, one target, bias fixed. Arrow labels are exact.
    for detailed in [False,True]:
        out = arrow(100,405,740,405,MUTED)+arrow(100,405,100,40,MUTED)
        out += text(65,40,"Loss",25,MUTED)+text(755,440,"w",27,MUTED)
        def point(w): return 100+(w-.5)*200,405-((2*w-4)**2)*36
        points=[point(w) for w in np.linspace(.5,3.5,101)]
        out += '<polyline points="'+" ".join(f"{x:.2f},{y:.2f}" for x,y in points)+'" fill="none" stroke="#94a3b8" stroke-width="4"/>'
        for w in [1,2,3]:
            px,_=point(w);out+=text(px,435,str(w),23,MUTED)
        px,py=point(1)
        out+=f'<circle cx="{px}" cy="{py}" r="12" fill="{ORANGE}"/>'
        out+=text(px,py-25,"현재 w = 1",26,ORANGE)
        out+=arrow(px-8,py,px-90,py,ORANGE)+text(200,195,"Gradient: 왼쪽",24,ORANGE)
        out+=arrow(px+12,py,px+160,py,GREEN)+text(465,py-18,"수정: 오른쪽",25,GREEN)
        out+=card(820,"Loss를 줄이는 방향",["현재 위치의 경사 확인","반대 방향으로 이동","한 번에 조금씩"],y=80,w=330,h=340)
        if detailed:
            out=out[:out.index('<rect x="820"')]
            out+=card(800,"x = 2, y = 4, b = 0",["L(w) = (2w − 4)²","dL/dw = 8w − 16","w = 1: Gradient = −8","w′ = 1 − 0.1 × (−8)","= 1.8, Loss = 0.16"],y=35,w=370,h=430)
        svg("gradient_detail" if detailed else "gradient_basic",out)

    out = ""
    for i,(title,line) in enumerate([("예측","ŷ = 2"),("정답과 비교","y = 4"),("오차","Loss = 4"),("가중치 수정","w: 1 → 1.8")]):
        out+=card(45+i*295,title,[line],y=100,w=230,h=230)
        if i<3:out+=arrow(280+i*295,215,330+i*295,215)
    out+=f'<path d="M1045 345 L1045 405 L160 405 L160 345" stroke="{GREEN}" stroke-width="4" fill="none" marker-end="url(#arrow-36756f)"/>'
    out+=text(600,455,"바뀐 가중치로 다음 예측을 계산",28,GREEN)
    svg("training_basic",out)
    pipeline("backprop_basic",[("입력",["x = 2"]),("모델 계산",["ŷ = wx + b"]),("오차",["정답과 비교"])],"Forward: 예측 계산 / Backward: 각 가중치의 Gradient 계산")
    out = card(40,"Forward",["x = 2, w = 1, b = 0","ŷ = wx + b = 2","y = 4","L = (ŷ − y)² = 4"],y=35,w=330,h=430)
    out += card(435,"Backward",["∂L/∂ŷ = 2(ŷ − y) = −4","∂ŷ/∂w = x = 2","∂L/∂w = −4 × 2 = −8","∂L/∂b = −4"],y=35,w=330,h=430)
    out += card(830,"SGD, η = 0.1",["w′ = 1 − 0.1 × (−8)","= 1.8","b′ = 0.4","ŷ′ = 1.8 × 2 + 0.4 = 4"],color=GREEN,y=35,w=330,h=430)
    out += arrow(375,245,425,245) + arrow(770,245,820,245)
    svg("backprop_detail",out)

    out=""
    for x,title,lines in [(50,"학습 Training",["사진 + 정답","예측과 오차 계산","Weight 수정"]),
                          (650,"사용 Inference",["새 사진","학습된 Weight 고정","예측 결과 출력"])]:
        out+=rect(x,35,500,430)+text(x+250,80,title,31,BLUE,bold=True)
        out+=photo(x+130,115,240)
        for i,line in enumerate(lines):out+=text(x+250,320+i*49,line,27)
    svg("training_inference_basic",out)

    out=rect(45,50,1110,370)
    out+=text(600,100,"정답과 판정을 나란히 비교합니다",30,BLUE,bold=True)
    matrix=[("실제 불량","불량 판정: TP = 18","정상 판정: FN = 2"),
            ("실제 정상","불량 판정: FP = 4","정상 판정: TN = 76")]
    for i,row in enumerate(matrix):
        for j,v in enumerate(row):out+=text(235+j*360,210+i*130,v,28,INK if j==0 else GREEN if i==j-1 else ORANGE)
    out+=text(600,465,"전체 100개: 실제 불량 20개 / 실제 정상 80개",27,MUTED)
    svg("confusion_counts",out)
    out=card(55,"Precision 정밀도",["불량이라고 알린 22개","진짜 불량은 18개","18 / 22 = 81.8%"],w=490)
    out+=card(655,"Recall 재현율",["실제 불량 20개","찾아낸 불량은 18개","18 / 20 = 90%"],color=GREEN,w=490)
    svg("precision_recall",out)
    out=card(55,"Accuracy 정확도",["전체 중 맞춘 비율","(18 + 76) / 100","= 94%"],w=490)
    out+=card(655,"F1",["정밀도와 재현율의 조화평균","2TP / (2TP + FP + FN)","36 / 42 = 85.7%"],color=GREEN,w=490)
    svg("accuracy_f1",out)

    out=card(55,"Parameter",["모델이 배우는 값","Weight w = 1 → 1.8","Bias b = 0 → 0.4"],w=490)
    out+=card(655,"Hyperparameter",["학습을 설정하는 값","학습률 0.1","Batch 크기 4"],color=GREEN,w=490)
    svg("parameters_basic",out)

    out=""
    for i,(title,lines) in enumerate([
        ("촬영 조건",["밝기·거리·가림"]),("정답 기준",["일관된 Label"]),
        ("희귀 사례",["적은 불량도 확인"]),("운영 환경",["설비·시간대 확인"]) ]):
        x=35+i*295
        out+=rect(x,60,250,365)+text(x+125,110,title,29,BLUE,bold=True)
        if i==0:
            out+=photo(x+20,155,210)+text(x+125,365,lines[0],23)
        elif i==1:
            out+=fruit(x+125,210,scale=1.4)+text(x+125,295,"사과",32,GREEN)
            out+=text(x+125,365,lines[0],23)
        elif i==2:
            for j in range(8):
                out+=f'<circle cx="{x+55+(j%4)*46}" cy="{185+(j//4)*70}" r="15" fill="{ORANGE if j==7 else BLUE}"/>'
            out+=text(x+125,365,lines[0],23)
        else:
            for yy,label in [(170,"설비 A / 설비 B"),(235,"낮 / 밤")]:
                out+=rect(x+20,yy-30,210,60,"#f4f7fa")+text(x+125,yy+10,label,25)
            out+=text(x+125,365,lines[0],23)
    svg("dataset_basic",out)

    out=""
    for i,(title,label) in enumerate([("사진","960 × 640 RGB"),("크기 맞추기","예: 640 × 640"),("값 변환","0~255 → 0~1"),("축 순서","[1, 3, 640, 640]")]):
        x=35+i*295
        out+=rect(x,60,250,350)+text(x+125,110,title,29,BLUE,bold=True)
        if i==0:out+=photo(x+20,150,210)
        elif i==1:
            out+=rect(x+55,150,140,140,"#f4f7fa",BLUE,0)
            out+=text(x+125,225,"Resize",27,BLUE)
        elif i==2:
            out+=text(x+125,205,"128 / 255",30,BLUE)+text(x+125,260,"≈ 0.502",30,GREEN)
        else:
            for dx,dy,c in [(20,0,"#fee2e2"),(10,10,"#dcfce7"),(0,20,"#e5edf3")]:
                out+=rect(x+65+dx,150+dy,120,120,c,BLUE,0)
            out+=text(x+125,300,"B · C · H · W",24)
        out+=text(x+125,365,label,22)
        if i<3:out+=arrow(x+255,240,x+285,240)
    svg("preprocess_basic",out)

    out='<defs><filter id="dark"><feComponentTransfer><feFuncR type="linear" slope="0.5"/><feFuncG type="linear" slope="0.5"/><feFuncB type="linear" slope="0.5"/></feComponentTransfer></filter><filter id="blur"><feGaussianBlur stdDeviation="4"/></filter></defs>'
    for i,label in enumerate(["원본","어두운 조명","회전","초점 흐림"]):
        x=35+i*295
        out+=rect(x,60,250,350)+text(x+125,110,label,29,BLUE,bold=True)
        picture=photo(x+20,180,210)
        if i==1:picture='<g filter="url(#dark)">'+picture+'</g>'
        if i==2:picture=f'<g transform="rotate(12 {x+125} 250)">'+picture+'</g>'
        if i==3:picture='<g filter="url(#blur)">'+picture+'</g>'
        out+=picture+text(x+125,365,"정답: 불량",25,GREEN)
    svg("augmentation_basic",out)

    out=rect(55,65,1090,350)
    out+=text(600,120,"불량 점수에 기준을 적용합니다",31,BLUE,bold=True)
    out+=arrow(165,255,1040,255,MUTED)
    out+=text(165,300,"0",27,MUTED)+text(1040,300,"1",27,MUTED)
    out+='<path d="M605 180 L605 320" stroke="#334155" stroke-width="3" stroke-dasharray="8 6"/>'
    out+=text(605,165,"Threshold = 0.5",28)
    for value,label,color in [(.31,"정상",BLUE),(.82,"불량",ORANGE)]:
        x=165+875*value
        out+=f'<circle cx="{x}" cy="255" r="14" fill="{color}"/>'
        out+=text(x,365,f"{value}: {label}",28,color,bold=True)
    out+=text(600,465,"기준이 0.9이면 점수 0.82도 정상으로 판정",27,MUTED)
    svg("threshold_basic",out)

    out=card(55,"Loss",["학습의 목적함수","예측과 정답으로 계산","Gradient로 Weight 수정"],w=490)
    out+=card(655,"Metric",["성능을 해석하는 기준","Accuracy·Recall·IoU 등","모델·운영 성능 비교"],color=GREEN,w=490)
    svg("loss_metric_basic",out)

    # CNN: show patterns before numbers.
    out=rect(35,45,330,400)+text(200,90,"입력 이미지",30,BLUE,bold=True)+photo(60,130,280)
    out+=rect(440,45,325,400)+text(602,90,"작은 영역 확인",30,BLUE,bold=True)
    edge=[[0,0,1],[0,0,1],[0,0,1]]
    out+=grid(505,145,edge,65,highlights=[(y,x) for y in range(3) for x in range(3)])
    out+=text(602,395,"주변 Pixel의 밝기 변화",26)
    out+=rect(840,45,325,400)+text(1002,90,"반응 위치를 모으기",29,GREEN,bold=True)
    out+=heatmap(900,140,[[0,0,3,0],[0,1,3,0],[0,0,3,0],[0,0,1,0]],50)
    out+=text(1002,395,"경계에 강한 반응",27)
    out+=arrow(370,245,430,245)+arrow(775,245,830,245)
    svg("cnn_local_basic",out)

    out=card(35,"같은 필터",["세로 밝기 차이에 반응"],w=300)
    out+=grid(103,245,[[-1,0,1]]*3,55)
    out+=card(425,"경계가 있는 영역",["반응값 3"],w=330)
    out+=grid(500,245,edge,55)
    out+=card(830,"평평한 영역",["반응값 0"],color=GREEN,w=330)
    out+=grid(905,245,[[1,1,1]]*3,55)
    svg("kernel_basic",out)

    image=np.array([[1,2,3,0,1],[4,5,6,1,0],[7,8,9,2,1],[0,1,2,3,1],[1,0,1,2,3]])
    kernel=np.array([[1,0,-1]]*3)
    output=np.array([[int((image[y:y+3,x:x+3]*kernel).sum()) for x in range(3)] for y in range(3)])
    assert output.tolist()==[[-6,12,16],[-6,8,15],[-4,2,7]]
    out=text(205,55,"입력: 5 × 5",30,BLUE,bold=True)
    out+=grid(65,95,image.tolist(),56,[(y,x) for y in range(3) for x in range(3)])
    out+=text(560,55,"Kernel: 3 × 3",30,BLUE,bold=True)+grid(470,120,kernel.tolist(),60)
    out+=text(975,55,"출력: 3 × 3",30,GREEN,bold=True)+grid(885,120,output.tolist(),60,[(0,0)])
    out+=arrow(355,200,450,200)+arrow(665,200,860,200)
    out+=text(600,420,"첫 칸: (1 − 3) + (4 − 6) + (7 − 9) = −6",30)
    out+=text(600,470,"stride = 1, padding = 0, bias = 0 / 한 채널 예시",24,MUTED)
    svg("convolution_detail",out)

    for kind in ["stride","padding","downsampling"]:
        out=""
        if kind=="stride":
            for x,s,ow in [(60,1,3),(660,2,2)]:
                out+=rect(x,35,480,430)+text(x+240,80,f"Stride {s}: {s}칸씩 이동",30,BLUE,bold=True)
                out+=grid(x+95,110,[["" for _ in range(5)] for _ in range(5)],48,
                          [(y,x) for y in range(3) for x in range(3)])
                out+=arrow(x+119,135,x+119+48*s,135,ORANGE)
                out+=text(x+240,415,f"5 × 5 입력 → {ow} × {ow} 출력",28)
        elif kind=="padding":
            out+=text(235,60,"가장자리에 0을 채우기",30,BLUE,bold=True)
            padded=[[0 if y in [0,6] or x in [0,6] else "·" for x in range(7)] for y in range(7)]
            out+=grid(55,100,padded,50,[(y,x) for y in range(1,6) for x in range(1,6)])
            out+=arrow(430,270,625,270)+card(670,"Padding = 1",["5 × 5 → 7 × 7로 둘러쌈","Kernel 3, Stride 1","출력은 5 × 5"],y=80,w=475,h=340)
        else:
            values=np.arange(64).reshape(8,8)%11
            pooled=values.reshape(4,2,4,2).max(axis=(1,3))
            out+=text(240,65,"공간 크기 8 × 8",30,BLUE,bold=True)+heatmap(80,105,values,40)
            out+=arrow(445,265,735,265)+text(600,225,"2 × 2 Max Pooling",26,BLUE)
            out+=text(980,65,"공간 크기 4 × 4",30,GREEN,bold=True)+heatmap(840,125,pooled,70)
            out+=text(600,470,"각 2 × 2 영역의 최댓값을 남기는 예시",27,MUTED)
        svg(kind+"_basic",out)

    out=text(600,60,"Hout = floor((H + 2P − K) / S) + 1",34,BLUE,bold=True)
    out+=text(600,105,"dilation = 1 / Wout도 같은 식으로 계산",25,MUTED)
    for i,(title,lines) in enumerate([
        ("줄어드는 출력",["H = 5, K = 3","S = 1, P = 0","Hout = 3"]),
        ("크기 유지",["H = 5, K = 3","S = 1, P = 1","Hout = 5"]),
        ("두 칸씩 이동",["H = 5, K = 3","S = 2, P = 0","Hout = 2"]) ]):
        out+=card(45+i*395,title,lines,y=150,w=320,h=300)
    svg("spatial_detail",out)

    out=photo(35,130,310)+text(190,95,"같은 입력",30,BLUE,bold=True)
    out+=arrow(355,230,460,230)
    for i,(label,vals) in enumerate([
        ("세로 경계",[[0,1,4,0]]*4),
        ("가로 경계",[[0]*4,[1]*4,[4]*4,[0]*4]),
        ("밝은 영역",[[0,0,0,0],[0,4,4,0],[0,4,4,0],[0,0,0,0]])]):
        x=490+i*235
        out+=text(x+90,95,label,27,GREEN,bold=True)+heatmap(x,135,vals,45)
        out+=text(x+90,370,f"반응 지도 {i+1}",26)
    out+=text(600,460,"설명용 반응 지도: 실제 모델의 Feature Map은 학습으로 결정",25,MUTED)
    svg("feature_basic",out)

    out=card(35,"RGB 입력",["H × W × Cin","224 × 224 × 3"],y=100,w=300,h=290)
    out+=card(440,"64개 필터",["필터 하나: 3 × 3 × 3","RGB 전체를 곱하고 합산","stride 1, padding 1"],y=100,w=330,h=290)
    out+=card(870,"64개 출력 Channel",["Hout × Wout × Cout","224 × 224 × 64"],color=GREEN,y=100,w=300,h=290)
    out+=arrow(345,245,430,245)+arrow(780,245,860,245)
    out+=text(600,460,"PyTorch Weight: [64, 3, 3, 3] / Weight 1,728개 + Bias 64개",27,MUTED)
    svg("feature_detail",out)

    out=photo(30,145,255)+text(158,105,"같은 사과 사진",29,BLUE,bold=True)
    out+=arrow(295,230,360,230)+card(370,"Backbone",["판단에 유용한","특징 계산"],y=120,w=255,h=270)
    for i,(title,mode,result) in enumerate([("분류 Head","plain","불량"),("검출 Head","box","결함 Box"),("분할 Head","mask","결함 Mask")]):
        y=20+i*155
        out+=arrow(635,250,720,y+70,BLUE)+rect(740,y,420,140,"#f8fafc")
        out+=text(835,y+45,title,27,BLUE,bold=True)+text(835,y+100,result,26,GREEN)
        out+=photo(950,y+10,180,mode)
    svg("backbone_basic",out)
    out=text(455,60,"Backbone: Conv 3 × 3, Stride 2, Padding 1",30,BLUE,bold=True)
    for i,(label,shape) in enumerate([("Input","224² × 3"),("Conv 1","112² × 64"),("Conv 2","56² × 128"),("Conv 3","28² × 192"),("Conv 4","14² × 256")]):
        x=30+i*170
        out+=text(x+65,135,label,26,BLUE)
        out+=rect(x+10,180,100,140-i*17,"#e5edf3",BLUE,0)
        out+=f'<path d="M{x+110} 180 l20 -15 v{140-i*17} l-20 15Z" fill="#a9bfcc" stroke="{BLUE}" stroke-width="2"/>'
        out+=text(x+65,380,shape,23)
        if i<4:out+=arrow(x+135,240,x+165,240)
    for i,(label,result) in enumerate([("분류 Head","Class logits"),("검출 Head","Box + Class"),("분할 Head","Pixel logits")]):
        y=105+i*120
        out+=arrow(855,245,920,y+43)+rect(935,y,240,90,"#f2f7f5",GREEN)
        out+=text(1055,y+35,label,27,GREEN,bold=True)+text(1055,y+72,result,25)
    out+=text(600,465,"크기는 H × W × C / 예시 구조이며 Task별 Head·Decoder는 다름",26,MUTED)
    svg("backbone_detail",out)

    out=card(35,"이미 배운 모델",["여러 이미지로 학습","기본적인 특징 계산"],w=330)
    out+=card(435,"내 사진 + 정답",["새 Task의 Label","내 조건으로 추가 학습"],w=330)
    out+=card(835,"내 Task에 맞춘 모델",["새 조건에서 평가","필요하면 더 학습"],color=GREEN,w=330)
    out+=arrow(375,245,425,245)+arrow(775,245,825,245)
    svg("transfer_basic",out)
    out=rect(45,55,1110,365)
    out+=text(325,110,"Feature Extractor",31,BLUE,bold=True)+text(905,110,"새 Head",31,GREEN,bold=True)
    for i in range(4):out+=rect(105+i*115,150,90,130,"#e5edf3",BLUE)
    out+=arrow(585,215,745,215)+rect(775,150,270,130,"#e4efec",GREEN)
    out+=text(325,345,"Freeze: Weight 고정",27,BLUE)+text(905,345,"Task Label로 학습",27,GREEN)
    out+=text(600,475,"Fine-tuning: Backbone 일부 또는 전체까지 업데이트하며 검증",27,MUTED)
    svg("transfer_detail",out)

    # A clean numeric IoU example; no ambiguous overlap approximation.
    out=""
    for x,title,color in [(110,"정답과 예측",BLUE),(610,"겹침 / 합집합",GREEN)]:
        out+=text(x+190,60,title,30,color,bold=True)
    for x in [110,610]:
        for iy in range(4):
            for ix in range(5):
                gt=ix<3;pred=ix>=2
                fill="#99f6e4" if gt and pred else "#e5edf3" if gt else "#fed7aa"
                out+=rect(x+ix*75,110+iy*75,75,75,fill,"white",0)
    out+=text(300,455,"파랑: 정답 / 주황: 예측",27)
    out+=text(800,455,"초록 4칸 / 전체 20칸",27)
    svg("iou_detail",out)

    out=rect(35,35,470,420)+text(270,80,"ReLU: 음수는 0, 양수는 그대로",27,BLUE,bold=True)
    out+=arrow(95,345,445,345,MUTED)+arrow(270,395,270,115,MUTED)
    out+=f'<path d="M105 345 H270 L420 155" fill="none" stroke="{BLUE}" stroke-width="5"/>'
    out+=text(180,400,"x < 0 → 0",25)+text(360,400,"x > 0 → x",25)
    out+=rect(570,35,590,420)+text(865,80,"비선형 계산으로 XOR 경계 표현",28,GREEN,bold=True)
    # In these plot coordinates, s=x1+x2=.5 and 1.5 form a diagonal strip.
    out+='<path d="M705 245 L825 345 L945 345 L945 245 L825 145 L705 145Z" fill="#e4efec" fill-opacity=".65"/>'
    out+=f'<path d="M705 245 L825 345 M825 145 L945 245" fill="none" stroke="{GREEN}" stroke-width="4"/>'
    for a,b in [(0,0),(0,1),(1,0),(1,1)]:
        px=705+a*240;py=345-b*200
        out+=f'<circle cx="{px}" cy="{py}" r="15" fill="{BLUE if a!=b else "white"}" stroke="#334155" stroke-width="2"/>'
        out+=text(px,py+38,f"({a}, {b})",22)
    out+=text(865,425,"두 경계 사이: x₁ + x₂가 0.5~1.5",24,GREEN)
    svg("activation_basic",out)

    out=""
    for i,(title,lines) in enumerate([("Data",["사진·Label","분리 기준"]),("Train",["Weight 학습","설정 선택"]),("Evaluate",["최종 Test","실패 사례"]),("Deploy",["추론 시스템","전처리 일치"]),("Monitor",["운영 실패","새 조건 확인"]) ]):
        x=30+i*235
        out+=card(x,title,lines,y=60,w=200,h=260)
        if i<4:out+=arrow(x+205,190,x+230,190)
    out+=f'<path d="M1070 340 V385 H130 V340" fill="none" stroke="{GREEN}" stroke-width="4" marker-end="url(#arrow-36756f)"/>'
    out+=text(600,450,"운영 실패 사례를 데이터 보강과 재학습에 연결",29,GREEN)
    svg("workflow_basic",out)


def build_opening_figures():
    """Give opening slides fixed text bands, generous margins and aligned rows."""
    out = text(35, 32, "기술·방법의 포함 관계", 24, MUTED, "start", True)
    out += rect(35, 55, 705, 390, "#f2f6fa", BLUE)
    out += text(65, 98, "AI · Artificial Intelligence", 30, BLUE, "start", True)
    out += text(65, 136, "판단·추론·인식 등을 수행하는 넓은 기술 영역", 25, INK, "start")
    out += rect(85, 164, 625, 251, "#edf5f2", GREEN)
    out += text(115, 207, "ML · Machine Learning", 30, GREEN, "start", True)
    out += text(115, 245, "데이터에서 규칙과 패턴을 학습하는 방법", 25, INK, "start")
    out += rect(135, 272, 545, 113, "white", BLUE)
    out += text(165, 315, "DL · Deep Learning", 30, BLUE, "start", True)
    out += text(165, 353, "여러 층의 신경망으로 학습하는 방법", 25, INK, "start")
    out += text(790, 32, "이미지·영상 문제를 다루는 분야", 24, MUTED, "start", True)
    out += rect(790, 55, 375, 390, "white", "#cbd5e1")
    out += text(820, 98, "Computer Vision", 30, BLUE, "start", True)
    out += text(820, 136, "분류 · 검출 · 분할 등", 25, INK, "start")
    out += '<path d="M820 167 H1135" stroke="#cbd5e1"/>'
    out += text(820, 206, "문제에 맞는 방법을 사용", 25, INK, "start", True)
    for y, label in [(259, "전통적 영상처리"), (313, "Machine Learning"), (367, "Deep Learning")]:
        out += text(820, y, label, 25, MUTED, "start")
    svg("ai_methods_scope", out, 475)

    out = ""
    for x, color, title, subtitle in [
        (35, BLUE, "규칙 기반 · Rule-based", "판단 조건을 사람이 직접 작성"),
        (625, GREEN, "학습 기반 · Machine Learning", "사진과 정답으로 모델의 가중치를 학습"),
    ]:
        out += rect(x, 25, 540, 425, "white", "#cbd5e1")
        out += text(x+25, 70, title, 28, color, "start", True)
        out += text(x+25, 109, subtitle, 24, MUTED, "start")
    out += rect(60, 145, 490, 86, "#f2f6fa", "#d8e2ea")
    out += text(85, 180, "사람이 설정한 기준", 23, MUTED, "start")
    out += text(85, 213, "밝기 < 100이면 후보로 판단", 26, BLUE, "start", True)
    out += text(60, 272, "적용", 22, MUTED, "start", True)
    for x, w, label in [(60, 200, "입력 밝기 80"), (350, 200, "결과: 후보")]:
        out += rect(x, 290, w, 64, "#f2f6fa", "#d8e2ea")
        out += text(x+w/2, 330, label, 25, BLUE, bold=True)
    out += arrow(275, 322, 333, 322)
    out += text(60, 398, "기준을 바꾸려면 조건식을 수정", 24, INK, "start")
    out += text(650, 154, "학습", 22, MUTED, "start", True)
    out += text(650, 272, "추론 · 학습한 모델을 적용", 22, MUTED, "start", True)
    for y, labels in [(173, ["사진 + 정답", "학습", "가중치"]),
                      (290, ["새 사진", "학습된 모델", "예측 결과"])]:
        for x, label in zip([650, 830, 1010], labels):
            out += rect(x, y, 130, 64, "#edf5f2", "#d8e5df")
            out += text(x+65, y+40, label, 22, GREEN, bold=True)
        out += arrow(790, y+32, 817, y+32, GREEN)
        out += arrow(970, y+32, 997, y+32, GREEN)
    out += text(650, 398, "기준을 바꾸려면 데이터로 다시 학습", 24, INK, "start")
    svg("rule_learning_comparison", out, 475)


def legacy_figure(name):
    """Copy an existing diagram without repeating the slide title inside it."""
    source=REPO_DIR / "docs/assets" / f"{name}.svg"
    root=etree.parse(str(source)).getroot()
    for child in list(root):
        if child.tag==f"{{{SVG_NS}}}text" and float(child.get("y","999"))<=100:
            root.remove(child)
    for element in root.iter(f"{{{SVG_NS}}}text"):
        if element.text=="위치 구조가 숫자 나열로 사라짐":
            element.text="공간 이웃 구조를 명시하지 않음"
        if element.text=="Weight가 크면 그 입력이 Output에 더 크게 영향을 줍니다.":
            element.text="가중치의 부호·크기와 입력 범위를 함께 봅니다."
    for element in root.iter():
        if element.tag==f"{{{SVG_NS}}}path" and element.get("stroke") and not element.get("fill"):
            element.set("fill","none")
        if element.tag==f"{{{SVG_NS}}}image" and element.get("href"):
            element.set("{http://www.w3.org/1999/xlink}href",element.get("href"))
    # Existing content starts below the removed headings.
    root.set("viewBox","0 105 1200 495")
    path=ASSET_DIR / f"context_{name}.svg"
    serialized = etree.tostring(root,encoding="unicode",xml_declaration=False)
    for old, new in {"#2563eb":BLUE,"#0f766e":GREEN,"#ea580c":ORANGE,
                     "#dbeafe":"#e5edf3","#93c5fd":"#a9bfcc"}.items():
        serialized = serialized.replace(old, new)
    serialized = serialized.replace('rx="18"', 'rx="4"').replace('rx="20"', 'rx="4"')
    path.write_text(serialized, encoding="utf-8")
    return "assets/lesson/"+path.name


def build_deck(filename, title, subtitle, cards, lessons, prev_page, next_page=""):
    """Write a complete deck, continuous visible numbers, and a source manifest."""
    header=f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="slide.css?v=generatedfigfit-20260927-27">
<link rel="stylesheet" href="lesson.css?v={VERSION}">
<script src="slide.js?v=generatedfigfit-20260927-27" defer></script>
</head><body class="deck-page lesson-deck" data-prev-page="{prev_page}" data-next-page="{next_page}">
<header class="site-header"><nav class="nav"><a class="brand" href="index.html">Vision AI</a>
<div class="nav-links"><a href="index.html">목차</a><a href="intro.html">01 Intro</a><a href="ai_basics.html">02 AI Basics</a>
<a href="vision_ai.html">03 Vision AI</a></div></nav></header>
<main class="deck" aria-live="polite">
<section class="slide active"><div class="slide-inner">
<div class="lesson-meta">{html.escape(title)}</div>
<h1 class="slide-title">{html.escape(subtitle)}</h1>
<div class="lesson-outline">'''
    for label,body in cards:
        header+=f'<article><strong>{html.escape(label)}</strong><p>{html.escape(body)}</p></article>'
    header+='</div></div></section>\n'
    manifest=[]
    for index, lesson in enumerate(lessons,1):
        topic,heading,description,asset,takeaway,*extra=lesson
        detailed=bool(extra and extra[0])
        if asset.startswith("old:"):
            asset=legacy_figure(asset[4:])
        else:
            asset=f"assets/lesson/{asset}.svg"
        reference=""
        if detailed:
            url="https://cs231n.github.io/convolutional-networks/" if filename=="vision_ai.html" else "https://cs231n.github.io/"
            reference=f'<p class="lesson-reference">개념 참고: <a href="{url}" target="_blank" rel="noopener">Stanford CS231n</a> · 직접 재구성한 설명용 Figure</p>'
        if any(name in asset for name in ["learning_basic", "network_basic", "capture_conditions", "shortcut_professional", "hierarchy_professional"]):
            reference += '<p class="lesson-reference">사진: AI 생성 교육용 예시 · 실제 측정/실험 결과가 아님</p>'
        figure_version = VERSION
        if Path(asset).stem in {"loss_basic", "gradient_basic", "gradient_detail", "optimizer_learning_rates"}:
            figure_version = "loss-optimizer-20261006-2"
            reference = '<p class="lesson-reference">개념 참고: <a href="https://cs231n.github.io/optimization-1/" target="_blank" rel="noopener">Stanford CS231n · Optimization</a> · 실제 계산한 단일 샘플 회귀 예시</p>'
        if Path(asset).stem in SURVEY_REFERENCES:
            section, primary_url, primary_label = SURVEY_REFERENCES[Path(asset).stem]
            figure_version = "survey-20261006-1"
            if Path(asset).stem == "survey_feature_learning":
                figure_version = "survey-20261006-2"
            reference = (
                f'<p class="lesson-reference">참고: <a href="{SURVEY_URL}" '
                f'target="_blank" rel="noopener">Alzubaidi et al. (2021) · {section}</a>'
                f' · <a href="{primary_url}" target="_blank" rel="noopener">{primary_label}</a>'
                ' · 강의용 재구성</p>'
            )
        if Path(asset).stem.startswith("lecture_"):
            figure_version = "visual-20261013-1"
            reference = (
                '<p class="lesson-reference">참고: '
                '<a href="https://cs.brown.edu/courses/csci1430/2020_Spring/lectures/2020Spring_02_ImageFiltering.pdf" '
                'target="_blank" rel="noopener">Brown CSCI1430 Image Filtering (2020)</a> · '
                '<a href="https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html" '
                'target="_blank" rel="noopener">OpenCV Image Filtering</a> · 검산된 설명용 도식</p>'
            )
        if Path(asset).stem in PROCESSING_SECTIONS:
            section = PROCESSING_SECTIONS[Path(asset).stem]
            figure_version = "processing-20261006-2" if Path(asset).stem == "processing_pyramid" else "processing-20261006-1"
            reference = (
                '<p class="lesson-reference">참고: <a href="https://szeliski.org/Book/1stEdition.htm" '
                f'target="_blank" rel="noopener">Szeliski · Ch. 3 {section}</a>'
                ' · 기존 AI 생성 사진 / 합성 데이터에 실제 연산 적용</p>'
            )
        if reference:
            reference = reference.replace(
                '<p class="lesson-reference">',
                '<details class="lesson-reference"><summary>출처 · 근거</summary><div>'
            ).replace('</p>', '</div></details>')
        header+=f'''<section class="slide" data-topic="{html.escape(topic)}" data-level="{"detail" if detailed else "basic"}">
<div class="slide-inner"><div class="lesson-meta"><span>{index:02d} · {html.escape(topic)}</span>
<span class="lesson-level{" lesson-level--detail" if detailed else ""}">{"심화 학습" if detailed else "핵심 개념"}</span></div>
<h2 class="slide-title">{html.escape(heading)}</h2>
<p class="slide-subtitle">{html.escape(description)}</p>
<figure class="lesson-figure"><a href="{asset}?v={figure_version}" target="_blank" rel="noopener" title="그림 원본 크기로 확대"><img src="{asset}?v={figure_version}" alt="{html.escape(FIGURE_ALT_DESCRIPTIONS.get(Path(asset).stem, heading))}"></a></figure>
<p class="lesson-takeaway">{html.escape(takeaway)}</p>{reference}</div></section>\n'''
        manifest.append({"number":index,"topic":topic,"level":"detail" if detailed else "basic","title":heading,"asset":asset})
    header+='''</main><div class="deck-controls"><div class="deck-controls-inner">
<button class="deck-button" type="button" data-slide-prev>← 이전</button>
<div class="deck-status"><div class="lesson-mode-controls"><button class="lesson-mode-toggle" type="button" data-lesson-mode-toggle aria-pressed="false" aria-label="핵심/전체 학습 경로 전환">핵심만 보기</button><span class="lesson-mode-summary" data-lesson-mode-summary>전체 과정 · 심화 포함</span></div><span class="deck-counter"><span data-slide-current>1</span> / <span data-slide-total>1</span></span>
<div class="deck-progress"><div class="deck-progress-bar" data-slide-progress></div></div></div>
<button class="deck-button" type="button" data-slide-next>다음 →</button></div></div></body></html>\n'''
    (REPO_DIR / "docs" / filename).write_text(header,encoding="utf-8")
    return manifest


def build_lessons():
    # Basic illustrations are followed by selected exact diagrams, not mixed on one slide.
    ai=[
        ("AI의 범위","AI·머신러닝·딥러닝은 어떻게 다를까요?","AI는 넓은 기술 영역입니다. 머신러닝은 데이터에서 배우고, 딥러닝은 여러 층의 신경망으로 학습합니다.","ai_methods_scope","Computer Vision(컴퓨터 비전)은 이미지·영상 문제를 다루는 분야입니다."),
        ("규칙과 학습","판단 기준을 사람이 쓰거나, 데이터에서 배웁니다","규칙 기반은 사람이 조건을 정합니다. 학습 기반은 사진과 정답에서 판단 기준을 학습합니다.","rule_learning_comparison","실제 시스템에서는 영상처리 규칙과 학습 모델을 함께 사용하기도 합니다."),
        ("지도학습과 비지도학습","지도학습과 비지도학습은 학습 목표가 다릅니다","지도학습은 사진과 정답을 함께 사용합니다. 비지도학습은 정답 이름표 없이 데이터의 공통 구조를 찾습니다.","learning_basic","정답 Label(라벨)은 모델이 배워야 할 목표를 알려주는 데이터입니다."),
        ("지도학습과 비지도학습","사진을 숫자로 표현하면 경계와 군집으로 설명할 수 있습니다","Feature(특징)는 판단에 유용한 단서입니다. 특징 공간은 각 데이터를 그 단서들의 숫자로 배치한 공간입니다.","learning_detail","점의 색은 지도학습의 정답, 오른쪽 원은 비슷한 데이터의 군집을 나타냅니다.",True),
        ("분류와 회귀","분류는 이름을, 회귀는 연속적인 숫자를 예측합니다","Classification(분류)은 사과·오렌지 같은 범주를, Regression(회귀)은 입력 숫자에서 3.6 같은 연속적인 값을 예측합니다.","classification_basic","먼저 어떤 형태의 결과가 필요한지 정하면 학습 목표가 분명해집니다."),
        ("분류의 출력","두 종류 또는 여러 종류 중에서 점수를 비교합니다","Binary Classification(이진 분류)은 두 Class, Multi-class Classification(다중 클래스 분류)은 세 개 이상을 구분합니다.","classification_outputs","그림은 확률 형식의 점수 예시입니다. 높은 점수가 현실의 정확한 확률이나 정답을 보장하지는 않습니다."),
        ("Perceptron","입력마다 가중치를 곱하고, 더해서 하나의 판정을 만듭니다","Perceptron(퍼셉트론)은 입력에 가중치를 곱하고 Bias를 더해 판정합니다. 밝기와 모양을 사용한 가상 수치를 직접 계산합니다.","lesson_perceptron_numeric_flow","Weight는 입력의 기여도를, Bias는 합계의 기준 위치를 조절합니다."),
        ("Perceptron","입력·가중합·판정 함수를 계산 그래프로 연결합니다","z는 가중합, b는 Bias(편향) Parameter입니다. 여기서는 z≥0이면 1을 출력하는 임계값 판정을 사용합니다.","perceptron_detail","가중치의 영향은 부호·절댓값과 입력의 크기를 함께 봐야 합니다.",True),
        ("Parameter와 Hyperparameter","모델이 배우는 값과, 학습을 설정하는 값은 다릅니다","Parameter(파라미터)는 Weight·Bias처럼 학습하는 값입니다. Hyperparameter(하이퍼파라미터)는 학습률·Batch 크기 등 설정입니다.","parameters_basic","Bias Parameter와 데이터가 한쪽으로 치우쳤다는 의미의 Data Bias는 다른 개념입니다."),
        ("Neural Network","여러 계산을 Layer로 연결하면 신경망이 됩니다","Neural Network(신경망)의 각 Layer(층)는 앞에서 받은 숫자를 조합해 다음 층으로 전달합니다.","network_basic","그림의 노드·연결은 계산 구조를 나타내며, 실제 모델의 뉴런 수와는 다릅니다. 사진 1장을 입력하는 예시입니다."),
        ("AND와 XOR","하나의 직선으로 나눌 수 없는 문제도 있습니다","AND는 두 입력 모두 1일 때만 1입니다. XOR는 두 입력이 서로 다를 때 1입니다. 파란 점은 출력 1, 흰 점은 출력 0입니다.","lesson_and_xor_separability","AND의 경계는 x₁+x₂=1.5입니다. XOR의 파란 점 두 개는 직선 하나로 분리할 수 없습니다."),
        ("Activation","Layer를 쌓을 때 비선형 계산도 필요합니다","Activation Function(활성화 함수)은 계산에 비선형성을 넣습니다. ReLU는 입력이 0보다 작으면 0, 크면 입력값을 그대로 출력합니다.","lesson_relu_value_graph","ReLU f(x)=max(0,x)는 x=0에서 그래프가 꺾입니다. 이것이 여러 Layer의 계산을 단순한 직선에서 벗어나게 할 수 있습니다."),
        ("선형 Layer의 한계","비선형성이 없으면 여러 Layer도 하나로 합쳐집니다","예시: h=2x+1, y=3h−2라면 활성화가 없을 때 y=6x+1로 합쳐집니다. 중간에 ReLU를 넣으면 x=−0.5에서 기울기가 달라집니다.","lesson_affine_relu_comparison","Affine 연산만 연속하면 다시 Affine 연산입니다. 비선형 Activation이 있어야 선형으로 표현할 수 없는 관계를 학습할 가능성이 생깁니다.",True),
        ("학습의 의미","학습은 예측 오차가 줄도록 계산 기준을 바꾸는 과정입니다","입력 x=2, 정답 y=4를 사용합니다. 모델 ŷ=w×x의 w를 바꾸면 같은 입력의 예측값이 달라집니다.","learning_update","여기서 w는 학습으로 바꾸는 가중치이고, Bias는 0으로 고정한 예시입니다."),
        ("Loss","Loss는 예측과 정답의 차이를 학습용 숫자로 바꿉니다","정답 y=4를 고정하고 후보 예측 2·3.6·4를 비교합니다. 회귀용 제곱오차는 차이의 부호를 없애고, 큰 오차에 더 큰 Loss를 부여합니다.","loss_basic","여러 샘플의 제곱오차를 평균하면 MSE(Mean Squared Error, 평균제곱오차)입니다. 문제에 따라 다른 Loss를 사용합니다."),
        ("Loss와 Metric","학습할 때 줄이는 값과, 평가할 때 보는 값은 역할이 다릅니다","Loss는 가중치를 갱신하는 목적함수입니다. Metric(평가지표)은 실제 문제에서 성능을 해석하고 비교하는 기준입니다.","loss_metric_basic","Loss가 줄었다고 원하는 Metric이나 운영 성능이 항상 개선되는 것은 아닙니다."),
        ("Gradient","기울기는 가중치를 어느 방향으로 바꿀지 알려줍니다","입력 x=2와 정답 y=4는 고정하고, 가중치 w만 바꿉니다. 현재 w=1에서 기울기가 음수이므로, w를 조금 늘리면 Loss가 줄어듭니다.","gradient_basic","가로축은 예측값이나 학습 시간이 아닌 가중치 w입니다. 이 곡선은 한 가중치를 사용하는 회귀 예시입니다."),
        ("Gradient와 Learning Rate","기울기 계산 → 가중치 수정 → Loss 재계산을 연결합니다","Gradient는 −8, Learning Rate(학습률) η는 0.1입니다. SGD(Stochastic Gradient Descent, 확률적 경사하강법)의 기본 갱신식으로 w를 1에서 1.8로 바꿉니다.","lesson_sgd_update_flow","같은 x=2에서 예측은 2 → 3.6, Loss는 4 → 0.16입니다. Bias는 0으로 고정하고 Momentum·Weight Decay는 사용하지 않습니다.",True),
        ("Optimizer","같은 수정 규칙도 학습률에 따라 결과가 달라집니다","Optimizer(최적화 알고리즘)는 가중치의 갱신 규칙입니다. 여기서는 SGD를 고정하고 학습률 η만 0.025·0.1·0.3으로 바꿔 Loss 변화를 실제 계산했습니다.","optimizer_learning_rates","Loss는 줄일 목표, Gradient는 변화율, Optimizer는 수정 규칙입니다. 적절한 학습률은 문제에 따라 다르며 0.1이 항상 최선인 것은 아닙니다."),
        ("Training Loop","예측 → 오차 → Gradient → 수정을 반복합니다","Training(학습)은 한 번의 계산으로 끝나지 않습니다. 바뀐 가중치로 다음 예측을 계산하고 다시 오차를 줄입니다.","training_basic","Forward는 예측 계산, Backward는 Gradient 계산, Update는 가중치 수정입니다."),
        ("Training과 Inference","배울 때는 Weight를 바꾸고, 사용할 때는 고정합니다","Inference(추론)는 학습된 모델에 새 입력을 넣어 결과를 얻는 과정입니다. 정답 없이도 예측할 수 있습니다.","training_inference_basic","추론 과정 자체는 새로운 데이터로 가중치를 학습하는 과정이 아닙니다."),
        ("분류용 Loss", "분류에서는 정답 클래스의 확률을 이용할 수 있습니다", "Cross-entropy(교차 엔트로피)는 정답 클래스에 낮은 확률을 주면 큰 Loss를 부여합니다. 회귀에서 사용한 제곱오차와 구분합니다.", "survey_classification_loss", "단일 정답·단일 샘플에서 L=−ln(p정답)입니다. PyTorch CrossEntropyLoss에는 Softmax 확률 대신 원래 Logit(정규화 전 점수)을 입력합니다.", True),
        ("특징 학습", "딥러닝은 특징을 만드는 계산도 학습합니다", "전통적 ML의 한 예는 사람이 특징을 설계한 뒤 분류기를 학습합니다. 딥러닝은 특징 층과 분류 층을 함께 학습할 수 있습니다.", "survey_feature_learning", "자동 특징 학습도 데이터·정답·학습 목표의 설계가 필요합니다. 모든 ML 방법을 이 비교로 나눌 수는 없습니다."),
        ("Feature와 Representation","이미지 숫자는 판단에 유용한 내부 표현으로 바뀝니다","Feature는 판단에 유용한 단서이고, Representation(표현)은 모델 내부에서 이를 담는 숫자입니다. 여기서는 이미지가 수치적 특징 표현으로 바뀐다는 개념을 살펴봅니다.","hierarchy_professional","특징을 숫자로 표현한다는 개념을 익힙니다. Convolution으로 Feature Map을 실제 계산하는 과정은 Vision AI 강의에서 이어집니다."),
        ("Backpropagation","오차에서 각 가중치의 Gradient를 뒤로 계산합니다","Backpropagation(역전파)은 출력의 오차가 각 가중치에 얼마나 민감한지 계산합니다. 가중치 수정은 Optimizer가 수행합니다.","old:backpropagation_visual","오차를 뒤로 보내는 그림은 Gradient 계산 흐름을 표현합니다."),
        ("Backpropagation","Chain Rule로 각 Parameter의 변화율을 계산합니다","같은 x=2, y=4 예제에 Bias를 추가합니다. w=1, b=0에서 가중치와 Bias의 Gradient를 계산합니다.","lesson_chain_rule_graph","이 장에서는 w와 b를 모두 학습합니다. 앞의 Gradient 예제에서는 b를 0으로 고정했습니다.",True),
        ("Batch·Iteration·Epoch","데이터를 작은 묶음으로 나누어 반복해서 봅니다","Batch는 한 번에 처리하는 묶음, Iteration은 보통 한 묶음의 처리, Epoch은 학습 데이터 전체를 한 번 보는 주기입니다.","old:batch_epoch","이미지 10장, batch_size=4, 마지막 묶음을 버리지 않으면 4+4+2의 3번 처리가 1 Epoch입니다."),
        ("Dataset","데이터는 실제 사용할 조건을 대표해야 합니다","Dataset(데이터셋)은 학습·평가에 사용하는 데이터 모음입니다. 조명·크기·배경·설비·시간대와 일관된 정답 기준을 확인합니다.","capture_conditions","특정 배경만 정답과 함께 반복되면, 모델이 물체 대신 배경으로 판단할 수 있습니다."),
        ("데이터 분리","학습·모델 선택·최종 평가의 데이터를 나눕니다","Train은 가중치 학습, Validation은 모델·설정·Threshold 선택, Test는 최종 일반화 평가에 사용합니다.","old:dataset_split","예: 1,000장의 70/15/15 분리. 비율보다 서로 독립적인 평가 데이터 확보가 중요합니다."),
        ("Group Split","같은 영상의 비슷한 Frame은 통째로 분리합니다","동일한 원본 영상 A·B·C에서 각각 3개 Frame을 뽑은 예시입니다. 무작위 Frame 분할과 원본 Video를 통째로 나누는 Group Split을 비교합니다.","lesson_video_group_split_comparison","같은 원본 영상의 Frame이 Train·Validation·Test에 동시에 들어가지 않게 합니다. 새 설비 성능을 평가하려면 설비 자체로 Group을 정합니다."),
        ("Data Leakage","평가 데이터의 정보가 학습·선택에 새어들면 점수가 왜곡됩니다","앞 장의 Random Frame Split처럼 같은 원본 장면이 서로 다른 데이터 세트에 섞이면 평가가 왜곡될 수 있습니다. 전체 데이터 통계를 사용하는 전처리나 Test를 보며 반복 수정하는 경우도 점검합니다.","old:data_leakage_visual","학습하는 전처리 통계는 Train에서 계산합니다. 미리 정한 255 나누기는 통계를 학습하는 과정이 아닙니다."),
        ("전처리","모델이 기대하는 크기·값 범위·채널 순서를 맞춥니다","Preprocessing(전처리)은 입력 형식을 맞추는 과정입니다. 1920×1080을 640×640으로 맞출 때는 Resize·Crop·Padding의 차이를 고려합니다.","preprocess_basic","RGB/BGR, 0~255/정규화 값, HWC/CHW를 확인하고 Train·Inference의 기본 규칙을 맞춥니다."),
        ("Data Augmentation","의미를 유지하는 변화를 학습 중에 보여줍니다","Data Augmentation(데이터 증강)은 밝기·회전·가림 같은 변화를 적용하는 방법입니다. 현실적인 변화 범위와 정답 유지 여부를 확인합니다.","augmentation_basic","검출·분할에서는 이미지와 Box·Mask에 같은 공간 변환을 적용해야 합니다."),
        ("Overfitting","Train에서 잘하는 것과 새 데이터에서 잘하는 것은 다릅니다","Overfitting(과적합)은 학습 데이터에 지나치게 맞춰 새 데이터 성능이 떨어지는 현상입니다. Validation 추세와 실패 사례를 함께 봅니다.","old:overfit_leakage","Generalization(일반화)은 직접 학습하지 않은 데이터에서도 성능을 유지하는 능력입니다."),
        ("과적합 대응", "새 데이터에서도 잘하도록 학습을 조절합니다", "증강·Dropout·Early Stopping은 서로 다른 방식으로 과적합을 줄입니다. 각 방법의 효과는 Validation에서 비교합니다.", "survey_regularization", "Early Stopping은 Validation을 사용합니다. 증강 강도와 Dropout 확률을 높인다고 항상 성능이 좋아지는 것은 아닙니다."),
        ("K-Fold","평가 대상을 바꾸어 성능의 변동도 확인합니다","K-Fold Cross Validation(교차검증)은 데이터 부분집합을 번갈아 Validation으로 사용하며 모델을 각각 새로 학습합니다.","old:kfold_visual","같은 원본을 공유하는 샘플은 Group K-Fold로 분리하고, 최종 Test는 별도로 유지합니다.",True),
        ("Threshold","점수에 기준을 적용하면 실제 판정이 됩니다","설명용 불량 점수 0.82를 기준 0.50과 0.90에 각각 적용합니다. 점수는 같아도 판정 결과는 바뀝니다.","lesson_threshold_score_decision","임계값을 바꾸면 불량 미검과 오알람 수가 달라질 수 있습니다. 기준은 Validation에서 선택하며, 점수 0.82는 다음 100개 평가 사례와 별개입니다."),
        ("Confusion Matrix","정답과 판정을 비교해 네 가지 결과를 셉니다","총 100건의 같은 평가 데이터를 다음 지표 계산까지 이어갑니다. 실제 불량 20건 중 18건을 찾고, 정상 80건 중 4건을 잘못 알렸습니다.","lesson_confusion_100cases","TP: 찾은 불량 / FN: 놓친 불량 / FP: 오알람 / TN: 정상 통과."),
        ("Precision과 Recall","알람의 정확성과 불량을 찾는 비율을 구분합니다","직전 혼동행렬의 TP=18·FP=4·FN=2를 그대로 사용합니다. Precision은 불량이라고 알린 22건, Recall은 실제 불량 20건을 분모로 계산합니다.","lesson_precision_recall_sharedcase","동일한 TP=18이어도 Precision=18/22=81.8%, Recall=18/20=90%입니다. 임계값이 바뀌면 두 지표도 변할 수 있습니다."),
        ("Accuracy와 F1","전체 정답률과 Precision·Recall의 균형을 함께 봅니다","동일한 100건에서 Accuracy=(18+76)/100=94%, F1=2×18/(2×18+4+2)=85.7%를 계산합니다.","lesson_accuracy_f1_same100","F1은 Precision·Recall의 조화평균이며 TN은 포함하지 않습니다. 다음 장의 극단적 클래스 불균형 사례는 별도 가상 데이터입니다.",True),
        ("클래스 불균형", "불량이 적을수록 학습과 평가를 함께 점검합니다", "정상 95장·불량 5장처럼 Class 수가 다르면 소수 Class의 오류가 가려질 수 있습니다.", "survey_class_imbalance", "Accuracy는 전체 정답률, F1은 Precision·Recall의 조화평균입니다. Test는 운영 분포를 유지하고 불량 Recall·Precision·오알람을 함께 봅니다."),
        ("Shortcut Learning","모델이 우리가 원한 단서를 사용했는지도 확인합니다","Shortcut Learning(지름길 학습)은 물체 형태 대신 배경처럼 쉬운 단서로 정답을 맞추는 현상입니다.","shortcut_professional","Leakage는 정보가 새는 문제, Shortcut은 입력의 원치 않는 상관관계를 이용하는 문제입니다."),
        ("개발과 운영","운영의 실패 사례를 다음 데이터와 학습에 연결합니다","배포 후에도 조명·설비·제품 조건이 바뀔 수 있습니다. 실패 이미지를 모으고 정답 기준과 평가 조건을 다시 확인합니다.","workflow_basic","데이터 수집 → 학습 → 평가 → 배포 → 관찰을 반복하며 개선합니다."),
    ]
    vision=[
        ("문제 정의","필요한 결과부터 정하면 Vision Task가 정해집니다","이미지 전체가 불량인지, 결함이 어디에 있는지, 정확한 면적이 얼마인지에 따라 필요한 결과가 다릅니다.","old:vision_task_selection","질문 → 결과 형태 → Task → Label → 평가 기준과 모델 순으로 연결합니다."),
        ("Classification","이미지 전체의 상태나 종류를 예측합니다","Classification(분류)은 이미지 단위의 클래스와 점수를 출력합니다. 아래 예시는 사과 사진 전체의 불량 여부입니다.","old:task_classification","이 예시는 단일 Label 분류입니다. 위치나 정확한 결함 영역은 출력하지 않습니다."),
        ("Object Detection","객체나 결함의 위치를 사각형으로 찾습니다","Object Detection(객체 검출)은 클래스·Bounding Box(경계 상자)·점수를 출력합니다.","old:task_detection","Box 내부 전체가 결함인 것은 아닙니다. 상자는 위치를 둘러싸는 표현입니다."),
        ("Segmentation","어느 Pixel이 관심 영역인지 구분합니다","Segmentation(분할)은 Pixel별 클래스나 Mask(영역 표시)를 출력합니다. 아래 예시는 결함 영역입니다.","old:task_segmentation","형상·면적·경계가 필요하면 Box보다 Mask가 적합합니다."),
        ("Label","같은 사진이라도 Task가 바뀌면 정답 형태가 바뀝니다","분류는 이미지 클래스, 검출은 클래스와 Box, 분할은 Pixel Mask를 정답으로 사용합니다.","task_labels_three_outputs","여기서 결과 그림을 정답으로 작성한 것이 Label이고, 모델이 계산한 것이 Prediction입니다."),
        ("IoU","위치와 영역은 정답과 얼마나 겹치는지 평가합니다","IoU(Intersection over Union, 교집합/합집합 비율)는 정답 영역과 예측 영역의 겹침 정도입니다.","old:iou_visual","완전 일치하면 1, 겹치는 영역이 없으면 0입니다."),
        ("IoU","겹친 칸 수를 전체 합집합 칸 수로 나눕니다","정답 12칸과 예측 12칸이 4칸 겹치면, 합집합은 12+12−4=20칸입니다.","iou_detail","IoU = 4/20 = 0.2. 검출은 Box, 분할은 Mask의 영역으로 계산합니다.",True),
        ("Mask 후처리", "작은 점 제거와 작은 구멍 메우기는 다른 연산입니다", "Morphology(형태학)는 구조 요소로 Mask의 모양을 처리합니다. 침식은 1 영역을 줄이고, 팽창은 1 영역을 넓힙니다.", "processing_morphology", "Opening·Closing은 원래 Mask를 각각 처리한 결과입니다. 작은 실제 결함이 지워지거나 가까운 영역이 붙을 수 있어 크기를 검증해야 합니다."),
        ("영상처리의 기본", "한 Pixel을 바꿀 수도, 주변 Pixel을 함께 볼 수도 있습니다", "영상처리는 밝기·잡음·경계 같은 이미지 성질을 바꿉니다. 한 픽셀을 보는 연산과 주변 3×3을 함께 보는 연산을 비교합니다.", "lecture_point_neighborhood", "밝기 변환은 해당 Pixel 값으로 계산하고, 필터는 주변 값도 사용합니다. 이 연산 자체가 물체 이름을 예측하지는 않습니다."),
        ("Kernel의 이동","3×3 Kernel은 움직이며 출력 Pixel을 하나씩 만듭니다","5×5 입력의 중앙 3×3 값을 골라 평균을 계산하고 위치를 옮겨 반복합니다.","lecture_kernel_slide","Kernel을 옮길 때마다 선택되는 9개 값이 달라지고, 출력 Pixel도 순서대로 달라집니다. 구체적인 산술평균 계산은 다음 장에서 다룹니다.",True),
        ("평균 필터 계산", "주변 9개 값을 평균해 출력 한 칸을 계산합니다", "3×3 평균 필터는 주변 9개 Pixel에 각각 1/9의 가중치를 적용합니다. 중심 값 255를 포함한 9개의 합은 1053입니다.", "lecture_mean_calculation", "평균 필터는 사람이 정한 고정 가중치입니다. CNN은 같은 가중합 구조의 필터 값을 데이터에서 학습할 수 있습니다.", True),
        ("Gaussian 필터", "잡음을 줄이면 작은 변화도 함께 흐려질 수 있습니다", "Mean(평균) 필터는 이웃 Pixel에 같은 가중치를 주고, Gaussian은 가까운 Pixel에 더 큰 가중치를 줍니다. σ(시그마)는 가중치가 퍼지는 정도를 정합니다.", "processing_gaussian", "σ는 원본 Pixel 단위입니다. 잡음 감소와 작은 결함 보존을 함께 확인하고, 실제 Task의 평가 결과로 전처리를 선택합니다."),
        ("중앙값 필터", "튀는 점 잡음에는 중앙값이 유용할 수 있습니다", "Median(중앙값) 필터는 주변 3×3 Pixel 값을 크기순으로 정렬해 가운데 값을 선택합니다. 평균처럼 모두 더하지 않으므로 튀는 점 잡음에 강할 수 있습니다.", "processing_median", "중앙값은 선형 가중합이 아닌 비선형 연산입니다. 얇은 선이나 작은 결함도 없어질 수 있어 모든 잡음에 최선인 것은 아닙니다."),
        ("필터 비교","동일 입력에서도 Mean·Gaussian·Median 결과는 다릅니다","중앙 값만 255로 튄 동일한 3×3 입력을 서로 다른 필터로 계산했습니다.","lecture_filter_comparison","Mean 117, Gaussian 약 138.69, Median 100. 점 잡음에는 Median이 유리할 수 있습니다.",True),
        ("Sobel 직관","Sobel은 잡음을 지우기보다 경계 반응을 계산합니다","Sobel Gx의 3×3 가중치를 사용해 좌우 밝기 차이를 계산합니다. 특히 세로 경계에서 큰 반응이 나타나는 이유를 살펴봅니다.","lecture_sobel_concept","이 장의 Gx는 이미지 밝기의 가로 방향 변화량입니다. 다음 장에서는 Gx와 Gy를 합쳐 경계 반응을 시각화합니다."),
        ("영상 기울기", "밝기가 급격히 바뀌는 위치에서 경계 단서를 얻습니다", "Sobel(소벨) 필터로 좌우·상하 밝기 변화를 계산합니다. 부호 있는 값을 계산한 뒤 절댓값과 크기로 시각화합니다.", "processing_gradient", "두 기울기 그림은 같은 최대값으로 표시했습니다. 경계 반응은 밝기 변화의 단서이며, 그 자체가 물체나 결함의 정답은 아닙니다."),
        ("고정 필터와 학습 필터","Spatial Filtering의 Kernel 개념은 CNN으로 연결됩니다","두 방법 모두 주변 Pixel을 계산하지만, 평균·Gaussian은 사람이 정한 고정 가중치이고 CNN 가중치는 데이터 학습으로 갱신됩니다.","lecture_filter_to_cnn_bridge","이 장은 서로 다른 목적의 연산을 연결하는 개념도입니다. CNN의 실제 학습 가중치 값을 표시한 것은 아닙니다."),
        ("CNN","CNN은 작은 영역을 보고 같은 가중치를 재사용합니다","Convolutional Neural Network(합성곱 신경망)는 지역 연결과 가중치 공유로 이미지의 공간적 패턴을 계산합니다.","old:cnn_why_local","Flatten은 값과 순서를 유지하지만, 완전연결층에는 공간 이웃 관계와 가중치 공유가 명시되어 있지 않습니다."),
        ("Kernel","같은 필터도 이미지 영역에 따라 반응이 달라집니다","Kernel 또는 Filter(커널·필터)는 작은 가중치 배열입니다. 세로 밝기 변화가 있는 영역과 평평한 영역의 반응을 비교합니다.","kernel_basic","그림은 사람이 정한 경계 필터 예시입니다. CNN의 필터 값은 학습으로 정해집니다."),
        ("Convolution","같은 위치끼리 곱하고 더해 출력 한 칸을 만듭니다","입력의 3×3 영역과 필터를 곱해 합산하고, 필터를 옮겨 다음 칸을 계산합니다. 모든 출력은 실제 계산한 값입니다.","lesson_convolution_calculated","이 장은 한 채널·Bias 0 예시입니다. 일반적인 딥러닝 Conv는 필터를 뒤집지 않는 Cross-correlation 연산입니다.",True),
        ("Feature Map","반응값을 위치대로 모으면 특징 지도가 됩니다","5×5 입력에서 3×3 필터를 한 칸씩 이동하며 계산하면 3×3개의 반응값이 생깁니다. 이 값을 같은 위치에 모은 것이 Feature Map입니다.","lesson_featuremap_numeric_continuation","Feature Map은 한 필터의 위치별 반응입니다. 이 예시에는 활성화 함수(ReLU)를 적용하지 않아 음수도 남아 있습니다."),
        ("Feature Map과 Channel","RGB 전체를 보는 필터 하나가 출력 Channel 하나를 만듭니다","일반적인 Conv2d에서 필터 하나는 입력 Channel 전체를 곱해 합산합니다. 출력 Channel 수는 필터 수입니다.","lesson_multichannel_filter_to_maps","3×3×3 필터 64개라면 가중치 1,728개와 Bias 64개이며, Stride 1·Padding 1의 출력은 224×224×64입니다.",True),
        ("Stride","필터를 몇 칸씩 이동할지 정합니다","Stride(이동 간격)가 1이면 한 칸, 2이면 두 칸씩 이동합니다. 같은 입력과 필터에서 이동 간격이 크면 출력 크기가 작아집니다.","stride_basic","5×5 입력과 3×3 필터, Padding 0: Stride 1은 3×3, Stride 2는 2×2 출력입니다."),
        ("Padding","가장자리 주변에 값을 채워 계산 범위를 조절합니다","Padding(패딩)은 입력 주위를 채우는 방법입니다. 아래는 가장자리 한 칸에 0을 채우는 Zero Padding입니다.","padding_basic","5×5 입력, Kernel 3·Stride 1·Padding 1이면 출력의 공간 크기가 5×5로 유지됩니다."),
        ("Downsampling","공간 해상도를 줄여 더 작은 특징 지도를 만듭니다","Downsampling(다운샘플링)은 가로·세로 크기를 줄이는 과정입니다. 아래는 2×2에서 최댓값을 남기는 Max Pooling 예시입니다.","downsampling_basic","8×8 → 4×4는 위치 수가 64개에서 16개로 줄어듭니다. 작은 결함이나 경계의 위치 정보가 일부 사라질 수 있습니다."),
        ("이미지 피라미드", "평활화 후 축소해 여러 해상도의 영상을 만듭니다", "Gaussian Pyramid(가우시안 피라미드)는 평활화 후 가로·세로를 절반으로 줄입니다. 축소 전 평활화는 Aliasing(가짜 패턴)을 줄이는 데 쓰입니다.", "processing_pyramid", "사진의 Gaussian 피라미드와 CNN의 Max Pooling은 계산이 다릅니다. 가로·세로가 절반이면 Pixel 수는 1/4이 됩니다.", True),
        ("출력 크기 계산","Kernel·Stride·Padding으로 출력 크기를 계산합니다","H는 입력 높이, K는 필터 크기, S는 Stride, P는 양쪽 Padding입니다. floor는 소수점 아래를 버립니다.","spatial_detail","Dilation 1 기준 식입니다. Channel 수는 공간 크기와 별도로 필터 수가 결정합니다.",True),
        ("특징의 조합","Layer는 앞의 특징을 조합해 더 복잡한 표현을 만듭니다","사과 이미지를 예시로 국소 밝기 반응 → 곡선·무늬의 조합 → 더 넓은 형태의 단서로 이어지는 개념적 특징 표현을 살펴봅니다.","lesson_cnn_feature_hierarchy","국소 반응을 여러 Layer에서 조합한 개념도입니다. 실제 학습된 Feature Map이 항상 이 순서로 사람에게 해석되는 것은 아닙니다."),
        ("Receptive Field","깊은 층의 한 위치는 더 넓은 입력 범위의 영향을 받습니다","동일한 원본 7×7 위치를 기준으로 3×3 Convolution을 3개 Layer에 쌓을 때 한 출력 위치에 영향을 주는 이론적 입력 범위를 비교합니다.","lesson_receptive_field_growth","3×3 Conv, Stride 1, Dilation 1의 이론적 수용영역은 3×3 → 5×5 → 7×7입니다. 실제 강하게 반응한 영역과는 다릅니다.",True),
        ("CNN 전체 흐름", "작은 연산들을 연결하면 이미지 분류기가 됩니다", "224×224×3 입력을 특징 지도로 바꾸고, 전역 평균 풀링으로 요약한 뒤 분류 점수를 계산합니다.", "survey_cnn_pipeline", "H×W×C 순서의 설명용 작은 CNN입니다. 검출·분할 모델에는 위치를 보존하거나 복원하는 추가 구조가 필요합니다."),
        ("Backbone과 Head","특징을 만드는 부분과, 결과를 만드는 부분을 나눠 봅니다","같은 입력 특징을 추출하는 Backbone과, Classification·Detection·Segmentation 가운데 필요한 결과를 만드는 Task Head를 구분합니다.","lesson_backbone_head_roles","세 가지 Head는 구조 비교를 위한 개념도입니다. 실제 한 모델이 항상 세 Task를 동시에 출력하는 것은 아닙니다."),
        ("Backbone과 Head","블록을 연결하고 각 단계의 특징 크기를 표시합니다","224×224×3 입력에서 Conv 단계의 공간 크기가 112→56→28→14로 감소하는 예시입니다. Task별 Head는 같은 특징을 서로 다른 출력으로 바꿉니다.","lesson_backbone_tensor_head_options","분류는 Pooling과 Class logits, 검출은 Box·Class·Score, 분할은 Pixel Mask를 만듭니다. 검출·분할에는 Neck·Decoder 등이 추가될 수 있습니다.",True),
        ("CNN 구조의 설계", "순차·병렬·우회 연결로 서로 다른 구조를 만듭니다", "VGG는 순차, Inception은 병렬, ResNet은 우회 연결을 사용합니다. 그림은 각 구조의 연결 원리입니다.", "survey_architecture_patterns", "깊이만 늘리는 것 외에도 연결 방식이 중요합니다. 구조의 우열은 데이터·정확도·메모리·처리시간을 함께 검증해 결정합니다."),
        ("Residual 연결", "입력을 그대로 전달하는 경로와 변환 경로를 더합니다", "Residual(잔차) 블록은 F(x)+x를 계산합니다. 56×56×64 입력을 더하려면 두 경로의 Tensor Shape가 같아야 합니다.", "survey_residual_detail", "원소별 합산이며 Channel 결합과 다릅니다. ResNet v1은 합산 뒤 ReLU를 적용합니다. 우회 경로는 깊은 모델의 최적화를 돕습니다.", True),
        ("CNN 학습","CNN의 필터도 오차를 줄이는 방향으로 학습합니다","Forward로 예측하고 Label과 Loss를 비교한 뒤, Backpropagation으로 Gradient를 계산하고 Optimizer가 필터를 갱신합니다.","old:cnn_training","기본 학습 원리는 AI Basics와 같습니다. 학습하는 Parameter에 Kernel 가중치가 포함됩니다."),
        ("Transfer Learning","이미 배운 가중치에서 내 Task의 학습을 시작합니다","사전학습으로 얻은 Backbone 가중치를 새 Task의 출발점으로 사용합니다. 새로운 Label에 맞춘 Head를 준비하고 대상 데이터에서 추가 학습합니다.","lesson_transfer_pretraining_to_task","내 데이터가 사전학습 데이터와 다르면 효과가 달라질 수 있으므로 별도 평가가 필요합니다."),
        ("Freeze와 Fine-tuning","고정할 부분과 추가 학습할 부분을 구분합니다","Freeze 방식은 Backbone 가중치를 고정하고 Head를 학습합니다. Fine-tuning에서는 선택한 Backbone 가중치까지 업데이트합니다.","lesson_transfer_freeze_vs_finetune","같은 대상 데이터로 두 방식을 검증하고, 데이터 양·도메인 차이·Validation 성능에 따라 업데이트 범위를 선택합니다.",True),
        ("평가와 실패 사례","높은 점수만으로 판단 근거가 맞다고 보장할 수 없습니다","Vision AI에서 배경·조명·설비의 차이가 Class·Box·Mask 결과에 어떤 영향을 주는지 확인해야 합니다. 다른 조건의 이미지로도 판단 근거가 유지되는지 비교합니다.","shortcut_professional","분류 오판뿐 아니라 Box 위치·Mask 경계의 실패도 구분합니다. 설비별·조명별 오류 유형을 모아 모델이 바라본 단서를 점검합니다."),
        ("운영 Cycle","문제 정의부터 운영 관찰까지 연결해 개선합니다","Vision Task별 성공 기준(분류 판정·Box 위치·Mask 품질)을 정하고, 운영 중 수집한 오류를 Label 검토 및 재평가로 연결합니다.","old:vision_project_pipeline","운영 Cycle에서는 Task별 Metric·오류 이미지·촬영 조건을 함께 추적하고, 개선 전후를 같은 기준으로 다시 평가합니다."),
    ]
    ai_manifest=build_deck("ai_basics.html","02. AI Basics","AI는 오차를 줄이며 판단 기준을 배웁니다",[("예측하고 배우기","입력·정답·오차·가중치 수정"),("신경망 이해하기","작은 계산을 층으로 연결"),("제대로 평가하기","데이터 분리·실패 사례·지표")],ai,"intro.html","vision_ai.html")
    vision_manifest=build_deck("vision_ai.html","03. Vision AI","이미지에서 필요한 패턴을 찾아 결과로 바꿉니다",[("결과 정하기","분류·검출·분할과 Label"),("이미지 계산하기","작은 영역·필터·특징 지도"),("학습하고 적용하기","모델 구조·전이학습·운영")],vision,"ai_basics.html")
    manifest={"generated_assets":["assets/generated/apple_studio.webp","assets/generated/orange_studio.webp","assets/generated/capture_conditions.webp"],"version":VERSION,"ai_basics":ai_manifest,"vision_ai":vision_manifest}
    used={Path(item["asset"]).name for key in ["ai_basics","vision_ai"] for item in manifest[key]}
    for asset in ASSET_DIR.glob("*.svg"):
        if asset.name not in used and asset.name not in {
            "lecture_rgb_channel_stack.svg",
            "lecture_noise_outlier.svg",
            "lecture_2d_brightness_surface.svg",
        }:
            asset.unlink()
    (ASSET_DIR / "manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for folder,key in [("02_ai_basics","ai_basics"),("03_vision_ai","vision_ai")]:
        note=REPO_DIR / "lectures" / folder / "README.md"
        previous=note.read_text(encoding="utf-8")
        for old_heading in ("## 2026-10-06 배포 슬라이드 순서", "## 2026-10-13 배포 슬라이드 순서"):
            if old_heading in previous:
                previous=previous.split(old_heading)[0].rstrip()+"\n"
                break
        previous+="\n## 2026-10-13 배포 슬라이드 순서\n\n현재 배포 HTML의 순서는 아래를 기준으로 합니다. 상세 설명은 관련 개념 바로 뒤에 배치합니다. 앞의 개념 노트는 참고용입니다.\n\n"
        for item in manifest[key]:
            previous+=f"{item['number']}. {item['title']} ({'상세' if item['level']=='detail' else '기본'})\n"
        previous+="\n계산·숫자·Tensor 구조 그림은 `scripts/build_lesson_revision.py`에서 생성하며, 외부 이미지 서버나 CDN을 사용하지 않습니다.\n"
        note.write_text(previous,encoding="utf-8")
    print(json.dumps({key:len(value)+1 for key,value in manifest.items() if key in ["ai_basics", "vision_ai"]}))


if __name__=="__main__":
    build_figures()
    build_loss_optimizer_figures()
    build_opening_figures()
    build_survey_figures()
    build_image_processing_figures()
    build_lessons()
    for target, source in {
        "and_xor_linear_separability": "and_xor",
        "gradient_intuition": "gradient_basic",
        "convolution_visual": "convolution_detail",
        "feature_maps": "feature_detail",
        "backbone_head": "backbone_basic",
    }.items():
        (REPO_DIR / f"docs/assets/{target}.svg").write_bytes(
            (ASSET_DIR / f"{source}.svg").read_bytes()
        )
