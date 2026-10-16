#!/usr/bin/env python3
"""Create five faithful image-processing demonstrations from the repository's
CS231n dog photograph (Stanford CS231n 2017 Lecture 5). Each visual is computed
using NumPy/Pillow, not generated as an imaginary trained model output.
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "docs/assets/lesson"
src = Image.open(DIR / "cs231n_vgg16_feature_hierarchy_original.png").convert("RGB")
assert src.size == (1134, 541), f"Unexpected source image size: {src.size}"
dog = src.crop((11, 1, 175, 132))
dog224 = dog.resize((224, 224), Image.Resampling.BILINEAR)
gray = np.array(dog224.convert("L"), dtype=np.float32)

font_choices = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]
font_path = next(x for x in font_choices if Path(x).exists())
font = lambda size: ImageFont.truetype(font_path, size)
W, H = 1600, 650
COLOR = {"text": "#244858", "secondary": "#526f80", "border": "#d4e2e9", "bg": "#f7fbfc", "teal": "#278195"}

def panel(title, desc, tiles, takeaway, note, outname):
    """Tiles (label, PIL RGB image, subtitle). Always shows REAL computed images."""
    n = len(tiles)
    image = Image.new("RGB", (W,H), "#fff")
    d = ImageDraw.Draw(image)
    d.text((38,24),title,font=font(36),fill=COLOR["text"])
    d.text((38,82),desc,font=font(19),fill=COLOR["secondary"])
    d.line((38,121,W-38,121),fill=COLOR["border"],width=2)
    gap=15
    cw=(W-76-(n-1)*gap)//n
    for k,(label,tile,sub) in enumerate(tiles):
        x=38+k*(cw+gap)
        d.rounded_rectangle((x,144,x+cw,527),radius=15,fill=COLOR["bg"],outline=COLOR["border"],width=2)
        d.text((x+17,159),label,font=font(25),fill=COLOR["text"])
        tw,th=tile.size
        maxw=cw-38;maxh=259
        scale=min(maxw/tw,maxh/th)
        size=(round(tw*scale),round(th*scale))
        show=tile.resize(size,Image.Resampling.NEAREST if max(tw,th)<=112 else Image.Resampling.LANCZOS)
        xx=x+(cw-size[0])//2; yy=215+(maxh-size[1])//2
        image.paste(show,(xx,yy))
        d.rectangle((xx,yy,xx+size[0],yy+size[1]),outline="#aac6d0",width=2)
        d.text((x+17,487),sub,font=font(17),fill=COLOR["secondary"])
    d.rounded_rectangle((38,545,W-38,634),radius=12,fill="#eef7f8",outline="#d6e7eb",width=2)
    d.text((59,561),"핵심",font=font(21),fill=COLOR["teal"])
    d.text((138,560),takeaway,font=font(21),fill=COLOR["text"])
    d.text((59,602),note,font=font(15),fill=COLOR["secondary"])
    dest=DIR/outname
    image.save(dest,optimize=True)
    print(outname, dest.stat().st_size)
    return dest

def gray_img(a):
    arr=np.clip(a,0,255).astype("uint8")
    return Image.fromarray(arr,"L").convert("RGB")

def sobel(arr,pad=0,stride=1):
    kernel=np.array([[-1.,0.,1.],[-2.,0.,2.],[-1.,0.,1.]],dtype=np.float32)
    a=np.pad(arr,pad_width=pad,mode="constant") if pad else arr
    windows=np.lib.stride_tricks.sliding_window_view(a,(3,3))[::stride,::stride]
    return np.einsum("ijkl,kl->ij",windows,kernel).astype("float32")

def edge_image(x,scale=600.0):
    # Single consistent scale across stride/padding cases, NOT per-frame arbitrary.
    return gray_img(np.clip(np.abs(x)/scale*255,0,255))

def maxpool(a,factor=2):
    h,w=a.shape
    return a.reshape(h//factor,factor,w//factor,factor).max(axis=(1,3))

def letterbox(im,size=(320,320)):
    w,h=im.size; tw,th=size
    k=min(tw/w,th/h)
    w2,h2=int(round(w*k)),int(round(h*k))
    out=Image.new("RGB",size,(112,119,127))
    out.paste(im.resize((w2,h2),Image.Resampling.LANCZOS),((tw-w2)//2,(th-h2)//2))
    return out

# 1. Actual 3x3 fixed Sobel response, 224x224 input:
# without padding: stride1 -> 222x222, stride2 -> 111x111.
edge1=sobel(gray,0,1)
edge2=sobel(gray,0,2)
assert edge1.shape==(222,222) and edge2.shape==(111,111)
panel("Stride · 필터의 이동 간격과 실제 출력",
    "한 장의 강아지 사진에 같은 3×3 Sobel Kernel을 적용한 결과 (Padding = 0)",
    [("입력 사진",dog224,"224 × 224 Pixel"),("Stride 1",edge_image(edge1),"222 × 222 출력"),("Stride 2",edge_image(edge2),"111 × 111 출력")],
    "같은 필터여도 이동 간격이 커지면 출력 위치와 해상도가 줄어듭니다.",
    "※ 동일 입력·동일 Sobel 가중치 · 실제 계산 결과 · 각 결과에 같은 밝기 척도 적용",
    "cnn_real_stride_dog.png")

# 2. True zero-padding: Sobel without pad is 222x222, with pad=1 224x224.
padded=sobel(gray,1,1)
assert padded.shape==(224,224)
# 224 grayscale + eight px gray canvas with clear black zero-edge visualization.
with_border=Image.new("RGB",(240,240),(173,185,191))
with_border.paste(dog224,(8,8))
zero_canvas=gray_img(np.pad(gray,8,mode="constant"))
panel("Padding · 가장자리도 계산에 포함",
    "3×3 Sobel Kernel, Stride 1 · Zero Padding의 유무에 따른 실제 계산 크기",
    [("입력 사진",dog224,"224 × 224 Pixel"),("Padding 0",edge_image(edge1),"222 × 222 출력"),("Padding 1",edge_image(padded),"224 × 224 출력")],
    "가장자리에 0을 한 칸 채우면 주변 위치의 출력까지 계산할 수 있습니다.",
    "※ 실제 3×3 연산 계산 · Padding=1은 0 값 추가 · 경계 효과는 입력 조건에 따라 달라짐",
    "cnn_real_padding_dog.png")

# 3. Actual max-pooling applied to grayscale values, not falsely labeled as
# SqueezeNet's trained intermediate features.
pool112=maxpool(gray,2)
pool56=maxpool(pool112,2)
assert pool112.shape==(112,112) and pool56.shape==(56,56)
panel("Max Pooling · 최댓값만 남기는 공간 축소",
    "강아지 사진의 Grayscale Pixel에 2×2 Max Pooling을 두 번 적용한 실제 결과",
    [("입력 Gray",gray_img(gray),"224 × 224 Pixel"),("Max Pool 1",gray_img(pool112),"112 × 112 출력"),("Max Pool 2",gray_img(pool56),"56 × 56 출력")],
    "작은 영역의 최댓값을 남기면서 가로·세로 위치 수가 점차 줄어듭니다.",
    "※ 실제 Gray 영상값에 적용한 고정 Max Pooling · 학습 CNN의 Feature Map 아님",
    "cnn_real_maxpool_dog.png")

# 4. Actual preprocessing of same landscape dog crop: input -> distorted
# square resize -> letterbox that preserves original aspect ratio.
# Make a genuine 3:2 photo crop (not an aspect-distorted resize).
landscape=dog.crop((0,11,164,120)).resize((390,260),Image.Resampling.LANCZOS)
stretched=landscape.resize((320,320),Image.Resampling.LANCZOS)
boxed=letterbox(landscape,(320,320))
panel("Preprocessing · 같은 사진, 다른 크기 조정",
    "한 장의 사진을 320 × 320 입력으로 맞출 때 달라지는 비율과 여백",
    [("원본 사진",landscape,"가로:세로 = 3:2"),("강제 Resize",stretched,"정사각형 · 비율 왜곡"),("Letterbox",boxed,"비율 유지 · Padding")],
    "학습·추론에서 입력 크기, 채널 순서, 정규화 규칙을 일관되게 맞춥니다.",
    "※ 실제 Resize 및 Letterbox 처리 결과 · 예시 크기 320 × 320 · 실제 모델 전처리 설정과 구별",
    "cnn_real_preprocess_dog.png")

# 5. Actual augmentation of the same dog photo; no fake network output.
base=dog.resize((344,258),Image.Resampling.LANCZOS)
bright=ImageEnhance.Brightness(base).enhance(0.58)
rotated=base.rotate(13,resample=Image.Resampling.BICUBIC,expand=False,fillcolor=(110,115,120))
occluded=base.copy()
ImageDraw.Draw(occluded).rounded_rectangle((172,126,236,169),radius=5,fill=(160,178,185))
panel("Data Augmentation · 같은 대상의 여러 학습 조건",
    "같은 사진에 밝기·회전·가림을 직접 적용한 실제 변형 예시",
    [("원본",base,"같은 강아지"),("밝기 감소",bright,"조명 변화"),("13° 회전",rotated,"시점·회전 변화"),("부분 가림",occluded,"작은 가림 영역")],
    "객체 종류는 유지하되, Bounding Box·Mask는 공간 변환에 맞게 수정해야 합니다.",
    "※ Pillow로 실제 변형 · 현장에 없는 과도한 증강 금지 · 개념 비교용, 모델 추론 아님",
    "cnn_real_augment_dog.png")


# 6. Same real photo + deterministic salt-pepper corruption -> compare
# a mean box filter, Gaussian blur and Median filter on IDENTICAL input.
rng=np.random.default_rng(20261016)
noisy=np.array(dog224).copy()
mask=rng.random((224,224))
noisy[mask<0.025]=0
noisy[(mask>=0.025)&(mask<0.05)]=255
noisy_im=Image.fromarray(noisy,"RGB")
mean_im=noisy_im.filter(ImageFilter.BoxBlur(2)) # 5×5 box mean.
gaussian_im=noisy_im.filter(ImageFilter.GaussianBlur(radius=2))
median_im=noisy_im.filter(ImageFilter.MedianFilter(size=5))
panel("Mean · Gaussian · Median · 같은 입력 비교",
    "한 장의 실사 사진에 동일한 점 잡음을 넣고 세 필터를 실제로 적용",
    [("잡음 입력",noisy_im,"Salt-and-Pepper 5%"),
     ("Mean 5×5",mean_im,"주변 Pixel의 산술 평균"),
     ("Gaussian",gaussian_im,"거리 가중치가 있는 Blur"),
     ("Median 5×5",median_im,"이웃 밝기 중앙값")],
    "같은 점 잡음 입력에서 Median은 극단적인 점을 제거하는 데 유리합니다.",
    "※ 동일 잡음 입력 · 직접 계산 · BoxBlur 반경 2 · Gaussian 반경 2 · Median 크기 5",
    "cnn_real_filter_compare_dog.png")

# 7. Actual horizontal and vertical Sobel of the SAME grayscale dog image.
kernel_y=np.array([[-1.,-2.,-1.],[0.,0.,0.],[1.,2.,1.]],dtype=np.float32)
view=np.lib.stride_tricks.sliding_window_view(gray,(3,3))
gx=sobel(gray,0,1)
gy=np.einsum("ijkl,kl->ij",view,kernel_y).astype("float32")
strength=np.hypot(gx,gy)
assert gx.shape==gy.shape==strength.shape==(222,222)
panel("Sobel · 사진에서 밝기 변화가 큰 위치",
    "동일한 Grayscale 강아지 영상에 3×3 Sobel X·Y Kernel을 적용한 실제 결과",
    [("입력 사진",dog224,"224 × 224 RGB"),
     ("가로 방향 변화",edge_image(gx),"Gx · 좌우 밝기 변화"),
     ("세로 방향 변화",edge_image(gy),"Gy · 위아래 밝기 변화"),
     ("경계 강도",edge_image(strength),"sqrt(Gx² + Gy²)")],
    "좌우·위아래 밝기 변화량이 큰 위치가 경계 후보로 강조됩니다.",
    "※ 같은 사진·동일 3×3 Sobel 실제 계산 · 출력 222×222 · 고정 필터, 학습 CNN 아님",
    "cnn_real_sobel_dog.png")
