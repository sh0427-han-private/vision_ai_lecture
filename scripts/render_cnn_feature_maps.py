#!/usr/bin/env python3
"""Render *actual* feature activations from an ImageNet pretrained CNN.
Source photo: unchanged CS231n Lecture 5 (2017), dog thumbnail cropped solely
for inference. Model: torchvision SqueezeNet1_1 ImageNet pretrained weights.
This is NOT the CS231n VGG-16 feature-optimization visualisation on the next slide.
"""
from pathlib import Path
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import torch
from torchvision.models import squeezenet1_1, SqueezeNet1_1_Weights
from torchvision.transforms import functional as TF

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/assets/lesson/cs231n_vgg16_feature_hierarchy_original.png"
DEST = ROOT / "docs/assets/lesson/cnn_squeezenet_actual_feature_maps.png"
assert SOURCE.exists(), "Stanford CS231n photograph source is missing"

# Crop the actual dog photograph from the CS231n montage (1134×541).
montage = Image.open(SOURCE).convert("RGB")
assert montage.size == (1134, 541), f"Unexpected montage size {montage.size}"
dog_crop = montage.crop((11, 1, 175, 132))
display_photo = dog_crop.resize((340, 280), Image.Resampling.LANCZOS)
input_tensor = TF.normalize(
    TF.to_tensor(dog_crop.resize((224, 224), Image.Resampling.BILINEAR)),
    mean=(0.485, 0.456, 0.406),
    std=(0.229, 0.224, 0.225),
).unsqueeze(0)

# Official torchvision pretrained classification CNN, *not* VGG-16.
torch.set_num_threads(2)
model = squeezenet1_1(weights=SqueezeNet1_1_Weights.IMAGENET1K_V1).eval()
chosen = {1: "얕은층", 7: "중간층", 12: "깊은층"}
activations = {}
with torch.inference_mode():
    x = input_tensor
    for idx, layer in enumerate(model.features):
        x = layer(x)
        if idx in chosen:
            activations[idx] = x.detach()[0].cpu().float().numpy().copy()
assert list(activations) == [1, 7, 12], "Missing real model activations"

# Pick 4 high-variation channels per block, without pretending these represent
# all channels. Each heatmap is normalized *independently* for visibility.
def choose_channels(a):
    spread = a.reshape(a.shape[0], -1).std(axis=1)
    mag = np.abs(a.reshape(a.shape[0], -1)).mean(axis=1)
    scores = spread * np.sqrt(mag + 1e-8)
    ranked = np.argsort(-scores)
    picks = [int(i) for i in ranked if np.isfinite(scores[i]) and scores[i] > 0][:4]
    assert len(picks) == 4
    return picks

def activation_rgb(data):
    # ReLU feature maps are >=0. High = warm yellow, low = dark blue.
    lo, hi = np.percentile(data, [2, 99])
    v = np.clip((data - lo) / max(float(hi - lo), 1e-6), 0, 1)
    stops = np.array([
        [20, 40, 67], [24, 84, 121], [35, 136, 153],
        [100, 187, 157], [226, 208, 114], [255, 239, 184]
    ], dtype=float)
    indices = v * (len(stops) - 1)
    low = np.floor(indices).astype(int)
    high = np.minimum(low + 1, len(stops) - 1)
    w = (indices - low)[..., None]
    rgb = stops[low] * (1 - w) + stops[high] * w
    return Image.fromarray(np.uint8(np.round(rgb)), "RGB")

# 1600×690 PNG for a 16:9 lecture canvas; clear original photo and four raw
# channel activation maps per level. No simulated features.
BG = "#ffffff"; TEXT = "#234556"; MUTED = "#5a7382"; EDGE = "#d7e5eb"
canvas = Image.new("RGB", (1600, 690), BG)
draw = ImageDraw.Draw(canvas)
font_candidates = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]
font_path = next(p for p in font_candidates if Path(p).exists())
font = lambda px: ImageFont.truetype(font_path, px)
bold = lambda px: ImageFont.truetype(font_path, px)

def text(x, y, value, size=22, fill=TEXT):
    draw.text((x, y), value, font=font(size), fill=fill)
def round_rect(box, fill="#f7fbfc", outline=EDGE, radius=14, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
def arrow(x, y, right):
    draw.line((x, y, right-11, y), fill="#7295a5", width=5)
    draw.polygon(((right-16,y-9),(right,y),(right-16,y+9)), fill="#7295a5")

text(38, 20, "실제 CNN에 사진을 입력하면 위치별 Feature Map이 만들어집니다", 36)
text(38, 77, "ImageNet 사전학습 SqueezeNet 1.1 · 같은 입력 사진 1장 · 각 단계에서 4개 채널만 선택", 20, MUTED)
draw.line((38, 116, 1562, 116), fill="#dbe8ee", width=2)
cards = [(38, 267), (343, 391), (747, 391), (1151, 391)]  # x, width
labels = ["입력 사진", "얕은층", "중간층", "깊은층"]
descriptions = [
    "실제 강아지 사진",
    "단순한 국소 반응",
    "부분·질감 반응",
    "압축된 복합 반응",
]
for i, (x, width) in enumerate(cards):
    round_rect((x, 142, x+width, 574))
    text(x+19, 160, labels[i], 30)
    text(x+19, 208, descriptions[i], 21, MUTED)
for x, xx in [(311,338),(738,742),(1142,1147)]:
    arrow(x, 347, xx)

# Photo is a TRUE crop of the exact CS231n image; upscaling does not invent maps.
canvas.paste(display_photo.resize((226, 266), Image.Resampling.LANCZOS), (59, 263))
text(59, 542, "RGB 입력 · 224 × 224 × 3", 17, MUTED)

specs = [
    (1, 343, "Conv + ReLU"),
    (7, 747, "중간 Feature 추출"),
    (12, 1151, "후반 Feature 추출"),
]
for idx, x0, subtitle in specs:
    feat = activations[idx]
    c, hh, ww = feat.shape
    assert c > 4 and hh >= 12 and ww >= 12
    ch = choose_channels(feat)
    text(x0+19, 242, f"출력 {hh} × {ww} × {c}", 18, MUTED)
    for j, ch_idx in enumerate(ch):
        gx, gy = j % 2, j // 2
        px = x0 + 19 + gx * 174
        py = 272 + gy * 131
        tile = activation_rgb(feat[ch_idx]).resize((157, 109), Image.Resampling.NEAREST)
        canvas.paste(tile, (px, py))
        draw.rectangle((px,py,px+156,py+108),outline="#b7d2d9",width=2)
        text(px+6,py+87,f"채널 {ch_idx}",14,"#ffffff")
    text(x0+19, 542, "색상 = 채널별 상대 반응", 17, MUTED)

round_rect((38, 593, 1562, 664), fill="#edf7f8",outline="#d5e7ea",radius=12)
text(63, 608, "핵심", 21, "#27788a")
text(140, 607, "사진의 가로·세로 구조는 처음엔 비교적 남지만, 값은 RGB가 아닌 특징별 반응으로 바뀝니다.", 21)
text(63, 641, "※ 실제 사전학습 모델 출력 · SqueezeNet 1.1 · 4개 채널 예시 · 각 Tile 대비 개별 정규화", 17, MUTED)
DEST.parent.mkdir(parents=True, exist_ok=True)
canvas.save(DEST, optimize=True)
print("Created", DEST, "size", DEST.stat().st_size)
for i in chosen:
    f = activations[i]
    print(chosen[i], "shape", f.shape, "channels", choose_channels(f))
