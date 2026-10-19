# Vision AI Study & Lecture

## 🌐 배포 사이트

강의용 웹 슬라이드는 아래 GitHub Pages에서 바로 확인할 수 있습니다.

**https://sh0427-han.github.io/vision_ai_lecture/**



Vision AI를 처음 접하는 사람도 **필요성 → Pixel·RGB → Vision의 어려움 → 현재 Vision AI → Task·모델·Label 선택 → CNN → 학습 → 평가** 순서로 이해할 수 있도록 만든 완전 기초 강의 자료입니다.

이 저장소는 세 가지를 함께 목표로 합니다.

1. **학습 노트** — 개념을 쉬운 말과 수치 예제로 정리
2. **강의 자료** — 한 슬라이드에 한 메시지, 그림과 비교 중심으로 설명
3. **실습 자료** — Notebook과 웹 데모로 개념을 직접 확인

## 강의 바로 시작하기

- **[Intro 처음부터 보기](https://sh0427-han.github.io/vision_ai_lecture/)**
- **[통합 Vision AI 바로 보기](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html)**
- **[왜 필요한가 · Intro 3번](https://sh0427-han.github.io/vision_ai_lecture/intro.html#slide-3)** · **[왜 어려운가 · Intro 13번](https://sh0427-han.github.io/vision_ai_lecture/intro.html#slide-13)** · **[현재 모델 · Course 3번](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-3)** · **[과제별 모델·Label · Course 5번](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-5)** · **[CNN 원리 · Course 13–23번](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-13)** · **[CNN 학습 구조 · Course 31번](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-31)**
- **[2시간 강의 운영안](TWO_HOUR_LECTURE_PLAN.md)**
- **[남은 작업 · 현재 활성 TODO](TODO_VISION_AI_LECTURE.md)** — P0/P1 슬라이드별 수정 사양 및 실제 브라우저/배포 검증

> 배포 URL 주의: 저장소 파일은 `docs/vision_ai_course.html`이지만 GitHub Pages는 `docs/` 디렉터리 자체를 웹사이트의 루트로 게시합니다. 따라서 공개 링크에는 `/docs/`를 넣으면 안 됩니다. 과거에 공유된 `/docs/vision_ai_course.html#slide-N` 링크는 자동으로 올바른 경로로 이동하도록 호환 페이지를 제공합니다.



**[Vision AI Lecture · Intro 1번부터 보기](https://sh0427-han.github.io/vision_ai_lecture/)**

사이트 주소를 열면 Intro 첫 슬라이드부터 **13장 + 통합 45장 = 58장**을 순서대로 봅니다. Vision AI의 원리를 이해하는 **별도 질의응답 없이 120분 전체 강의**로 구성합니다. 핵심 목표는 **Pixel 숫자 → CNN 특징 추출 → 가중치 학습 → 새 사진 평가**를 학생 자신의 말로 설명하는 것입니다.

왼쪽 상단의 **☰ 강의 목차**를 클릭하면 58개 슬라이드가 주제별로 표시되어 원하는 장으로 바로 이동할 수 있습니다. 목차 버튼을 다시 누르거나 **✕ 닫기**, 패널 바깥 클릭, **Esc** 키로 목차를 숨길 수 있습니다.

## 강의 슬라이드 안에서 직접 확인하는 Interactive Figure

통합 강의 29번 **모델 학습 · 오차를 줄이는 반복**에서는 '한 단계 학습' 또는 '자동 학습' 버튼을 누르면 모델이 예측 오차에 따라 가중치를 갱신하고 정답에 접근하는 장면을 볼 수 있습니다. 가중치를 직접 수정하는 입력창은 사용하지 않습니다.

CNN은 동일 수치 입력을 Kernel → Feature Map → Stride까지 연결합니다. Mean·Gaussian·Sobel 세부 연산은 본강의에서 다루지 않습니다.

**실습은 별도 페이지가 아니라 기존 강의 슬라이드 안에 배치됩니다.** Intro 1번부터 넘기면 Vision AI 과제를 먼저 살펴보고, 해당 개념에 필요한 AI 원리를 그 자리에서 배웁니다.

## 학습 순서

공개 강의 순서는 Vision AI 필요성 → Pixel·숫자 → Vision의 어려움 → Task·모델·Label 선택 → 신경망·비선형성 → CNN → 데이터 준비 → 학습 → 평가 → 원리 복습입니다. 아래 세 폴더는 주제별 참고 노트이며 공개 발표 순서와 구분합니다.

| 순서 | 챕터 | 핵심 질문 |
|---|---|---|
| 1 | [Vision AI 입문](lectures/01_intro/README.md) | 컴퓨터는 현실 세계를 어떤 데이터로 보는가? |
| 2 | [AI 기초](lectures/02_ai_basics/README.md) | 신경망은 왜 비선형성이 필요하고 어떻게 학습하는가? |
| 3 | [Vision AI](lectures/03_vision_ai/README.md) | 어떤 Vision Task를 선택하고 CNN은 이미지를 어떻게 특징으로 바꾸는가? |

## 설명 방식

별도 용어집을 외우게 하지 않습니다. 각 챕터에서 처음 등장하는 용어를 바로 설명합니다.

```text
Vision AI
 ├─ Classification / Detection / Segmentation
 └─ CNN
     ├─ 사람이 특징을 보고 판단한다는 직관
     ├─ Kernel / Convolution
     ├─ Feature Map / Channel
     └─ Receptive Field
```

## CNN을 이해하는 핵심 직관

사람은 사물을 볼 때 단순히 모든 Pixel 값을 통째로 비교하지 않습니다.

예를 들어 사과를 볼 때:

```text
색
+ 둥근 형태
+ 꼭지
+ 표면 질감
        ↓
"사과 같다"
```

라고 여러 특징을 종합해 판단합니다.

CNN도 교육적인 관점에서는 비슷하게 이해할 수 있습니다.

```text
Pixel
 ↓
Edge / Texture
 ↓
Shape
 ↓
Object Part
 ↓
Object-level Feature
```

단, 이 비유는 이해를 돕기 위한 것이며 **인간의 시각 처리 메커니즘과 CNN의 계산 구조가 실제로 동일하다는 뜻은 아닙니다.**

## 저장소 구조

```text
vision_ai_lecture/
├── README.md
├── lectures/
│   ├── 01_intro/
│   ├── 02_ai_basics/
│   └── 03_vision_ai/
├── assets/
│   ├── diagrams/
│   └── SOURCES.md
├── notebooks/
├── demos/
└── docs/
```

## 작업 가이드

강의자료를 수정하거나 AI coding agent를 사용할 때는 다음 문서를 우선 확인합니다.

- [PROJECT_GUIDE.md](PROJECT_GUIDE.md) — 강의 범위, 교육 흐름, 프로젝트 전체 원칙
- [CHATGPT_PROJECT_INSTRUCTIONS.md](CHATGPT_PROJECT_INSTRUCTIONS.md) — ChatGPT 프로젝트 개인용 지침
- [HTML_DESIGN_RULES.md](HTML_DESIGN_RULES.md) — HTML 슬라이드의 시각/레이아웃/구현/검증 기준
- [AGENTS.md](AGENTS.md) — AI coding agent용 핵심 작업 규칙

## 작성 원칙

- 수식보다 먼저 **입력 → 처리 → 출력** 흐름을 설명합니다.
- 핵심 개념에는 가능한 한 **수치 예시**를 붙입니다.
- 용어는 별도 목록보다 **실제 맥락 안에서 바로 설명**합니다.
- 인간의 직관과 비교할 때는 교육적 비유와 실제 메커니즘을 구분합니다.
- 모델 구조뿐 아니라 **Dataset, 평가, 운영 환경**까지 함께 설명합니다.

## Web Lecture

정적 강의 사이트는 [Intro 1번](https://sh0427-han.github.io/vision_ai_lecture/)에서 바로 시작합니다. Intro 13장 → [통합 Vision AI 강의 45장](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html), 총 58장입니다. 기존 [AI Basics](docs/ai_basics.html) 및 [Vision AI](docs/vision_ai.html) 개별 슬라이드는 이전 직접 링크의 호환성을 위해 원본으로 유지합니다.

디자인은 **흰색 배경, 한 화면 한 슬라이드, 최소한의 포인트 컬러**를 기본으로 합니다.


### 원리 중심 강의 학습 경로

- Intro 1–8: 사과 결함 문제 → 인간의 장면 이해 → 활용 필요성 → Pixel/RGB/해상도
- Intro 9–13: 조명·회전·가림·품종 차이 → 의미와 Pixel 변화의 차이
- 통합 1–5: Class/Box/Mask, 현재 Vision AI, 규칙 vs 학습, 기존 모델, Classification/Detection/Segmentation별 Label·데이터 선택
- 통합 6–12: 퍼셉트론의 1뉴런·입력별 Weight → AND 규칙·직선 실습 → XOR 규칙·비선형 실습 → ReLU
- **통합 13–23: CNN 전체 Architecture → Kernel/Feature Map → Weight Sharing·Channel·Stride·Padding·Pooling → 실제 Feature Map·Task Head**
- 통합 24–28: 데이터·독립 분할·전처리·증강
- 통합 29–35: 가중치 학습 실습·Loss·추론·**CNN 학습 구조**·전이학습·과적합
- 통합 36–40: Threshold·혼동행렬·불균형·Precision/Recall·IoU
- 통합 41–45: 공통 사과 사진으로 원리·검증 과정 복습

[임계값·오류 확인 실습](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-43)의 임계값 연습은 교육용 저장 점수100건을 직접 계산합니다. 실제 모델이나 외부 AI API의 실행 결과가 아닙니다. 실제 SqueezeNet Feature Map, 강아지 사진 전처리·증강 계산은 해당 모델/사진의 조건과 출처를 명시합니다.

현재 공개 강의의 순서·120분 운영은 [강의 운영안](TWO_HOUR_LECTURE_PLAN.md), 미완료 작업과 QA는 [활성 TODO](TODO_VISION_AI_LECTURE.md)를 기준으로 합니다. 상세 진단은 [기존 50장 내용 검토](reviews/2026-10-18_VISION_AI_CONTENT_FLOW_REVIEW.md)와 [기존 50장 UI·Figure 검토](reviews/2026-10-18_VISION_AI_UI_FIGURE_REVIEW.md), 최근 반영 내역은 [구현 기록](reviews/2026-10-18_VISION_AI_PRINCIPLES_IMPLEMENTATION.md)을 참고하세요. 과거 Figure 매핑은 현재 슬라이드 번호가 아닌 참고용 이력입니다.


## 이전 54장 내용·흐름 재검토 기록

2026-10-18 추가 요청(왜 필요한가/어려운가, 현재 활용 모델과 Task·데이터 구성, CNN 학습 구조) 반영 현황 및 후속 개선 권고는 [54장 내용·흐름 전수 재검토서](reviews/2026-10-18_VISION_AI_54_SLIDE_FLOW_REVIEW.md)를 참고합니다. **과거 50장 링크의 고정 슬라이드 번호는 현재 강의와 다릅니다.**


## 2026-10-19 · CNN·퍼셉트론 강의 그림 보완

현재 58장 순서에서 퍼셉트론은 Course 6, AND 규칙은 Course 7, AND 실습은 Course 8, XOR 규칙은 Course 9, XOR 실습은 Course 10, CNN 구조는 Course 13, Kernel은 Course 15, Padding은 Course 20, Max Pooling은 Course 21, 학습 구조는 Course 31, 전이학습은 Course 33입니다. 얼룩말 CNN Architecture 원본은 이미지 출처 표기 및 로컬 대체 그림과 함께 제공합니다. [수정·검증 기록](reviews/2026-10-19_CNN_SLIDE_REFINEMENT.md)을 참조하세요.


## 2026-10-19 · AND/XOR Gate 실시간 실습

- [Course 8 AND Gate](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-8): W와 Bias 슬라이더 2개로 기울기(−W)와 y절편(−b)을 각각 변경합니다. W를 움직이면 결정 직선이 회전합니다.
- [Course 10 XOR Gate](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-10): Layer 1의 W₁·b₁, Layer 2의 W₂·b₂, 총 4개 슬라이더로 최종 선형 경계의 기울기·절편을 조절합니다. 이 예제의 Layer 2에는 원래 입력 x₁을 더하는 고정 연결이 포함됩니다. **비선형 없음(3/4) → 비선형 추가(4/4)**를 비교합니다. 비선형 |t|는 두 ReLU 반응의 합으로 구현할 수 있습니다.
- **강의 시간은 총 120분**이며 별도 질의응답/Q&A 시간은 없습니다. 강의 일정은 [운영안](TWO_HOUR_LECTURE_PLAN.md)을 따릅니다.


## 2026-10-19 · AND와 XOR의 동작 원리 먼저 학습

- [Course 6 · 퍼셉트론](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-6): 뉴런 1개에도 입력마다 Weight가 붙습니다. 일반형 z=w₁x₁+w₂x₂+b, AND의 동일 가중치 예시 z=w(x₁+x₂)+b를 구분합니다. [Course 7 · AND 동작](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-7)에서는 두 입력이 모두 1일 때만 1이라는 규칙을 확인합니다.
- [Course 9 · XOR 동작 규칙](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-9): 두 입력이 다를 때만 1. Course 10에서 선형층의 단일 직선 한계와 비선형성 비교.
- 최신 강의: **Intro 13 + Course 45 = 총 58장**, 120분 전체 강의. 외부 이미지 없이 자체 HTML/CSS 도식으로 4가지 입력 조합을 설명합니다.


## 2026-10-19 · 퍼셉트론 입력선과 뉴런 수 구분 (최신)

- Course 6 퍼셉트론 → Course 7 AND 규칙 → Course 8 AND 직선 실습 → Course 9 XOR 규칙 → Course 10 XOR 선형·비선형 실습.
- 퍼셉트론 뉴런 1개에 입력 x₁,x₂는 각각 Weight w₁,w₂를 갖습니다. w₁,w₂는 뉴런 두 개를 뜻하지 않습니다.
- AND 특별 예시에서 w₁=w₂=w로 묶으면 z=w(x₁+x₂)+b입니다. 이 경우 W만 바꿔서는 직선 기울기가 회전하지 않습니다.
- Course 8은 회전을 보여주기 위해 x₂ Weight=1로 고정한 z=Wx₁+1·x₂+b를 사용합니다. Course 10도 일부 입력선의 Weight=1 고정, 층마다 조절하는 W·b만 표시합니다.
