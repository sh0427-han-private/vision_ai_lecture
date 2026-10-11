"""Build Intro page 3 from the existing apple photo and its actual gray values.

Read the repository's embedded photo, convert to one channel, and reduce with
BOX averaging to 48 columns × 32 rows. Every displayed number is the resulting
8-bit pixel value. Requires Pillow, NumPy and lxml.
"""
import base64
import io
from pathlib import Path

import numpy as np
from lxml import etree
from PIL import Image

from build_survey_figures import BLUE, MUTED, label, box

REPO_DIR = Path(__file__).resolve().parents[1]
SOURCE_PATH = REPO_DIR / "docs/assets/task_classification.svg"
OUTPUT_PATH = REPO_DIR / "docs/assets/intro_grayscale_values.svg"
IMAGE_COLUMNS = 48
IMAGE_ROWS = 32


def grayscale_images():
    """Return the original gray photo and its 48×32 integer pixel matrix."""
    root = etree.parse(str(SOURCE_PATH))
    image = root.find(".//{http://www.w3.org/2000/svg}image")
    source = image.get("href") or image.get("{http://www.w3.org/1999/xlink}href")
    photo = Image.open(io.BytesIO(base64.b64decode(source.split(",", 1)[1])))
    rgba = photo.convert("RGBA")
    rgb = Image.alpha_composite(Image.new("RGBA", rgba.size, "white"), rgba)
    grayscale = rgb.convert("RGB").convert("L")
    small = grayscale.resize((IMAGE_COLUMNS, IMAGE_ROWS), Image.Resampling.BOX)
    return grayscale, np.asarray(small)


def embed_image(photo, x, y, width, height):
    """Embed the same gray source as a display-only compressed photograph."""
    buffer = io.BytesIO()
    photo.resize((480, 320), Image.Resampling.LANCZOS).save(
        buffer, format="JPEG", quality=92, optimize=True
    )
    data = base64.b64encode(buffer.getvalue()).decode("ascii")
    return (f'<image x="{x}" y="{y}" width="{width}" height="{height}" '
            f'xlink:href="data:image/jpeg;base64,{data}"/>')


def build_intro_grayscale():
    """Draw equal-size photo → plain digits → digits colored by pixel value."""
    grayscale, values = grayscale_images()
    photo_x, table_x, pixel_x = 20, 420, 820
    panel_y, panel_width, panel_height = 112, 360, 240
    cell_width = panel_width / IMAGE_COLUMNS
    cell_height = panel_height / IMAGE_ROWS
    content = label(200, 70, "흑백 사진 · 1채널", 25, BLUE, "middle", True)
    content += label(600, 70, "순수 숫자 배열", 25, BLUE, "middle", True)
    content += label(1000, 70, "숫자에 밝기를 적용", 25, BLUE, "middle", True)
    content += embed_image(
        grayscale, photo_x, panel_y, panel_width, panel_height
    )
    # Equal physical panels and equal row/column spacing; numeric background
    # stays completely white and all digits have the same ink color.
    for x in [table_x, pixel_x]:
        content += (
            f'<rect x="{x}" y="{panel_y}" width="{panel_width}" '
            f'height="{panel_height}" fill="white" stroke="#cbd5e1"/>'
        )
    content += '<g id="plain-digits" font-size="4" fill="#000000" text-anchor="middle">'
    for row in range(IMAGE_ROWS):
        for column in range(IMAGE_COLUMNS):
            x = table_x + (column + .5)*cell_width
            y = panel_y + (row + .5)*cell_height + 1.4
            value = int(values[row, column])
            content += f'<text x="{x}" y="{y}">{value}</text>'
    content += '</g>'
    # Only the glyph fill changes. No bitmap, shaded cell or photo overlay
    # exists in the right panel. Whitespace remains white in both arrays.
    content += '<g id="brightness-digits" font-size="4" text-anchor="middle">'
    for row in range(IMAGE_ROWS):
        for column in range(IMAGE_COLUMNS):
            x = pixel_x + (column + .5)*cell_width
            y = panel_y + (row + .5)*cell_height + 1.4
            value = int(values[row, column])
            content += (
                f'<text x="{x}" y="{y}" fill="rgb({value},{value},{value})">'
                f'{value}</text>'
            )
    content += '</g>'
    for x1, x2 in [(386, 412), (786, 812)]:
        content += (
            f'<path d="M{x1} 232 H{x2}" stroke="{BLUE}" '
            'stroke-width="2" marker-end="url(#arrow)"/>'
        )
    content += label(200, 392, "앞 장과 같은 사진", 22, MUTED, "middle")
    content += label(600, 392, "32행 × 48열 = 1,536개 값", 22, MUTED, "middle")
    content += label(1000, 392, "같은 숫자 · 글자색만 변화", 22, MUTED, "middle")
    content += box(20, 426, 1160, 54, "#f2f6fa")
    content += label(600, 460, "숫자 0은 검정 글자, 255는 흰 글자  ·  각 숫자가 자신의 밝기를 나타냅니다", 23, BLUE, "middle")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1200 500" '
        'font-family="Noto Sans CJK KR, Malgun Gothic, sans-serif" '
        'role="img" aria-labelledby="title desc">'
        '<title id="title">동일한 크기의 흑백 사진, 숫자 배열, 밝기 숫자 그림</title>'
        '<desc id="desc">사과 사진을 48열 32행으로 축소해 얻은 1536개 밝기 '
        '값을 중앙에 검정 숫자로 표시합니다. 오른쪽도 같은 숫자로만 구성하며 '
        '값 v의 글자색은 RGB(v,v,v)입니다. 세 패널은 360×240으로 같습니다.</desc>'
        f'<defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" '
        f'refY="3" orient="auto"><path d="M0 0 L6 3 L0 6Z" fill="{BLUE}"/>'
        '</marker></defs><rect width="1200" height="500" fill="white"/>'
        f'{content}</svg>\n'
    )
    OUTPUT_PATH.write_text(svg, encoding="utf-8")
    print(f"{IMAGE_COLUMNS}×{IMAGE_ROWS} = {values.size} corresponding values")


if __name__ == "__main__":
    build_intro_grayscale()
