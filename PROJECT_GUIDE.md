# Vision AI Lecture — Project Guide

Vision AI를 처음 접하는 사람을 대상으로 하는 입문 강의자료 제작 프로젝트입니다.

## Links

- GitHub Repository: https://github.com/sh0427-han/vision_ai_lecture
- GitHub Pages: https://sh0427-han.github.io/vision_ai_lecture/
- 현재 남은 작업: [TODO_VISION_AI_LECTURE.md](TODO_VISION_AI_LECTURE.md) — 최신 50장 기준, 슬라이드별 미완료 항목·QA 확인

## Course Structure

### 01. Vision AI Intro

- 사람과 컴퓨터가 이미지를 보는 방식의 차이
- Intro 3: 48×32 원본 Grayscale에서 실제 6×6 영역을 확대해 사진 → 실제 숫자 → 같은 값의 밝기 셀로 대응
- 다음 Pixel 설명에서 RGB 3채널과 H×W×3 구조를 소개
- 원근감: 단일 RGB 숫자 배열에는 실제 거리·실제 크기가 직접 들어 있지 않아 가까워서 큰 것과 실제로 큰 것을 해석해야 함
- Pixel / Channel의 의미와 8-bit 0~255 값
- Signal / Noise: 판단에 유용한 Pattern과 무관한 변화의 차이
- 조명, 방향, 크기, 가림, 초점, 색온도 등에 따른 Pixel 변화
- Generalization: 조건이 달라도 반복되는 공통 Pattern 학습
- RGB 입력 → Feature → Classification / Detection / Segmentation Output
- 대표 Vision Sensor: RGB / LiDAR / IR의 출력 데이터 비교
- 스마트폰·CCTV·로봇청소기·열화상 등 친숙한 Sensor 활용 사례

### 02. AI Basics

- AI / Machine Learning / Deep Learning / Computer Vision의 관계
- Supervised Learning / Unsupervised Learning
- Classification / Regression / Binary / Multi-class Classification
- Perceptron → Weight / Bias → Parameter / Hyperparameter
- AND / XOR와 Linear Separability
- Perceptron → Layer → Neural Network
- 비선형성과 Activation Function
- Feature / Representation
- Linear Regression으로 보는 Parameter 학습
- Loss Function → Gradient → Optimizer / Learning Rate
- Training Loop / Backpropagation
- Training / Inference
- Batch / Iteration / Epoch
- Dataset Quality와 Shortcut Learning / Spurious Correlation
- Image Preprocessing
- Data Augmentation
- Train / Validation / Test
- Data Leakage와 Group 단위 Split
- K-Fold / Group K-Fold
- Threshold / Confusion Matrix / Accuracy / Precision / Recall / F1
- Loss / Metric 차이
- Overfitting / Generalization

### 03. Vision AI

- 현장 질문 → 원하는 Output → Vision Task → Label → Model / Metric
- Classification / Object Detection / Segmentation
- Task별 Label 구조와 IoU
- Pixel/이웃 연산, Gaussian·평균·중앙값 필터와 잡음/세부 손실
- 영상 기울기와 Sobel, Mask의 Opening·Closing
- Gaussian 피라미드의 평활화·축소와 CNN Pooling의 차이
- CNN의 Local Connectivity / Weight Sharing
- Kernel: Local Pattern에 반응하는 학습 Weight
- Convolution 계산
- Stride / Padding / Downsampling
- Feature Map / Channel
- Feature Hierarchy / Receptive Field
- CNN Training
- Backbone / Task Head
- Transfer Learning / Fine-tuning
- 높은 Score ≠ 의미 이해: Shortcut Learning과 Slice / 실패 사례 점검
- 문제 정의 → Data/Label → Train → Evaluate → Deploy → Monitor Cycle

현재 강의 범위에서는 Tracking, Depth/3D, Vision Transformer를 제외합니다.

## Lecture Design Principles

2026-10-06부터 AI Basics와 Vision AI는 **쉬운 기본 그림 → 관련 개념의 상세 Figure** 순서로 설명합니다.
상세 Figure는 수식·계산 그래프·Tensor 크기·연산 조건을 담되, 기본 그림과 한 장에 압축하지 않습니다.
현재 순서와 기본/상세 구분은 `docs/assets/lesson/manifest.json`을 기준으로 합니다.
계산 그림은 `scripts/build_lesson_revision.py`로 생성하고 `scripts/verify_lesson_revision.py`로 검증합니다.

대상은 Vision AI를 처음 접하는 초보자입니다.

- 한 슬라이드에는 하나의 핵심 메시지만 전달합니다.
- 긴 텍스트 설명보다 그림과 예시를 우선합니다.
- 가능하면 슬라이드의 60~75%를 시각 자료로 구성합니다.
- 텍스트와 화살표 문자만으로 만든 흐름 표현은 최소화합니다.
- Process와 학습 과정은 실제 Flow Chart / Block Diagram으로 표현합니다.
- 같은 원본 이미지를 반복 활용해 Classification / Detection / Segmentation의 차이를 직관적으로 보여줍니다.
- 논문 Figure나 외부 이미지를 그대로 복사하기보다 강의용 Diagram으로 재구성합니다.
- 사진형·현장형 예시는 가능하면 ChatGPT에서 강의 목적에 맞게 생성한 뒤 `docs/assets/generated/`에 저장하고, HTML에서는 Repository 내부 자산만 참조합니다.
- 생성 Figure도 개념적 정확성을 먼저 검토하고 사용합니다. 포함관계·수식·Tensor/Convolution 구조처럼 정밀한 관계는 생성 이미지가 부정확하면 SVG/HTML Diagram을 우선합니다.
- 개념 관계·수식·구조 설명은 SVG/HTML Diagram을 사용하고, 실제 장면을 직관적으로 보여줘야 할 때는 생성 이미지 또는 실제 사진을 우선합니다.
- 실제 강의 화면에는 강사용 메모, 발표 지시, 다음 챕터 안내 같은 메타 문구를 넣지 않습니다.
- 흰색 배경, 최소한의 색상, 깔끔한 Presentation 스타일을 유지합니다.
- 초보자가 그림만 보고도 개념의 대략적인 의미를 이해할 수 있도록 구성합니다.
- 각 슬라이드는 발표 화면 한 Viewport 안에 들어오도록 구성하며, 세로 스크롤 없이 보이도록 자동 Fit을 적용합니다. 콘텐츠가 과도하게 길다면 축소에만 의존하지 말고 내용을 분리하거나 단순화합니다.

## Interactive Teaching (2026-10-14)

- 기존 강의 흐름에서 해당 개념이 등장하는 **바로 그 슬라이드**에 Interactive Figure를 통합합니다. 별도 실습 목차, 외부 페이지, 과도한 Dashboard UI를 만들지 않습니다.
- 초보자에게는 임의의 Kernel Weight 숫자를 바꾸게 하는 대신, **Mean/Gaussian/Median/Sobel 종류, Gaussian σ, Noise On/Off** 등 실제 해석할 수 있는 조작을 우선합니다.
- Kernel 행렬은 **읽기 전용**이며 선택한 필터의 실제 계산값을 표시합니다. Median은 가중합 방식이 아니라 중앙값 연산임을 명시합니다.
- 학습 원리를 보여줄 때는 가중치 수동 입력보다 **데이터 → 예측 → 오차 → Gradient로 Parameter 자동 갱신** 흐름을 보여줍니다.
- Input과 Output은 같은 이미지와 Pixel 위치를 사용하며, 표시된 수치와 실제 계산 결과가 반드시 일치해야 합니다.
- 일반 강의 스타일(흰 배경, 큰 영상, 충분한 여백)을 유지하고, 키보드·터치 조작과 viewport fit을 고려합니다.
- 현재 통합 구현: docs/vision_ai.html의 Gaussian 필터, docs/ai_basics.html의 학습의 의미. 구현 소스는 docs/interactive_lessons.css 및 docs/interactive_lessons.js 입니다.

## AI / HTML 작업 지침

Repository를 수정하는 AI coding agent와 HTML 작성 작업은 다음 문서를 함께 사용합니다.

- `CHATGPT_PROJECT_INSTRUCTIONS.md` — ChatGPT 프로젝트 개인용 지침에 붙여 넣을 권장 원문
- `AGENTS.md` — AI coding agent가 작업 전에 확인할 핵심 작업 규칙
- `HTML_DESIGN_RULES.md` — 강의용 HTML의 레이아웃, Figure, Typography, 구현 및 검증 기준
- `.github/copilot-instructions.md` — VS Code / GitHub Copilot용 Repository 지침

지침이 충돌하면 **현재 사용자의 명시적 요청 → PROJECT_GUIDE.md → HTML_DESIGN_RULES.md → 기존의 일관된 디자인 → 과거 TODO** 순서로 판단합니다.

## Repository Structure

주요 웹 강의 파일:

- `docs/intro.html`
- `docs/ai_basics.html`
- `docs/vision_ai.html`

강의용 Diagram:

- `docs/assets/`
- `assets/diagrams/`

학습 노트:

- `lectures/01_intro/`
- `lectures/02_ai_basics/`
- `lectures/03_vision_ai/`

시각 자료 출처:

- `assets/SOURCES.md`

## Working Rules

- 수정 전에 Repository의 최신 상태와 `AGENTS.md`, `HTML_DESIGN_RULES.md`를 확인합니다.
- 사용자가 강의자료 수정을 요청하면 가능한 경우 실제 Repository 파일까지 수정합니다.
- 수정 후 HTML 구조와 링크를 검증하고 GitHub Pages 배포 상태를 확인합니다.
- 기존 강의 흐름과 디자인을 유지하면서 내용을 추가합니다.
- 중복되는 설명은 제거합니다.
- 완전 초보자 관점에서 용어를 설명합니다.
- 그림, Diagram, Flow Chart를 우선 사용합니다.
- 강의자료와 학습노트의 내용이 서로 크게 어긋나지 않도록 함께 관리합니다.

## Current Entry Point

강의는 다음 파일에서 시작합니다.

- `docs/intro.html`

GitHub Pages:

- https://sh0427-han.github.io/vision_ai_lecture/

## Professional Visual Style (2026-10-06)

- 쉬운 설명은 유지하되 유아용 아이콘·만화풍 그림을 사용하지 않습니다.
- 개념을 보여주는 물체·촬영 환경은 `docs/assets/generated/`의 생성 사진을 우선 재사용합니다. 사진 자산을 저장한 뒤 그 파일을 읽어 설명 Figure와 슬라이드를 구성합니다.
- 절제된 청회색/녹색, 얇은 선, 작은 모서리 반경, 정렬된 패널과 여백을 사용합니다.
- 수식·Tensor shape·계산 그래프는 검증 가능한 벡터 도표로 표현합니다.
- 생성 사진과 설명용 Feature 그림을 실제 모델의 측정·실험 결과로 표현하지 않습니다.


## Visual Filtering Curriculum (2026-10-13, 초기 변경 기록)

- 초기 Intro 14장: Gray 영상 숫자 배열 → 2D 평면과 원근감 → 밝기값의 3D 그래프(실제 Depth 아님) → RGB 3개 Channel → Noise 단일 Pixel 변화 → 일반화.
- 초기 Vision AI 41장(표지 포함): IoU 뒤 영상처리 파트에 노이즈 픽셀·공간 커널 이동·Mean/Gaussian/Median 검산·Sobel 경계 단서를 추가했습니다.
- 신규 계산 도식 8개는 `docs/assets/lesson/lecture_*.svg`, 배포 순서는 `docs/assets/lesson/manifest.json`과 `scripts/build_lesson_revision.py`가 기준입니다.
- 같은 합성 3×3 배열을 재사용하여 용어 소개 → 지역 계산 → 세 가지 필터 결과 비교가 단절되지 않게 합니다.
- 이미지의 채널(C=3)과 장면의 공간적 깊이(Z)를 혼동하지 않으며, 필터링이 객체 인식이나 모든 종류의 잡음 제거를 보장한다고 표현하지 않습니다.


## 2026-10-13 전체 99장 커리큘럼 개편 (당시 기록)

- 2026-10-13 당시 웹 강의는 Intro 15장 / AI Basics 44장 / Vision AI 40장 = 총 99장이었습니다. 현재 구성은 아래 최신 항목을 우선합니다.
- Intro의 수치 이미지는 `intro_grayscale_crop_6x6.svg`를 사용합니다. 원본 48×32 픽셀 중 6×6 구간은 값과 밝기가 동일하게 대응해야 합니다.
- AI Basics는 신경 계산의 구조를 Loss·Gradient 이전에 설명합니다. Vision AI는 Label을 Class/Box/Mask로 교체하고 Mean → Gaussian → Median 및 고정 필터→CNN 학습 필터 브리지로 연결합니다.
- 수치·수식·구조는 SVG 유지, 계산이 아닌 현상 묘사는 사진 중심, 출처는 접을 수 있는 섹션, 이미지 원본 확대를 제공합니다.
- GitHub Pages 배포에서는 `scripts/verify_curriculum_overhaul.py`로 HTML 구조·자산·SVG·커널 계산을 확인합니다.
- 실사·사진 기반 고급 강의 개선은 기존 저장소의 합성 사과 이미지와 실제 필터 결과 자산을 활용합니다. Brown 원문 Figure 복제나 PPT 원본의 binary 복사는 하지 않았습니다.


