# FINAL SLIDE ORDER AUDIT — Approved 55 / 120분

> 작성: 2026-10-19 (Asia/Seoul) · **독립 Reviewer 순서·내용 정적 전수 검수**  
> 대상 저장소: [sh0427-han-private/vision_ai_lecture](https://github.com/sh0427-han-private/vision_ai_lecture)  
> **고정 대상**: `automation/approved-55-20261019` @ [`90bf3767b33199f9833c07970007f8df795ac976`](https://github.com/sh0427-han-private/vision_ai_lecture/commit/90bf3767b33199f9833c07970007f8df795ac976)  
> 현재 `main`: [`23d48aeeb9124edcbffa3662c63cd7cf34f80315`](https://github.com/sh0427-han-private/vision_ai_lecture/commit/23d48aeeb9124edcbffa3662c63cd7cf34f80315)  
> 보고서 작업 브랜치: `review/final-slide-order-audit-20261019`. HTML/CSS/JS/이미지는 변경하지 않음. `main` Merge 없음.

## 1. 판정

**슬라이드 배치 순서: PASS (정적 55/55). 통합 운영·독립 화면 검증까지 포함한 판정: CONDITIONAL PASS.**

- 승인 원본 `planning/SLIDE_STORYBOARD.md`의 `#### P01`~`#### P55`와 `planning/approved55.json`의 55개 계획 Concept 순서가 일치.
- `docs/intro.html`의 `section.slide` **13개**, `docs/vision_ai_course.html`의 **42개**를 문서 DOM 등장 순서대로 합치면 `P01`~`P55`와 **55/55 동일**. **순서를 고쳐야 할 이동 대상 없음**.
- `docs/two_hour_manifest.json`과 `docs/lecture_outline.js`의 55개 Concept/전역번호/로컬번호/파일 경로 역시 DOM·계획과 **55/55 동일**. 8개 단원, 승인 `minutes` 총합 120분. `manifest.duration_minutes=120`, `outline.version=manifest.version=approved55-20261019-1`.
- 본문의 `h2`·실제 설명 문장·Figure에 나타나는 예제와 매체를 55장 모두 개별 대조. **계획된 개념이 다른 위치로 밀려 나타난 사례는 정적 검사 범위에서 없음.** 단, 이미지의 실제 렌더 크기·픽셀 정렬·보이지 않는 Canvas의 완성 화면을 자체 Chromium으로 재관찰한 것은 아님.
- 9개 계획 제목(P01/P05/P06/P07/P08/P09/P10/P11/P17)은 HTML 제목에서 의도적으로 짧거나 다른 질문형으로 쓰였으나, 본문 내용·Figure·순서가 일치해 **순서 Issue가 아님**. 강의용 제목의 문자 단위 일치가 필수라면 Builder가 별도 표현 통일 여부를 결정할 수 있음.
- `main`은 2026-10-19에 PR #117로 이미 작업 브랜치를 병합한 상태. `main...automation/approved-55-20261019` 비교는 **작업 브랜치가 1 Commit 뒤, ahead 0, 변경 파일 0**. 본 검수에서 병합하지 않음.

**해석 주의:** 55장은 하나의 HTML 파일이 아니라 **Intro 13장 → Course 42장**의 두 연속 Deck. 사이트 루트 `docs/index.html`은 `intro.html#slide-1`로 이동하도록 작성되어 있다. 따라서 `vision_ai_course.html`만 열어 보면 P14부터 시작하는 것이 정상이며, 그것만 보고 P01~P13이 빠졌다거나 기존 순서라고 판정하면 안 된다.

## 2. 검수 방법과 증거 수준

| 구분 | 확인한 내용 | 상태 |
| --- | --- | --- |
| 계획 순서 | 스토리보드의 P01~P55 Heading/교육 목표, approved55.json의 Concept/제목/시간 | **검증 완료** |
| HTML 실제 순서 | Intro 13 + Course 42개의 `section.slide[data-concept]` 등장 순서 및 각 실제 `h2`/본문/매체 마크업 | **검증 완료(정적)** |
| Manifest | `decks.intro` + `decks.vision_ai_course` 55개 순서 및 Concept | **검증 완료** |
| Outline/목차 | `lecture_outline.js`의 8개 Group, 전역/로컬 번호/페이지, `lecture_sidebar.js`의 href 생성 | **검증 완료(코드)** |
| 이전/다음/딥링크 | `slide.js`의 DOM 순서 인덱스, `data-prev-page`/`data-next-page`, `#slide-N`, `#slide-last`, 키보드 분기 | **검증 완료(코드)** |
| 실제 110화면 렌더 | 기존 GitHub Actions `39251750943` 로그: `VISUAL_AUDIT_OVERVIEW {"rendered":110,"issue_records":0,...}`, 1920×1080 및 1366×768 | **CI 증거 확인 / Reviewer 독립 렌더 NOT VERIFIED** |
| 사용자 공개 GitHub Pages | `main` @ `23d48ae...`의 Pages 배포 작업 `39251750940` 성공 및 `pages build and deployment` `39251750965` 성공 | **배포 CI 검증 / 공개 HTTP 실화면 NOT VERIFIED** |
| 실제 강의 발표 | P01→P55 구두 설명 리허설, 120분 실측 | **NOT VERIFIED** |

재현 근거: [Actions: Full visual QA](https://github.com/sh0427-han-private/vision_ai_lecture/actions/runs/39251750943) / [Pages 배포](https://github.com/sh0427-han-private/vision_ai_lecture/actions/runs/39251750940). 2026-10-19 CI의 `visual-audit-56-slides`라는 artifact 이름은 **과거 명칭**이다. 해당 Job 로그의 실제 `rendered=110`이 올바른 수량 증거다. 동일 로그에서 강의 탐색 검사 `TWO_HOUR_NAV_QA_PASSED: 55 slides`도 확인했다. **기존 CI 성공을 이번 Reviewer가 새 브라우저에서 실행한 시험이라고 표현하지 않는다.**

공개 웹 URL `https://sh0427-han-private.github.io/vision_ai_lecture/` 및 `/vision_ai_course.html`을 직접 읽으려는 요청은 현 도구 환경에서 실패했다. 따라서 **공개 Pages가 구버전이라는 주장도, 현재 URL이 반드시 최신을 서빙한다는 주장도 직접 확정하지 않는다.** 다만 최신 `main` SHA의 성공적 GitHub Pages 배포는 구버전 가설에 반하는 강한 간접 증거다. 캐시·주소 혼용·브라우저 강제 새로고침은 후속 현장 확인 필요.

## 3. P01~P55 계획 vs 실제 위치·본문·Figure 전수 비교

판정 **일치(정적)**는 (1) 해당 위치의 Concept이 계획과 같고 (2) HTML 제목·주요 설명·Figure 구성 목적이 해당 슬라이드의 교육 목표와 부합한다는 의미다. 실제 사진 화질, SVG 픽셀 좌표, 전체 화면에서의 레이아웃, 상호작용 결과는 자동 CI 참조 외에 개별 육안 독립 확인하지 않았으므로 이 표의 판정을 **시각적 완전 PASS**로 해석하지 말 것.

| 계획 번호 / Concept | 계획된 내용(스토리보드 목표 포함) | 현재 실제 위치 | 실제 내용과 Figure(HTML 정적 증거) | 일치 여부 | 권장 조치 |
| --- | --- | --- | --- | --- | --- |
| P01 / `start` | Vision AI란 무엇인가? · 사과 사진·영상에서 결함 찾기 <small>(Vision AI는 이미지·동영상의 시각 정보를 AI로 분석하여 판단을 돕는 기술이며, 사과 표면의 작은 갈색 반점을 검사하는 것이 강의)</small> | `docs/intro.html#slide-1` (전역 P01) | **Vision AI란 무엇인가?**. 사과의 사진이나 카메라 영상에서 작은 표면 결함을 찾아 사람이 판단하도록 도울 수 있습니다.. Figure: 사과 사진·Frame 2장 → AI 분석 → 주석 ROI | **일치(정적)** | 유지 |
| P02 / `ai-ml-dl-cv` | AI·ML·DL과 Computer Vision의 관계 <small>(AI⊃ML⊃DL은 기술적 포함 관계, CNN은 DL 아키텍처 한 예다. Computer Vision은 사진·영상의 시각 정보를 분석하는 )</small> | `docs/intro.html#slide-2` (전역 P02) | **AI·ML·DL과 Computer Vision의 관계**. AI·ML·DL은 문제를 푸는 기술의 포함 관계 , Computer Vision은 사진·영상의 시각 문제 분야입니다.. Figure: AI⊃ML⊃DL 중첩 도식 / 별도 CV 영역 | **일치(정적)** | 유지 |
| P03 / `vision-value` | Vision AI가 필요한 이유 <small>(반복적인 시각 품질검사에서 Vision AI가 결함 후보 판단을 도울 수 있지만 사람의 확인 및 모델의 오류 검증도 필요함을 이해한다.)</small> | `docs/intro.html#slide-3` (전역 P03) | **Vision AI가 필요한 이유**. 같은 유형의 제품을 반복 검사할 때 AI가 결함 후보 를 제시하면 사람이 확인할 위치에 집중할 수 있습니다.. Figure: 반복 검사 → 100장 개념 예시 → 후보·사람 검증 | **일치(정적)** | 유지 |
| P04 / `photo-numbers` | 사람의 의미 인식 vs Pixel 숫자 <small>(사람이 보는 의미와 컴퓨터 입력의 Pixel 숫자가 다름을 구분한다)</small> | `docs/intro.html#slide-4` (전역 P04) | **사람의 의미 인식 vs Pixel 숫자**. . Figure: 같은 사과의 의미 인식과 숫자 격자 대응 | **일치(정적)** | 유지 |
| P05 / `gray` | 흑백 사진은 H×W · 2차원 숫자 배열 <small>(흑백(Grayscale) 이미지는 세로 H × 가로 W 두 축을 가진 2차원 배열이며 한 Pixel에 밝기 숫자 1개(일반 8-bit 예)</small> | `docs/intro.html#slide-5` (전역 P05) | **흑백 사진은 H × W 숫자 배열**. Grayscale 이미지는 높이 H × 너비 W의 2축 배열 입니다. 클릭하여 6 × 6개의 밝기 숫자를 확인해 보세요.. Figure: 6×6 Gray Pixel 클릭·36개 밝기 칸 | **일치(정적)** | 유지 |
| P06 / `rgb` | RGB 사진 클릭 · 한 Pixel에 세 숫자 <small>(기존 Intro 6장의 RGB 실측 인터랙션으로 한 Pixel의 R/G/B 세 값(일반 8-bit 0~255)을 확인하고 흑백 Pixel)</small> | `docs/intro.html#slide-6` (전역 P06) | **RGB · Pixel당 세 숫자**. 사진의 한 점을 클릭하여 [R,G,B] 세 숫자 를 확인해 보세요. 각 값은 일반적인 8-bit 예시에서 0~255입니다.. Figure: 사과 RGB Pixel 클릭·[R,G,B] 실제 샘플링 | **일치(정적)** | 유지 |
| P07 / `hwc` | RGB 이미지 전체 · H×W×3 (3차원 배열) <small>(RGB 사진 전체는 각 Pixel의 [R,G,B] 값이 H행 W열에 채워진 3축 숫자 배열 H×W×3이며 RGB의 3은 공간의 깊이가 아)</small> | `docs/intro.html#slide-7` (전역 P07) | **RGB 이미지 전체는 H × W × 3**. 높이 H=640 × 너비 W=960의 사진에서 각 Pixel에 R·G·B 세 값 이 들어갑니다. 마지막 3은 공간 깊이가 아닌 Channel 축입니다.. Figure: RGB 채널 3층 및 640×960×3 계산 | **일치(정적)** | 유지 |
| P08 / `video-frames` | 동영상은 시간순으로 이어진 RGB 이미지 여러 장 <small>(동영상은 디코딩해 얻은 RGB 프레임 여러 장이 시간 순서로 이어지는 것으로 이해한다. 한 Frame은 H×W×3, Frame을 T장 쌓)</small> | `docs/intro.html#slide-8` (전역 P08) | **동영상은 시간순 RGB 이미지 여러 장**. 동영상 파일을 디코딩하면 시간 순서가 있는 Frame(이미지) 이 나옵니다. 각 Frame은 한 장의 RGB 사진입니다.. Figure: 동일 사과의 시간 순 Frame 1/2/3/30과 T×H×W×3 | **일치(정적)** | 유지 |
| P09 / `resolution` | 해상도에 따른 정보 차이 <small>(정지 이미지 또는 동영상 Frame을 축소하면 작은 결함 정보가 사라질 수 있음을 이해한다 (G1))</small> | `docs/intro.html#slide-9` (전역 P09) | **해상도가 낮으면 작은 결함도 사라질까?**. 같은 960×640 사진의 중앙 960×540 영역을 세 크기로 축소했습니다. 화면 크기를 같게 맞춰 보면, 작은 세부가 얼마나 남는지 차이가 보입니다.. Figure: 동일 Crop의 160×90·320×180·640×360 Canvas | **일치(정적)** | 유지 |
| P10 / `lighting` | 조명·색감에 따른 Pixel 변화 <small>(동일 결함에서 조명이 변하면 RGB도 변함을 이해한다)</small> | `docs/intro.html#slide-10` (전역 P10) | **조명이 달라지면 Pixel 숫자도 변한다**. 같은 사과 사진에서 표시 밝기만 바꾸었습니다. 결함 정답은 같지만 Pixel의 RGB 값은 달라질 수 있습니다.. Figure: 동일 ROI 밝기 ×1·×0.45·×1.6 비교 | **일치(정적)** | 유지 |
| P11 / `transform` | 회전·크기·가림·흐림에 따른 변화 <small>(회전·가림·흐림이 픽셀 위치 또는 정보량을 바꾸는 이유를 설명한다)</small> | `docs/intro.html#slide-11` (전역 P11) | **회전·크롭·가림·흐림은 무엇을 바꿀까?**. 같은 사과 사진에 회전·크롭 확대·가림·흐림을 적용했습니다. 물체가 같아도 경계와 질감, Pixel의 배치가 달라집니다.. Figure: 원본·회전20°·Crop·가림·Blur 다섯 뷰 | **일치(정적)** | 유지 |
| P12 / `diversity` | 다르게 생겨도 같은 종류 <small>(사과 종류 인식과 사과 결함 판정의 Label이 다른 문제임을 구분한다)</small> | `docs/intro.html#slide-12` (전역 P12) | **다르게 생겨도 같은 종류**. “사과인가?” 와 “표면의 지정된 갈색 반점이 있나?” 는 서로 다른 Label입니다.. Figure: 정상·불량·어두운 불량 3장과 두 Label | **일치(정적)** | 유지 |
| P13 / `relevant-change` | 큰 변화보다 중요한 차이 <small>(사진의 큰 조명 변화보다 작은 지정 결함이 과제상 중요할 수 있음을 말한다)</small> | `docs/intro.html#slide-13` (전역 P13) | **큰 변화보다 중요한 차이**. 정답의 기준은 갈색 반점 유무 입니다. 밝기가 바뀌어도 Label을 유지하고 작은 지정 결함은 구분해야 합니다.. Figure: 정상/불량 × 원본/어두움 2×2 비교 | **일치(정적)** | 유지 |
| P14 / `task` | 같은 사진, 다른 질문과 정답 <small>(최종 출력 요구사항에 따라 Classification/Detection/Segmentation을 선택한다)</small> | `docs/vision_ai_course.html#slide-1` (전역 P14) | **같은 사진, 다른 질문과 정답**. 지정한 갈색 반점에 대해 무엇을 알아내고 싶은지 에 따라 학습용 정답(Ground Truth)의 형식이 달라집니다.. Figure: 하나의 사과: Class/Box/Mask GT 세 시각화 | **일치(정적)** | 유지 |
| P15 / `rules` | 규칙 기반 · 답을 구하는 방법을 사람이 정한다 <small>(입력→명시된 덧셈 규칙→출력은 사람이 규칙을 직접 쓸 수 있음을 이해한다)</small> | `docs/vision_ai_course.html#slide-2` (전역 P15) | **규칙 기반 · 답을 구하는 방법을 사람이 정한다**. 덧셈은 어떻게 계산할까요? 사람이 Python 함수로 규칙을 작성하면, 숫자가 달라져도 같은 코드가 답을 구합니다.. Figure: add(1,1)/add(2,1) + Python 함수 → 반환값 | **일치(정적)** | 유지 |
| P16 / `rules-image` | 이미지 판단 · 규칙을 어디까지 만들어야 할까? <small>(이미지의 결함 판단에는 사람의 수동 조건이 복잡해질 수 있고 Label 기반 학습이 대안임을 구분한다)</small> | `docs/vision_ai_course.html#slide-3` (전역 P16) | **이미지 판단 · 규칙을 어디까지 만들어야 할까?**. 동일한 세 사례에서 수동 조건의 예외 와 Label을 이용한 학습 의 차이를 비교합니다.. Figure: 같은 3사례의 사람이 정한 조건 vs 지도학습 | **일치(정적)** | 유지 |
| P17 / `model-choice` | 사과 결함 검사 · 규칙, 기존 모델, 추가 학습 중 선택 <small>(Intro에서 배운 AI/ML/DL 기술 관계도를 다시 설명하지 않고, 실제 사과 결함 문제에 명시 규칙·기존 모델·추가 학습 중 적절한)</small> | `docs/vision_ai_course.html#slide-4` (전역 P17) | **사과 결함 검사 · 무엇부터 시도할까?**. 사과 객체를 찾는 모델이 사과의 작은 갈색 반점 도 알아본다는 보장은 없습니다. 검사 조건을 보고 선택합니다.. Figure: 규칙 / 기존 결함 모델 / Label 추가 학습 선택 분기 | **일치(정적)** | 유지 |
| P18 / `task-model-data` | 내 과제에 맞는 모델과 Label <small>(같은 사과 사진이라도 Classification·Detection·Segmentation에 필요한 학습 정답 Label의 형식과 제작 비)</small> | `docs/vision_ai_course.html#slide-5` (전역 P18) | **내 과제에 맞는 모델과 Label**. P14가 원하는 출력 을 설명했다면, 이제 그 결과를 학습하기 위해 사람이 만들어야 하는 정답 을 비교합니다.. Figure: Class·Box·Mask Label 및 제작 부담 비교 | **일치(정적)** | 유지 |
| P19 / `cnn-why` | 왜 CNN인가? · 사과의 작은 특징 반복 탐색 <small>(사과 표면의 반점·모서리 등 작은 지역 특징을 같은 필터로 찾아내는 구조가 이미지에 적합한 이유를 설명한다.)</small> | `docs/vision_ai_course.html#slide-6` (전역 P19) | **왜 CNN인가? · 사과의 작은 특징 반복 탐색**. 사람이 반점과 윤곽 같은 시각적 단서를 모아 판단하듯, CNN은 작은 지역의 패턴을 여러 위치에서 반복 탐색 합니다.. Figure: 동일 사과의 지역 A/B/C를 같은 3×3 관찰창으로 반복 | **일치(정적)** | 유지 |
| P20 / `cnn-overview` | CNN Architecture 전체 그림 · 사과 판정까지 <small>(CNN 전체 Architecture를 먼저 보고 Conv/Kernel·Feature Map·ReLU·Max Pool·Stride·Padd)</small> | `docs/vision_ai_course.html#slide-7` (전역 P20) | **CNN Architecture 전체 그림 · 사과 판정까지**. 사진에서 특징을 찾는 Feature Extractor 와, 그 특징을 결과로 바꾸는 Classification Head 를 한 구조로 봅니다.. Figure: Conv A/B·ReLU·Pool·GAP·Dense 2 전체 구조/파라미터 | **일치(정적)** | 유지 |
| P21 / `perceptron` | 퍼셉트론 · 하나의 W와 b로 판정 <small>(단일 뉴런도 입력별 Weight가 있으며 교육용 예시에서는 W를 공유함을 이해한다)</small> | `docs/vision_ai_course.html#slide-8` (전역 P21) | **퍼셉트론 · 하나의 W와 b로 판정**. 퍼셉트론은 입력의 가중합 을 계산하고, Step 함수로 0 또는 1 을 결정하는 뉴런 하나입니다.. Figure: 두 입력의 가중합 z와 Step 뉴런 도식 | **일치(정적)** | 유지 |
| P22 / `and-rule` | AND Gate · 두 입력이 모두 1일 때 <small>(AND 논리 정답 네 조합을 먼저 알고 모델 출력을 검증한다)</small> | `docs/vision_ai_course.html#slide-9` (전역 P22) | **AND Gate · 두 입력이 모두 1일 때**. 두 조건이 모두 참(1)일 때만 정답이 1입니다.. Figure: AND 4진리값·4점·분리 직선 | **일치(정적)** | 유지(멘트 개선 참고) |
| P23 / `and-gate` | AND Gate · Weight와 Bias로 직선 이동 <small>(AND는 하나의 직선 결정 경계로 분리 가능함을 체험한다)</small> | `docs/vision_ai_course.html#slide-10` (전역 P23) | **AND Gate · Weight와 Bias로 직선 이동**. 두 입력 x₁, x₂를 구분하는 결정 직선입니다. W를 바꾸면 기울기가 회전 하고, b를 바꾸면 위치가 이동 합니다.. Figure: W·b Slider와 AND 결정경계 | **일치(정적)** | 유지(멘트 개선 참고) |
| P24 / `xor-rule` | XOR Gate · 입력이 다를 때만 1 <small>(XOR 정답은 직선 하나로 분리 불가능한 배치를 이룸을 발견한다)</small> | `docs/vision_ai_course.html#slide-11` (전역 P24) | **XOR Gate · 입력이 다를 때만 1**. 두 입력이 서로 다를 때만 정답이 1입니다. 같은 네 좌표에서 AND와 비교합니다.. Figure: XOR 4진리값·대각선 양성점 | **일치(정적)** | 유지(멘트 개선 참고) |
| P25 / `nonlinear` | 비선형성 · 깊어져도 직선이면? <small>(비선형성 없는 Affine 층의 합성은 하나의 직선 판정과 같음을 이해한다)</small> | `docs/vision_ai_course.html#slide-12` (전역 P25) | **비선형성 · 깊어져도 직선이면?**. 가중합(Affine) 계산만 반복하면 하나의 가중합 으로 다시 합칠 수 있습니다. 층을 늘리는 것만으로 XOR의 한계를 넘지는 못합니다.. Figure: Affine 합성식 두 층→단일 식 전개 | **일치(정적)** | 유지(멘트 개선 참고) |
| P26 / `relu` | ReLU · 비선형성의 시작 <small>(Architecture의 ReLU는 가중합을 꺾는 비선형 연산 max(0,z)이며 여러 층을 결합할 때 복잡한 패턴을 표현하도록 돕는다.)</small> | `docs/vision_ai_course.html#slide-13` (전역 P26) | **ReLU · 비선형성의 시작**. ReLU는 음수는 0으로, 0 이상은 그대로 통과시킵니다. 같은 축과 같은 눈금에서 0의 꺾임을 비교합니다.. Figure: y=z vs ReLU=max(0,z) 동일 축 비교 | **일치(정적)** | 유지 |
| P27 / `xor-gate` | XOR · 선형층을 쌓아도 직선 하나 <small>(선형2층의 단일 직선 한계와 비선형 조합의 XOR 분리 효과를 비교한다)</small> | `docs/vision_ai_course.html#slide-14` (전역 P27) | **XOR · 선형층을 쌓아도 직선 하나**. 가중합만 연결하면 경계의 기울기·위치는 바뀌어도 한 직선 입니다. ∣t∣를 사이에 넣어 꺾이는 경계와 비교합니다.. Figure: 선형 g(t)=t vs 두 ReLU 조합 ∣t∣ XOR Slider | **일치(정적)** | 유지(멘트 개선 참고) |
| P28 / `kernel` | Kernel · 작은 영역의 가중합 <small>(Kernel이 작은 영역에서 곱셈·덧셈으로 하나의 반응값을 만든다)</small> | `docs/vision_ai_course.html#slide-15` (전역 P28) | **Kernel · 작은 영역의 가중합**. 작은 영역의 값과 Kernel Weight를 같은 위치끼리 곱하고 더하면, 반응값 하나 가 됩니다.. Figure: 5×5 정수 입력×3×3 Kernel → 첫 반응 −6 | **일치(정적)** | 유지 |
| P29 / `feature-map` | Feature Map · 같은 계산을 위치마다 <small>(같은 Kernel의 이동이 Feature Map의 다른 셀을 채운다는 원리를 설명한다)</small> | `docs/vision_ai_course.html#slide-16` (전역 P29) | **Feature Map · 같은 계산을 위치마다**. P28과 같은 입력·같은 Kernel 입니다. 입력 창의 시작 (행, 열)이 출력의 (행, 열)과 대응합니다.. Figure: 동일 Kernel 9번 이동 → 3×3 Feature Map | **일치(정적)** | 유지 |
| P30 / `sharing` | CNN · 지역 연결과 가중치 공유 <small>(지역 연결과 Weight Sharing이 완전연결 대비 매개변수를 줄이는 이유를 설명한다)</small> | `docs/vision_ai_course.html#slide-17` (전역 P30) | **CNN · 지역 연결과 가중치 공유**. 비교 조건: 32×32 단일 입력·출력 채널 · Kernel 3×3 · Stride 1 · Padding 1 · Bias 제외.. Figure: FC 1,048,576 vs 지역 9,216 vs 공유 Weight 9 | **일치(정적)** | 유지 |
| P31 / `channels` | RGB에서 Feature Channel까지 <small>(RGB 입력3채널과 특징 출력 채널N의 뜻을 구분한다)</small> | `docs/vision_ai_course.html#slide-18` (전역 P31) | **RGB에서 Feature Channel까지**. 필터 한 개는 R·G·B 세 채널 전체의 3×3 값 을 합쳐 출력 Map 한 장을 만듭니다.. Figure: RGB 3채널에서 필터 2개 → 출력 Map 2장 | **일치(정적)** | 유지 |
| P32 / `stride` | Stride · 계산 위치의 간격 <small>(Stride는 Conv/Pool 계산 창을 이동하는 칸 수로서 출력 공간 크기와 반응을 확인하는 위치를 바꾼다.)</small> | `docs/vision_ai_course.html#slide-19` (전역 P32) | **Stride · 계산 위치의 간격**. P28·P29의 같은 5×5 입력과 3×3 Kernel 을 사용합니다. 점은 Kernel 왼쪽 위의 시작 위치입니다.. Figure: 동일 5×5/K3×3: Stride 1(3×3)·2(2×2) | **일치(정적)** | 유지 |
| P33 / `padding` | Padding · 같은 입력, 다른 출력 크기 <small>(Padding은 연산 전에 경계 바깥에 0 등을 추가하는 설정으로, 가장자리 계산과 출력 크기에 영향을 주지만 별도의 학습 Layer는 )</small> | `docs/vision_ai_course.html#slide-20` (전역 P33) | **Padding · 같은 입력, 다른 출력 크기**. 입력 바깥에 0을 더하면 가장자리 위치도 중심으로 계산 할 수 있습니다.. Figure: 3×3 all-one Kernel: Padding 0(1×1) vs 1(3×3) | **일치(정적)** | 유지 |
| P34 / `pool` | Max Pooling · 영역별 최댓값 <small>(Max Pooling은 각 작은 영역의 최댓값만 남겨 가로·세로를 줄이며 Channel은 유지한다. 작은 결함 위치 정보를 잃을 수 있다)</small> | `docs/vision_ai_course.html#slide-21` (전역 P34) | **Max Pooling · 영역별 최댓값**. 각 채널의 작은 영역에서 가장 큰 반응 하나 만 남겨 가로·세로를 줄입니다.. Figure: 4×4 반응→2×2 Max Pool 수치 | **일치(정적)** | 유지 |
| P35 / `actual-map` | 실제 Feature Map · CNN 내부 반응 <small>(실제 CNN에서 다양한 층의 Feature Map이 서로 다른 반응 지도를 만든다)</small> | `docs/vision_ai_course.html#slide-22` (전역 P35) | **실제 Feature Map · CNN 내부 반응**. 이번에는 실제 ImageNet 사전학습 SqueezeNet 1.1 입니다. 같은 강아지 한 장에서 세 단계의 반응을 계산했습니다.. Figure: 강아지 입력 + 실제 SqueezeNet 얕은/중간/깊은 Map | **일치(정적)** | 유지(멘트 개선 참고) |
| P36 / `backbone` | Backbone과 Task Head <small>(같은 Backbone의 특징에서 최종 Task Head에 따라 Class/Box/Mask 출력이 달라진다)</small> | `docs/vision_ai_course.html#slide-23` (전역 P36) | **Backbone과 Task Head**. 지금까지 배운 Conv·ReLU·Pool은 공간 특징을 만드는 Backbone 입니다. 필요한 출력에 맞춰 Head를 연결합니다.. Figure: 동일 Backbone → Class/Box/Mask Head 분기 | **일치(정적)** | 유지 |
| P37 / `dataset` | 데이터셋 · 어떤 사진으로 배우나 <small>(정상/불량과 조명 조건을 교차 수집해야 shortcut을 줄인다는 사실을 이해한다)</small> | `docs/vision_ai_course.html#slide-24` (전역 P37) | **데이터셋 · 어떤 사진으로 배우나**. 정상·불량과 밝기 조건을 교차해서 모아야 엉뚱한 단서를 외울 위험을 줄일 수 있습니다.. Figure: 정상/불량 × 밝음/어두움 데이터 교차표 | **일치(정적)** | 유지 |
| P38 / `split` | Train · Validation · Test <small>(Train/Validation/Test의 역할을 구분한다)</small> | `docs/vision_ai_course.html#slide-25` (전역 P38) | **Train · Validation · Test**. 데이터를 학습 · 선택 · 최종 평가 의 서로 다른 역할로 나눕니다.. Figure: 1000장 Train700/Val150/Test150 역할 | **일치(정적)** | 유지 |
| P39 / `leakage` | Video Group Split · 데이터 누출 방지 <small>(같은 사과 개체/원본 영상의 연속 촬영은 데이터 누출을 일으킬 수 있다)</small> | `docs/vision_ai_course.html#slide-26` (전역 P39) | **Video Group Split · 데이터 누출 방지**. 사진이 달라도 같은 사과·영상의 인접 Frame 이면 거의 같은 정보를 공유할 수 있습니다.. Figure: 영상 Frame 무작위 분할 vs Group A/B/C 분할 | **일치(정적)** | 유지 |
| P40 / `augment` | Data Augmentation · 같은 정답, 다른 조건 <small>(Train에서만 정답 의미를 보존하는 변형을 만들어 일반화를 돕는다)</small> | `docs/vision_ai_course.html#slide-27` (전역 P40) | **Data Augmentation · 같은 정답, 다른 조건**. 분할을 끝낸 Train에서만 , 정답 의미를 유지하는 밝기·회전 변형을 만듭니다.. Figure: 밝기·회전 Label 보존 / 결함 가림 반례 | **일치(정적)** | 유지 |
| P41 / `learn` | 모델 학습 · 오차를 줄이는 반복 <small>(지도학습에서는 이미지/프레임 데이터와 정답 Label을 제공하며, 예측과 정답의 Loss를 줄이도록 Weight를 반복 갱신해 모델을 학)</small> | `docs/vision_ai_course.html#slide-28` (전역 P41) | **모델 학습 · 오차를 줄이는 반복**. 사진 + 정답 Label로 배우는 원리를, x=2 · y=4인 회귀 문제 로 작게 확인합니다.. Figure: 동일 사과 학습 예고 + x2,y4,w0.5 회귀 갱신 | **일치(정적)** | 유지 |
| P42 / `loss` | Loss · 틀린 정도를 줄이는 방향 <small>(Gradient와 Optimizer의 역할을 Loss 감소 방향과 연결한다)</small> | `docs/vision_ai_course.html#slide-29` (전역 P42) | **Loss · 틀린 정도를 줄이는 방향**. Gradient는 어느 방향으로 얼마나 바꿀지 , Optimizer는 실제 Weight 갱신 을 담당합니다.. Figure: Loss9 → Gradient−12 → w1.7 → Loss0.36 | **일치(정적)** | 유지 |
| P43 / `cnn-training` | CNN 학습 · 예측에서 Weight 갱신까지 <small>(CNN에서 Kernel과 Head의 학습 대상 Weight가 업데이트됨을 설명한다)</small> | `docs/vision_ai_course.html#slide-30` (전역 P43) | **CNN 학습 · 예측에서 Weight 갱신까지**. 앞서 본 같은 CNN에서 Conv Kernel과 Dense Head의 W,b 를 학습합니다.. Figure: P20 CNN Forward→Loss→Gradient/Optimizer→Conv·Head 갱신 | **일치(정적)** | 유지 |
| P44 / `infer` | Training과 Inference의 차이 <small>(Training은 Label·Loss를 사용해 모델 Weight를 갱신하지만, Inference는 학습된 Weight를 고정하고 새 이미)</small> | `docs/vision_ai_course.html#slide-31` (전역 P44) | **Training과 Inference의 차이**. 배울 때는 정답으로 Weight를 바꾸고, 사용할 때는 고정된 Weight로 새 입력을 예측 합니다.. Figure: Training Label/Loss/Weight 변경 vs Inference 단방향 | **일치(정적)** | 유지 |
| P45 / `transfer` | 전이학습 · 특징은 고정하고 분류기만 학습 <small>(전이학습 Head-only와 Fine-tuning의 차이를 이해한다)</small> | `docs/vision_ai_course.html#slide-32` (전역 P45) | **전이학습 · 특징은 고정하고 분류기만 학습**. P20 같은 사과 CNN 구조로, 고정할 부분과 학습할 부분 을 비교합니다.. Figure: 동일 구조 Head-only Freeze vs Conv B Fine-tune | **일치(정적)** | 유지 |
| P46 / `cnn-learning-paths` | 같은 CNN 특징 · 지도와 비지도 활용 <small>(같은 사전학습 CNN Feature의 후단을 지도 분류/비지도 군집화로 활용하는 차이를 설명한다)</small> | `docs/vision_ai_course.html#slide-33` (전역 P46) | **같은 CNN 특징 · 지도와 비지도 활용**. 두 경로 모두 하나의 고정 Backbone이 만든 같은 특징 을 사용합니다.. Figure: 공통 Frozen Feature → Label 분류 vs K-means 군집 | **일치(정적)** | 유지 |
| P47 / `overfit` | Overfitting · 새 데이터 일반화 <small>(Train 성능 상승이 Validation 일반화를 보장하지 않음을 이해한다)</small> | `docs/vision_ai_course.html#slide-34` (전역 P47) | **Overfitting · 새 데이터 일반화**. Train Loss가 계속 내려가도 Validation Loss가 다시 오르면 새 데이터 성능을 점검합니다.. Figure: Train/Val Loss 곡선과 밝기 변화 가설 | **일치(정적)** | 유지 |
| P48 / `threshold` | Score Threshold · 판정 기준 <small>(Score Threshold는 FP/FN의 균형을 바꾸며 Validation에서 선택해야 함을 이해한다)</small> | `docs/vision_ai_course.html#slide-35` (전역 P48) | **Score Threshold · 판정 기준**. 같은 교육용 저장 점수 100건 · 실제 불량 20 / 정상 80. 기준만 바꾸어 놓침과 오알람을 비교합니다.. Figure: 동일 100 Score + Threshold .30/.50/.70 상호작용 | **일치(정적)** | 유지 |
| P49 / `confusion` | Confusion Matrix · 100건 평가 <small>(TP/FN/FP/TN과 100건 실제-예측 혼동행렬을 해석한다)</small> | `docs/vision_ai_course.html#slide-36` (전역 P49) | **Confusion Matrix · 100건 평가**. 앞 실습의 기준을 0.50으로 고정한 참조 표입니다. 실제 불량 20건 중 18건을 찾고, 정상 80건 중 4건을 잘못 알렸습니다.. Figure: TP18·FN2·FP4·TN76 2×2 Confusion Matrix | **일치(정적)** | 유지 |
| P50 / `imbalance` | Accuracy의 함정 · 모두 정상이라면? <small>(불균형 데이터에서 Accuracy만으로 실패를 볼 수 없음을 설명한다)</small> | `docs/vision_ai_course.html#slide-37` (전역 P50) | **Accuracy의 함정 · 모두 정상이라면?**. 정상 80건, 불량 20건입니다. 전부 정상이라고 말해도 맞힌 비율이 80%가 됩니다.. Figure: 정상80/불량20 중 전부 정상 분류 기준 | **일치(정적)** | 유지 |
| P51 / `metrics` | Precision과 Recall <small>(Precision과 Recall 분모 및 업무상 의미를 구분한다)</small> | `docs/vision_ai_course.html#slide-38` (전역 P51) | **Precision과 Recall**. Threshold 0.50 고정 참조 · P49의 TP=18·FP=4·FN=2를 그대로 사용합니다. Precision은 불량이라고 알린 22건, Recall은. Figure: 알람22중 TP18/FP4 vs 실제 불량20중 TP18/FN2 | **일치(정적)** | 유지 |
| P52 / `iou` | IoU · 박스 겹침 비율 <small>(검출·분할의 위치 정확성은 Class 판정과 다른 평가가 필요함을 이해한다)</small> | `docs/vision_ai_course.html#slide-39` (전역 P52) | **IoU · 박스 겹침 비율**. 위치도 맞아야 하는 검출에서는 정답(GT)과 예측 박스의 교집합 ÷ 합집합 을 계산합니다.. Figure: 사과 Box 겹침과 별도 격자 IoU 20/40 | **일치(정적)** | 유지 |
| P53 / `workflow` | Vision AI 원리 · 한 장으로 연결 <small>(입력→과제→특징→학습→평가의 전체 결정 흐름을 복습한다)</small> | `docs/vision_ai_course.html#slide-40` (전역 P53) | **Vision AI 원리 · 한 장으로 연결**. 같은 사과의 결함을 찾는 문제로 돌아와, 사진의 숫자부터 새 사진의 평가까지 연결합니다.. Figure: 동일 사과 + Pixel→Task/Label→CNN→Training→평가 | **일치(정적)** | 유지 |
| P54 / `project-iterate` | 실패 사진이 알려 주는 것 <small>(실패 사례를 조명·배경·해상도 조건별로 나눠 검증한다)</small> | `docs/vision_ai_course.html#slide-41` (전역 P54) | **실패 사진이 알려 주는 것**. 실패를 발견했다면 먼저 원인 가설을 세우고, 한 조건만 바꾼 비교로 확인합니다.. Figure: 조명/배경/해상도 가설별 통제 비교 | **일치(정적)** | 유지 |
| P55 / `project-check` | Vision AI 원리 · 무엇을 설명할 수 있나? <small>(수강생 스스로 Pixel·Feature·Learning·Evaluation을 설명하는지 확인한다)</small> | `docs/vision_ai_course.html#slide-42` (전역 P55) | **Vision AI 원리 · 무엇을 설명할 수 있나?**. 같은 사과 한 장을 네 가지 관점으로 설명할 수 있다면, AI와 프로젝트를 시작할 기초가 연결된 것입니다.. Figure: 동일 사과 + Pixel/Map/Loss/Recall 네 회상 카드 | **일치(정적)** | 유지 |

**전수 결론:** 계획 번호별 실제 위치는 모두 동일(P01→P01, …, P55→P55), 이탈/중복/누락 **0개**. Figure의 입력·중간 단계·결과/GT/교육용 예제 표기는 각 위치에서 관련 설명과 함께 존재했다. 원본 사진·교육용 합성·실제 SqueezeNet 특징지도 간 증거 수준을 분리하는 문구도 정적으로 확인했다. 향후 자산 이미지 자체 및 브라우저에 그려지는 SVG/Canvas 화살표·글자·ROI를 수작업으로 재검토하는 작업은 별도의 렌더 QA 범위다.

## 4. 핵심 교육 인과관계 독립 판정

| 중점 질문 | 실제 연속 배치와 본문 증거 | 결론 |
| --- | --- | --- |
| Rule-based / ML 차이가 먼저 나오는가? | **P15** Python `add(a,b)`는 규칙 직접 작성, **P16** 동일 사진 3사례의 Rule-based 의사조건 vs `정답 사진+Label → Weight 학습 → 새 사진 예측`을 명시. **P19 CNN 시작 전에 설명** | **PASS** |
| CNN 전체→내부 연산 순서인가? | **P19** 지역 패턴 반복 필요성 → **P20** Conv·ReLU·Pool·GAP·Head 전체 아키텍처 → **P21~P27** 뉴런/AND/XOR/비선형성 → **P28~P36** Kernel/Map/Sharing/Channel/Stride/Padding/Pooling/실측Map/Head | **PASS** |
| Perceptron→AND/XOR→비선형성인가? | **P21** 가중합/Step → **P22–23** AND 정답/경계 → **P24** XOR 선형 분리 불가 → **P25** Affine 합성 → **P26** ReLU → **P27** 비선형 조합 XOR 실습 | **PASS**, 교육 멘트 개선 가능 |
| 특징 추출→학습·지도/비지도 연결인가? | **P28–36** 특징 추출을 해부, **P37–40** 데이터·분할·증강, **P41–45** Loss·CNN Weight·Training/Inference·Transfer, **P46** 동일 Frozen Feature Vector의 지도 Head 학습 vs 비지도 K-means, **P47** 일반화 | **PASS** |
| 평가와 결론은 연결되는가? | **P48** Threshold 조작 → **P49** 0.50 혼동행렬 → **P50** Accuracy 함정 → **P51** Precision/Recall → **P52** IoU → **P53** 원리 전체 → **P54** 실패 가설 → **P55** 스스로 설명 | **PASS** |

정량 예제의 순서 연결도 정적 교차 확인: P07 `640×960×3=1,843,200`, P20 학습 대상 수 `224+1,168+34=1,426`, P28→P29 첫 Kernel 출력 `−6`, P32 Stride 1의 3×3→Stride 2의 2×2, P42 `w=0.5→1.7`와 `Loss 9→0.36`, P48→P49 기준 0.50의 `TP18,FN2,FP4,TN76`, P51 `18/22=81.8%, 18/20=90%`, P52 `20/40=0.5`. 이런 연결 때문에 슬라이드를 임의로 원래 위치로 되돌리면 설명의 선행관계를 오히려 깨뜨린다.

## 5. 별도 교육적 개선 사항 (순서 문제와 구분)

### EDU-ORDER-01 · Minor · P22–P25에서 'ReLU의 이유' 챕터 배지 선행 노출

- **근거**: `docs/vision_ai_course.html`의 `data-concept="and-rule"`, `and-gate`, `xor-rule`, `nonlinear`에는 공통 구간 배지 `ReLU의 이유`가 포함된다. ReLU의 실제 정의는 **P26**에서 처음 자세히 설명.
- **영향**: 앞부분에서 처음 만나는 초보자가 ReLU의 의미를 이미 알아야 하는 용어라고 오해할 수 있음. 전체 슬라이드의 순서를 바꿀 이유는 아니다.
- **담당/수정**: **Builder(선택적)** — 해당 배지를 '직선 판정의 한계' 또는 '비선형성이 필요한 이유'처럼 선수 설명 없이 읽히는 표현으로 변경하거나 강의자 노트에 'ReLU는 P26에서 배운다' 연결문을 추가. P21~P27 위치·내용 유지.
- **재검증**: P22 시작에서 정의하지 않은 전문용어가 요구되는지 강의 대본 확인 + 양 해상도 배지 표시 확인.

### EDU-ORDER-02 · Minor · P25와 P27의 Affine 한계 설명 중복 체감 방지

- **근거**: **P25**는 `W₂(W₁x+b₁)+b₂`의 단일 Affine 환원, **P27**은 `g(t)=t`와 `|t|=ReLU(t)+ReLU(−t)`를 Slider 프리셋으로 비교. 모두 '비선형성 없는 층은 직선'이라는 말을 사용하지만 **증명용 개념과 조작용 실습**으로 역할은 다름.
- **영향**: 아무 연결 멘트 없이 진행하면 같은 설명 반복처럼 느껴질 수 있음.
- **담당/수정**: **Planner(강의 멘트 권장)** / 필요 시 Builder — P25 '왜 안 되나?' 수식 유도 1회, P26 '어떤 함수가 해결하나?', P27 '실제로 경계가 달라지는가?' 실습으로 명확히 구분. **삭제/교환 권고 없음**.
- **재검증**: P25→P26→P27 순서 3장 연속 설명 리허설.

### EDU-ORDER-03 · Minor · P35 실측 강아지 CNN Figure의 사례 전환 고지

- **근거**: **P01~P34**는 사과를 중심 예시로 진행하지만 **P35**는 실제 ImageNet 사전학습 SqueezeNet 1.1의 **강아지 Crop**·Feature Maps를 사용한다. 다만 HTML에서 사과 CNN과 **다른 모델**임을 이미 명시했고, 실제 계산/출처를 구분했다.
- **영향**: 전환 목적을 말하지 않으면 초보자가 '사과 검사 CNN을 이미 학습했다'고 오해할 가능성.
- **담당/수정**: **Planner(강의 멘트)** — '지금 한 장만은 실제 학습 모델의 반응을 보여주는 검증 예시이며, 다음 P36에서 다시 사과 과제 구조로 복귀'라는 문장을 넣을 것. 본문에 이미 한계 표기가 있으므로 Figure 자체 교체/슬라이드 이동 불필요.
- **재검증**: P34→P35→P36 연결 멘트, 실제 Figure 렌더·asset 로딩 확인.

### TOOLING-ORDER-01 · Minor · CI Artifact 명칭의 옛 '56장' 표기

- **근거**: `.github/workflows/visual-audit.yml`의 Job 단계명 'Render 56 slides at two resolutions', 업로드 명 `visual-audit-56-slides`. 실제 `audit_visual_slides.py`는 현재 Manifest로 Deck 수를 계산하며 최신 CI 로그는 **110장면** 처리.
- **영향**: 실수로 예전 강의 수량이라고 판단할 수 있으나 실제 렌더 순서 오류는 아님.
- **담당/수정**: **Builder(선택적 문구 정리)** — 해당 워크플로의 Step/Artifact 이름을 `55-slide`로 정정. 내용 코드·HTML 수정 불필요.
- **재검증**: 향후 CI 수행 시 Job명과 rendered=110 상호 일치.

**Critical 0 / Major 0 / Minor(교육·CI 문구) 4**, 별개로 공개 Pages·수동 렌더 **NOT VERIFIED**.

## 6. Builder 직접 실행 지침

**현 단계 재배치 대상 = 없음.** 승인 계획의 순서와 실제 HTML DOM 순서는 이미 일치한다. 불필요한 `section.slide` 이동·Manifest 변경·Outline 재번호 부여는 하지 말 것.

향후 계획 변경으로 위치를 옮겨야 할 때의 **안전한 변경 순서**:

1. Planner의 승인된 `planning/approved55.json` 및 `planning/SLIDE_STORYBOARD.md`에서 새 Plan/Concept 순서를 먼저 확정. 승인 없이 Reviewer 의견만으로 배치 변경 금지.
2. `docs/intro.html`의 `section.slide[data-concept]` 13장, `docs/vision_ai_course.html`의 42장을 각각 **실제 DOM 순서로 이동**. 이 두 문서 간 경계를 바꾸는 경우 파일 이동 및 관련 내부 Asset·JS 선택자도 확인.
3. `docs/two_hour_manifest.json`의 각 Deck `slide`(로컬 번호), `docs/lecture_outline.js`의 `global`·`page`·`slide`·Group을 새 DOM에 맞게 **동시에 갱신**. 단순 Concept ID의 내부 번호만 교체해서 DOM 재배치를 대신하지 말 것.
4. `docs/lecture_sidebar.js`가 생성하는 `page#slide-N`과 `docs/slide.js`의 `[data-slide-next]`/`[data-slide-prev]`·`#slide-N`·`#slide-last`·경계 `data-next-page`/`data-prev-page`를 확인. 특히 **P13→P14**, **P14→P13** 양방향 전환.
5. 슬라이드 본문 내부의 '앞/뒤 슬라이드', 'Pxx', 수식 참조, 공유 CNN 미니맵, 이미지 Caption이 새 위치에서도 맞는지 별도 검색·수정.
6. **검증 게이트**: `python scripts/verify_two_hour_course.py`, `python scripts/verify_learning_routes.py`, `python scripts/audit_visual_slides.py`; Manifest 기반 **55×2=110** 장면을 캡처·육안 대조. 실행 시 로컬 정적 서버 및 Playwright 환경 필요. 그 후 공개 Pages HTTP에서 실제 최신 Commit의 내용과 딥링크 확인.

**현 시점 Builder 우선순위**: 순서 재배치 **하지 않음** → 선택적 교육 연결/배지 개선 → 공개 Pages를 실제 브라우저에서 열어 P01/P13/P14/P20/P21/P27/P35/P46/P55를 포함한 진입·목차·경계·끝 화면을 수동 점검하고 배포 SHA 확인. 이 작업은 실제 최신 Pages가 구버전인지 판정하는 최종 현장 확인 조건이다.

## 7. 최종 범위/미검증 보고

- **고정 SHA** `90bf3767b33199f9833c07970007f8df795ac976`.
- **슬라이드 커버리지** 55/55 (A13·B5·C9·D9·E4·F7·G5·H3) 및 120분 계획.
- **정적 일치** 승인 계획↔DOM↔Manifest↔Outline↔목차 **55/55**; 단원/Deck 양방향 탐색은 코드 수준 확인.
- **독립적으로 실행한 Chromium/스크린샷 수작업 비교/강의 리허설** 없음. GitHub Actions 성공 **외부 기존 CI 증거** 확인.
- **공개 Pages** 최신 Commit에 대한 성공적 배포 CI 확인, 별도 URL HTTP 응답 확인 실패 → **NOT VERIFIED**.
- **변경** Reviewer Branch에 보고서 1개 추가만. HTML/CSS/JS/Assets/Manifest/기획 파일 변경 없음. `main` Merge 없음.
- **최종 판정** 정적 슬라이드 순서 **PASS**, 전체 실서비스·시각 독립 검증까지 포함하면 **CONDITIONAL PASS**.

