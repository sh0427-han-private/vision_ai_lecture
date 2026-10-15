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
