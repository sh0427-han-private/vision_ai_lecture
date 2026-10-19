# CURRENT REVIEW REPORT — Rule-based vs Machine Learning (P15–P16)

- 검수일: 2026-10-19
- Reviewer: 독립 기술·교육·시각 검수
- 대상 PR: https://github.com/sh0427-han/vision_ai_lecture/pull/113
- 대상 브랜치: `builder/rule-based-ml-approved-p15-p16-20261019`
- 비교 기준: `main` commit `4db8cd14c16fbfe1d2d597d80e10af5867ddf63c`
- 비교 시 공통 조상: `d52f42c0dcfdc60daf51ff69927e2345802fa2da`
- 주의: 비교 응답에 대상 브랜치 HEAD의 전체 SHA는 제공되지 않아 **브랜치 HEAD SHA 미확인**. 검수 내용은 검수 시점의 해당 branch 파일을 기준으로 함.
- 승인 기획 출처: `planning/vision-ai-120min-storyboard-draft-20261019`의 `planning/SLIDE_STORYBOARD.md`, Approved P15/P16. 이 문서는 Builder 브랜치와 main에는 존재하지 않음.
- **최종 판정: CONDITIONAL PASS (정적 검수)** / **발표 화면: NOT VERIFIED**

## 1. 종합 평가

두 슬라이드는 입문자에게 ‘사람이 알고리즘을 직접 지정하는 방법’과 ‘사람이 정답·목표를 주고 데이터에서 가중치를 학습하는 지도 머신러닝’을 비교해 보여준다. P15의 덧셈 계산과 P16의 공통 사과 사례는 핵심 기술 원리를 왜곡하지 않는다. Critical 이슈 0건. 일부 연결 관계와 교육적 표현의 소규모 보완 및 미실행 브라우저 검증이 남았다. **현재 상태는 실화면 검수까지 완료된 PASS가 아니다.**

장점: (1) P15의 단일 함수 `f(a,b)=a+b`가 두 입력에 재사용됨; (2) P16의 좌우에서 같은 사진을 사용해 촬영 조건 차이가 논점이라는 점을 유지함; (3) 수동 Rule도 유효하다고 명시하고 ML의 일반화는 독립 데이터 평가 대상으로 남김; (4) 실제 생성·예측 결과가 아님을 고지함.

## 2. 검수 범위·변경 범위

- 기획: `planning/SLIDE_STORYBOARD.md`(기획 브랜치에서 조회), `TWO_HOUR_LECTURE_PLAN.md`, `PROJECT_GUIDE.md`, `HTML_DESIGN_RULES.md`, `AGENTS.md`.
- 구현: `docs/vision_ai_course.html`의 C01 `task` → C02 `rules` → C03 `rules-image` → C04 `vision-evolution` → C05 `model-choice` 및 C06 `task-model-data`; `docs/rules_vs_learning.css`; 공통 `docs/slide.css`, `docs/lesson.css`; `docs/two_hour_manifest.json`; `docs/lecture_outline.js`; `assets/SOURCES.md`.
- 메인과 Builder 브랜치 비교 결과: **diverged**, ahead 8 / behind 1, 변경 파일 세 개: `docs/vision_ai_course.html`(+30/-22), `docs/rules_vs_learning.css`(+172/-37), `scripts/verify_learning_routes.py`(+15/-5). 이 수치는 GitHub compare API가 반환한 것으로 비교 시점의 branch 간 차이이며 PR 설명만으로 추정한 값이 아님.
- 현행 manifest/outline: Intro 13 + Course 46 = 59장, 비교 대상 Course 2·3은 전역 15·16. Approved 계획은 55장으로 전체 재편을 별도로 예정하나 이번 Builder 범위에는 포함하지 않음. 전체 재편 미구현을 이번 두 장의 결함으로 판정하지 않음.
- 자료: `docs/assets/vision_task_apple_reference.jpg`와 `docs/assets/generated/apple_studio_preview.png` 경로 참조. 후자는 바이너리 직접 조회 불가였으며 실제 로드·화질 미검증. `assets/SOURCES.md`는 사과 사진을 AI 생성 교육 이미지로 명시. P16 하단에도 화면 brightness 변화 및 비실측 사실 표기.
- 검증 방식: GitHub Connector로 소스 텍스트 및 compare 메타데이터 검토. 로컬 Chromium·Playwright에 필요한 브랜치 체크아웃은 네트워크 DNS 문제로 실패. 브라우저 스크린샷, 이미지 로딩, 콘솔, JavaScript 상호작용, 120분 리허설을 **실행하지 않았음**. 공개 Pages는 기본적으로 main 배포이며 미병합 Builder 결과의 렌더링 증거로 사용하지 않음.

## 3. 기술 정확성 평가

### P15 / C02 / `rules` / 전역 15