## 2026-10-15 · 설명 밀도와 Pixel Interactive 원칙 (최신)

- **새로운 개념을 처음 만날 때** 실제 사진·다이어그램·조작 예시로 직관을 만들고, 이미 소개한 개념을 다시 설명할 때는 불필요한 그림을 반복하지 않습니다.
- 그다음에는 핵심 문장, 수식, 실제 계산값을 우선합니다. 수강생이 원리를 확인하기 위한 Figure는 남깁니다.
- Intro 3은 실제 사과 사진을 **48×32로 축소한 영상**에서 클릭한 6×6 영역을 표시합니다. 36개 Grayscale 값은 `round(0.299R + 0.587G + 0.114B)`로 계산하며, 숫자 행렬과 밝기 셀에 동일한 결과를 사용합니다.
- Intro 3의 밝기 배율 `k`는 숫자에 `min(255, round(k×Y))`를 적용합니다. 슬라이드의 고해상도 사진 표시는 이해를 돕기 위한 근사 미리보기이며, **정확한 숫자의 기준은 48×32 축소본**입니다.
- Intro 5는 원본 JPEG의 **실제 픽셀 위치와 RGB 3개 값**을 Canvas에서 읽습니다. 예시 숫자를 하드코딩하지 않습니다.
- 수식에는 연산 조건(반올림, 0~255 제한, 축소 여부)을 적고, 클릭/방향키/밝기 슬라이더/원본 복귀가 정상 동작해야 합니다.
- Intro 10에서는 시각적 밝기 비교를 앞서 학습한 숫자·수식과 연결하되, 화면상 밝기 처리와 실제 촬영 환경의 물리적 변화는 혼동하지 않습니다.
- 당시 Intro는 15장이었으며 현재 Intro는 새 해상도 슬라이드를 추가한 16장입니다. 기존 URL `#slide-3`, `#slide-5`, `#slide-6`은 보존하며, JS/CSS의 Version Query는 모든 참조 페이지에서 동기화합니다.


## 2026-10-15 · HWC와 해상도, AND 결정 경계 (최신)

- 강의 규모: Intro **16장** / AI Basics **44장** / Vision AI **40장** = **100장**; 핵심 모드 **80장**.
- 실제 사과 사진은 W=960px, H=640px로, RGB 배열의 **H × W × C = 640 × 960 × 3**입니다. 사진의 가로×세로 표기(W×H)와 배열(H×W×C)을 바꾸어 쓰지 않습니다.
- Intro 7의 예시: 16:9 영상의 360p=640×360, 720p=1280×720, 1080p=1920×1080. 앞의 W×H는 영상의 가로·세로이고, p는 보통 영상의 세로 Pixel 수입니다. 1280은 720p의 **너비**이며 1280p로 표현하지 않습니다.
- 새 슬라이드 추가 후 Intro 7~15의 옛 번호는 8~16이 됩니다. 기존 Intro 3·5·6 Deep Link는 유지합니다.
- AND/XOR에서는 AND의 결정 경계 x₁+x₂=1.5를 눈에 띄게 표시하고 0/1 영역의 차이를 명확하게 설명합니다.
- 시각 QA, 학습 경로, 정적 구조 검증 스크립트의 강의 수치를 함께 갱신합니다.


## 2026-10-15 · AND/XOR 결정 경계 시각화 (최신)

- AI Basics AND/XOR Figure의 x₁·x₂ 축은 **0~2** 범위로 표시하여 분리선의 방향과 경계를 시각적으로 이해하기 쉽게 합니다.
- 실제 AND/XOR 입력 데이터는 여전히 **(0,0), (0,1), (1,0), (1,1)** 네 개의 이진 좌표뿐입니다. 축의 확장은 새로운 학습 입력이나 이진 논리의 정의를 바꾸는 것이 아닙니다.
- AND의 결정 경계 **x₁+x₂=1.5**는 첫사분면에서 **(0,1.5)~(1.5,0)**로 정확히 그리며, 양쪽 분류 영역을 연한 배경색으로 구분합니다.
- 양쪽 그래프의 범위, 실제 데이터 점 위치, 분류 색상과 0/1 값, 직선 양 끝점은 자동 검증하고 텍스트·점 간 겹침도 확인합니다.

## 2026-10-15 · SVG 연결선 여백 품질 관리

- 사각형/패널을 잇는 일반 연결 화살표는 **도형 외곽과 화살표 시작·끝 사이에 최소 7 SVG 좌표 단위**의 여유를 두고, 가능하면 양쪽 여백을 비슷하게 유지합니다.
- 짧은 간격에는 큰 Arrowhead가 도형 테두리를 침범할 수 있으므로 연결 공간을 넓히거나 Marker 크기를 줄여야 합니다. **직선만 옮겨서 공간을 더 좁게 만들지 않습니다.**
- `scripts/audit_svg_connectors.py`로 사용 중인 SVG의 연결 요소를 재조사하고, 정렬을 검토한 주요 Figure에 대해 사각형 외곽 거리와 대칭성을 회귀 검사합니다.
- 변환(transform)이 있는 복잡한 그룹의 내부선, Pixel 격자 안의 이동 방향 화살표, 실제 계산 그래프 축은 일반적인 카드-카드 연결선과 구분하여 판단합니다.
- 이미지에 손을 댄 뒤 img src와 확대용 a href의 버전 쿼리를 함께 바꾸고, 전체 강의 렌더링과 텍스트 잘림 검사를 수행합니다.


## 2026-10-15 · 동일 사진 360p/720p/1080p 해상도 비교 (최신)

- 강의 규모: Intro **17장**, AI Basics **44장**, Vision AI **40장**, 전체 **101장**; 핵심 경로 **81장**.
- Intro 7은 가로×세로, p=세로 Pixel 수를 설명합니다. 신규 Intro 8은 같은 사과 사진을 16:9로 크롭한 뒤 **640×360, 1280×720, 1920×1080** 픽셀 Raster로 실제 재샘플링하여 비교합니다.
- 세 영상은 동일한 장면과 동일한 자르기 위치를 사용하고, 각 영상의 **같은 정규화 좌표 영역**을 nearest-neighbor로 확대하여 픽셀 크기 차이를 직접 확인하게 합니다.
- 기존 원본보다 큰 Raster로 Upscale한다고 원본에 없던 새로운 디테일이 생성되는 것은 아닙니다. 화질 개선 효과를 원본 해상도와 무관하게 보장하는 표현은 하지 않습니다.
- Intro 8 추가로 기존 Intro 8~16의 번호는 9~17로 이동합니다. 기존 Intro 3, 5, 6, 7 직접 링크는 그대로 유지합니다.
- 모듈: `docs/intro_resolution_demo.js`, `docs/intro_resolution_demo.css`. `scripts/verify_intro_pixel_interactive.py`에서 사진 로딩, 정확한 출력 Raster, 같은 확대 영역의 정상 렌더링을 검사합니다.


## 2026-10-15 · Intro 'What / Where' 시각 이해와 3D 역문제 (최신)

- 최신 장수: Intro **19장**, AI Basics **44장**, Vision AI **40장** = 전체 **103장**; 핵심 경로 **83장**.
- 기존 Intro 1의 메시지는 사람은 사진을 보고 의미·공간관계를 빠르게 추론하지만 컴퓨터가 처음 받는 입력은 **Pixel 숫자 배열**이라는 것입니다.
- Intro 9 신규: **Recognition(무엇인지)** / **Spatial Understanding(어디에 있고 어떤 공간관계인지)**를 실제 건축 사진과 분리된 두 시각 결과로 표시합니다. Marr(1982) 원문 **'to know what is where by looking'** 을 짧게 인용하고 MIT Foundations Ch.1과 Marr & Nishihara (1978)를 출처로 명시합니다.
- Intro 10 신규: 3D 물체를 2D 이미지로 투영할 때 정보가 손실되어 **가까운 작은 물체와 멀리 있는 큰 물체가 동일한 영상 높이로 보일 수 있음**을 정확한 원근비 예시로 설명합니다. Marr & Nishihara(1978), DOI 10.1098/rspb.1978.0020 논문 내용을 간단히 인용합니다.
- 공간 재구성은 대표적인 시각 이해 과제이며 **모든 Vision AI 모델이 반드시 3D를 재구성하지는 않습니다**. 이미지 형성, 3D 추론, Model 출력은 구별해 설명합니다.
- 원문 인용은 짧고 정확하게 하며 책의 문구를 논문 인용처럼 표기하지 않습니다. SVG 도식은 직접 작성한 교육용 개념도이며 실제 측정·모델 추론 결과가 아닙니다.
- 신규 슬라이드는 기존 Intro 8 뒤에 삽입해 **Intro 1~8 딥링크를 보존**합니다. 이전 Intro 9~17은 11~19로 이동합니다.
- 새 자산은 `docs/assets/lesson/intro_inverse_2d_3d_ambiguity.svg`, 스타일은 `docs/intro_vision_foundations.css`. 전체 206 화면의 레이아웃·이미지 자산·슬라이드 수·논문 인용·투영 비율 회귀 검사를 수행합니다.


## 2026-10-15 · Vision AI morphology 슬라이드 정리 및 연결 화살표 일체화 (최신)

- Vision AI에서 기존 9번의 Opening·Closing(Morphology) 슬라이드를 제거했습니다. 기존 10번 영상처리 기초는 9번이 되고 뒤의 번호도 한 칸씩 앞당깁니다. Morphology 자산은 보존하지만 웹 강의에서 인용하지 않습니다.
- 현재 장수: Intro **19장**, AI Basics **44장**, Vision AI **39장**, 전체 **102장**, 핵심 경로 **82장**입니다.
- 2026-10-15 기존 SVG 연결 화살표 수정에서 일부 짧은 선과 SVG marker의 삼각형 화살촉이 분리되어 보이는 문제가 있어, 영향을 받은 20개 SVG의 직선 연결부를 **선몸통과 화살촉이 이어지는 단일 폐곡선 SVG path**로 변경했습니다.
- 화살표 몸통과 삼각형은 동일한 채우기 색으로 렌더링하며, 시작·끝점의 도형 여백을 유지합니다. 굽은 경로 2개는 선과 화살촉이 겹쳐 자연스럽게 연결됩니다.
- `scripts/audit_svg_connectors.py`에서 연결선의 기하학적 시작·끝점과 닫힌 path 구조를 검사하고, 기존 도형 간 최소 7px 여백 회귀 검사도 유지합니다.
- SVG 변경 시 HTML의 image cache key를 갱신하고 전체 강의 102장 × 2개 화면의 레이아웃을 재검증합니다.


## 2026-10-15 · Vision AI 기존 33·34번 삭제 (최신)

- 현재 `main`의 Vision AI 물리 슬라이드 33번 ‘순차·병렬·우회 연결로 서로 다른 구조를 만듭니다’와 34번 ‘입력을 그대로 전달하는 경로와 변환 경로를 더합니다’를 동시에 제거했습니다. 개별 SVG 원본 자산은 보존하지만 강의에서 참조하지 않습니다.
- 기존 35번 ‘CNN의 필터도 오차를 줄이는 방향으로 학습합니다’가 **새 33번**이 되며 뒤의 모든 번호 및 `manifest.json`의 메타 번호를 연속으로 변경합니다.
- 최신 장수: Intro **19장**, AI Basics **44장**, Vision AI **37장**, 전체 **100장**, 핵심 과정 **81장**(Intro 19 + AI Basics 36 + Vision AI 26).
- 핵심/전체 모드 전환 및 AI Basics → Vision AI 이동, 전체 슬라이드 100장 × 2개 viewport, 자산·HTML·Figure 겹침 검사를 함께 수행합니다. 자산과 공통 SVG 스타일은 변경하지 않습니다.


## 2026-10-15 · 단일 전체 강의 경로 / 목차·핵심 모드 제거 (최신)

