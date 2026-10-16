# Vision AI Lecture — Project Guide

Vision AI를 처음 접하는 사람을 대상으로 하는 입문 강의자료 제작 프로젝트입니다.

## Links

- GitHub Repository: https://github.com/sh0427-han/vision_ai_lecture
- GitHub Pages: https://sh0427-han.github.io/vision_ai_lecture/

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