- `1+1=2`, `2+1=3` 정확. 공통 함수 `f(a,b)=a+b`는 두 결과를 산출한다.
- Figure의 왼쪽 두 입력 → 중앙 단일 규칙 → 오른쪽 각 출력은 SVG 연결선을 이용한다. 입력별 규칙을 두 개 학습한 것처럼 오해시킬 표현 없음.
- ‘명확한 계산 규칙에는 학습이 불필요할 수 있다’는 주장은 해당 예시 범위에서 타당함. 이는 ‘모든 이미지에 Rule-based를 사용할 수 없다’는 주장과 다름.

### P16 / C03 / `rules-image` / 전역 16

- 밝은 불량 / 어두운 불량 / 어두운 정상 예시를 좌우 같은 순서로 배치; `filter: brightness(.48)`는 **CSS 표시 변형**이지 실제 별도 촬영 데이터가 아님.
- Rule-based: `갈색 Pixel 수 ≥ k → 불량?`는 가능한 **가상 임계값 규칙**. k 수치, 픽셀 색상 범위, 실제 판정 결과를 제공하지 않으므로 성능/실패를 계산으로 입증한 사례로 읽어선 안 됨. 현재 질문형 표기와 합성 예시 고지는 이 범위를 대체로 준수.
- 지도 ML: 정답 Label → Training → 학습된 Model; 새 사진 → Inference → Prediction? 순서가 개념적으로 타당. 정확도를 지어내지 않으며 Weight 조정, 목표 및 Model 선택에 사람의 역할을 명시한다.
- `Supervised Learning`을 명시해 ML 전체와 동치로 서술하지 않음. 비지도학습 등 다른 ML 종류는 후반 C34에서 다룸.
- `Validation/Test`는 최종 성능 확인을 위해 분할이 필요하다는 취지에서 적절하지만 두 데이터의 역할을 하나로 읽을 수 있어 국소적 설명 개선 가능.

## 4. 교육 흐름·난이도

- Intro 9~13에서 조명·색감·회전·가림 등 이미지 변화를 소개하고, C01에서 같은 사진에 대해 목표 출력/Label을 제시한 후, C02의 쉬운 산술 규칙 → C03의 이미지 조건 예외로 진입함. 연결의 인과관계는 적절.
- C03에서 C04의 학습 기반 모델 및 사전학습, C05의 Rule/기존 Model/추가 학습 선택으로 이어짐. 승인 Storyboard의 P17은 기존 C04가 아니라 C05로 직접 연결하는 구상이며 **전체 재편 단계에서 Planner가 해결할 차이**임. 이번 두 슬라이드에서 임의로 C04를 제거할 사유가 아님.
- P15는 함수 기호 `f(a,b)`를 단일 예시로 쓰고 별도 수학적 정의를 요구하지 않아 입문 난이도 허용 가능. P16은 Label/Training/Weight/Inference/Validation/Test 용어가 집중되어 있지만 사진과 정답→학습 및 새 사진→추론의 구분을 실제로 소개하는 장이라는 맥락을 고려하면 심각한 과밀이라고 단정하기 어렵다.

## 5. Figure·디자인 품질

- P15 입력 2개, 규칙 1개, 출력 2개를 단일 그리드로 구현. SVG 화살표의 논리 방향 및 결과 대응이 코드상 일치.
- P16 동일 사진 3종 × 2패널과 좌측 규칙 조건/예외/보완, 우측 지도학습/추론/평가 비교는 목적에 부합. 외부 이미지와 실측 이미지가 아니라는 하단 고지 있음.
- 흰색 배경·청록/녹색 강조·카드 스타일은 `slide.css` / `lesson.css` 디자인과 정적 수준에서 일관됨.
- `rules_vs_learning.css`는 `@media (max-height:840px)`에서 카드·이미지 높이와 간격을 줄임. 그러나 `clamp(12px,...)`인 작은 단계 설명 및 Label은 1366×768에서 작게 보일 수 있으며, 공통 JS의 auto-fit이 실제 얼마나 축소하는지 미측정.
- **1920×1080: NOT VERIFIED. 1366×768: NOT VERIFIED.** 두 해상도에서 텍스트 clipping/overflow, CSS 이미지 밝기, 패널의 반응형 정렬, 이미지 로딩/콘솔을 시각적으로 판정하지 않았음.

## 6. 문제별 우선순위와 수정 지침

### RV-P16-01 — Minor · 학습 모델 재사용 시각 연결

- Slide: P16 / C03 / 전역 16 / `rules-image`
- 위치: `docs/vision_ai_course.html`의 `.rl-learning-path`, `.rl-learning-line` (Training/Model 행과 Inference/Prediction 행).
- 문제: 서로 분리된 두 행에서 학습된 **동일 Model**을 Inference에 사용한다는 연결선이 실제 도형으로 표현되지 않음. 문구에는 ‘같은 모델 적용’이 있으므로 기술적 오류는 아니나 그림만 보는 학습자의 경로 인지가 약해질 수 있음.
- 근거: 첫 행 `사진+Label → Training → 학습된 Model`; 다음 행 `Inference → Prediction?`; 두 행을 연결하는 SVG/화살표 없음.
- 권고: 기존 학습 Model 카드에서 추론 행으로 내려가는 연결선을 추가하거나, 두 행의 Model을 하나의 공통 카드로 시각적으로 연결. **Inference에 실제 새 사진이 입력**되는 문구는 유지하고, 결과는 `Prediction?`로 미측정임을 유지. 이미지를 늘리거나 별도 새 슬라이드 추가는 불필요.
- 담당: **Builder**. 영향: P16의 부분 HTML/CSS.
- 재검증: 시각적으로 Training에서 완성된 하나의 Model이 새 사진 판정에 사용되는 화살표를 따라갈 수 있는지 확인.
- 상태: **Open**.

