# Vision AI Study & Lecture

## 🌐 배포 사이트

강의용 웹 슬라이드는 아래 GitHub Pages에서 바로 확인할 수 있습니다.

**https://sh0427-han.github.io/vision_ai_lecture/**



Vision AI를 처음 접하는 사람도 **사진 → Pixel·RGB → Vision의 어려움 → Task → 학습·신경망 → CNN → 데이터·평가** 순서로 이해할 수 있도록 만든 완전 기초 강의 자료입니다.

이 저장소는 세 가지를 함께 목표로 합니다.

1. **학습 노트** — 개념을 쉬운 말과 수치 예제로 정리
2. **강의 자료** — 한 슬라이드에 한 메시지, 그림과 비교 중심으로 설명
3. **실습 자료** — Notebook과 웹 데모로 개념을 직접 확인

## 강의 바로 시작하기

- **[Intro 처음부터 보기](https://sh0427-han.github.io/vision_ai_lecture/)**
- **[통합 Vision AI 바로 보기](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html)**
- **[퍼셉트론·신경망 7–10번](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-7)** · **[CNN 구조·계산 11–21번](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-11)** · **[데이터·평가 22–34번](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-22)**
- **[2시간 강의 운영안](TWO_HOUR_LECTURE_PLAN.md)**

> 배포 URL 주의: 저장소 파일은 `docs/vision_ai_course.html`이지만 GitHub Pages는 `docs/` 디렉터리 자체를 웹사이트의 루트로 게시합니다. 따라서 공개 링크에는 `/docs/`를 넣으면 안 됩니다. 과거에 공유된 `/docs/vision_ai_course.html#slide-N` 링크는 자동으로 올바른 경로로 이동하도록 호환 페이지를 제공합니다.



**[Vision AI Lecture · Intro 1번부터 보기](https://sh0427-han.github.io/vision_ai_lecture/)**

사이트 주소를 열면 Intro 첫 슬라이드부터 **11장 + 통합 39장 = 50장**을 순서대로 봅니다. 원리 설명·AI 협업 활동 110분과 질문·복습 10분으로 구성합니다. Task·모델 선택·데이터·평가를 이해하고, AI에 작업을 요청한 뒤 결과와 오류를 직접 확인하는 것이 목표입니다.

왼쪽 상단의 **☰ 강의 목차**를 클릭하면 50개 슬라이드가 주제별로 표시되어 원하는 장으로 바로 이동할 수 있습니다. 목차 버튼을 다시 누르거나 **✕ 닫기**, 패널 바깥 클릭, **Esc** 키로 목차를 숨길 수 있습니다.

## 강의 슬라이드 안에서 직접 확인하는 Interactive Figure

통합 강의 4번 **모델 학습 · 오차를 줄이는 반복**에서는 '한 단계 학습' 또는 '자동 학습' 버튼을 누르면 모델이 예측 오차에 따라 가중치를 갱신하고 정답에 접근하는 장면을 볼 수 있습니다. 가중치를 직접 수정하는 입력창은 사용하지 않습니다.

CNN은 동일 수치 입력을 Kernel → Feature Map → Stride까지 연결합니다. Mean·Gaussian·Sobel 세부 연산은 본강의에서 다루지 않습니다.

**실습은 별도 페이지가 아니라 기존 강의 슬라이드 안에 배치됩니다.** Intro 1번부터 넘기면 Vision AI 과제를 먼저 살펴보고, 해당 개념에 필요한 AI 원리를 그 자리에서 배웁니다.

## 학습 순서

공개 강의 순서는 사진·숫자 → Vision의 어려움 → Task와 학습 → 신경망·비선형성 → CNN → 데이터·평가입니다. 아래 세 폴더는 주제별 참고 노트이며 공개 발표 순서와 구분합니다.

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

정적 강의 사이트는 [Intro 1번](https://sh0427-han.github.io/vision_ai_lecture/)에서 바로 시작합니다. Intro 11장 → [통합 Vision AI 강의 39장](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html), 총 50장입니다. 기존 [AI Basics](docs/ai_basics.html) 및 [Vision AI](docs/vision_ai.html) 개별 슬라이드는 이전 직접 링크의 호환성을 위해 원본으로 유지합니다.

디자인은 **흰색 배경, 한 화면 한 슬라이드, 최소한의 포인트 컬러**를 기본으로 합니다.


### 원리에서 AI와 첫 프로젝트까지

- 통합 3번: 기존 모델·API·규칙 기반으로 먼저 시험할 방법 선택
- 통합 7–10번: 퍼셉트론·직선의 한계·ReLU, 상세 수식 전개는 참고로 분리
- 통합 11–21번: 전체 CNN 구조 → 동일 수치의 Kernel/Feature Map → 실제 내부 반응
- 통합 22–34번: 데이터 독립성·전이학습·학습 로그·전처리·불균형·임계값·평가
- 통합 35–39번: 작업 명세 → 저장 점수 재집계 → 실패 분석 → 완료 기준

[AI와 첫 프로젝트 구간](https://sh0427-han.github.io/vision_ai_lecture/vision_ai_course.html#slide-35)의 임계값 연습은 교육용 저장 점수100건을 직접 계산합니다. 실제 모델이나 외부 AI API의 실행 결과가 아닙니다. 실제 SqueezeNet Feature Map, 강아지 사진 전처리·증강 계산은 해당 모델/사진의 조건과 출처를 명시합니다.

현재 순서와120분 운영은 [강의 운영안](TWO_HOUR_LECTURE_PLAN.md), 재편 전 진단은 [검토 보고서](LECTURE_REVIEW.md)를 참고합니다.