- **공개 사이트 루트** `/`와 기존 `/docs/index.html`은 모두 즉시 `/docs/intro.html#slide-1`로 리디렉션합니다. 목차 화면 및 챕터 선택 카드를 제공하지 않습니다.
- Intro/AI Basics/Vision AI 페이지의 헤더에서는 **목차·챕터 바로가기 메뉴를 제거**하고 단일 브랜드 링크(항상 Intro 1번으로 이동)만 표시합니다.
- AI Basics·Vision AI의 **‘핵심만 보기’, ‘심화 포함 전체 보기’ 버튼/설명과 학습 모드 필터**를 제거합니다. 데이터의 `detail/basic` 표시는 과거 레슨 메타데이터로 남더라도 모든 슬라이드를 무조건 표시합니다.
- 학습 순서는 **Intro 19장 → AI Basics 44장 → Vision AI 37장, 총 100장**입니다. Intro 1번에서 이전 버튼은 비활성화하고 Vision AI 마지막 장에서 다음 버튼도 비활성화합니다.
- 두 챕터 사이에서는 다음 버튼으로 다음 챕터 1번을, 이전 버튼으로 앞 챕터 **마지막 장**을 표시합니다. 기존 `#slide-N` 주소는 유지하며, 과거 `?mode=core` 링크는 전체 강의를 그대로 열고 URL에서 더는 지원하지 않는 모드 값을 제거합니다.
- `scripts/verify_learning_routes.py`는 기존 핵심/전체 이중 경로 검사 대신 루트 리디렉션, 100장 전수 순차 이동, 두 챕터 경계의 왕복 이동, 심화 슬라이드 접근성 및 옛 모드 URL 정규화를 확인합니다.
- 본 항목 이후 과거 ‘핵심 과정 81장’ 등에 대한 가이드 내 기록은 당시 변경 이력일 뿐, 현재 서비스 운영 원칙이 아닙니다.


## 2026-10-15 · Intro 3: 사람은 사과, 컴퓨터·AI 입력은 숫자 (최신)

- 사용자 요청에 따라 Intro 2의 실제 사과 사진 직후에 **새로운 Intro 3**을 넣습니다. Intro 2에서는 사과를 즉시 인식하는 사람의 시각, Intro 3에서는 **동일 사진으로부터 계산한 진짜 Grayscale 밝기 숫자 12×8 행렬**을 동일 크기로 배치해 비교합니다.
- 핵심 문장: 숫자 행렬에는 '사과'라는 의미가 직접 주어져 있지 않습니다. AI는 다양한 숫자값에서 **대상을 구별하는 공통 특징(Pattern)** 을 학습해야 하므로 Vision AI가 어렵다는 문제의식을 형성합니다.
- 오른쪽 12×8은 설명용 **Grayscale 축소**입니다. 실제 원본(960×640)은 RGB 3채널이며, 확대/추적/밝기 계산은 다음 Intro 4의 기존 48×32→6×6 Interactive Figure에서 정밀하게 설명합니다. 모든 컴퓨터 영상이 흑백으로 입력된다는 의미로 오해시키지 않습니다.
- 숫자 입력은 `docs/intro_apple_number_bridge.js`에서 **실제 같은 `vision_task_apple_reference.jpg`** 를 12×8로 축소한 후 `round(0.299R + 0.587G + 0.114B)`로 계산합니다. 생성하거나 임의로 만든 숫자를 그리지 않습니다. 로컬 CSS는 `docs/intro_apple_number_bridge.css`입니다.
- Intro는 20장으로 증가, 기존 Intro 3~19가 새 Intro 4~20으로 이동합니다. AI Basics 44, Vision AI 37은 그대로이며 총 **101장**입니다. 단일 순차 경로로 Intro 20 → AI Basics 1이 이어집니다.
- 실시간 브라우저에서는 사과 사진과 숫자의 정확한 일치, 96개 값 범위와 실제 이미지 사이즈, Intro 2→3→4 이동을 확인합니다. 전체 **202개 발표 viewport** 겹침·잘림 검사도 수행합니다.


## 2026-10-15 · Vision AI 주도 통합 강의와 접이식 왼쪽 목차 (최신)

- **실제 공개 학습 경로:** Intro **20장** → `docs/vision_ai_course.html` Vision AI 중심 통합 **81장** = **101장**입니다. 기존 'Intro → AI Basics → Vision AI' 연속 수업은 종료했습니다.
- 단순히 챕터 순서를 뒤집지 않고, Vision AI의 **과제·출력(Classification/Detection/Segmentation)** 설명으로 시작합니다. 필요한 AI 이론은 관계 있는 흐름에 배치합니다: Task 출력 → AI 개념/분류, 영상처리 → 전처리·증강, CNN → Perceptron/Activation/Feature, CNN 학습 → Loss/Gradient/Backpropagation, Transfer Learning → Dataset·평가·현장.
- 기존 AI Basics 44장·Vision AI 37장은 원본 HTML과 `manifest.json`을 보존하며, 신규 통합 페이지에서 내용과 그림을 재사용합니다. 새 페이지는 원본 슬라이드 메타 `data-source-deck`, `data-source-slide`로 출처 위치를 추적해 각 슬라이드의 손실·누락·중복을 검사합니다.
- 현재 Intro의 다음 챕터는 `vision_ai_course.html`; 통합 마지막 장에서 강의를 종료하고 이전 버튼으로 Intro 마지막 장까지 돌아갈 수 있습니다.
- **왼쪽 목차 UI**는 Intro와 통합 강의의 상단 '☰ 강의 목차' 버튼으로 열 수 있습니다. 목차는 주제별 `details`로 101개 제목을 나누고, 모든 항목은 개별 `#slide-N`으로 직접 이동합니다. 목차 열기/닫기, 내부의 닫기 버튼, 바깥 클릭, Escape 키를 지원합니다.
- 발표 슬라이드를 침범하지 않도록 기본 상태는 목차가 닫힌 상태이며, 열었을 때만 왼쪽 오버레이로 나타납니다. 모바일과 키보드 조작 접근성을 지원합니다. 이전에 제거한 전체 페이지 목차, '핵심만 보기' 모드는 다시 추가하지 않습니다.
- 새 파일: `docs/vision_ai_course.html`, `docs/lecture_outline.js`, `docs/lecture_sidebar.js`, `docs/lecture_sidebar.css`. 이전 링크 `docs/ai_basics.html`, `docs/vision_ai.html`은 원본 참고를 위해 유지합니다.
- 필수 검증: 101개 목차 링크·주제 이동·접힘/펼침·양방향 챕터 전환, 원본 Vision 37/AI 44 슬라이드의 정확한 한 번씩 재사용, 전체 202화면 레이아웃/이미지 경로·SVG·실습 상호작용 검사. 공유 JS 변경 시 cache key를 갱신합니다.


## 2026-10-15 · Vision AI 6번 Label 그림과 3·4·5번 사과 예시 일치

- 통합 Vision AI 강의 3번 Classification / 4번 Object Detection / 5번 Segmentation에서 사용하는 **동일한 960×640 사과 JPEG**와 결함 위치를 6번 Label 비교 Figure에서도 그대로 사용합니다.
- `docs/assets/lesson/task_labels_three_outputs.svg`에는 원본 JPEG를 한 번만 담고, 세 카드에서 동일 사진을 `<use>`로 재사용합니다. 검출 Box 좌표와 분할 Mask 경로는 각각 `context_task_detection.svg`와 `context_task_segmentation.svg`에 그려진 작은 결함의 좌표·경계를 옮긴 것입니다. 별도의 큰 사과 전체 Mask나 상이한 결함 표시를 임의로 사용하지 않습니다.
- 분류 Label은 이미지 전체 클래스, 검출 Label은 결함 Class와 Bounding Box, 분할 Label은 결함 Class와 Pixel Mask라는 핵심 메시지를 유지합니다. Box와 Mask는 강의용 개념 오버레이로, 실제 수작업 라벨 또는 모델 Prediction이라고 주장하지 않습니다.
- 통합 `docs/vision_ai_course.html#slide-6` 및 이전 링크 호환용 `docs/vision_ai.html#slide-6`이 동일 Figure를 참조하며 버전 query를 변경해 캐시를 갱신했습니다. 슬라이드 수·목차·공통 CSS/JS는 변경하지 않습니다.
- 검증 시 동일 원본 이미지 데이터, 검출 Box 변환 좌표, 분할 Path 일치, 202개 viewport의 렌더링을 점검합니다.


## 2026-10-16 · Intro 3 대비 픽토그램 / 이미지 이해의 어려움 순서

- 현재 공개 학습 경로는 Intro **18장** → Vision AI 중심 통합 **81장**, 총 **99장**입니다. 기존 Intro 13·14의 Noise / Signal 예시는 Intro에서 제거했으며, 후속 Vision AI 영상처리·Filtering 단원은 유지합니다.
- Intro 3에서 실제 동일한 사과 사진의 **12×8 Grayscale 숫자 배열**을 보존하되, 사람과 컴퓨터 아이콘·말풍선을 추가해 **“아, 사과구나!” / “?! 그냥 숫자 배열이네”**를 대비합니다. 아이콘·말풍선은 교육용 도식이며 실제 AI 모델의 추론 결과가 아닙니다.
- 이전 Intro 15 (밝기·색감 변화)와 16 (평면 회전·축소·가림·블러)를 새로운 **Intro 4·5**로 옮깁니다. 새 Intro 6에서 원본 Pixel 계산을 도입하므로 앞선 Intro 4는 수식이 이미 설명되었다는 표현을 사용하지 않습니다.
- Intro 6~14는 이전 Intro 4~12에 해당하며, 이전 Intro 17~20은 새 Intro 15~18입니다. 딥링크 `#slide-N`은 항상 **현재 위치 기반**입니다. 이동된 내용에 대해 목차·슬라이드 번호를 최신으로 갱신합니다.
- 목차 `docs/lecture_outline.js`를 99개로 재생성하고, 공유 목차 JS를 읽는 Intro·통합 Vision HTML 양쪽에 cache key를 갱신합니다. 브라우저 탐색/픽셀 실습 검증은 새 번호를 사용합니다.


## 2026-10-16 · 시각의 중요성에서 시작하는 Vision AI 흐름 (최신)

- 공개 경로: Intro **19장** → Vision AI·AI 통합 **79장** = 총 **98장**입니다. 이전 Intro 18장·통합 81장 표기는 변경 이력입니다.
- Intro 1: 사람은 시각으로 대상·위치·공간 관계를 빠르게 파악합니다. 임의로 수치화된 시각 정보 비율은 사용하지 않습니다.
- Intro 2: Vision이 중요한 이유를 카메라·센서 이동 로봇·열화상 기기 사진으로 보여줍니다. Intro 3은 기존 사과 질문, Intro 4는 사람·컴퓨터 인식 비교입니다.
- Intro 5는 밝기·색감 변화, Intro 6은 화각·평면 회전·가림·초점 변화를 보여줍니다. 화각 설명은 같은 사진을 크롭·확대한 개념 예시로서 실제 렌즈 측정 결과가 아닙니다.
- 통합 강의 기존 8번 IoU 수치 계산 슬라이드는 삭제하고, 기존 7번 IoU 개념 슬라이드는 평가 단원 후반으로 이동합니다. 원본 vision_ai.html 및 manifest는 참고용 보존본입니다.
- 공개 통합 강의 순서: Task·Label(6장) → AI 판단의 학습(7장) → 데이터·분할·전처리(6장) → 공간 필터(9장) → Perceptron·Activation(7장) → CNN(16장) → Loss·Optimizer·Training(12장) → Transfer Learning·Generalization(6장) → 평가·운영(10장).
- data-source-deck·data-source-slide 원본 식별자는 보존하고, 98개 목차 항목·물리 슬라이드 순서·브라우저 QA 수치·캐시 키를 함께 최신으로 유지합니다.

## 2026-10-16 · 기존 첫 장 복원과 목차 스크롤 독립 처리 (최신)

- 기존 Intro 1 타이틀 **“AI는 세상을 어떻게 볼까?”**의 원래 HTML·문구를 복원하여 공개 강의 맨 앞에 배치합니다. 직전에 추가한 시각 정보와 Vision 중요성 슬라이드는 각각 Intro 2·3에 유지합니다.
- 공개 장수는 **Intro 20장 + Vision AI 통합 79장 = 총 99장**, 두 발표 화면 기준 **198개 viewport**입니다.
- 공개 목차는 99개 항목으로 복구하고 global 번호와 Intro #slide-N 순서를 연속화합니다. docs/slide.js에서 목차가 열린 동안 wheel·touchend·슬라이드 이동 keydown을 처리하지 않아 목록 스크롤만으로 슬라이드가 바뀌지 않습니다. 목차 링크 클릭·이전/다음 버튼은 정상 작동합니다.
- 공통 slide.js 수정에 대해 Intro·통합 Vision AI·기존 AI Basics·Vision AI 페이지의 cache query를 갱신합니다. 공유 lecture_outline.js의 양쪽 공개 페이지 cache query도 함께 갱신합니다.
- 브라우저 회귀 검사는 목차 휠 스크롤 및 backdrop에서의 휠 입력이 slide hash를 바꾸지 않고 목록 자체가 스크롤되는지 확인합니다.