### RV-P16-02 — Minor · Validation/Test 역할 압축 표기

- Slide: P16 / C03 / 전역 16 / `rules-image`
- 위치: `.rl-learning-check` 문구 ‘독립 Validation/Test’.
- 문제: Validation과 Test가 완전히 동일한 성능 평가 단계인 것처럼 받아들여질 여지. 실제로 Validation은 모델 선택/튜닝 중 활용되고, Test는 최종 독립 평가에 사용된다.
- 근거: 학습/평가 데이터 분할의 표준적인 목적 차이; 후반 C26 `split`에서 자세한 학습 예정.
- 권고: 초반 장표에서 부연이 부담스러우면 ‘학습에 사용하지 않은 별도 데이터로 확인’으로 바꾸고, C26에서 Validation/Test를 구분. 혹은 ‘Validation으로 점검 · 최종 Test로 확인’으로 국소 정정. 이번 장에서 전체 분할 강의를 시작할 필요는 없음.
- 담당: **Builder**. 영향: P16 문구 1곳.
- 재검증: C26의 상세 구분과 모순되지 않는지 점검.
- 상태: **Open**.

### RV-QA-01 — 확인 보류 · 발표 화면 및 실행 환경 검증

- 우선순위: **검증 게이트 / 미검증**, 확인 전 임의로 Critical·Major 오류로 분류하지 않음.
- Slide: P15/P16 / C02/C03 / 전역 15/16, Concept `rules` / `rules-image`.
- 대상: `docs/vision_ai_course.html`, `docs/rules_vs_learning.css`, 공통 CSS·JS, 이미지 파일.
- 사실: 1920×1080 및 1366×768의 실 렌더링, 읽기 크기, 겹침, 이미지 로딩, sidebar navigation, console/runtime 오류를 독립 확인하지 못함.
- 권고: PR 브랜치로 정적 서버 + Chromium/Playwright 실행하여 두 해상도 스크린샷과 element bounding box, `naturalWidth` 및 `document.fonts.ready`, console/pageerror 확인. 전체 59장 회귀는 별도 QA에서 실시.
- 담당: **Builder (실행 자료 제공), Reviewer (독립 확인)**.
- 재검증: 브랜치 기반 캡처·로그 및 독립 실화면 점검.
- 상태: **Open / NOT VERIFIED**.

## 7. Planner / Builder 후속 작업

- **Planner:** P15/P16 자체의 필수 내용·순서 변경 없음. 승인 55장 재편 중 P16→P17(현 C05) 연결 시 현 C04 중복을 해소하는 별도 기존 계획 유지; 이번 Builder 두 장에 범위 확대 지시 불필요.
- **Builder:** RV-P16-01/02 국소 수정 여부 검토, 브랜치 기준 1920×1080·1366×768 렌더/asset/콘솔/탐색 QA 자료 제출. 이 보고서 외 HTML/CSS/JS/자산은 Reviewer가 변경하지 않음.

## 8. 판정 및 통과 조건

**정적 기술·교육 검수: CONDITIONAL PASS.** Critical 0 / Major 0 / Minor 2, 발표 화면 검증 1개 보류. 이슈 둘은 치명적 개념 오류가 아니라 표현 명료성 수준이므로 구현자가 교육 목표를 유지하며 간소한 방식으로 해소 가능.

**시각·실행 검수: NOT VERIFIED.** 실제 1920×1080, 1366×768에서 이미지/텍스트/레이아웃, 내비게이션·콘솔을 확인한 뒤 단원 전체 PASS로 변경 가능. 브랜치 자체가 main과 diverged인 상태이므로 최종 병합 이후 동일 commit 기준으로 회귀 확인할 것.

## 근거 링크

- PR: https://github.com/sh0427-han/vision_ai_lecture/pull/113
- 대상 HTML: https://github.com/sh0427-han/vision_ai_lecture/blob/builder/rule-based-ml-approved-p15-p16-20261019/docs/vision_ai_course.html
- 대상 CSS: https://github.com/sh0427-han/vision_ai_lecture/blob/builder/rule-based-ml-approved-p15-p16-20261019/docs/rules_vs_learning.css
- 기획: https://github.com/sh0427-han/vision_ai_lecture/blob/planning/vision-ai-120min-storyboard-draft-20261019/planning/SLIDE_STORYBOARD.md
