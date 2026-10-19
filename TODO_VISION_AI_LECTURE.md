# TODO · Vision AI 원리 중심 강의 — 남은 작업

> **현재 활성 작업 목록(Single Source of Truth)** · 2026-10-19 · 최신 강의 기준: `docs/two_hour_manifest.json` (과거 최초 개편 PR [#101](https://github.com/sh0427-han/vision_ai_lecture/pull/101)은 이력)
> **강의 목표 A:** Vision AI를 처음 접하는 수강생이 **Pixel → CNN 특징 추출 → Loss/Weight 학습 → 독립 평가**를 그림으로 설명할 수 있도록 구성한다.
> **공개 강의:** Intro **13장** + `vision_ai_course.html` **46장** = **59장** / **120분 전체 강의**(별도 Q&A 없음).
> **이 문서는 앞으로 할 일만 추적한다.** 과거 진단 보고서의 옛 슬라이드 번호를 그대로 실행하지 않는다. `data-concept`와 현재 `docs/two_hour_manifest.json`을 사용한다.

> **후속 작업 상태:** P0·P1 및 로컬 QA-01~03 완료. 작업 브랜치의 검증이며 main 배포 완료가 아닙니다. [구현·검증 기록](reviews/2026-10-18_VISION_AI_TODO_IMPLEMENTATION.md)을 참고하세요. QA-04 중 main 병합과 Pages 배포 성공을 확인했습니다. 공개 URL 직접 검증 및 현장 리허설은 남았습니다. 사용자의 후속 요청으로 PR API 대신 Git 병합·push를 승인받았습니다.

> [!IMPORTANT]
> **현행 활성 기준 (2026-10-19 추가 개편): Intro 13장 + Course 46장 = 총 59장.** 이 파일의 아래 50장 P0/P1 체크는 **이전 PR에서 완료된 작업의 이력**입니다. 이전 54장 진단은 [54장 전체 내용·흐름 재검토](reviews/2026-10-18_VISION_AI_54_SLIDE_FLOW_REVIEW.md)의 신규 슬라이드 번호와 `docs/two_hour_manifest.json`을 기준으로 합니다. 새 59장 공개 배포·화면 QA는 아직 완료 처리하지 않습니다.

## 2026-10-19 · Course 6 W/b 단순화와 CNN 지도·비지도 비교 (최신)

- [x] C6에서 `w₁x₁+w₂x₂+b` 일반형을 본문과 그림에서 제거. **W 한 개, b 한 개**로 공통 Weight 예시 `z=W(x₁+x₂)+b`, Step 판정을 시각화한 로컬 SVG 신규 추가.
- [x] C7 AND에서는 W=0.5,b=−0.7의 공통 Weight 예시로 연결. C8의 기울기 실습은 다른 설정(입력 x₂ 계수1 고정)이므로 유지.
- [x] **C34 CNN 지도/비지도**: 동일 사전학습 CNN Feature Extractor Freeze → Feature → 지도 Label+Classification Head 학습 / 비지도 No Label+K-means 군집화. 지도/비지도 기준은 Label 및 학습 목표라는 개념 설명.
- [x] 군집 A/B가 자동으로 정상/불량 Classification이 되는 듯한 표현 금지, 전체 CNN Backbone이 비지도 방식으로 학습되었다고 주장하지 않음.
- [x] **Intro13 + Course46 = 59장**, 120분 강의(별도 Q&A 없음) Manifest/Outline/Guide/운영 문서 반영.
- [ ] C6/C34 실제 Chromium 1366×768, 1920×1080 화면 가독성·로컬 SVG/사과 사진 로딩 확인. 전체 59×2=118 View QA.
- [ ] PR 병합 후 main·Pages Workflow·공개 URL 반영 확인.

## 2026-10-19 · 퍼셉트론 수식·AND 설명 순서 정정 (이전 이력)

- [x] C6 퍼셉트론: 뉴런 1개여도 두 입력에는 w₁,w₂의 서로 다른 Weight가 존재. 일반식 z=w₁x₁+w₂x₂+b. w₂는 두 번째 뉴런이 아님.
- [x] 같은 Weight를 갖는 AND 특수 예시: w₁=w₂=w이면 z=w(x₁+x₂)+b. 기존 그림의 w₁=w₂=0.5와 정확히 대응.
- [x] C7 AND 동작을 퍼셉트론 뒤로 이동. C8 AND 실습은 x₂ 연결 Weight=1 고정, W·b를 조절하면서 직선의 회전/이동을 보여줌.
- [x] C10 XOR: Layer1과 Layer2의 나머지 입력선 Weight=1 고정 사실을 명시해 조절 가능한 W가 모든 Weight인 것처럼 표현하지 않음.
- [x] 58장 목차와 HTML, Manifest, 안내 문서의 강의 순서 동기화. 총 120분·Q&A 0분 유지.
- [ ] Chromium 1366×768과 1920×1080에서 퍼셉트론 일반식과 특수식 크기·절단·실제 실습 연동 재검증.
- [ ] Pages 배포 Workflow 및 116개 화면 전수 QA.

## 2026-10-19 · AND / XOR Gate 설명 장표 추가 (이전 순서 이력)

- [x] **이전 Course 6(현재 Course 7) AND Gate 동작:** (0,0),(0,1),(1,0),(1,1) 네 입력 그림으로 AND 규칙을 먼저 소개. 모두 1일 때만 1. AND는 논리 기능이며, 앞에서 설명한 퍼셉트론 뉴런 하나로 구현 가능한 예제라는 점을 연결.
- [x] **이전 Course 7(현재 Course 6) 퍼셉트론:** 먼저 개념을 설명하고 AND에 적용하도록 순서를 변경.
- [x] **Course 9 XOR Gate 동작:** 입력이 정확히 하나만 1일 때 1이라는 논리 규칙을 같은 그림 템플릿으로 설명. 다음 Course 10 선형/비선형 실습에 연결.
- [x] **Course 8·10 기존 인터랙션 유지:** W·b 조절, 직선 회전과 이동, XOR 선형 한계/비선형 비교는 기존 Concept ID를 유지하며 번호만 이동.
- [x] **교육 시간표:** Intro 13+Course45=58장, 기존처럼 Q&A 없이 120분. AND/XOR/퍼셉트론 설명 18분, CNN 핵심 31분.
- [ ] **실제 브라우저 QA:** 58장×2해상도=116개 화면, 특히 Course 6~10 네 가지 입력 그림·설명·다음 장 전환과 상호작용 확인.
- [ ] **배포 QA:** Merge 후 최신 `main`, GitHub Pages Workflow 및 공개 URL에 Course 6/9 설명이 표시되는지 확인.

**검증 기준:** `docs/two_hour_manifest.json`, `scripts/verify_two_hour_course.py`, `scripts/verify_learning_routes.py`, `TWO_HOUR_LECTURE_PLAN.md`.

## 2026-10-19 · 이전 AND/XOR 인터랙티브 작업 이력 / Q&A 제거

- [x] **이전 C7(현재 C8) AND**: W·Bias 슬라이더 2개, W는 기울기(회전), b는 y절편(평행 이동), 한 직선 결정 영역·네 점 정답/AI 판정·초기화.
- [x] **이전 C8(현재 C10) XOR**: Layer1 W₁·b₁, Layer2 W₂·b₂ 총 4개만 조절. 원래 입력 x₁을 Layer2에 더하는 고정 연결이 있음. 선형 없음(최종 Wx+b 직선 하나) → 비선형 |t|=ReLU(t)+ReLU(−t)(두 경계), 정답과 AI 판정 차이를 표현·초기화.
- [x] **운영 계획**: Q&A 별도 구간 제거, 58장 × 총 120분, Gate 학습 구간 18분, CNN 구간 31분. Manifest/운영안/검증 규칙 수정.
- [ ] **브라우저 QA**: 실제 Chromium에서 AND W1.0/b−1.2 기본 4/4, W0.4 기울기 변경, b−0.5 평행 이동/복원; XOR 선형 기본 3/4·직선 1개, W₁·W₂ 각각 기울기 변경, 비선형 전환 4/4·두 경계, W₁ 변경과 복원/색상·키보드·모바일 확인.
- [ ] **실화면 QA**: 1366×768, 1920×1080의 C7/C8에서 슬라이더 2개/4개·한 직선과 두 경계·정답/AI 판정 표기가 잘리거나 겹치지 않는지 확인.
- [ ] **배포 QA**: 병합 commit의 Pages Workflow 성공 및 실제 공개 URL에서 두 인터랙션 확인.

## 2026-10-19 · CNN 그림·게이트 단계학습 수정 후 미완료 검증

- [x] Intro 13: 사진 변환 CSS 범위 수정 (같은 사과 원본을 재사용).
- [x] Course 5: Anomaly Detection 제외, 분류/검출/분할 세 선택지만 유지.
- [x] AND/XOR 분리: Course 7·8; 각각 진리표, 좌표 분리 직관을 시각화.
- [x] Course 11–15: 기존 얼룩말 CNN Architecture 출처 Figure + 로컬 대체도 / Kernel 입력→출력 Matrix / Sharing·Channel 목적 설명.
- [x] Course 17·18: 같은 입력 Padding 0/1 및 Max Pooling 사용 목적 설명.
- [x] Course 24·25: 슬라이드 속 슬라이드 구조 제거, 동일 사과의 HTML 사진 변환 비교.
- [x] Course 28·30: Forward/Backward 학습 그림 정렬, Backbone Freeze/Head Train Transfer Learning.
- [ ] **실제 UI QA:** 두 발표 화면 크기 1920×1080/1366×768 × 55장 = **110개 화면**. 특히 C7/8, 11, 12, 17, 24/25, 28, 30에서 도형 간격·글자 가독성 확인.
- [ ] **외부 Figure 로딩/대체:** 기존 얼룩말 Figure 로딩 실패 시 로컬 CNN Fallback을 실제 브라우저에서 확인. 원본 이미지 보일 때와 막힐 때 모두 그림·출처·텍스트 잘림 없음.
- [ ] **회귀/배포:** Gate/Kernel/Padding/Pooling의 숫자, Course26 Weight 실습, Course40 Threshold 교육용 100건, 목차 55개 및 Pages Workflow 성공과 실 URL 검증.
- [ ] **2시간 리허설:** AND/XOR 설명을 별도 슬라이드로 나눠도 CNN32분/120분 강의 목표를 유지하는지 현장 시연.

**변경 확인:** [2026-10-19 그림·강의 수정 리뷰](reviews/2026-10-19_CNN_SLIDE_REFINEMENT.md). 앞의 50장·54장 지침은 과거 작업 기록이다.

## 2026-10-18 · 과거 54장 후속 작업 (이력)

- [ ] **F54-P0-01 / Course 5:** Task·Model·Label 4열 Figure를 1366×768, 1920×1080에서 읽을 수 있는지 확인; 필요하면 본문 압축 및 핵심 3 Task 우선.
- [ ] **F54-P0-02 / Course 27:** 새 CNN 학습 SVG의 Forward/Backward 방향·Gradient와 Kernel/Head 연결·Freeze 조건을 실제 렌더링으로 확인.
- [ ] **F54-P0-03 / Intro 3·13:** 사과/회랑 이미지와 밝기·회전·가림 화면상 변환의 이미지 크기/출처·개념 vs 실제 출력 구분 확인.
- [ ] **F54-QA / 전 구간:** 13+41=54개 슬라이드, 54개 목차, 두 해상도 **108개 화면**, 54장 이전/다음, C25 가중치 학습 버튼, C39 임계값 선택 및 계산, PDF 아닌 HTML 자산 경로, Pages 공개 배포 Workflow 점검.
- [ ] **F54-P1 / 발표 흐름:** I9–13 반복 설명 최소화, C2–5 규칙/발전/선택/Label 역할 구분, C22 Video Group Split과 사과 검사 연결, C36 IoU로 넘어가는 이유 보완, 마지막 5장 5분 리허설.

**상세 수정 명세:** [Vision AI 54장 전수 내용·흐름 재검토서](reviews/2026-10-18_VISION_AI_54_SLIDE_FLOW_REVIEW.md) (각 장 역할 및 우선순위·완료 조건).

## 상태 범례와 작업 규칙

- `[ ]` 미완료 / `[x]` 근거를 검증해 완료. PR Merge만으로 실제 UI·배포 QA를 완료로 표시하지 않는다.
- P0: **교육 핵심 또는 연속성이 부족한 부분** — 우선 해결. P1: 표현 정확성·시각적 완성도 향상. QA: 전체 수정 후 필수 회귀 검사.
- 각 항목은 **왜 필요한지 → 그림에 무엇을 표현할지 → 완료 판정**을 기준으로 한다.
- 공통 사과 결함 시나리오를 중심축으로 유지한다. 사진이 강아지로 바뀌면 **실제 측정 Feature Map/이미지 변환 자료를 보여주기 위해서**라고 이유를 설명한다.
- 실제 측정 결과, 사진 변환 결과, 생성/재구성한 교육용 개념도, 고정 예제 숫자를 구분한다. **직접 재사용한 외부 사진·Figure만 슬라이드 가까이에 출처**를 명시한다.
- 기존의 숫자 정확성·Pixel/RGB/해상도·학습 버튼·Threshold 상호작용과 레거시 `docs/ai_basics.html`, `docs/vision_ai.html`은 보존한다.
- 슬라이드 기본 구조: **간결한 제목 → 왜 지금 필요한가(부제) → 크게 보이는 Input/Process/Output Figure → 결과 한 문장**. 16:9 교실 화면에서 글자·선·숫자가 겹치지 않아야 한다.

---

## P0 · 강의 원리 설명과 사례 연결

### P0-01 · 실제 사진에서 Kernel로 연결 (Course 9 · `data-concept="kernel"`)

- [x] 사과 원본 사진의 작은 관심 영역(ROI)을 확대해서, **사진 속 어느 영역을 보고 있는지** 보이는 중앙 Figure로 변경한다.
- [x] ROI → Pixel 격자 → 3×3 Kernel → 반응값 **−6** 계산을 단계별로 연결한다.
- [x] **기존 교육용 5×5 배열은 실제 사과 JPEG에서 추출한 값이 아님**을 정확히 표시한다. 실제 이미지의 숫자로 보이게 하려면 그 ROI에서 직접 값을 계산하고 수식 전체를 다시 검증한다.
- [x] Kernel은 손으로 미리 정한 필터만 뜻하지 않고 CNN에서 **학습으로 바뀔 수 있는 Weight**임을 짧게 예고한다.
- **완료 기준:** 사진 속 ROI와 격자 위치가 혼동되지 않음. 기존 예제 사용 시 5×5 입력과 3×3 Kernel의 좌상단 출력 `−6`이 유지됨. 표기·색·눈금이 1366×768에서도 읽힘.

### P0-02 · Kernel 이동과 Feature Map 대응 (Course 10 · `feature-map`)

- [x] Course 9와 **동일한 5×5 숫자/3×3 Kernel/색상 체계**를 사용하고, 오른쪽 한 칸 이동하는 연산을 입력 격자의 선택 위치로 보여준다.
- [x] 첫 두 출력 `−6, 12`와 최종 3×3 결과 `[[-6,12,16],[-6,8,15],[-4,2,7]]`를 이동 위치와 연결한다.
- [x] Feature Map이 입력 RGB 사진의 축소판이나 사람이 지정한 결함 Mask가 아니라 **필터가 위치별로 계산한 반응 지도**임을 구분한다.
- **완료 기준:** 초보자가 그림만 보고 “같은 Kernel을 옮기면 출력 위치가 하나씩 채워진다”고 설명할 수 있고, C9/C10/C13의 숫자 대응이 동일하다.

### P0-03 · Intro 예시의 일관성 (Intro 10–11 · `diversity`, `relevant-change`)

- [x] 의자 4종과 균열 표면에서 사과 검사로 전환되는 끊김을 줄인다. **가능하면 동일 객체인 사과의 종류·품종·촬영조건과 작은 결함**으로 교체한다.
- [x] 정상/불량 기준을 **'사과 표면의 지정된 결함(예: 갈색 반점)'**으로 명확히 합의하고, 큰 조명 변화와 작은 결함의 차이를 같은 대상·유사한 Crop·비슷한 크기로 비교한다.
- [x] 생성 사진을 사용하면 **교육용 생성 예시**임을 표시하고, 서로 다른 원본을 **한 원본의 픽셀 변화 실험**이라고 주장하지 않는다.
- [x] Intro 11 → Course 1(같은 사과로 Classification/Detection/Segmentation) 전환 설명을 짧게 붙인다.
- **완료 기준:** I10→I11→C1에서 갑작스러운 객체/결함 기준 변경 없이 “중요한 특징은 Task·Label에 따라 달라진다”로 연결.

### P0-04 · 데이터셋을 '정답×촬영 조건'으로 표현 (Course 18 · `dataset`)

- [x] **정상/불량 × 밝음/어두움** 2×2 사진형 비교를 만든다. 지금처럼 같은 불량 사과 한 장을 색상·배경만 바꾼 3패널 설명으로 끝내지 않는다.
- [x] 배경·조명으로 우연히 Label을 맞히는 Shortcut Learning을 **두 클래스의 촬영조건 균형**과 연결해 설명한다.
- [x] 애매한 경계 사례의 Label 규칙, 정상과 불량 데이터 수의 균형, 독립적인 촬영 조건을 간단히 표시한다.
- **완료 기준:** 그림 안에 정상/불량 **양쪽 Class**가 나타나며, 밝기·배경 때문에 오인하는 구체적 이유가 한눈에 보임.

---

## P1 · 핵심 Figure와 설명의 완성도

### P1-01 · 선택지 자체보다 실제 출력 비교 (Course 3 · `model-choice`)

- [x] 사과 사진을 세 번 단순 반복하지 말고 **규칙 → 결과**, **기존 모델 → 내 결함 검출 가능 여부**, **Label + 추가 학습 → 목표 결과**의 3경로로 변경한다.
- [x] ‘사과를 검출한다’와 ‘사과의 작은 결함을 판정한다’는 서로 다른 Task임을 나타낸다.
- **완료 기준:** 수강생이 각 경로에서 어떤 결과를 확인하고 언제 학습을 선택할지 설명 가능.

### P1-02 · CNN 전체 Architecture의 전문성 (Course 8 · `cnn-overview`)

- [x] 현재 입체 Feature Map 개념도의 **입력 크기(H×W×3), 공간 해상도 변화(H′/W′), 채널 수(C), Conv+ReLU 반복, Head 출력**의 관계를 점검하고 기술적인 단면 Figure로 다듬는다.
- [x] ‘공간 축소는 가능하지만 모든 CNN/층에서 항상 일어나지는 않는다’는 정확성을 유지한다.
- [x] 실측 모델 구조가 아닌 경우 **개념적 CNN 구조**라고 표기한다.
- **완료 기준:** 구조도만 보고 사진→특징→판정 순서와 공간/채널 변화를 구분할 수 있으며 실제 모델 Architecture와 오인하지 않는다.

### P1-03 · RGB vs Feature Channel 명확성 (Course 12 · `channels`)

- [x] RGB 3채널 × 서로 다른 **3×3×3 필터 2개** → Feature Map 2장의 **병렬 연산**을 더 명확하게 시각화한다.
- [x] Filter A/B가 **같은 RGB 입력**을 각각 읽는다는 연결선을 정확히 연결한다.
- **완료 기준:** 출력 Feature Channel이 단순한 R/G/B 분해도 아니고, Filter A 출력에 Filter B를 연속 적용한 결과도 아님.

### P1-04 · Stride/Padding/Pooling의 입력·출력 변화 (Course 13–15 · `stride`, `padding`, `pool`)

- [x] Stride 1 vs 2의 **Kernel 시작 위치 9곳 vs 4곳**, 출력 3×3 vs 2×2를 격자로 나타낸다.
- [x] Padding 예제는 앞 Kernel 예제에서 **입력과 가중치를 바꿨다는 사실**을 명시하고, 바깥에 새로 생긴 0 셀과 출력 크기를 대비한다.
- [x] Pooling은 **4×4→2×2**, 채널별 영역 최댓값 `[[6,4],[7,9]]`와 위치정보 손실을 그림에 표현한다. 학습되는 Conv Weight와 혼동하지 않는다.
- **완료 기준:** 각 연산의 ‘왜 사용/무엇이 변함’을 수식 암기 없이 말할 수 있으며 숫자는 기존 검증과 일치.

### P1-05 · 앞부분 Pixel Figure를 실제 발표용으로 마무리 (Intro 3–7)

- [x] 사람의 사진 ↔ 컴퓨터의 동일 사과 수치 대응을 같은 크기의 Panel에서 볼 수 있는지 확인한다.
- [x] 사진 클릭 6×6 / Grayscale / RGB 3채널 숫자와 해상도 비교를 **실제 브라우저**에서 조작하고 값·좌표를 대조한다.
- [x] RGB 표기에서 **614,400 Pixel 위치 vs 1,843,200 채널 숫자** 구분 유지.
- **완료 기준:** 클릭·재설정·원본 로딩이 정상이고, 픽셀·숫자·밝기 Panel이 1366×768에서 겹치지 않는다.

### P1-06 · 실측 CNN 자료와 사과 예시를 연결 (Course 16–17, 21–22)

- [x] SqueezeNet Feature Map은 **실제 계산 결과의 일부 채널 4장**임을 형태/전체 Tensor와 구분한다. 강아지 사진이 등장하는 이유를 명시한다.
- [x] Backbone/Head를 Class/Box/Mask의 차이로 Intro의 **같은 사과 결함 Task**에 다시 연결한다.
- [x] Preprocessing/Augmentation의 강아지 사진은 외부 원본 출처를 유지하며 Intro의 ‘축소하면 작은 결함이 사라짐’·‘Label 보존’으로 연결한다.
- **완료 기준:** 개념 Figure·실제 모델 출력·사진 변환의 종류가 명시되고, ‘실제 강아지’ 자료를 ‘사과 모델의 실제 출력’이라고 오인하지 않는다.

### P1-07 · 평가 사례의 시각적 연결 (Course 30–34)

- [x] 임계값 → TP/FN/FP/TN → Accuracy/Precision/Recall을 **같은 100건**의 동일 표식·색상·용어로 연결한다.
- [x] `TP18/FN2/FP4/TN76` → `Accuracy94%`, `Precision81.8%`, `Recall90%` 숫자를 보존하고, “정상 80/불량 20” 분포와 대응한다.
- [x] IoU는 영역 예측 성능을 보는 **다른 Task의 지표**이며 사과 결함 분류의 Accuracy/Recall과 같은 의미가 아님을 시각적으로 분리한다.
- **완료 기준:** 분모가 다른 Precision·Recall의 차이를 그림만으로 설명 가능하고, 임계값 예시는 검증 데이터/교육용 예시임을 유지한다.

### P1-08 · Threshold 동적 혼동행렬 (Course 37 · `project-run`)

- [x] 기존 `docs/project_course.js`의 계산 결과와 연동해 **2×2 Confusion Matrix**와 FN·FP 변화 Bar/화살표를 동기화한다.
- [x] `0.30 → TP20/FN0/FP30/TN50`, `0.50 → TP18/FN2/FP4/TN76`, `0.70 → TP11/FN9/FP2/TN78` 확인. Precision/Recall도 함께 갱신.
- [x] Test 데이터로 임계값을 반복 최적화하지 않는다는 원칙 유지. 이 점수는 **실제 모델 평가가 아닌 교육용 100건**임을 계속 표시.
- **완료 기준:** 드롭다운 선택이 숫자·Matrix·시각적 강조를 한 번에 갱신하며 JS 오류가 없다.

### P1-09 · 마지막 5장의 원리 복습 (Course 35–39)

- [x] 35는 **사진→Task/Label→CNN→학습→평가→개선** 흐름을 한 장의 큰 Figure로 정리한다.
- [x] 36은 사과 사진과 ‘정상/불량 Label·촬영 조건·평가 기준’을 큰 도식으로 놓고 실무 작업명세 텍스트는 보조로 내린다.
- [x] 38의 3가지 교육용 실패 사진은 **실제 관찰한 실패 데이터가 아닌 가설 사례**임을 명확히 하고, 어떤 조건을 다시 비교할지 한 문장씩만 제시한다.
- [x] 39의 설치·실행·운영 체크리스트 비중을 줄이고 **처음 사과 사진으로 돌아와 원리를 설명할 4가지 질문**(입력, 특징, 학습, 평가)으로 끝낸다.
- **완료 기준:** 마지막 6분이 ‘AI 협업 실무 프로세스’로 새어나가지 않으며 교육 목표 A를 직접 복습한다.

---

## QA · 전체 강의 검증 (콘텐츠 수정 후 필수)

### QA-01 · 50장 실제 렌더링과 가독성

- [x] 로컬 웹서버로 강의를 열고 `scripts/audit_visual_slides.py` 실행. **1920×1080과 1366×768 × 50장 = 총 100개 화면** 스크린샷 및 문제 목록 생성.
- [x] 특히 I3–7/I10–11, C8–15/C18/C35–39의 Title, Matrix 숫자, 라벨, 선, Crop, 하단 Takeaway가 프레임 밖으로 나가지 않는지 실제 렌더 결과로 확인.
- [x] 글자 크기를 과도하게 줄여 문제를 숨기지 않는다. 슬라이드당 한 메시지·시각 자료 우선 기준 유지.
- **완료 기준:** 잘림/본문 중첩/미로드 이미지/과도한 축소가 **0건**. 결과 스크린샷과 조사 기록을 보존.

### QA-02 · 모든 상호작용과 목차 탐색

- [x] `scripts/verify_learning_routes.py` 실행: Intro→Course 연결, 50개 목차 이동, 50장 순차 다음/이전 이동, 구버전 URL 호환.
- [x] Intro 클릭 Pixel의 좌표·실제 값, RGB, 해상도 Crop, **Course 23** Weight `0.5→1.7`/Loss `9→0.36`, **Course 37** Threshold `0.30/0.50/0.70`를 실제 클릭으로 확인.
- [x] 브라우저 Console Error 0건, 접기/펼치기 복습, 좁은 화면 목차와 키보드 조작 확인.
- **완료 기준:** 실제 Chromium 테스트가 성공하고 실패 시 재현 가능한 Slide 번호·스크린샷 첨부.

### QA-03 · 정적·수치·출처 검사

- [x] `python scripts/verify_curriculum_overhaul.py` 및 `python scripts/verify_two_hour_course.py` 실행.
- [x] `docs/two_hour_manifest.json`(Intro 11 + Course 39), `docs/lecture_outline.js`(전역 1..50), 각 `data-concept`·Title·Slide 번호/100뷰 예상값 일치 확인.
- [x] 5×5 입력/3×3 Kernel의 **[-6,12,16;-6,8,15;-4,2,7]**, Padding, Pooling, 100건 평가의 TP/FN/FP/TN 재계산.
- [x] 내부 이미지 URL 실제 존재, 외부 직접 사용 이미지(출처 명시), 새 CSS/JS Cache Key 갱신 및 공통 CSS 적용 시 레거시 페이지 영향 확인.
- **완료 기준:** 정적 검사 성공 + 실제 파일 경로·출처 누락 0건.

### QA-04 · 배포와 현장 최종 점검

- [x] 사용자가 승인한 Git 병합·push 후 `main` Commit과 실제 파일 SHA를 재조회하고, GitHub Pages **Deploy Workflow 성공** 여부 확인.
- [ ] 공개 URL `https://sh0427-han.github.io/vision_ai_lecture/`와 `.../vision_ai_course.html#slide-8` 등에서 바뀐 그림, 그림 크기·Cache Key·이미지 로딩 확인.
- [x] 현장 리허설 실행표 준비: [시간표·4질문 평가표](reviews/2026-10-18_VISION_AI_REHEARSAL.md). 시간 배분 110+10분, CNN 30분, 복습 6분 검산 완료. 실제 발표 결과가 아님.
- [ ] 120분 실제 발표 흐름 리허설: 강의 120분(별도 Q&A 없음), CNN 핵심 32분, 마지막 복습 6분; 초보 수강생이 4가지 목표 질문에 답할 수 있는지 확인.
- **완료 기준:** 배포 성공 기록과 실제 렌더 검증, 최종 강의 리허설 기록. `main` 병합만으로 완료 체크하지 않는다.

---

## 최근 완료된 기반 작업 (다시 하지 말 것)

- [x] 사용자 **A안 원리 중심** 확정. 50장 공개 강의를 **Intro → Task → 신경망 → CNN → 데이터 → 학습 → 평가 → 복습**으로 재배치 (PR #101).
- [x] 학습/Loss/Inference를 CNN 뒤 Course 23–25로 이동. CNN Architecture 선행 배치 (Course 8).
- [x] Course 11의 Dense/Local/Shared 비교와 Course 12의 RGB→병렬 필터 구조를 HTML/SVG로 1차 개편.
- [x] 교육용 숫자·기존 실습을 유지한 상태로 PR #101의 **정적** 섹션/목차·수치·로컬 자산 교차 확인.
- [x] **실제 Chromium 로컬 검증 완료**: 100화면·전체 탐색·Pixel/RGB·학습/Threshold 검사 통과.
- [x] **main Git 병합 및 Pages 배포 성공**: `9822c11`, [배포 실행](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39130465056).
- [ ] **Pages 공개 URL 직접 검증·현장 리허설**은 별도 미완료 (QA-04 참고).

## 참고 문서와 작업 순서

1. **현재 운영 기준:** [2시간 강의 운영안](TWO_HOUR_LECTURE_PLAN.md) · [프로젝트 가이드](PROJECT_GUIDE.md) · `docs/two_hour_manifest.json`
2. **미반영 권고의 원본:** [내용·흐름 검토](reviews/2026-10-18_VISION_AI_CONTENT_FLOW_REVIEW.md) · [UI/Figure 검토](reviews/2026-10-18_VISION_AI_UI_FIGURE_REVIEW.md)
3. **이전 수정 내역:** [원리 중심 개편 구현 기록](reviews/2026-10-18_VISION_AI_PRINCIPLES_IMPLEMENTATION.md)
4. **수정 순서:** **P0-01/02 → P0-03/04 → P1-01~09 → QA-01~04**. 슬라이드 번호 이동 시 위 목록과 운영안·목차를 동시에 수정한다.
5. **GitHub 절차:** 최신 `main` 확인 → 작업 브랜치 → 파일·자산 수정 → 정적·브라우저 검증 → PR → Merge → `main` 재조회 → Pages Workflow와 배포 파일 확인.

## Markdown 정리 결정 (2026-10-18)

- **활성 TODO:** 이 파일 하나를 작업 시작점으로 사용.
- **삭제 완료 (이번 정리 PR):** `TODO_INTRO_RGB_TENSOR.md`(스스로 Legacy/Superseded 명시, 2026-09 이전 요구 기준), `LECTURE_REVIEW.md`(46장 기준 구버전 진단, 현행 두 50장 검토서로 대체). 변경 이력은 Git History/PR에서 복구 가능.
- **보존:** `PROJECT_GUIDE.md`, `AGENTS.md`, `HTML_DESIGN_RULES.md`, `CHATGPT_PROJECT_INSTRUCTIONS.md`, `TWO_HOUR_LECTURE_PLAN.md`, `assets/SOURCES.md`, 개별 장별 노트 및 현재 50장 검토·구현 기록.
- **과거 자료로 보존하되 현행 번호로 실행하지 않음:** `REFERENCE_VISION_AI_SOURCE_LIBRARY.md`(외부 논문/강의 출처 DB), `REFERENCE_SLIDE_SOURCE_MAP.md`(옛 69장 매핑). 출처 목록이 유용하므로 제거하지 않고 구버전 표시.

## 후속 사용자 승인 · 2026-10-18

PR API 차단이 지속되어 사용자가 기존 방식의 Git push 및 merge를 요청했다. 이에 작업 브랜치를 로컬 main에 병합하고 일반 push로 반영한다. 기존 PR 절차의 이번 작업 예외이며, 공개 URL 검증과 실제 수강생 리허설은 수행 근거가 있을 때만 완료 처리한다.

## 2026-10-19 · 얼룩말 특징 비유 및 전이학습

- [x] C11 Architecture 바로 뒤 C12 `cnn-why` 추가: 작은 특징 조합과 사람의 시각 비유의 한계 설명.
- [x] C31 전이학습에 C11 얼룩말 원본 구조 재사용: 특징 추출부 Freeze / 분류 Head 교체·학습 구분.
- [x] Intro13+Course43=56장, 120분 유지; 목차·manifest·현재 번호와 브라우저 탐색 검증.
- [ ] 외부 원본 Figure와 공개 Pages의 실접속 확인: 현재 환경의 네트워크 차단으로 대체 도식 경로만 로컬 확인.