## 2026-10-16 · Intro 9 삭제와 컬러 이미지 데이터량·해상도 정보량 (최신)

- 현행 공개 슬라이드는 **Intro 19장 + Vision AI 통합 79장 = 98장**입니다. 이전 Intro 9의 원근·실제 크기 비교 슬라이드를 삭제합니다. 이후 Intro 번호·목차 전역 번호·cache key를 맞춥니다.
- 원래 Intro 11(삭제 후 Intro 10)은 RGB 이미지 640 × 960 × 3의 전체 숫자 개수, **1,843,200개 채널 값**을 설명합니다. 640 × 960 = 614,400 Pixel은 위치 수이고, Pixel당 3개 RGB 색상 값을 갖는 8-bit 컬러 이미지 예시입니다. 1,843,200을 Pixel 개수라고 표기하지 않습니다.
- RGB Figure에서 오른쪽 개별 Pixel의 R/G/B 값 98/67/38 예시를 제거하고 사진과 전체 R/G/B 채널 배열의 대응만 보입니다. 원본 사과 JPEG의 인라인 데이터는 그대로 보존합니다. 슬라이드의 '핵심' 콜아웃도 제거합니다.
- 이후 Intro 11·12는 해상도가 증가할수록 같은 장면을 더 촘촘한 Pixel로 표현하여 **기존 원본에 있는 미세한 정보**를 보존할 수 있음을 강조합니다. 단순 업스케일은 사라진 디테일을 복원하지 않는다고 명시합니다.
- 레이아웃/SVG/상호작용 회귀 테스트를 Intro 19장·통합 79장 및 196개 viewport 기준으로 동기화합니다.

## 2026-10-16 · Vision AI 중심 CNN 아키텍처 개편 (최신)

- **공개 순서:** Intro 19장(변경 없음) + Vision AI 통합 **58장** = 총 **77장**, 2개 발표 화면 기준 **154개 렌더링**입니다.
- 기존 통합 강의 79장에서 Vision AI와 직접 관련성이 낮은 AI 일반론·Gradient/Chain Rule 수학 계산·중복 지표·K-Fold 등 **29장 제외**, CNN 기초·구성·대표 확장을 설명하는 새 Figure **8장**을 추가합니다. 기존 AI Basics와 Vision AI 독립 파일 및 lesson manifest는 원본 참고 자료로 보존합니다.
- 1. Vision Task/Label 5장 → 2. AI 기초 3장 → 3. Spatial Filtering 5장 → 4. 최소 신경망 기초 3장 → 5. CNN 구성 요소 16장 → 6. CNN 확장 구조 5장 → 7. 학습 6장 → 8. 데이터 5장 → 9. 전이학습 3장 → 10. 평가·운영 7장 순서입니다.
- 기본 CNN 단면 설명: RGB 입력 → Convolution/Batch Normalization/ReLU → Stride·Padding·Pooling → Feature Map/Channel → GAP/Flatten → Dense/Task Head. 실제 숫자 크기 예시는 모든 Layer의 Stride/Padding 설정에 종속됩니다.
- 대표 CNN 확장 개념: Residual/Skip Connection(ResNet), Standard/Grouped/Depthwise/Pointwise(1×1) Convolution, Dilated Convolution, Upsampling/Transposed Convolution, U-Net Encoder–Decoder와 Skip, FPN 멀티스케일 특징 및 Classification/Detection/Segmentation Head. 전체 CNN 모델 계보가 아니라 초보자가 구조를 이해하는 데 필요한 대표 구성요소입니다.
- 각 새 Figure는 `docs/assets/lesson/cnn_foundations_n1.svg` ~ `cnn_foundations_n8.svg` 로컬 SVG 파일입니다. `src/href`는 Repository 로컬 상대경로를 사용하고 CDN은 이용하지 않습니다.
- 77개 좌측 목차 링크, 페이지 간 이동, 앵커, 해상도, 이미지 로드, SVG 문법과 154개 레이아웃 점검을 함께 검증합니다.

## 2026-10-16 · YOLO 중심 개편: CNN의 원리까지만, 모델 예시는 YOLO 하나 (최신)

- 공개 강의는 Intro **19장**(원본 유지) + Vision AI 통합 **52장** = 전체 **71장**입니다. 이전 통합 58장은 이력이며 사용자 피드백에 따라 세부 아키텍처 ResNet·U-Net·FPN, Depthwise·Dilated, Transposed Convolution 독립 강의와 상세 출력 크기 계산 등을 제거했습니다. 해당 기존 SVG는 보존만 하며 공개 목차에서 더는 참조하지 않습니다.
- CNN 핵심은 **실제 사과 사진의 작은 영역 → Kernel의 이동 → Feature Map(입체적 Channel 스택) → 여러 층의 특징 → Head**로 표현합니다. 단순 상자 연결 그림 대신 입체 Feature Map 개념 Figure로 교체하고, 참고 자료 **CNN Explainer — Wang et al. (IEEE TVCG 2020), https://poloclub.github.io/cnn-explainer/** 를 공개 슬라이드에서 인용합니다. Figure는 실제 모델 Activation 측정이 아닌 개념 재구성임을 명시합니다.
- YOLO(You Only Look Once)는 물체 검출을 위해 등장한 모델 계열이며, 현대 Ultralytics 제품군은 Classify/Detect/Segment 등 Task별 모델을 지원합니다. 한 검출 모델이 Mask까지 자동으로 반환한다고 혼동하지 말아야 합니다. 참고 출처: Redmon et al., CVPR 2016 https://openaccess.thecvf.com/content_cvpr_2016/html/Redmon_You_Only_Look_CVPR_2016_paper.html , Ultralytics 아키텍처 https://docs.ultralytics.com/ko/guides/yolo-architecture , Task 문서 https://docs.ultralytics.com/tasks/.
- **YOLO 신규 5장**: 사람이 정한 고정 영상 필터 vs 학습되는 CNN Weight → YOLO Backbone/Neck/Head → 검출 예시(Class·Box·Score) → Classify/Detect/Segment에 맞는 모델·Label 선택 → 사전학습 YOLO + 데이터/Label + Train/Val/Predict와 현장 검증. 모든 예시 score/Box/Feature Map은 실제 추론값이 아닌 개념 예시입니다.
- “YOLO가 알아서 Filter를 학습한다”는 뜻은 **Convolution Weight가 Label/Loss에 의해 바뀐다**는 의미이지 데이터 품질·정답 라벨링·Train/Test 분리·환경 차이·운영 실패 검증도 완전히 자동화된다는 뜻이 아닙니다. 필요에 따라 전통 영상 필터/다른 모델도 사용될 수 있습니다.
- 강의 구성은 Task 5 / AI 차이 2 / Filter 5 / 신경망 3 / CNN 핵심 11 / YOLO 5 / 학습 6 / 데이터 5 / 전이학습 3 / 평가 7장입니다. 71개 목차·142개 두 해상도 화면·슬라이드 경계 이동·SVG 및 외부 출처 링크를 검증합니다.


## 2026-10-16 · CNN과 YOLO 구조 Figure의 출처 우선 적용

- 공개 통합 강의의 CNN 구조(16번)와 YOLO 아키텍처(28번)는 직접 제작한 구조 SVG 대신 인용 가능한 학술 논문 Figure를 우선 표시합니다. CNN은 Yamashita et al. (2018) Fig. 1, YOLO는 *Electronics* (2024) Fig. 1의 YOLOv8 아키텍처입니다.
- 라이선스·원문·그림 URL은 assets/SOURCES.md에 기록합니다. 논문 원본을 수정하지 않으며 표시 크기만 CSS로 조절합니다.
- 사내 환경에서 외부 이미지가 차단될 경우 기존 Repository 내부 SVG를 fallback으로 보이게 해 강의가 중단되지 않게 합니다. 완전한 오프라인 재현을 위해서는 적법한 원본 이미지 로컬 저장과 경로 교체가 추가로 필요합니다.
- ResNet·U-Net 등 개별 CNN 아키텍처 상세 소개는 공개 강의에서 제외하고, YOLO의 역할·데이터·검출 결과에 집중합니다.


## 2026-10-16 · Dragon1 CNN 기초 설명 참고 (최신)

- 사용자 지정 참고자료: https://www.dragon1.com/terms/convolutional-neural-networks-definition
- 통합 강의 **16번**: 학술 Figure(Yamashita et al., 2018)를 유지하면서 **Input → Convolution → ReLU → Pooling → Flatten/Fully Connected → Output** 단계 해설을 붙입니다. 설명은 전형적인 분류 CNN 예시이며 모든 CNN 구조가 고정 순서를 갖지는 않습니다.
- 별도로 재사용 허가를 확인할 수 없는 Dragon1 그림은 복제하지 않습니다. 출처는 본문과 assets/SOURCES.md에 명시합니다.
- YOLO 5장, ResNet·U-Net 제외 원칙, 논문 이미지가 차단되면 로컬 SVG를 표시하는 방식을 보존합니다.


## 2026-10-16 · CNN Figure GitHub 로컬 자산으로 전환 (현재)

- 공개 통합 강의 16번의 외부 CNN 논문 이미지를 **`docs/assets/lesson/cnn_dragon1_lecture.svg`** 로 대체했습니다. Dragon1 CNN 설명 순서를 참고한 **직접 제작 SVG**이며, 이미지 로드·확대 링크에서 해당 저장소 내부 파일만 참조합니다.
- 입력 사과/특징 지도/Convolution/활성화/Pooling/Flatten/FC/출력이 연결된 큰 단일 Figure로 보여지게 하며, 이전 여섯 개의 보조 설명 카드를 제거했습니다.
- 계산 예시는 ReLU(x)=max(0,x), 2×2 Max Pooling 및 총합 100%의 가상 분류 점수와 일치해야 합니다. 실제 모델에서 추출한 Activation 또는 Prediction이 아닙니다.
- 새 Figure는 CNN 입문용 **분류 구조 예시**이고 YOLO detection Head와 동일하지 않습니다. ResNet·U-Net 등의 독립 설명은 계속 제외합니다. YOLO 슬라이드와 전체 목차 구성은 유지합니다.
- `docs/cnn_structure_ref.css`를 새 단일 그림에 맞춰 정리하고 버전 쿼리를 갱신합니다. 외부 레퍼런스: https://www.dragon1.com/terms/convolutional-neural-networks-definition


## 2026-10-16 · CNN 얼룩말 원본 그림 + YOLO 학습 목표 (최신)
- 현재 CNN 16번은 [Developers Breach, Swapna K E (2020)](https://developersbreach.com/convolution-neural-network-deep-learning/)의 원본 얼룩말 CNN Banner를 그대로 외부 이미지로 표시합니다. 원본 https://i0.wp.com/developersbreach.com/wp-content/uploads/2020/08/cnn_banner.png?fit=1200%2C564&ssl=1
- CNN Figure는 얼룩말 입력 → Conv/ReLU·Pooling 반복 → Flatten → Fully Connected → Softmax → Zebra 분류라는 분류 CNN 예시입니다. 영어가 들어 있는 원본 Figure는 변경하지 않고, 한글 슬라이드 제목·설명과 핵심 문장으로 설명합니다.
- 사내 네트워크 등으로 원본 로드 실패 시 기존 로컬 cnn_dragon1_lecture.svg로 자동 대체합니다. 원본 PNG를 로컬에 복사한 것이 아니라 외부 이미지 URL을 직접 사용하므로 온라인 접근성에 따라 표시됩니다.
- YOLO 파트 신규 31번: 'YOLO 객체 검출은 종류와 위치를 함께 학습합니다'. 로컬 Figure: docs/assets/lesson/yolo_class_box_training_ko.svg.
- 'YOLO는 Classification만 학습한다'는 표현은 부정확합니다. YOLO Detect는 Class와 Bounding Box를 함께 예측하고 정답에 맞춰 학습합니다. Classification만 하는 YOLO Classify 모델은 별도 Task입니다.
- 이번 구성: Intro 19장 + 통합 53장 = 총 72장. 31번 삽입에 따른 목차 슬라이드 번호·Outline 캐시 버전도 함께 갱신합니다.


## 2026-10-16 · 검증된 외부 Figure / 강의자료 조사 기반 수업 개편

- 현재 참고 자료 조사와 슬라이드별 구성안은 루트의 [REFERENCE_VISION_AI_SOURCE_LIBRARY.md](REFERENCE_VISION_AI_SOURCE_LIBRARY.md) 및 [REFERENCE_SLIDE_SOURCE_MAP.md](REFERENCE_SLIDE_SOURCE_MAP.md)에 기록합니다. 대표 28건을 우선 검토하며 **모든 Computer Vision 논문을 다 찾았다고 주장하지 않습니다**.
- 강의자료의 우선순위: **실제 이미지/원본 Figure → 한국어 그림 해설 → 정확한 계산 → 출처 표기**입니다. 사용자 선호는 16번과 같은 명료한 Figure 배치이며 영어 본문이 아닙니다. 영어는 기술 용어에 한해 사용합니다.
- 본조사 문서의 `후보`는 원본 이미지 파일 URL·Figure 번호·사용 조건 등을 확인하기 전의 제안이며, 공개 슬라이드 반영을 뜻하지 않습니다. 강의 원본을 한 번에 덮어쓰지 않고 2~3장 단위로 샘플을 만들고 렌더링 검증합니다.
- 기존 16번 얼룩말 CNN 원본, 28번 YOLO 논문 Figure 및 Intro 19장/통합 53장의 강의 흐름, 실제 사과사진·Pixel 계산·인터랙티브 자료는 유지합니다.
- ResNet/U-Net 상세 아키텍처 추가는 하지 않습니다. CNN 공통 원리 → YOLO Detect/Classify 구별 → 데이터/학습/평가의 초보자 흐름을 지킵니다.



## 2026-10-16 · 원본 연구 Figure 시범 적용 (현재 10·11·25·51번)

- **10번 Spatial Filtering**: OpenCV 공식 튜토리얼의 `blur.jpg` (Mean), `gaussian.jpg` (Gaussian), `median.jpg` (Median) 원본 영상으로 실제 처리 전후를 비교합니다. 각각 다른 조건(특히 Median은 점 잡음 입력)을 사용하므로 동일 Pixel의 정량 결과처럼 주장하지 않습니다. 기존 단일 3×3 수치 비교 Figure는 별도의 펼침 영역에 보존합니다.
- **11번 Sobel**: OpenCV의 원본 인물 사진, 위치-밝기 곡선, 미분 곡선을 나란히 사용합니다. 원본 인물 사진에서 실제로 측정한 연속 신호인 것처럼 표현하지 않습니다. 기존의 실제 합성 데이터 Sobel 결과 그림은 펼침 영역에 보존합니다.
- **25번 CNN Feature Visualization**: Distill (2017) GoogLeNet의 `mixed4a Unit 97`과 `mixed5a Unit 9` 최적화 시각화 및 실제 반응 데이터셋 사진을 그대로 사용합니다. **최적화로 생성된 패턴 이미지**와 **해당 뉴런에 강하게 반응한 데이터셋 실제 사진**을 구분합니다. CNN Feature Map을 실제 이미지에 그대로 투영한 Figure라고 말하지 않습니다.
- **51번 판단 근거**: jacobgil/pytorch-grad-cam 공개 Classification 예제의 원본 고양이·개 사진과 Dog/Cat 클래스별 Grad-CAM 열지도를 사용합니다. 다른 클래스를 설명할 때 강조 영역이 달라지는 것으로 설명하고, 높은 Confidence와 정답/해석의 신뢰성을 동일시하지 않습니다.
- 모든 슬라이드의 제목·부제·핵심 문장은 한국어 중심이며, 외부 원본 링크는 출처를 표기합니다. 외부 로드 실패 시 원래 저장소의 로컬 Figure로 대체합니다.
- 전용 CSS `docs/research_original_figures.css?v=20261016-1`는 `docs/vision_ai_course.html`만 적용됩니다. 공용 CSS/JS는 수정하지 않으며 16번 얼룩말 구조, 31번 YOLO 학습 도식 및 기존 목차·전체 슬라이드 72장을 유지합니다.


## 2026-10-16 · CNN 특징 계층 3단계 수정 (최신)

- Vision AI 통합 강의 **25번**은 기존 연구용 추상 이미지만 비교하는 2패널 설명에서 **얕은층 / 중간층 / 깊은층** 3단계 구성으로 변경합니다. 원본 사과 사진 하나가 출발점임을 크게 표시하며, 모든 단계의 설명은 한국어가 원칙입니다.
- 사용 파일: `docs/assets/lesson/cnn_three_stage_apple_ko.svg`; 기존 사과 사진 재사용 및 자체 도형/경계 강조 예시를 조합한 **개념 설명 Figure**입니다. 실제 CNN 실험 결과처럼 설명하지 않습니다.
- Stanford CS231n과 Distill (2017) 논문을 이론 출처로 표기합니다. 기존 논문 원본 Figure를 그냥 나열하는 대신 학습 목표를 먼저 파악할 수 있는 구조로 사용합니다.
- 기존 10번 OpenCV Filtering, 11번 Sobel, 16번 얼룩말 CNN, 31번 YOLO 학습, 51번 Grad-CAM은 변경하지 않으며 **Intro 19장 + 통합 53장 = 총 72장**을 유지합니다.


## 2026-10-16 · Pages 공개 URL과 이전 주소 호환 (최신, 필수)

- **Pages 배포 설정**: `.github/workflows/deploy-pages.yml`에서 `actions/upload-pages-artifact`의 `path: ./docs`를 사용합니다. 따라서 **저장소 경로** `docs/vision_ai_course.html`의 공개 URL은 `https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html`입니다. 웹 주소에 **`/docs/`를 중복 삽입하지 않습니다.**
- 전체 강의 시작 주소: `https://sh0427-han.github.io/vision_ai_lecture/` (Intro 1번으로 자동 이동). Vision AI 25번 고정 링크: `https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-25`.
- 예전에 잘못 보낸 `https://sh0427-han.github.io/vision_ai_lecture/docs/vision_ai_course.html#slide-N`, `/docs/intro.html#slide-N`, `/docs/` 경로는 `docs/docs/*.html`에 설치한 **호환 리디렉션**으로 처리하며 **Query와 Hash(슬라이드 번호)**를 유지해 이동합니다.
- 외부에서 배포 URL을 줄 때 Repository의 `docs/` 디렉터리 경로와 Pages의 URL 경로를 반드시 구분합니다. 실제 GitHub Pages 도메인은 보안 정책/사내 프록시 등의 이유로 일부 환경에서 접근이 차단될 수 있으므로, URL 오류와 네트워크 차단은 구분해 안내합니다.
- 강의 슬라이드 수는 Intro 19장, Vision AI 53장, 합계 72장입니다.


## 2026-10-16 · 25번 최신 확정 방향: Stanford CS231n 원본 그림

- Vision AI 25번의 직접 제작 사과 개념도는 원본 Stanford CS231n의 VGG-16 학습 특징 시각화로 교체했습니다. 원본 PNG는 `docs/assets/lesson/cs231n_vgg16_feature_hierarchy_original.png`로 저장하고 픽셀을 수정하지 않았습니다.
- 3단계 얕은층/중간층/깊은층의 한글 설명을 그림 아래에 표시합니다. 원본 강의 2017 Lecture 5 Slide 37, 시각화 크레딧 Lane McIntosh.
- 별도 CSS `docs/cs231n_feature_hierarchy.css`는 Vision AI 25번에만 적용합니다. 기존 사과 도식은 기록으로 보존합니다. 전체 강의는 Intro 19장 + Vision AI 53장, 합계 72장입니다.


## 2026-10-16 · CNN 실제 Feature Map → 특징 시각화 2장 구성 (현재 최신)

- Vision AI **25번**: CS231n의 강아지 사진을 **사전학습된 SqueezeNet1.1**에 입력해 실제 중간 출력(Feature Map)을 얻어 같은 사진과 비교합니다. 이미지 `docs/assets/lesson/cnn_squeezenet_actual_feature_maps.png`, 재현 스크립트 `scripts/render_cnn_feature_maps.py`. 입력 및 학습 정규화, 선택 채널, 실제 Feature Map의 공간 해상도를 모두 표시합니다.
- Vision AI **26번**: 이전 25번 Stanford CS231n VGG-16 학습 특징 시각화 Figure를 원본 그대로 보존하고, Learned Feature Pattern이 무엇인지를 한글로 설명합니다. **Vision 25(SqueezeNet)와 Vision 26(VGG-16)은 서로 다른 모델**이며 Feature Map(입력 반응)과 Feature Visualization(학습 특징 분석)도 서로 다른 개념입니다.
- CNN층이 깊다고 원본 강아지가 만화 그림으로 바뀌는 것이 아닙니다. 구체적 입력 → 실제 모델 중간 출력 → 특징을 연구하는 Figure 순서입니다.
- 새 슬라이드 삽입에 따라 Intro 19 + Vision 54 = 전체 **73장**. 공개 딥링크는 `https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-25`와 `#slide-26`이며 `/docs/`를 포함하지 않습니다. 강의 구성의 이전 내용 번호는 26번 이후 +1씩 이동합니다. 공통 CSS는 변경하지 않습니다.

## 2026-10-16 · 전체 제목 간결화 + 실제 사진 계산 기반 강의 (최신)

- 전체 공개 강의 **Intro 19장 + 통합 Vision AI 54장 = 73장**의 제목을 **간결한 개념형 명사구**로 정리했습니다. `~입니다`, `~합니다`와 같은 완성문 대신 슬라이드 핵심을 바로 파악할 수 있는 제목을 사용합니다. 한글 설명은 기존대로 유지하고 필요한 영어 기술 용어만 병기합니다.
- 슬라이드 22·23·24·43·44번은 기존 삽화만 보는 방식에서 동일한 **실제 강아지 사진**을 직접 연산한 **실제 계산 결과 이미지**로 전면 교체합니다. 기존 정확한 Kernel·Stride·Padding·Pooling·Preprocessing·Augmentation 설명 도식은 펼침 영역에서 계속 확인할 수 있습니다. 
- 실제 이미지 자산: `docs/assets/lesson/cnn_real_stride_dog.png`, `cnn_real_padding_dog.png`, `cnn_real_maxpool_dog.png`, `cnn_real_preprocess_dog.png`, `cnn_real_augment_dog.png`. NumPy와 Pillow를 이용한 재현 코드는 `scripts/render_real_vision_examples.py`; 생성 워크플로는 `.github/workflows/generate-real-vision-examples.yml`.
- Stride·Padding의 반응도는 **학습 CNN 출력이 아니라 고정 Sobel Filter의 실제 계산 결과**입니다. Pooling은 실제 Gray 영상값에 적용한 2×2 Max Pooling이며 학습 Feature Map이 아닙니다. 전처리는 실제 Resize/Letterbox, 증강은 실제 밝기·회전·가림 처리 결과입니다. 이 구분을 그림과 본문에서 명시합니다.
- 기존 **동일 사과 사진의 Classification/Detection/Segmentation 비교**, **정확한 수치 계산**, **CNN 25·26번 실제 Feature Map 및 CS231n 논문 Figure**, **YOLO 실제 구조 논문 Figure**, **학습 인터랙티브**, **Grad-CAM 연구 예시**는 무작정 교체하지 않습니다. 원본 연구 Figure와 실제 계산값을 우선 사용하되, 필요한 상황에서는 재구성 도식도 사용합니다.
- 관련 수정은 `docs/scientific_photo_figures.css`에 5개 슬라이드 범위로 한정했습니다. `docs/lecture_outline.js`의 73개 제목을 Intro/Vision AI 파일과 동기화하고 URL에 `/docs/`를 삽입하지 않습니다. 배포 후 정적/시각 검증을 필수로 수행합니다.


## 2026-10-16 · 추가 개선: Filtering 10번·Sobel 11번 실제 계산 로컬화

- 외부 OpenCV 이미지 직접 로드는 브라우저/CI에서 깨질 수 있어, 강의 10·11번의 주요 이미지를 실제 동일 강아지 사진에서 계산한 로컬 PNG로 교체합니다 (`cnn_real_filter_compare_dog.png`, `cnn_real_sobel_dog.png`). OpenCV 공식 문서 링크는 원리/출처로 유지하며 외부 jpg 직접 로딩은 없앴습니다.
- NumPy·Pillow 계산 스크립트 `scripts/render_real_vision_examples.py`에서 모든 7개 실제 이미지 도식을 생성합니다. 10·11번과 22·23·24·43·44번으로 총 **7장**에 동일 실사 기반 연산을 연결하고, 예전 숫자 예시도 펼쳐 볼 수 있습니다. 전체 73장 제목은 간결한 개념형으로 통일합니다.


## 2026-10-16 · CNN 개념 우선·필터 세부사항 축소 (최신 적용)

- 본 강의는 **Vision Task → AI와 학습 차이 → CNN 전체 구조 → 실제 Feature Map → 학습된 특징 시각화 → Kernel의 존재 이유·역할 → 가중치 공유와 학습 → 기초 Neural Network → CNN 핵심 연산 → YOLO → 데이터·평가** 순서로 진행합니다.
- **과도한 Spatial Filtering 세부 설명을 강의 시작에서 제거**합니다. 기존 통합 강의 8번 Pixel vs 이웃연산, 10번 Mean/Gaussian/Median, 11번 Sobel, 12번 Spatial Filtering 다리 슬라이드는 독립 강의에서 제외합니다. 실제 필터 처리 결과는 통합 14번의 접기/펼치기 참고 이미지로 남깁니다. 기존 SVG/PNG 자산 자체는 유지합니다.
- **핵심 학습 목표**: Kernel=작은 가중치 배열, 국소 Pixel 계산, 같은 가중치의 반복 사용, 위치별 Feature Map, 학습 과정에서 Loss를 줄이기 위해 Kernel 가중치 수정. Mean·Gaussian·Sobel은 **고정된 사람의 규칙**이라는 대비용으로만 사용합니다.
- 실제 모델 계산 이미지를 예시로 제시한 9번은 SqueezeNet Feature Map, 10번은 VGG-16 특징 최적화 시각화로 **다른 네트워크·다른 분석 결과**임을 표시해야 합니다.
- 번호: Intro 19, 통합 Vision AI **50**, 전체 목차 **69**. 실제 바로가기: `https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-8` (CNN 개요), `#slide-9` (실제 Feature Map), `#slide-12` (Kernel), `#slide-14` (고정 vs 학습), `#slide-18` (Kernel 가중치 학습). 공개 주소에서 `/docs/`를 중복 사용하지 않습니다.
- `docs/cnn_kernel_foundations.css`는 선택형 고정 필터 참고 패널에만 적용되며 공통 CSS/JS는 수정하지 않습니다. 제목/목차/수치/이미지 경로 검증과 GitHub Actions/Pages 확인 필수입니다.

- 추가로 **12번**에는 `docs/assets/lesson/cnn_kernel_role_beginner_ko.svg`를 사용하여 CS231n 실제 강아지 입력 사진의 작은 영역 → 3×3 Kernel → 위치별 특징 반응을 보여줍니다. **오른쪽 반응 지도는 학습 CNN 실측값이 아닌 설명용 도식**이고, 기존 수치 계산 Figure는 펼침 참고로 남깁니다.


## 2026-10-16 · YOLO 설명 정리 및 CNN/Stride/Padding/Pooling/비선형성 재구성 (현재 최신)

- 공개 통합 강의는 **Intro 19장 + Vision AI Course 49장 = 총 68장**입니다. 기존 YOLO 전용 26~30번 5장은 전부 삭제했으며 Task(분류·검출·분할), Backbone/Head 및 학습·평가의 일반 원리는 보존합니다. 기존 YOLO 명칭이 섞인 '고정 필터 vs 학습 Kernel' 슬라이드는 일반 CNN 설명으로 바꿉니다.
- 통합 **8번**: CNN을 왜 쓰는지 32×32 입력/출력 한 채널 예시로 명확히 대비합니다. Dense 1024×1024 = 1,048,576 Weight vs 3×3 동일 Kernel 9 Weight (Stride1, Padding1). 두 아키텍처의 표현 가능 범위는 동일하지 않다고 설명합니다.
- **18번**: Bias를 포함한 순수 Affine Layer 합성 `W₂(W₁x+b₁)+b₂=(W₂W₁)x+(W₂b₁+b₂)`으로 깊은 선형층은 단일 선형층에 흡수될 수 있다고 명확히 합니다.
- **19번**: AND는 `x₁+x₂ > 1.5`인 직선으로 구분되지만 XOR는 (0,1),(1,0)만 1이라 직선 경계로 분리되지 않음을 정확한 2차원 점 그래프로 보여줍니다.
- **20~21번**: ReLU의 `max(0,x)`를 소개하고 두 ReLU `h₁=ReLU(x₁-x₂), h₂=ReLU(x₂-x₁), y=h₁+h₂`가 0/1 입력에서 XOR의 진리표와 일치한다는 사실을 실제 숫자로 검증합니다. 모든 함수를 비선형성만으로 자동 구현한다는 뜻은 아닙니다.
- **26번 Stride**: 5×5 원본과 3×3 중앙 선택 Kernel의 Padding0 계산에서 Stride1→3×3(9개), Stride2→2×2(4개) 정확한 배열을 비교합니다.
- **27번 Padding**: 3×3 데이터와 모든 값이 1인 3×3 Kernel을 사용해 Padding0→1×1 [45], Zero Padding1→3×3 [[12,21,16],[27,45,33],[24,39,28]]을 비교합니다. Zero는 인공적으로 추가되므로 경계값에 영향을 미침을 설명합니다.
- **28번 Max Pooling**: 4×4 수치 Feature Map에 2×2 Max, Stride2를 적용해 2×2 [[6,4],[7,9]]를 산출합니다. 위치 정보 손실, 채널 독립 연산, 학습되지 않는 Max 연산임을 명시합니다.
- 이 수치 예시는 실제 CNN 실측 출력이 아니라 **교육용 계산값**입니다. AI Basics/개별 Vision AI 원본 페이지 및 역사적 SVG/PNG 자산은 유지하되 현재 강의의 참조에서는 제외합니다.
- 신규 스타일 `docs/cnn_numeric_why_logic.css`는 통합 49장에만 적용하고, `docs/lecture_outline.js`, `README.md`, 정적 검증과 브라우저 검증 모두 68장 기준으로 동기화합니다. 전체 136개 viewport의 글자 잘림·과도 축소 여부를 확인합니다.
- 기술 출처: Stanford CS231n <https://cs231n.github.io/convolutional-networks/> · <https://cs231n.github.io/neural-networks-1/>; 슬라이드의 해당 계산 옆에 출처 링크 표시합니다.


## 2026-10-17 · 퍼셉트론 → 비선형성 학습 흐름 / AIBook 기반 시각 정리
- 통합 강의 16~21번은 퍼셉트론 가중합(z=Wx+b)과 고전적 Step 판정 → 여러 Affine Layer의 합성은 단일 Affine과 동등 → AND/XOR의 선형 분리 여부 → ReLU 함수 → ReLU XOR 예시 → 활성화 함수를 포함한 신경망 순서입니다.
- 고전적 Perceptron을 활성화 없는 Wx+b로 정의하지 않습니다. Wx+b는 pre-activation이며 Step은 출력 판정입니다.
- 원문 참고: Euiyun Kim, AIBook '뉴런과 신경망' https://aibook.euiyun.com/chapters/neuron.html ; Stanford CS231n https://cs231n.github.io/neural-networks-1/.
- AIBook에서 개념→핵심 식→간결한 Figure/검산을 잇는 편집 방식을 참고했습니다. 원본 스타일/코드 자산을 복제하지 않고 현재 16:9 강의에 맞춰 로컬 HTML/SVG/CSS로 재구성했습니다.
- 변경 범위: `docs/vision_ai_course.html`의 16~21번, 전용 `docs/neuron_concept_flow.css`, outline/검증 스크립트/문서. 다른 슬라이드와 공통 CSS/JS는 그대로 유지합니다.

## 2026-10-17 · 이미지 출처 표기 기준 (현행)
- 강의 화면에는 외부 이미지를 직접 재사용한 경우에만 출처를 표시합니다. 외부 논문 Figure, 학술자료 원본 이미지, 외부 사진이 해당합니다.
- 공식 문서·논문·블로그의 개념이나 설명만 참고하고 HTML/SVG·숫자 예제를 자체 구성했다면 슬라이드에 참고 문헌을 표시하지 않습니다.
- 외부 이미지 출처 기록은 `assets/SOURCES.md`에 계속 보존하고, 이미지 하단 또는 인접한 위치에서 원본 URL을 안내합니다.
- 16~21번은 외부 이미지를 사용하지 않고 자체 SVG/HTML 수치 그래프를 사용하므로 콘텐츠 참고 링크를 제거했습니다.
- 이번 수정에서는 16번 Step 경계와 실제 z=0.3, 17번 2→3→1 뉴런의 정확한 숫자 전개, 18번 AND/XOR 출력 배열, 19번 직선/ReLU 그래프, 20번 XOR 네 조합, 21번 변환의 차이를 시각화합니다.


## 2026-10-17 · 퍼셉트론 / AND·XOR 시각 설명
- 통합 16번: 입력 노드 → 가중치 연결선 → 가중합 Σ → Step → 출력. 고정 입력 1과 편향 b를 표시하고 AND의 (1,1) 계산을 연결합니다.
- 18번: 같은 좌표의 AND/XOR와 네 입력 진리표. AND 가중치 (0.5,0.5), 편향 -0.7에 맞춰 경계는 x₁+x₂=1.4입니다.
- 20번: NAND와 OR 은닉 뉴런 → AND 출력 뉴런으로 XOR를 구성합니다. 모든 게이트는 Step(z)=1 if z≥0 else 0을 사용합니다. 17번 Affine 합성, 19번 ReLU, 21번 신경망 구조는 보존합니다.
- 참고: WikiDocs https://wikidocs.net/60680 . 원본 이미지를 복사하지 않고 구조를 참고하여 한국어 SVG를 자체 작성했습니다. 원본 이미지 파일은 사용하지 않으므로 강의 화면에는 외부 이미지 출처를 추가하지 않았습니다.
- 신규 자산: perceptron_gate_structure_ko.svg, and_xor_gate_geometry_ko.svg, xor_multilayer_gates_ko.svg. Intro 19장 + 통합 49장 = 전체 68장 유지.


## 2026-10-18 · 두 입력 신경망 / Intro 순서 변경 (최신)
- 통합 17번은 2→3→2→1의 완전 연결 구조입니다. 입력 (1,2), 은닉층 1 (4,0,3), 은닉층 2 (7,11), 합산 출력 18을 표시합니다. 활성화가 없으므로 모든 입력에 대해 단일 Affine y=x₁+7x₂+3과 동등합니다.
- Intro의 기존 13번 '시각 이해 · What과 Where'를 기존 2번 뒤로 이동하여 새 3번으로 표시합니다. 기존 3~12번은 새 4~13번, 14~19번은 그대로입니다. 이전 순번 고정 규칙보다 이번 명시적 순서 변경을 우선합니다.
- Intro 19장 / 통합 49장 / 전체 68장 유지. 목차, 페이지 내 번호, 위치 기반 상호작용 검증, 목차 캐시 버전을 동기화합니다.


## 2026-10-18 · 강의 그림 원본 열기 제거 (현행)
- 모든 강의 페이지(Intro / AI Basics / Vision AI / 통합 강의)에서 그림 클릭 시 원본 파일 또는 새 탭을 여는 링크를 제거합니다. 그림은 강의 안에 정적으로 표시합니다.
- 원본 확대 링크를 추가하라는 이전 지침보다 이번 사용자 요청을 우선합니다. 이미지 출처 텍스트 링크와 강의 내 Pixel 선택·밝기·필터 등의 상호작용은 유지합니다.
- `figure-display` 비링크 컨테이너로 기존 레이아웃을 보존하고 돋보기 커서를 제거합니다. Figure 생성 스크립트도 확대 링크를 생성하지 않습니다.


## 2026-10-18 · Computer Vision의 어려움 보강 (최신)
- 현재 Intro 21장 + 통합 49장 = 전체 70장입니다. 기존 Intro 7·8번 조명/시점 변화 뒤에 새 9번 '다르게 생겨도 같은 종류', 10번 '큰 변화보다 중요한 차이'를 추가합니다. 기존 9~19번은 11~21번입니다. 기존 새 3번 What/Where는 보존합니다.
- 9번은 서로 다른 네 종류의 의자를 같은 클래스 '의자'로 연결하여 클래스 내부 다양성을 보여줍니다. 10번은 검사 기준을 '균열 유무'로 명시하고 조명 변화에는 판정을 유지하면서 작은 균열에는 판정을 바꾸어야 한다는 과제 의존성을 보여줍니다.
- 두 이미지는 ImageGen으로 만든 교육용 개념 예시입니다. 실제 검사 데이터, 동일 원본을 변형한 픽셀 실험, 실제 모델 예측 결과로 표현하지 않습니다. 정확한 생성 프롬프트는 assets/intro_challenges_generation.md에 기록합니다.
- 그림 클릭 원본 열기를 추가하지 않습니다. 목차·번호·전체 장수·상호작용 검증·화면 검사·캐시 버전을 함께 동기화합니다.


## 2026-10-18 · 2시간 원리 중심 강의 (현재 기준)

사용자의 전체 흐름 수정 요청에 따라 예전 슬라이드 수·순서·해시 보존 지침보다 이 항목을 우선합니다.

- 공개 본강의: **Intro 11장 + 통합 35장 = 46장**, 설명 110분 + 질문/복습 10분.
- 사진·Pixel/RGB → Vision의 어려움 → Task/Label → 학습/Loss → 퍼셉트론·선형성·AND/XOR·비선형성 → CNN 연산/구조 → 데이터·평가.
- 강의 수준은 원리 이해와 개념 선택입니다. 직접 학습 코드, 연구용 Feature Visualization, BatchNorm 상세, 3D/센서 확장, Grad-CAM은 본강의에서 제외합니다. 개별 참고 페이지와 자산은 보존합니다.
- 통합 6–12번은 신경망, 13–24번 CNN, 25–35번 데이터/평가입니다. 기존 17번의 두 입력·두 은닉층·합산 출력을 새 7번 큰 구조 그림과 8번 Affine 동등성 전개로 분리합니다.
- 합성곱/Feature Map/Stride는 동일 5×5 입력·3×3 Kernel의 수치를 사용합니다. Padding과 Pooling은 입력을 바꾼 이유를 밝힙니다. 학습 데모와 Loss 설명은 w0.5→1.7, 예측1→3.4, Loss9→0.36으로 통일합니다.
- Intro의 해상도 비교는 동일 960×640 사과의 중앙 960×540 crop을 160×90/320×180/640×360으로 축소합니다. 업샘플링을 원본 정보의 증가로 설명하지 않습니다.
- 화면의 그림 클릭 원본 열기와 돋보기는 계속 금지합니다. 출처 텍스트 링크와 강의 내 상호작용은 유지합니다.
- 본강의 기준: `docs/two_hour_manifest.json`, 운영 설명: `TWO_HOUR_LECTURE_PLAN.md`. 새 검증 `scripts/verify_two_hour_course.py`는 기존 정적 검증에서 함께 실행합니다. 목차·두 viewport(92화면)·상호작용·46장 이동·배포를 확인합니다.


## 2026-10-18 · 검토 반영: Vision AI 기초와 AI 협업 (현재 최우선 구성)

- 공개 본강의는 **Intro11장 + 통합39장 = 50장**, 설명·활동110분 + 복습·질의10분이다. 이전 46장 순서와 장수보다 이 항목을 우선한다.
- Intro는 유지한다. 통합1–6은 Task·모델 선택·학습/추론, 7–10은 신경망/비선형성, 11–21은 CNN 전체→세부, 22–34는 데이터/로그/평가, 35–39는 AI와 첫 프로젝트다.
- Affine 전체 전개2장과 NAND/OR 게이트 조합1장은 본강의에서 제외하고 기존 참고자료/자산을 보존한다. CNN 전체 구조를 Kernel보다 먼저 보여주고 전이학습은 Train/Validation/Test·그룹 분할 뒤에서 설명한다.
- 지도학습의 범위를 명확히 하고 Parameter/Hyperparameter·Batch/Step/Epoch·역전파/Optimizer·Score/확률·불균형·기하 증강의 Label·Train 통계·검출 평가 범위를 보충한다.
- 프로젝트는 같은 사과 결함 분류 사례로 작업 명세→결과 확인→실패 분석→완료 기준을 연결한다. `docs/project_course.js`는 교육용100건 점수의 임계값별 혼동행렬과 지표를 계산하며 실제 모델 성능이나 실제 Test 평가로 소개하지 않는다.
- 그림을 사용하지 않은 자체 HTML/수치 예제에는 외부 개념 출처를 붙이지 않는다. 외부 사진을 포함한 Feature Map/변환 그림의 원본 사진 출처는 유지한다.
- 기준: `docs/two_hour_manifest.json`, `TWO_HOUR_LECTURE_PLAN.md`. 목차·선행 개념·50장 탐색·두 해상도100화면·Threshold 재집계·복습 펼침을 검증한다. 통합 강의 번호는 새 순서다.


## 2026-10-18 · A안 확정: Vision AI 원리 이해 중심 개편 (최신·최우선)

- **최종 강의 목표:** AI 도구를 사용하는 프로젝트 실무보다 **Vision AI 내부 원리 이해**를 우선한다. 수강생이 Pixel → CNN Kernel/Feature Map → Weight 학습 → 데이터/평가의 관계를 직접 설명하게 한다.
- 공개 장수: **Intro 11장 + 통합 39장 = 전체 50장**. 상세 배분과 현재 번호는 `docs/two_hour_manifest.json` 및 `TWO_HOUR_LECTURE_PLAN.md`를 최신 기준으로 사용한다. 예전 번호로 설명한 과거 가이드 내용보다 이 항목을 우선한다.
- **현 통합 순서:** C1–3 Task/모델 선택 → C4–7 퍼셉트론/AND·XOR/ReLU → **C8–17 CNN 구조·연산·실제 반응** → C18–22 데이터 준비 → C23–29 Loss·Weight 학습·추론·전이학습 → C30–34 평가 → C35–39 원리 복습·응용.
- 원리의 선행 관계를 개선하기 위해 **기존 학습/Loss/Inference를 CNN 이후로 이동**했다. 새 CNN 개요는 기존처럼 4개 텍스트 칸이 아닌 **사과 사진 → 입체 Feature Map → 공간 축소/특징 → Task Head**로 시각화한다.
- 텍스트 중심이던 **모델 선택·비선형성·지역 연결/공유·RGB Feature Channel·Dataset·Loss·Batch/Step/Epoch·불균형 Accuracy·종합 과정/실패 사례**는 정확한 자체 HTML/SVG/사진 시각 중심으로 구성한다. 직접 계산한 수치·기존 실습·SqueezeNet 실측 반응은 유지한다.
- 마지막 5장의 목적은 **AI 협업 방법 교육이 아니라 이미 배운 원리를 한 사과 검사 시나리오에 적용·회수**하는 것이다. 발표시간은 약 **6분**, CNN 원리 구간은 약 **30분**으로 조정했다. 본강의 110분 + 질의/복습 10분.
- 공개 슬라이드 공통 구성: **간결한 제목 / 왜 필요한지 알려주는 짧은 부제 / Input→Process→Output 중심 큰 시각 Figure / 결과 한 문장 정리**. 어려운 개념을 쉬운 말로 설명하되 사진·기술 Figure는 전문적으로 유지한다.
- 직접 재사용한 **외부 원본 이미지에만 발표 화면 출처 표시**. 기존 회랑 사진, Stanford CS231n 사진을 포함한 실제 CNN Feature Map/전처리·증강 출처는 유지. 자체 제작 텐서/Kernel 도식과 수치 예제에는 외부 개념 참고 문헌을 장식처럼 붙이지 않는다.
- 신규 범위: `docs/principles_course.css`, `docs/intro.html`, `docs/vision_ai_course.html`, `docs/lecture_outline.js`, `docs/two_hour_manifest.json`. 원본 `docs/ai_basics.html`/`docs/vision_ai.html`은 호환용으로 보존.
- 기존 Click Pixel/RGB/해상도 · Weight 학습 · Threshold 100건 실습을 유지하고, 새 physical slide-number로 Deep Link·브라우저 QA·cache key를 동기화한다.
- 작업 근거: `reviews/2026-10-18_VISION_AI_CONTENT_FLOW_REVIEW.md` 및 `reviews/2026-10-18_VISION_AI_UI_FIGURE_REVIEW.md`.
- **변경 후 필수 검증:** `scripts/verify_two_hour_course.py`, `scripts/verify_curriculum_overhaul.py`, `scripts/verify_learning_routes.py`, `scripts/audit_visual_slides.py`. 코드 정적 검증/로컬 브라우저 확인/실배포 Pages 확인은 서로 다른 완료 조건이다.


## 2026-10-18 · 현재 활성 TODO 및 Markdown 자료 정리

- 최신 미완료 작업은 **`TODO_VISION_AI_LECTURE.md`** 하나에서 관리한다. 각 슬라이드의 실제 `data-concept`와 `docs/two_hour_manifest.json`의 현재 번호를 우선한다.
- `TODO_INTRO_RGB_TENSOR.md`는 기존 파일 자체가 구버전/대체된 작업 지침임을 명시했으며, 현재 사과 Grayscale/RGB 교육 구성과 충돌하므로 제거한다.
- `LECTURE_REVIEW.md`는 46장 이전 상태의 완료된 진단으로, 현재 **50장**의 내용/흐름 및 UI/Figure 검토서와 구현 기록이 대체하므로 제거한다. 옛 기록은 Git 이력에 남는다.
- `REFERENCE_SLIDE_SOURCE_MAP.md`와 `REFERENCE_VISION_AI_SOURCE_LIBRARY.md`는 옛 69장/72장 번호가 포함된 연구·소스 라이브러리다. URL과 Figure 후보의 참고 가치가 있어 **역사적 참고용으로 보존**하며, 현행 구현 지시나 TODO로 사용하지 않는다.
- 완료된 구조 개편(PR #101)과 미검증 사항(실제 브라우저 렌더·상호작용·GitHub Pages 배포 확인)은 [현재 활성 TODO](TODO_VISION_AI_LECTURE.md)에서 구분한다. 코드 정적 QA 통과와 브라우저/배포 실제 성공을 혼동하지 않는다.


## 2026-10-18 · Vision AI 중요성/어려움 · 실무 Task/모델·Label · CNN 학습 Figure (최신)

- 공개 기준: **Intro 13장 + Course 41장 = 총 54장**, 110분 강의 + 질의 10분. 이전 50장 또는 더 과거 슬라이드 번호는 역사적 기록이다. 현재 `docs/two_hour_manifest.json` / `docs/lecture_outline.js` / `TWO_HOUR_LECTURE_PLAN.md`을 기준으로 한다.
- **Intro 3**: 왜 Vision AI가 중요한지 제조 검사/안전·공간 이해/정밀 영역 분석으로 설명; **Intro 9–12**: 같은 사과의 조명·회전·가림/결함 중요성; **Intro 13**: 조건별 Pixel 변화와 공통 의미를 요약하고 Task로 연결.
- Course **1–5**: Task·Label 소개 → 규칙 vs 학습 → 실제 Vision AI 모델 활용 방식(일반 학습 모델, 범용 사전학습) → 기존모델 선택 → 유무/위치/영역/희귀 이상별 Classification·Detection·Segmentation·Anomaly Detection 모델/Label 예시. 모델 계열은 Task 그 자체가 아니며 범용 SAM 2도 산업 불량을 자동 판별한다고 주장하지 않는다.
- Course **6–9** 신경망/비선형성, **10–19** CNN 원리, **20–24** 데이터, **25–31** 학습과 일반화, **32–36** 평가, **37–41** 개념 회수.
- Course **27**: 사과 입력→Kernel/Feature Map→Task Head→Prediction (Forward) → Label/Loss→Gradient→Optimizer→가중치 갱신 (Backward)의 전문적 자체 SVG 큰 Figure. 학습 Weight는 설정에 따라 Freeze될 수 있으며 CNN 외 Transformer 기반 모델도 있음.
- 실습은 Intro Pixel/RGB/해상도, Course25 Weight 업데이트, Course39 Threshold 100건 예제 유지. 기존 SVG/JS/레거시 슬라이드 수정 시 동일 예제·cache key·목차·정적/브라우저/Pages QA 회귀.
- 최신 종합 검토 및 후속 수정 제안: `reviews/2026-10-18_VISION_AI_54_SLIDE_FLOW_REVIEW.md`. 이전 검토서 50장 기준의 번호를 현재 실행 지침으로 사용하지 말 것.


## 2026-10-19 · 최신 55장 도식/순서 (이전 지침보다 우선)

- 공개 2시간 강의: **Intro 13 + Course 42 = 55장**, 본강의 110분 + 질의 10분.
- Course 5 Anomaly Detection 제외. Course 6–10 = 퍼셉트론 → AND → XOR → ReLU → Affine층과 비선형성. Course 11 = 이전 얼룩말 CNN Architecture 원본 Figure(외부 링크, 출처 인접 표기), 접속 실패 시 로컬 자체 CNN 구조 Fallback.
- Course 12 입력 5×5 + Kernel 3×3 → Feature Map 3×3의 전체 수치 대응, Course 13 위치별 반복, Course 14 Weight Sharing, Course 15 Feature Channel, Course 16 Stride, Course 17 동일 3×3 입력 Padding0→1×1 vs Padding1→3×3, Course 18 Pool 사용 이유(공간크기↓·강한 반응 유지/정확 위치 손실).
- Course 24–25 Preprocessing/Augmentation은 슬라이드 안에 복합 슬라이드를 삽입하지 않고 자체 원본 사과 비교용 HTML을 사용. Course 28 CNN Forward/Backward 화살표를 두 줄로 정렬. Course 30 Transfer Learning에서 Feature Extractor Freeze + Classification Head Train 시각 구분.
- Intro 13의 기존 사진이 잘못 보인 이유는 `iv-revision` 적용 CSS 범위 불일치였으며 이를 수정했다. 표시는 동일 원본의 CSS 밝기·회전·가림 시뮬레이션이다.
- 기본 문서: `docs/two_hour_manifest.json`, `TWO_HOUR_LECTURE_PLAN.md`, `reviews/2026-10-19_CNN_SLIDE_REFINEMENT.md`, `TODO_VISION_AI_LECTURE.md`. 페이지 QA/110개 뷰/배포 확인은 별도 완료 판단.


## 2026-10-19 · 최신 인터랙티브 Gate 강의와 120분 운영 (최우선)

- 기존 Intro13+Course42=55장 유지. **Q&A 전용 10분 구간 제거**, `docs/two_hour_manifest.json`의 `teaching_minutes=120`, `discussion_minutes=0`, 9개 구간 합계 120분을 현행 공식 운영안으로 사용.
- Course7 AND에서 Weight w₁, w₂, Bias 슬라이더를 움직이면 결정 직선·네 진리표 결과·정답 개수가 실시간 변화하며 초기화 가능.
- Course8 XOR은 두 층의 Weight6/Bias3 총 9개 슬라이더와 **Step 사용 vs 활성화 없음** 토글이 있어, 활성화 없는 두 선형층은 결국 한 직선으로 합쳐져 XOR를 풀 수 없음을 보여 준다. 기본 Step XOR는 4/4 정답으로 초기화.
- 기존 기타 학습/평가 슬라이드·Sidebar·로컬 네트워크 독립성·공유 CSS cache 및 검증 조건 유지. 새 JS/CSS는 `docs/interactive_gates.js`, `docs/interactive_gates.css`로 독립 관리.


## 2026-10-19 · Course 7–8 최종 단순화: 한 층은 W,b만 (이전 2+9 슬라이더 지침보다 우선)

- **Course 7:** 공통 입력 s=x₁+x₂에 공유 W와 b만 사용하여 `z=W·s+b`. 슬라이더 **2개**로 직선 경계와 AND 판정을 변화시킨다.
- **Course 8:** Layer 1 `t=W₁·(x₁+x₂)+b₁`, Layer 2 `z=W₂·g(t)+b₂`. 두 층 W₁,b₁,W₂,b₂ **총 4개** 슬라이더. 최초 `g(t)=t`(비선형 없음)로 시작해 선형 변환 둘이 하나의 `Wx+b`로 합쳐지는 **직선 하나**를 보여 준다(기본 XOR 3/4).
- 다음 토글 `g(t)=|t|`(비선형 추가): `|t|=ReLU(t)+ReLU(-t)`이며, 그림에서는 **두 경계 사이의 영역**이 XOR를 표현해 4/4가 된다. 두 ReLU 계산을 단순화한 교육용 모델이며 단일 ReLU만으로 XOR를 해결한다는 설명을 금지한다.
- 그래프 점 안 숫자는 **정답 Label**, 옅은 초록 영역은 **AI가 1이라 판단한 영역**, 빨간 테두리는 **AI 판정 오답**; 점 아래 칸에는 각 입력의 정답과 AI 판정을 모두 표시. “출력”만 단독 표기하지 않는다.
- `docs/interactive_gates.js` / `docs/interactive_gates.css` 버전을 `20261019-simplewb-2`로 갱신했고 `docs/two_hour_manifest.json` / `docs/lecture_outline.js` 제목 동기화. 55장·120분 무Q&A 구성 불변.


## 2026-10-19 · Course 7–8 직선 기울기/절편 버그 수정 (가장 최근 기준)

- **원인:** 기존 `z=W(x₁+x₂)+b`의 경계는 `x₂=−x₁−b/W`이므로 W를 바꾸더라도 기울기가 −1 고정이었다. **해결:** C7은 `z=Wx₁+x₂+b`; 경계 `x₂=−Wx₁−b`. 따라서 W는 기울기(−W), b는 y절편(−b) 조절. 초기값 W1.0,b−1.2로 AND 4/4 유지.
- **C8 선형:** Layer1 `t=W₁x₁+x₂+b₁`; Layer2 `z=W₂t+x₁+b₂`. Layer2의 `+x₁`은 고정(조절 파라미터 없음) 연결임을 슬라이드에 명시. 최종 선형 식 `z=(1+W₁W₂)x₁+W₂x₂+W₂b₁+b₂`이라 W₁, W₂ 둘 다 기울기에 영향. 초기 W₁1,b₁−1,W₂−2,b₂0.5로 선형 XOR 3/4.
- **C8 비선형:** `z=W₂|t|+x₁+b₂`, `|t|=ReLU(t)+ReLU(−t)`. 각 절댓값 분기의 결정선을 실제 분기 입력 영역에 잘라서 그림에 표시. 초기 XOR 4/4.
- 테스트: 실제 경계 선분 양 끝 좌표로 W 변화 시 기울기 변화, b 변화 시 기울기 유지 확인. 최신 JS/CSS cache `20261019-rotate-w-3`. 55장·120분 강의 유지.

## 2026-10-19 · 얼룩말 특징 조합과 전이학습 (최신)

- Intro13 + Course43 = 56장, 120분 강의 유지. C11 Architecture 뒤 C12 `cnn-why`를 추가하고 이후 Course 번호를 하나씩 이동한다.
- C12는 작은 경계/줄무늬 → 형태·부분 배치 조합 → 분류를 설명하는 자체 SVG 개념도다. 사람도 전체 형태와 맥락을 함께 보며, CNN과 사람의 시각을 동일한 작동으로 설명하지 않는다.
- C31 전이학습에서 C11의 외부 얼룩말 아키텍처 원본과 출처를 재사용하고 특징 추출부 Freeze / Head 교체·학습을 연결한다. 원본 로딩 실패 시 기존 로컬 도식을 표시하고 외부 이미지 출처 대신 대체 안내를 표시한다.
- 현행 목차·manifest·시간표·검증은 56장 및 두 해상도 112화면을 기준으로 한다. 기존 AND/XOR 상호작용은 보존한다.

## 2026-10-19 · C12 사진형 시각 설명 (최신)

- 사용자 요청으로 C12의 “설명용 개념도입니다” 및 “뇌의 작동을 그대로 재현한 모델이 아닙니다” 문구를 제거한다. 시각 정보를 얻는 흐름과 유사하다는 긍정적인 설명을 사용한다.
- 직접 생성한 사진형 얼룩말 한 장의 줄무늬/목·머리/전체를 확대해 특징 조합을 보여준다. 생성 이력은 assets/SOURCES.md에 보존한다.
- 계산량의 비교 기준은 모든 Pixel을 각 뉴런에 완전 연결하는 방식이다. CNN의 지역 연결·Kernel 공유가 가중치와 연산 부담을 줄인다고 설명하며, CNN이 입력 Pixel 일부를 아예 읽지 않는다고 설명하지 않는다.

## 2026-10-19 · AND/XOR 동작 설명 선행 2장 (가장 최신 기준)

- 현행 강의: **Intro 13 + Course 45 = 총 58장**, 120분 강의, 별도 Q&A 없음. `docs/two_hour_manifest.json` / `docs/lecture_outline.js`가 번호·시간의 단일 기준.
- Course **6**는 AND Gate 논리 규칙(00→0, 01→0, 10→0, 11→1)의 **네 가지 스위치 입력 그림**. AND는 논리 기능, 단일 Step 퍼셉트론은 이를 구현하는 가장 간단한 인공 뉴런이라는 구분을 명확히 한다.
- Course **7**은 그 AND 규칙을 Weight·Bias·가중합 Wx+b·Step으로 계산하는 **퍼셉트론 설명**. Course **8**은 W·b 슬라이더로 직선을 움직이는 AND 실습.
- Course **9**는 XOR Gate(00→0, 01→1, 10→1, 11→0)를 AND와 **동일한 시각 템플릿**으로 설명. Course **10**은 선형 여러 층이라도 하나의 직선인 한계와 비선형성을 인터랙티브로 비교. C11 ReLU, C12 Affine, C13 CNN Architecture로 연결.
- 각 새 장은 하나의 메시지·큰 네 가지 입력 그림·짧은 Takeaway, 이미지 외부 CDN 없이 `docs/gate_basics.css`의 로컬 스타일을 사용. 강의 내용에서 Gate 규칙과 모델 구현을 동일 개념으로 혼동하지 않는다.
- 이후 최신 번호: C13–23 CNN, C24–28 데이터, C29–35 학습, C36–40 평가, C41–45 복습. 두 화면 58×2=116뷰 QA/실제 Pages 반영 확인 필요. **이전 55장/56장 숫자와 C7·C8 Gate Interactive 번호는 이력임.**


## 2026-10-19 · 최신 퍼셉트론 수식/슬라이드 순서 (기존 이력보다 우선)

- **현행 58장·120분**에서 C6 퍼셉트론 → C7 AND 논리 규칙 → C8 AND Weight/Bias 실습 → C9 XOR 논리 규칙 → C10 XOR 두 층/비선형 실습.
- **한 뉴런과 Weight 개수는 다르다.** 입력 x₁,x₂가 들어오는 뉴런 하나의 일반식은 z=w₁x₁+w₂x₂+b. w₂는 두 번째 뉴런이 아니라 x₂ 입력 연결 Weight.
- **AND 특수식** z=w(x₁+x₂)+b는 w₁=w₂=w라는 제약 조건에만 적용. 사용자가 요청한 w₁(x₁+x₂)+b₁은 Weight를 첫 층의 공유 매개변수로 명명했을 때 같은 특별한 경우이며 일반적인 퍼셉트론 공식과 구분한다.
- 이 특수식만 사용하면 경계 기울기가 −1로 고정되어 W만으로 회전할 수 없다. C8은 의도적으로 x₂ Weight=1을 고정한 z=Wx₁+x₂+b로 W를 바꿔 회전시키는 **서로 다른 AND 파라미터 예시**임을 표기한다.
- C10은 Layer1 t=W₁x₁+1·x₂+b₁, Layer2 z=W₂g(t)+1·x₁+b₂이고 추가 입력선 계수는 1로 고정한다. W₁,W₂는 층별 조절 Weight 이름일 뿐, 층마다 실제 연결 하나만 있다는 뜻은 아니다.
- `docs/perceptron_weights_clarity.css?v=weights-20261019-1` 추가. `docs/lecture_outline.js?v=perceptron-weights-20261019-1` 캐시 동기화. 116뷰 브라우저 QA 및 배포 실화면 검증 필요.


## 2026-10-19 · 최신 Course6 W/b 교육용 단순식 및 CNN 지도/비지도 (최상위 기준)

- 현행 강의: **Intro13 + Course46 = 59장**, 120분 강의, Q&A 별도 시간 없음. `docs/two_hour_manifest.json` 기준 최신 Course 34에 **`cnn-learning-paths`** 신규 삽입.
- **Course 6:** 본문·그림에 W(가중치) 한 개, b(편향) 한 개만 표시한 `z=W(x₁+x₂)+b`. 스칼라 W를 두 입력에 동일하게 적용하는 특별한 퍼셉트론 예시이므로 '뉴런 하나면 모든 입력 연결 Weight도 한 개뿐'이라는 일반 주장 금지. 예시 이미지 `docs/assets/lesson/perceptron_one_weight_ko.svg` 사용. 과거 일반형 병기 및 옛 퍼셉트론 그림은 C6에서 더 이상 표시하지 않음.
- **C7 AND:** W=0.5,b=−0.7 → Step으로 AND 네 사례. **C8 기울기 실습:** x₂ Weight=1로 고정하고 W·b를 조절하는 별개 단일 뉴런 설정이며, W 공유 예시와 혼동하지 않는다.
- **C34:** 같은 사전학습 CNN Feature Extractor를 Freeze한 예시로 `Feature 벡터→정답 Label 있는 Classification Head 학습(지도) / Label 없는 Clustering(K-means, 비지도)`을 두 갈래 그림으로 설명. 그룹 A/B는 의미가 없는 발견된 군집이며 자동 정상/불량 판정이 아님.
- 주의: 지도/비지도는 **분류 Head만 교체하면 변하는 속성**이 아니라 **Label과 학습 목표**의 구분이다. 고정 Backbone이 과거 Label로 지도 사전학습됐을 수도 있으므로 C34의 비지도는 Feature를 활용한 **후단 군집화 단계**를 뜻한다. CNN 추출기 자체 학습은 지도/자기지도 등 별도 방식 가능.
- 새 로컬 CSS: `docs/supervised_unsupervised_cnn.css?v=cnn-paths-20261019-1`; W/b 도식 CSS `docs/perceptron_weights_clarity.css?v=one-w-20261019-2`; 공유 TOC cache `cnn-paths-20261019-1`. 59장×2뷰=118 브라우저 시각 QA 필요.
