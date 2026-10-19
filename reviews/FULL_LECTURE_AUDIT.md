# Vision AI FULL LECTURE AUDIT

검수일: 2026-10-19 KST | 기준: main 실제 HTML/Manifest | 범위: Intro 13 + Course 46 = **59장**, 120분.

Manifest version: 20261019-arithmetic-rule-vision-learning. Source blob: manifest b939a7bfa7fa1d0a09c13d770300195b31df5651, intro 5bd3c23b5dca748bb54a4b0123e9ae9ca1405b0e, course c2f59fe33f23f4bf1f3997976782f67a669dba01. 승인 기획: planning/vision-ai-120min-storyboard-draft-20261019의 planning/SLIDE_STORYBOARD.md (55장 Approved, 실제 구현 전).

**판정: 정적 콘텐츠 CONDITIONAL PASS / 실제 발표 화면 NOT VERIFIED.** 기술 수치 Critical 오류는 발견하지 못했으나 59장 전체 브라우저 렌더는 시행하지 않았다. 이 보고서의 '유지'는 화면/그림의 최종 PASS가 아니다. 과거 보고서는 대조자료이지 최신 검증의 대체가 아니다.

## 1. 전체 59장 전수 검수표

현재 `main`의 59개 HTML 슬라이드를 기준으로 Concept ID·Title·Subtitle를 실제 코드에서 확인했습니다. 각 Figure 설명은 HTML·자산 경로·SVG 텍스트 기반 **정적 판단**입니다. 발표 1920×1080 / 1366×768 실렌더에서 글자 잘림·그림 겹침·화살표 종점·사진 자체의 가독성은 **전 장 미검증**입니다. P##는 승인 계획 전역 번호이며 아직 `main` 구현 완료가 아닙니다.

| 현재 번호 / Concept ID / HTML 위치 | 기존 제목·핵심 메시지 | 필요성·기술 정확성 | 사진·Figure 구성 및 교육적 적절성(정적) | 전후 연결과 문제 근거 | 유지/수정/이동/통합/삭제 | 승인 55장 계획에서 해결 여부 및 추가 조치 | 우선순위 |
|---|---|---|---|---|---|---|---|
| [1/I01](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L31) `start` | **AI와 시각의 출발점** · 한 장의 사과 사진에서 작은 결함을 찾으려면, 컴퓨터가 이미지를 어떻게 처리하고 학습하는지 알아야 합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`. 중심 사과 사진과 질문만 있고 Vision AI 분석→교육용 출력 관계가 빠져 첫 Figure만으로 역할을 설명하기 어려움 | 도입→I2; 중심 사과 사진과 질문만 있고 Vision AI 분석→교육용 출력 관계가 빠져 첫 Figure만으로 역할을 설명하기 어려움 | **유지** / 수정: P01 실제 출력이 아닌 결함 후보 예시를 표시 | P01: 수정: P01 실제 출력이 아닌 결함 후보 예시를 표시. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [2/I02](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L38) `scene` | **사람의 시각 · 장면 이해** · 우리는 한 장면에서 무엇이 있는지 와 어디에 있는지 를 빠르게 이해합니다. | **필요성:** 독립 장 불필요, 정보 보존. **정확성:** 사람 시각 사례는 I03 필요성으로 흡수 | `intro_photos/perspective.webp`, SVG 1개. 회랑 원근 사진은 사람 시각 예로 정확하지만 중심 사과 품질검사와 직접 대응하지 않아 교육 흐름 이탈 | I1→I3; 회랑 원근 사진은 사람 시각 예로 정확하지만 중심 사과 품질검사와 직접 대응하지 않아 교육 흐름 이탈 | **통합** / 통합: P03 필요성에 흡수 | 55장 계획에서 별도 장 제외: 통합: P03 필요성에 흡수. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [3/I03](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L65) `vision-value` | **Vision AI가 필요한 이유** · 카메라 영상의 중요한 단서를 사람이 매번 찾아야 한다면 시간이 오래 걸립니다. Vision AI는 이미지를 분석해 판단과 확인을 돕습니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`, `intro_photos/perspective.webp`, SVG 1개. 세 가지 활용 카드가 검사·위치·마스크 출력을 보여주지만 '반복 검사→후보 표시→검증' 순차성이 없음 | I2→I4; 세 가지 활용 카드가 검사·위치·마스크 출력을 보여주지만 '반복 검사→후보 표시→검증' 순차성이 없음 | **유지** / 수정: P03 반복 사과 검사 흐름으로 구성 | P03: 수정: P03 반복 사과 검사 흐름으로 구성. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [4/I04](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L77) `photo-numbers` | **사람의 의미 인식 vs Pixel 숫자** ·  | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`, SVG 1개. 동일 사과/12×8 그레이 숫자 비교가 입력과 의미 차이를 설명. 수치 행렬이 실제 crop과 동일한 위치인지는 화면 QA 필요 | I3→I5; 동일 사과/12×8 그레이 숫자 비교가 입력과 의미 차이를 설명. 수치 행렬이 실제 crop과 동일한 위치인지는 화면 QA 필요 | **유지** / 유지 | P04: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [5/I05](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L105) `gray` | **사진에서 밝기 숫자로** · 사과 사진을 48 × 32 크기로 축소해 흑백(Grayscale) 숫자로 변환했습니다. 사진을 클릭하여 다른 6 × 6 영역을 살펴보세요. | **필요성:** 학습 목표상 필요. **정확성:** 0–255 밝기/round/clipping은 타당; 클릭 6×6 실제 값 미실행 | `vision_task_apple_reference.jpg`. 실제 48×32 사진에서 6×6 밝기 숫자와 tile을 연결; 밝기 배율 k까지 함께 제시해 H×W 핵심 분산 가능 | I4→I6; 실제 48×32 사진에서 6×6 밝기 숫자와 tile을 연결; 밝기 배율 k까지 함께 제시해 H×W 핵심 분산 가능 | **유지·검증** / H/W 강조 후 유지 | P05: H/W 강조 후 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [6/I06](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L144) `rgb` | **RGB · Pixel당 세 숫자** · 사진의 한 점을 클릭해 실제 Red · Green · Blue 값을 확인해 보세요. 각각 0~255인 8-bit 값입니다. | **필요성:** 학습 목표상 필요. **정확성:** RGB 3채널 입력은 적절; 클릭 좌표/원본 pixel 값 미실행 | `vision_task_apple_reference.jpg`. 동일 사진 클릭→RGB/선택색 비교, 실제 좌표 연동·로드/키보드 미실행 | I5→I7; 동일 사진 클릭→RGB/선택색 비교, 실제 좌표 연동·로드/키보드 미실행 | **유지·검증** / 유지, 기능 QA | P06: 유지, 기능 QA. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [7/I07](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L185) `hwc` | **RGB 이미지와 숫자 배열** · 가로 960 × 세로 640인 RGB(Red·Green·Blue) 컬러 이미지에서는 각 Pixel마다 색상 값 3개 를 받습니다. | **필요성:** 학습 목표상 필요. **정확성:** 640×960×3=1,843,200 일치 | `lesson/lecture_rgb_channel_stack.svg`. 로컬 RGB Channel SVG와 H×W×3 배열이 대응. 640×960×3 값 일치 | I6→I8; 로컬 RGB Channel SVG와 H×W×3 배열이 대응. 640×960×3 값 일치 | **유지** / 3은 물리적 깊이가 아닌 Channel 축임을 보강 | P07: 3은 물리적 깊이가 아닌 Channel 축임을 보강. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [8/I08](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L199) `resolution` | **해상도에 따른 정보 차이** · 같은 960×640 사진의 중앙 960×540 영역을 세 크기로 축소했습니다. 화면 크기를 같게 맞춰 보면, 작은 세부가 얼마나 남는지 차이가 보입니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | HTML 수치·비교 카드. Canvas 기반 동일 Crop 세 축소 해상도 비교. 확대 ROI가 결함 위치와 겹치는지는 화면 QA 필요 | I7→I9; Canvas 기반 동일 Crop 세 축소 해상도 비교. 확대 ROI가 결함 위치와 겹치는지는 화면 QA 필요 | **유지** / 유지, 렌더 QA | P09: 유지, 렌더 QA. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [9/I09](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L237) `lighting` | **조명·색감에 따른 Pixel 변화** · 앞에서 숫자로 읽은 사과 사진의 밝기·색감을 바꿨습니다. 같은 대상이라도 입력 숫자는 크게 달라집니다. 실제 재촬영 결과가 아닌 화면상 변환입니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`. 같은 사과에 화면상 조명·색감 변환, 실측 재촬영과 구분됨 | I8→I10; 같은 사과에 화면상 조명·색감 변환, 실측 재촬영과 구분됨 | **유지** / 유지 | P10: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [10/I10](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L240) `transform` | **회전·크기·가림·흐림에 따른 변화** · 같은 사과 사진에 회전·크롭 확대·가림·흐림을 적용했습니다. 물체가 같아도 경계와 질감, Pixel의 배치가 달라집니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`. 회전/크롭/가림/흐림이 각각 픽셀 위치 혹은 정보 유실을 낳는 예시 | I9→I11; 회전/크롭/가림/흐림이 각각 픽셀 위치 혹은 정보 유실을 낳는 예시 | **유지** / P11 사례 개수·요점 축약 | P11: P11 사례 개수·요점 축약. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [11/I11](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L243) `diversity` | **다르게 생겨도 같은 종류** · 색·무늬·모양과 촬영 조건이 달라도 모두 사과입니다. 한 모습만 외우면 새로운 사과를 놓칩니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `generated/apple_studio_preview.png`, `vision_task_apple_reference.jpg`, SVG 3개. 사과라는 Class와 표면 결함 Label을 다른 과제로 구분하나 I12와 핵심이 가까움 | I10→I12; 사과라는 Class와 표면 결함 Label을 다른 과제로 구분하나 I12와 핵심이 가까움 | **유지** / P12 Label 2개만 선명하게 대비 | P12: P12 Label 2개만 선명하게 대비. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [12/I12](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L249) `relevant-change` | **큰 변화보다 중요한 차이** · 검사 기준은 표면의 지정된 갈색 반점 유무 입니다. 사과라는 종류가 같아도 이 기준에 따라 정상·불량 Label이 달라집니다. | **필요성:** 학습 목표상 필요. **정확성:** 지정 결함은 구별하고 촬영 변화에는 견고해야 한다는 목표 명확 | `generated/apple_studio_preview.png`, `vision_task_apple_reference.jpg`, SVG 3개. 조명 변화는 무시하되 지정 갈색 반점에는 민감해야 한다는 과제 정의가 분명 | I11→I13; 조명 변화는 무시하되 지정 갈색 반점에는 민감해야 한다는 과제 정의가 분명 | **유지** / P13에서 I13 결론 통합 | P13: P13에서 I13 결론 통합. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [13/I13](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/intro.html#L255) `vision-challenge` | **Vision AI는 왜 어려울까?** · 같은 사과라도 밝기·회전·가림에 따라 입력 Pixel 값과 배치가 달라집니다. 그러나 우리가 찾으려는 결함의 의미 는 가능한 한 유지되어야 합니다. | **필요성:** 독립 장 불필요, 정보 보존. **정확성:** I09–12의 조명·가림·변화 재설명 | `vision_task_apple_reference.jpg`. I09~I12와 동일한 어둠/회전/가림을 새 지식 없이 다시 설명 | I12→C01; I09~I12와 동일한 어둠/회전/가림을 새 지식 없이 다시 설명 | **통합** / P13에 한 문장만 보존 후 독립 장 제외 | 55장 계획에서 별도 장 제외: P13에 한 문장만 보존 후 독립 장 제외. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [14/C01](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L32) `task` | **같은 사진, 다른 질문과 정답** · 사과의 갈색 반점을 결함으로 정했다고 가정합니다. 필요한 결과가 Task(해결할 과제)와 Label(학습용 정답)의 형태를 결정합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`, SVG 2개. 동일 사과에서 Classification/Detection/Segmentation의 Class/Box/Mask 차이를 정확히 시각화 | I13→C2; 동일 사과에서 Classification/Detection/Segmentation의 Class/Box/Mask 차이를 정확히 시각화 | **유지** / 유지 | P14: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [15/C02](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L33) `rules` | **규칙 기반 · 답을 구하는 방법을 사람이 정한다** · 덧셈은 어떻게 계산할까요? 사람이 Python 함수로 규칙을 작성하면, 숫자가 달라져도 같은 코드가 답을 구합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | SVG 2개. 정수 입력 두 종류가 동일 add Python 함수로 처리되는 화살표; 수학 결과 정확 | C01→C3; 정수 입력 두 종류가 동일 add Python 함수로 처리되는 화살표; 수학 결과 정확 | **유지** / 유지 | P15: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [16/C03](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L67) `rules-image` | **이미지 판단 · 규칙을 어디까지 만들어야 할까?** · 같은 질문: 사과에 갈색 반점이 있나요? 덧셈처럼 직접 조건을 만들 수 있을까요, 아니면 정답이 표시된 사진으로 판단 기준을 학습할까요? | **필요성:** 학습 목표상 필요. **정확성:** 비교 사과의 촬영구도 통제·새 사진→동일 Model→예측 연결 불명확; 조건식은 실제로 brown_pixels >= k이며 문법 오류가 아니다 | `vision_task_apple_reference.jpg`, `generated/apple_studio_preview.png`. 실제 if 조건은 brown_pixels >= k로 문법상 올바름. 비교 사진·학습 Weight는 개념 예시이며 독립 새 사진의 추론 경로 없음 | C2→C4; 실제 if 조건은 brown_pixels >= k로 문법상 올바름. 비교 사진·학습 Weight는 개념 예시이며 독립 새 사진의 추론 경로 없음 | **수정** / P16 신사진→동일 학습 Model→Prediction 연결 보강 | P16: P16 신사진→동일 학습 Model→Prediction 연결 보강. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [17/C04](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L107) `vision-evolution` | **지금 Vision AI는 어디까지 왔나?** · 앞서 이미지에서 규칙을 일일이 작성하기 어려운 이유를 봤습니다. 그 문제에 대응하는 Vision AI 접근을 규칙 → Task별 학습 모델 → 사전학습 모델 활용 순서로 비교합니다. | **필요성:** 독립 장 불필요, 정보 보존. **정확성:** 규칙/모델/사전학습 소개가 C05와 중복 | `vision_task_apple_reference.jpg`, SVG 3개. Rule/Task 모델/사전학습 소개는 C05 방법 선택과 중복; SAM2 사례는 대표 예시 | C3→C5; Rule/Task 모델/사전학습 소개는 C05 방법 선택과 중복; SAM2 사례는 대표 예시 | **통합** / P17 통합 | 55장 계획에서 별도 장 제외: P17 통합. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [18/C05](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L118) `model-choice` | **첫 선택 · 어떤 모델을 쓸까?** · 사과를 알아보는 모델이 작은 결함까지 알아보는 것은 아닙니다. 필요한 결과부터 확인합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | HTML 수치·비교 카드. 규칙/기존모델/새 데이터 학습 선택의 근거를 3경로로 비교. C04 내용과 반복 | C4→C6; 규칙/기존모델/새 데이터 학습 선택의 근거를 3경로로 비교. C04 내용과 반복 | **유지** / P17 방식 선택 조건으로 통합 | P17: P17 방식 선택 조건으로 통합. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [19/C06](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L122) `task-model-data` | **내 과제에 맞는 모델과 Label** · 먼저 필요한 출력부터 결정합니다. 같은 사과 사진이어도 분류·검출·분할에 따라 모델과 학습 데이터 가 달라집니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`, SVG 3개. C01 Task 결과와 비슷한 그림을 다시 사용. 이 장은 Label 제작 형식/비용이라는 독립 학습 목적 | C5→C7; C01 Task 결과와 비슷한 그림을 다시 사용. 이 장은 Label 제작 형식/비용이라는 독립 학습 목적 | **유지** / P18 Label 비용 강조 | P18: P18 Label 비용 강조. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [20/C07](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L134) `perceptron` | **퍼셉트론 · 하나의 W와 b로 판정** · 퍼셉트론(Perceptron)은 입력을 계산한 뒤 Step 함수로 0 또는 1 을 결정하는 뉴런 하나 입니다. 여기서는 가장 쉬운 예시로 두 입력에 같은 W 를 적용합니다. | **필요성:** 학습 목표상 필요. **정확성:** 동일 W 두 입력은 일반 뉴런이 아닌 특수 예시; 일반식과 대비 | `lesson/perceptron_one_weight_ko.svg`. perceptron_one_weight_ko.svg에서 x1+x2 뒤 W 한 개를 곱하는 특수형만 시각화; 모든 단일 뉴런 Weight 1개로 일반화 위험 | C6→C8; perceptron_one_weight_ko.svg에서 x1+x2 뒤 W 한 개를 곱하는 특수형만 시각화; 모든 단일 뉴런 Weight 1개로 일반화 위험 | **수정** / P21 일반식 w1*x1+w2*x2+b 추가 | P21: P21 일반식 w1*x1+w2*x2+b 추가. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [21/C08](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L144) `and-rule` | **AND Gate · 두 입력이 모두 1일 때** · AND(논리곱)는 두 조건이 모두 참(1) 일 때만 결과가 1입니다. 스위치 하나라도 꺼져 있으면 0입니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | HTML 수치·비교 카드. AND 네 입력과 Step 퍼셉트론 0,0,0,1 일치 | C7→C9; AND 네 입력과 Step 퍼셉트론 0,0,0,1 일치 | **유지** / 유지 | P22: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [22/C09](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L158) `and-gate` | **AND Gate · Weight와 Bias로 직선 이동** · 두 입력 x₁, x₂를 구분하는 결정 직선입니다. W를 바꾸면 기울기가 회전 하고, b를 바꾸면 위치가 이동 합니다. | **필요성:** 학습 목표상 필요. **정확성:** C07의 동일 Weight와 다른 w₂=1 고정 설정을 시각적으로 구분 | SVG 1개. AND z=Wx1+x2+b에서 w2=1 고정; C07 동일 W 모델과 별개 설정임을 색/범례로 연결 필요 | C8→C10; AND z=Wx1+x2+b에서 w2=1 고정; C07 동일 W 모델과 별개 설정임을 색/범례로 연결 필요 | **수정** / P23 Reset/4점 시각 QA | P23: P23 Reset/4점 시각 QA. 실제 적용·브라우저 검증 전 해결 미확정 | Minor |
| [23/C10](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L159) `xor-rule` | **XOR Gate · 입력이 다를 때만 1** · XOR(eXclusive OR, 배타적 논리합)는 두 입력이 서로 다를 때 만 결과가 1입니다. 둘 다 꺼져 있거나 둘 다 켜져 있으면 0입니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | HTML 수치·비교 카드. XOR 진리표 0,1,1,0과 대각 배치 적합. 바로 뒤 실습에 ReLU 선행지식이 없음 | C9→C11; XOR 진리표 0,1,1,0과 대각 배치 적합. 바로 뒤 실습에 ReLU 선행지식이 없음 | **유지** / P24→P25/P26 선행 | P24: P24→P25/P26 선행. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [24/C11](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L173) `xor-gate` | **XOR · 선형층을 쌓아도 직선 하나** · XOR 정답은 (0,1), (1,0)만 1입니다. 두 선형층의 W를 바꿔도 최종 경계는 하나의 직선으로 기울기만 달라질 뿐 입니다. | **필요성:** 학습 목표상 필요. **정확성:** ReLU 전에 비선형 /t/ 사용; 직선의 위치 변경을 기울기 변경으로 축소 서술 | SVG 1개. 선형합성 Affine. 비선형 /t/ 토글이 ReLU 소개 전 나오고 '기울기만'은 b의 위치 변화를 누락 | C10→C12; 선형합성 Affine. 비선형 /t/ 토글이 ReLU 소개 전 나오고 '기울기만'은 b의 위치 변화를 누락 | **이동·수정** / P27로 이동, 기울기·위치로 수정 | P27: P27로 이동, 기울기·위치로 수정. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [25/C12](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L174) `relu` | **ReLU · 비선형성의 시작** · Activation Function(활성화 함수)은 계산에 비선형성을 넣습니다. ReLU는 입력이 0보다 작으면 0, 크면 입력값을 그대로 출력합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | SVG 2개. max(0,z) 대비 SVG 적합하지만 현 순서에서는 C11에 필요한 설명이 뒤에 있음 | C11→C13; max(0,z) 대비 SVG 적합하지만 현 순서에서는 C11에 필요한 설명이 뒤에 있음 | **유지** / P26으로 선행 이동 | P26: P26으로 선행 이동. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [26/C13](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L194) `nonlinear` | **비선형성 · 깊어져도 직선이면?** · 더하고 곱하는 층을 여러 개 연결해도 한 번의 Affine 변환으로 합칠 수 있습니다. 중간의 ReLU가 이 한계를 바꿉니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | SVG 2개. Affine 합성 vs ReLU 꺾임 도식. C11 이전이면 선수개념 제공 | C12→C14; Affine 합성 vs ReLU 꺾임 도식. C11 이전이면 선수개념 제공 | **유지** / P25로 이동 | P25: P25로 이동. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [27/C14](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L198) `cnn-overview` | **CNN Architecture · 사진에서 분류까지** · Convolutional Neural Network(CNN, 합성곱 신경망)는 Convolution으로 특징을 추출 하고, 마지막 분류기로 결과를 만듭니다. 전체 구조를 먼저 살펴봅니다. | **필요성:** 개념 필요, 선행순서 조정. **정확성:** CNN 이유 C15보다 전체 Architecture C14가 앞섬 | `vision_task_apple_reference.jpg`. 원격 CNN Architecture 배너에 의존, onerror 3단 폴백은 Conv/ReLU/Pool/Shape 전체 계산을 못 보여줌 | C13→C15; 원격 CNN Architecture 배너에 의존, onerror 3단 폴백은 Conv/ReLU/Pool/Shape 전체 계산을 못 보여줌 | **이동** / P20 로컬 상세 모델/Shape 도식으로 교체 | P20: P20 로컬 상세 모델/Shape 도식으로 교체. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [28/C15](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L199) `cnn-why` | **왜 CNN인가? · 특징을 모아 얼룩말을 알아보기** · 사람이 줄무늬와 형태를 모아 얼룩말을 알아보듯, CNN도 작은 특징을 모아 판단합니다. 시각 정보를 얻는 흐름과 유사합니다. | **필요성:** 개념 필요, 선행순서 조정. **정확성:** CNN 전체 구조에 앞서 지역 특징 필요성 설명 권장 | `generated/zebra_feature_photo.png`, SVG 3개. AI 생성 얼룩말 사진의 3단 Crop은 실제 CNN Feature Map이 아님. 중심 사과 결함으로 설명 주제가 이탈 | C14→C16; AI 생성 얼룩말 사진의 3단 Crop은 실제 CNN Feature Map이 아님. 중심 사과 결함으로 설명 주제가 이탈 | **이동** / P19 사과 ROI·반복 Kernel·반응도 교체 | P19: P19 사과 ROI·반복 Kernel·반응도 교체. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [29/C16](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L207) `kernel` | **Kernel · 작은 영역의 가중합** · Kernel(커널)은 작은 가중치 배열입니다. 대응하는 값끼리 곱한 뒤 더하면 한 위치의 반응값 하나가 나옵니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`, SVG 2개. 사과 ROI에서 바로 교육용 5×5 정수로 연결. 숫자는 실제 JPEG Pixel이 아니므로 시각적 오인 가능 | C15→C17; 사과 ROI에서 바로 교육용 5×5 정수로 연결. 숫자는 실제 JPEG Pixel이 아니므로 시각적 오인 가능 | **유지** / P28 합성 숫자/실측 사진 분리 표시 | P28: P28 합성 숫자/실측 사진 분리 표시. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [30/C17](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L208) `feature-map` | **Feature Map · 같은 계산을 위치마다** · 같은 입력과 같은 Kernel을 사용합니다. 가로·세로 한 칸씩 이동해 얻은 숫자들을 위치대로 놓습니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | HTML 수치·비교 카드. 이동 Window①-6/②12가 3×3 map과 수치 일치; 테두리의 실제 화면 매칭 QA 필요 | C16→C18; 이동 Window①-6/②12가 3×3 map과 수치 일치; 테두리의 실제 화면 매칭 QA 필요 | **유지** / 유지 | P29: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [31/C18](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L209) `sharing` | **CNN · 지역 연결과 가중치 공유** · 이전 Kernel을 사진 모든 위치에서 다시 계산할 때 같은 Weight 9개를 공유 하면 어떤 이점이 있을까요? 지역 연결과 가중치 공유의 이유를 비교합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | SVG 3개. FC1048576, local9216, shared9 수치 정확. 세 구조 표현력이 같지는 않음 | C17→C19; FC1048576, local9216, shared9 수치 정확. 세 구조 표현력이 같지는 않음 | **유지** / 유지 | P30: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [32/C19](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L214) `channels` | **RGB에서 Feature Channel까지** · 앞 장의 Kernel을 여러 개 사용한다면? 각 필터는 같은 RGB 3채널 입력을 보고 다른 특징 지도 한 장 을 만듭니다. 필터 개수가 출력 Channel 수를 정합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | SVG 1개. 3×3×3 Filter A/B가 각각 Feature Map 1개를 출력하는 병렬 SVG. 전체 CNN 지도와 용어 통일 필요 | C18→C20; 3×3×3 Filter A/B가 각각 Feature Map 1개를 출력하는 병렬 SVG. 전체 CNN 지도와 용어 통일 필요 | **유지** / P31 색/Shape 통일 | P31: P31 색/Shape 통일. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [33/C20](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L217) `stride` | **Stride · 계산 위치의 간격** · 앞의 5×5 입력과 3×3 Kernel을 그대로 씁니다. Kernel의 왼쪽 위 시작 위치를 한 칸 또는 두 칸씩 이동합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | HTML 수치·비교 카드. 5×5/K3에서 S1 3×3, S2 2×2와 값 일치; 위치 강조와 최종 셀 시각 QA 필요 | C19→C21; 5×5/K3에서 S1 3×3, S2 2×2와 값 일치; 위치 강조와 최종 셀 시각 QA 필요 | **유지** / 유지 | P32: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [34/C21](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L218) `padding` | **Padding · 같은 입력, 다른 출력 크기** · Padding을 사용하면 입력 바깥에 0을 더해 가장자리도 중심으로 계산 하고, Stride 1에서 출력의 크기가 줄어드는 것을 막을 수 있습니다. | **필요성:** 학습 목표상 필요. **정확성:** Padding0 1×1=45; Padding1 출력 12/21/16,27/45/33,24/39/28 정확 | HTML 수치·비교 카드. P0 45, P1의 3×3 값은 정확. '가장자리도 중심으로 계산' 문구는 오해 가능 | C20→C22; P0 45, P1의 3×3 값은 정확. '가장자리도 중심으로 계산' 문구는 오해 가능 | **유지** / 경계 위치 계산 가능으로 국소 수정 | P33: 경계 위치 계산 가능으로 국소 수정. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [35/C22](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L219) `pool` | **Max Pooling · 영역별 최댓값** ·  | **필요성:** 학습 목표상 필요. **정확성:** 4×4→2×2 MaxPool 결과 6,4,7,9 정확 | HTML 수치·비교 카드. 2×2/S2 Max Pool 수치 정확, '절반'이 모든 Pool 설정에 적용되는 것은 아님 | C21→C23; 2×2/S2 Max Pool 수치 정확, '절반'이 모든 Pool 설정에 적용되는 것은 아님 | **유지** / 예제 조건 한정 표시 | P34: 예제 조건 한정 표시. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [36/C23](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L227) `actual-map` | **실제 Feature Map · CNN 내부 반응** · 실제 계산된 반응을 보기 위해 강아지 사진 자료를 사용합니다. ImageNet 사전학습 SqueezeNet 1.1의 출력이며, 사과 결함 모델의 결과가 아닙니다. | **필요성:** 학습 목표상 필요. **정확성:** 실측 SqueezeNet feature의 stage, channel, 정규화·입력 사진 대응 실렌더 검증 필요 | `lesson/cnn_squeezenet_actual_feature_maps.png`, SVG 4개. SqueezeNet1.1의 실제 강아지 Feature Stage로 사과 합성 학습과 구별. 색상은 채널별 분위수 조정됨 | C22→C24; SqueezeNet1.1의 실제 강아지 Feature Stage로 사과 합성 학습과 구별. 색상은 채널별 분위수 조정됨 | **유지·검증** / 실험 출처·원본 PNG 렌더 별도 QA | P35: 실험 출처·원본 PNG 렌더 별도 QA. 실제 적용·브라우저 검증 전 해결 미확정 | Minor |
| [37/C24](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L252) `backbone` | **Backbone과 Task Head** · 같은 사과 사진에서 특징을 모으는 부분이 Backbone입니다. 갈색 반점의 유무(Class)·위치(Box)·모양(Mask)에 따라 마지막 Task Head를 선택합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `lesson/lesson_backbone_head_roles.svg`. 사과 사진→Backbone→Task Head 세 가지 분기 SVG; 동시 출력이 아닌 선택 예시 주석 있음 | C23→C25; 사과 사진→Backbone→Task Head 세 가지 분기 SVG; 동시 출력이 아닌 선택 예시 주석 있음 | **유지** / Head 선택 지점의 시각 강조 | P36: Head 선택 지점의 시각 강조. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [38/C25](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L258) `dataset` | **데이터셋 · 어떤 사진으로 배우나** · 사과의 결함 여부를 배우려면 정답 기준뿐 아니라 조명과 배경이 다른 사진도 준비해야 합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `generated/apple_studio_preview.png`, `vision_task_apple_reference.jpg`, SVG 4개. 정상/불량×밝음/어두움 2×2 생성 사진으로 Shortcut 위험 설명. 실제 독립 촬영 증거 아님 | C24→C26; 정상/불량×밝음/어두움 2×2 생성 사진으로 Shortcut 위험 설명. 실제 독립 촬영 증거 아님 | **유지** / 유지 | P37: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [39/C26](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L259) `split` | **Train · Validation · Test** · Train은 가중치 학습, Validation은 모델·설정·Threshold 선택, Test는 최종 일반화 평가에 사용합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `lesson/context_dataset_split.svg`. Train/Val/Test 각 역할과 1000장 700/150/150 분할 정확. Video Group은 후속 장에서 보완 | C25→C27; Train/Val/Test 각 역할과 1000장 700/150/150 분할 정확. Video Group은 후속 장에서 보완 | **유지** / 유지 | P38: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [40/C27](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L265) `leakage` | **Video Group Split · 데이터 누출 방지** · 동일한 원본 영상 A·B·C에서 각각 3개 Frame을 뽑은 예시입니다. 무작위 Frame 분할과 원본 Video를 통째로 나누는 Group Split을 비교합니다. | **필요성:** 학습 목표상 필요. **정확성:** Video Frame의 시간축 도입 없이 Video Group Split 등장 | `lesson/lesson_video_group_split_comparison.svg`. A1/B1/C1 등 문자 Frame의 랜덤/그룹 분할 도식이나 앞서 T 시간 축과 Frame 자체를 설명하지 않음 | C26→C28; A1/B1/C1 등 문자 Frame의 랜덤/그룹 분할 도식이나 앞서 T 시간 축과 Frame 자체를 설명하지 않음 | **수정** / P08 Frame 신규+P39 사과 그룹 이미지 | P39: P08 Frame 신규+P39 사과 그룹 이미지. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [41/C28](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L271) `augment` | **Data Augmentation · 같은 정답, 다른 조건** · Train 사진에 밝기·회전 등의 변화를 만들어 촬영 조건이 달라도 중요한 결함을 찾도록 학습시킬 수 있습니다. 단, Label이 바뀌면 안 됩니다. | **필요성:** 학습 목표상 필요. **정확성:** Train-only 증강과 Box/Mask 보정 원칙 명시 | `vision_task_apple_reference.jpg`. Train-only 증강과 회전 시 Box/Mask Label 정합성, 결함을 가리지 않을 것이라는 한계 정확 | C27→C29; Train-only 증강과 회전 시 Box/Mask Label 정합성, 결함을 가리지 않을 것이라는 한계 정확 | **유지** / 유지 | P40: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [42/C29](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L272) `learn` | **모델 학습 · 오차를 줄이는 반복** · 학습은 모델 내부의 숫자 Weight(가중치)를 바꾸는 과정입니다. 먼저 사진 대신 입력 x=2, 정답 y=4인 아주 작은 회귀 문제로 원리를 확인합니다. | **필요성:** 학습 목표상 필요. **정확성:** 단일 x=2,y=4,w=.5; Loss9 교육용 예제, JS 단계 미실행 | HTML 수치·비교 카드. 1차원 회귀 예시 자동 Gradient 갱신·Loss 값은 맞지만 Step/Auto/Reset 실실행 미확인 | C28→C30; 1차원 회귀 예시 자동 Gradient 갱신·Loss 값은 맞지만 Step/Auto/Reset 실실행 미확인 | **유지·검증** / 기능 QA | P41: 기능 QA. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [43/C30](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L303) `loss` | **Loss · 틀린 정도를 줄이는 방향** · 방금 학습 실습의 숫자입니다. 예측과 정답이 다를 때 Weight를 어느 방향으로 바꿀지 Gradient가 알려줍니다. | **필요성:** 학습 목표상 필요. **정확성:** Gradient=-12, w'=1.7, Loss'=0.36 정확 | HTML 수치·비교 카드. Grad=-12, Weight 1.7, Prediction3.4, Loss0.36 계산 정확 | C29→C31; Grad=-12, Weight 1.7, Prediction3.4, Loss0.36 계산 정확 | **유지** / 유지 | P42: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [44/C31](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L308) `cnn-training` | **CNN 학습 · 예측에서 Weight 갱신까지** · 사과 사진의 Forward(예측) 결과를 정답과 비교해 Loss를 계산합니다. Backward(역전파) 와 Optimizer가 학습 대상 Weight를 갱신합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`. Forward Prediction과 Backward Loss/Gradient/Optimizer가 별도 패널; 실제 Conv Kernel·Head의 Weight로 돌아가는 선이 약함 | C30→C32; Forward Prediction과 Backward Loss/Gradient/Optimizer가 별도 패널; 실제 Conv Kernel·Head의 Weight로 돌아가는 선이 약함 | **유지** / P43 갱신 대상 Weight까지 역화살표 | P43: P43 갱신 대상 Weight까지 역화살표. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [45/C32](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L309) `infer` | **Training과 Inference의 차이** · Inference(추론)는 학습된 모델에 새 입력을 넣어 결과를 얻는 과정입니다. 정답 없이도 예측할 수 있습니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `lesson/training_inference_basic.svg`. Training/Inference 로컬 SVG의 Weight Update/Fixed 구분 적절 | C31→C33; Training/Inference 로컬 SVG의 Weight Update/Fixed 구분 적절 | **유지** / 유지 | P44: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [46/C33](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L315) `transfer` | **전이학습 · 특징은 고정하고 분류기만 학습** · Course 11의 얼룩말 CNN 구조에서 학습할 부분을 구분합니다. Feature Extractor는 Freeze 하고 사과 결함 판정을 위한 Classification Head만 먼저  | **필요성:** 학습 목표상 필요. **정확성:** 외부 Figure 차단 시 fallback과 Freeze/Update 표시 브라우저 확인 필요 | `vision_task_apple_reference.jpg`. 'Course 11의 얼룩말 CNN 구조'는 현재 C11 XOR이므로 참조 오류. C14 원격 Architecture 의존도 반복 | C32→C34; 'Course 11의 얼룩말 CNN 구조'는 현재 C11 XOR이므로 참조 오류. C14 원격 Architecture 의존도 반복 | **유지·검증** / P45 오참조 정정+P20 로컬 그림 재사용 | P45: P45 오참조 정정+P20 로컬 그림 재사용. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [47/C34](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L316) `cnn-learning-paths` | **같은 CNN 특징 · 지도와 비지도 활용** · 이미지의 특징을 추출하는 CNN은 같이 사용 할 수 있습니다. 그다음 정답 Label로 분류를 학습 할지, Label 없이 비슷한 특징끼리 묶을지 에 따라 활용 방식이 달라집니다. | **필요성:** 학습 목표상 필요. **정확성:** Freeze Backbone 공유+지도 Head 학습/비지도 군집 그림의 학습 목표를 우선 강조 | `vision_task_apple_reference.jpg`. 고정 사전학습 CNN Feature를 Label 기반 Head 학습/무라벨 K-means로 분기. 전체 CNN 훈련 유형과 구분돼 정확 | C33→C35; 고정 사전학습 CNN Feature를 Label 기반 Head 학습/무라벨 K-means로 분기. 전체 CNN 훈련 유형과 구분돼 정확 | **수정** / P46 유지, 실제 도식 복잡도 실화면 QA | P46: P46 유지, 실제 도식 복잡도 실화면 QA. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [48/C35](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L341) `training-log` | **Batch · Step · Epoch** · CNN을 학습시킬 때 사진을 몇 장씩 보고, 가중치를 몇 번 바꿨는지 읽기 위한 용어입니다. | **필요성:** 독립 장 불필요, 정보 보존. **정확성:** Batch/Step/Epoch를 C29 노트로 흡수, 10장/4장=3step 보존 | HTML 수치·비교 카드. 10장 Batch4에서 3Step, 2Epoch→6Step 정확하나 학습 원리 목표상 C29 노트로 흡수 가능 | C34→C36; 10장 Batch4에서 3Step, 2Epoch→6Step 정확하나 학습 원리 목표상 C29 노트로 흡수 가능 | **통합** / P41 통합 | 55장 계획에서 별도 장 제외: P41 통합. 실제 적용·브라우저 검증 전 해결 미확정 | Minor |
| [49/C36](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L345) `overfit` | **Overfitting · 새 데이터 일반화** · Overfitting(과적합)은 학습 데이터에 지나치게 맞춰 새 데이터 성능이 떨어지는 현상입니다. Validation 추세와 실패 사례를 함께 봅니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `lesson/context_overfit_leakage.svg`. Train loss/Validation 악화 관계를 개념 그래프로 제시, 학습된 실측 모델 그래프 아님 | C35→C37; Train loss/Validation 악화 관계를 개념 그래프로 제시, 학습된 실측 모델 그래프 아님 | **유지** / 유지 | P47: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [50/C37](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L351) `threshold` | **Score Threshold · 판정 기준** · 교육용 저장 점수 100건에 기준 0.50을 적용합니다. 같은 점수에도 기준을 바꾸면 판정과 오류 수가 달라집니다. | **필요성:** 학습 목표상 필요. **정확성:** TP18 FN2 FP4 TN76 같은 100건; Score는 실제 확률 아님, 집계 JS 미실행 | HTML 수치·비교 카드. 같은 교육용 100건 임계값 0.50 결과만 정적 카드로 제시, C44 변화 실습과 분리 | C36→C38; 같은 교육용 100건 임계값 0.50 결과만 정적 카드로 제시, C44 변화 실습과 분리 | **유지·검증** / P48에 UI 통합 | P48: P48에 UI 통합. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [51/C38](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L357) `confusion` | **Confusion Matrix · 100건 평가** · 총 100건의 같은 평가 데이터를 다음 지표 계산까지 이어갑니다. 실제 불량 20건 중 18건을 찾고, 정상 80건 중 4건을 잘못 알렸습니다. | **필요성:** 학습 목표상 필요. **정확성:** TP18 FN2 FP4 TN76, 정확도94% 일치 | HTML 수치·비교 카드. 2×2 Confusion Matrix TP18 FN2 FP4 TN76·Accuracy94% 정확 | C37→C39; 2×2 Confusion Matrix TP18 FN2 FP4 TN76·Accuracy94% 정확 | **유지** / 유지 | P49: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [52/C39](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L363) `imbalance` | **Accuracy의 함정 · 모두 정상이라면?** · 정상 80건, 불량 20건입니다. 전부 정상이라고 말해도 맞힌 비율이 80%가 됩니다. | **필요성:** 학습 목표상 필요. **정확성:** 전부 정상 예측 Accuracy80%, 불량 Recall0% 일치 | HTML 수치·비교 카드. all-normal Accuracy80%/Recall0%와 94%/90% 비교 정확. 100칸 색상의 가독성 미검증 | C38→C40; all-normal Accuracy80%/Recall0%와 94%/90% 비교 정확. 100칸 색상의 가독성 미검증 | **유지** / 유지 | P50: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [53/C40](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L366) `metrics` | **Precision과 Recall** · 직전 혼동행렬의 TP=18·FP=4·FN=2를 그대로 사용합니다. Precision은 불량이라고 알린 22건, Recall은 실제 불량 20건을 분모로 계산합니다. | **필요성:** 학습 목표상 필요. **정확성:** Precision 18/22=81.8%, Recall18/20=90% 정확 | HTML 수치·비교 카드. Precision18/22과 Recall18/20의 분모를 점 집합으로 다르게 제시 | C39→C41; Precision18/22과 Recall18/20의 분모를 점 집합으로 다르게 제시 | **유지** / 유지 | P51: 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [54/C41](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L372) `iou` | **IoU · 박스 겹침 비율** · 분류의 정답 여부와 달리, 검출·분할에서는 위치나 영역도 맞아야 합니다. IoU(Intersection over Union)는 정답과 예측의 교집합/합집합 비율입니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `lesson/context_iou_visual.svg`. GT Box/Mask IoU의 교집합/합집합은 정확하나 사과 ROI나 면적 숫자 예가 없어 초보자 직관 부족 | C40→C42; GT Box/Mask IoU의 교집합/합집합은 정확하나 사과 ROI나 면적 숫자 예가 없어 초보자 직관 부족 | **유지** / P52 overlap20/union40=0.5 추가 | P52: P52 overlap20/union40=0.5 추가. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [55/C42](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L378) `workflow` | **Vision AI 원리 · 한 장으로 연결** · 처음 본 사과 사진을 다시 떠올려 봅니다. 각 개념은 결함을 찾는 같은 문제의 서로 다른 단계를 설명합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`. Pixel→Task→CNN→Train→Eval 5단 도식. C43 실무 질문과 기능 중복 | C41→C43; Pixel→Task→CNN→Train→Eval 5단 도식. C43 실무 질문과 기능 중복 | **유지** / P53 C43 질문 결합 | P53: P53 C43 질문 결합. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [56/C43](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L384) `project-brief` | **첫 과제를 위한 네 가지 질문** · 원리를 안다면 무엇을 찾아야 하고 어떤 사진으로 배울지 설명할 수 있습니다. AI를 사용하더라도 질문은 사람이 정합니다. | **필요성:** 독립 장 불필요, 정보 보존. **정확성:** 과제 정의 네 질문이 C42 워크플로와 중복 | `vision_task_apple_reference.jpg`. Task/Label/Data/Metric 4질문은 C42 전체 흐름과 의미 중복 | C42→C44; Task/Label/Data/Metric 4질문은 C42 전체 흐름과 의미 중복 | **통합** / P53에 질문만 이전 | 55장 계획에서 별도 장 제외: P53에 질문만 이전. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [57/C44](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L391) `project-run` | **실행 결과 확인 · 임계값과 오류 수** · AI가 평가 결과를 만들었다고 가정하고, 교육용 저장 점수 100건을 직접 다시 집계합니다. 실제 모델을 실행한 결과는 아닙니다. | **필요성:** 독립 장 불필요, 정보 보존. **정확성:** C37 임계값 실습과 100건 재집계 중복 | HTML 수치·비교 카드. C37과 같은 교육용 100건 Score를 t0.3/0.5/0.7으로 재집계; 중복이나 실제 UI 자산은 필수 | C43→C45; C37과 같은 교육용 100건 Score를 t0.3/0.5/0.7으로 재집계; 중복이나 실제 UI 자산은 필수 | **통합** / P48 인터랙션 이전 | 55장 계획에서 별도 장 제외: P48 인터랙션 이전. 실제 적용·브라우저 검증 전 해결 미확정 | Major |
| [58/C45](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L395) `project-iterate` | **실패 사진이 알려 주는 것** · 전체 Accuracy가 높아도 새 촬영 조건이나 아주 작은 결함에서 실패할 수 있습니다. 결과를 사진과 함께 살펴봅니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`. 어두운 사진·배경·작은 해상도 오류를 가정한 생성 사과, 실제 실패 측정 결과 아님 | C44→C46; 어두운 사진·배경·작은 해상도 오류를 가정한 생성 사과, 실제 실패 측정 결과 아님 | **유지** / P54 유지 | P54: P54 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |
| [59/C46](https://github.com/sh0427-han/vision_ai_lecture/blob/b4ec5ee9ef8e846fdb30590a883b2e66badfe9bd/docs/vision_ai_course.html#L399) `project-check` | **Vision AI 원리 · 무엇을 설명할 수 있나?** · 처음 본 사과 사진으로 돌아갑니다. 좋은 Vision AI는 무엇을 찾을지 알고, 새 사진에서도 결과를 검증할 수 있어야 합니다. | **필요성:** 학습 목표상 필요. **정확성:** 현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증 | `vision_task_apple_reference.jpg`. 강의 전체 사과 질문으로 Pixel/Kernel/Loss/Eval을 되묻는 형성평가 | C45→종료; 강의 전체 사과 질문으로 Pixel/Kernel/Loss/Eval을 되묻는 형성평가 | **유지** / P55 유지 | P55: P55 유지. 실제 적용·브라우저 검증 전 해결 미확정 | — |

## 2. 강의 전체 스토리라인의 구조적 문제

I09~I13의 변화 사례 반복, C03~C05 방법 선택 중복, C11~C13 비선형성 순서, C14/C15 CNN 구조의 동기 역전, C42~C44 마무리 중복이 핵심이다. 독립 장의 삭제를 곧 개념 삭제로 간주하면 안 된다. 아래 AUD-01~04를 구조 개선의 기준으로 사용한다.

## 3. 기술적으로 부정확하거나 오해 가능한 내용

**정정:** 이전 작성본에서 C03의 의사 Python 조건식을 `if brown_pixels = k`로 판독한 것은 HTML entity `&gt;=`를 잘못 해석한 오류다. 실제 `docs/vision_ai_course.html`은 `if brown_pixels &gt;= k:`이고 브라우저에는 `if brown_pixels >= k:`로 표시된다. 이 조건식의 문법 오류 지적(AUD-07)은 **취소**한다. 다만 미완성 영상 판단 규칙 예시라는 표시와 새 사진 추론 연결은 별도로 검수할 수 있다.

검증된 계산: RGB 640×960×3=1,843,200; AND z=0.5(x1+x2)-0.7 의 00/01/10/11 출력 0/0/0/1; XOR 대각 1은 직선 하나로 분리 불가. Padding 입력 1..9, all-ones 3×3 kernel에서 Padding0 45, Padding1 출력 [[12,21,16],[27,45,33],[24,39,28]]. MaxPool 2×2 stride2 출력 [[6,4],[7,9]]. 회귀 x=2, y=4, w=.5, L=(wx-y)^2: L=9, dL/dw=-12, lr=.1, w'=1.7, 예측 3.4, L'=.36. TP18 FN2 FP4 TN76: Accuracy94%, Precision18/22=81.8%, Recall18/20=90%. 전부 정상 가상 모델의 Accuracy80%, Recall0%. **Critical 계산 오류 확인 없음.** 기술적 정정은 AUD-05·06 및 AUD-13 참고.

## 4. 수정 또는 교체가 필요한 Figure

C03 우측 Training→Model→Inference 단절과 사진 통제(AUD-08)는 필수 Figure 개선. C34 Freeze Backbone에서 지도 Head/비지도 군집 대비의 시각적 우선순위(AUD-09). C23 실제 Feature Map stage와 채널 비교 및 C33 외부 원본 fallback(AUD-10). 단, 최신 1920×1080 및 1366×768 화면을 직접 확인하지 않았으므로 Crop/겹침/자산 실패를 이번 검수에서 확정했다고 주장하지 않는다.

## 5. 중복·불필요·누락 슬라이드

통합 대상 I02 scene, I13 vision-challenge, C04 vision-evolution, C35 training-log, C43 project-brief, C44 project-run 6장. 신규 ai-ml-dl-cv와 video-frames 2장. **59−6+2=55장**. 빠지는 정보는 기존 인접 장에 명시적으로 옮긴다.

## 6. 현재 55장 승인 계획으로 해결 가능한 문제

중복 여섯 개 제거 및 신규 두 장, CNN 필요성→전체 구조, XOR/활성화 순서, C37 임계값과 C44 실습 통합은 Approved 기획에 포함. 기획 승인 자체는 Builder 구현이나 화면 검증 완료를 뜻하지 않는다.

## 7. 승인 계획에 추가 반영이 필요한 문제

P45는 현재 스토리보드의 외부 CNN Figure 참조가 유지될 여지가 있어 **P20 신규 로컬 Architecture 재사용을 필수**로 바꿔야 한다. P43 Backward에는 `Loss → Gradient → Optimizer → Conv/Head Weight`의 실제 역방향 화살표, P20/P21 및 P27/P28에는 논리 Gate와 CNN 계산의 명시적 연결문을 보완한다. 이 세 항목은 **55장 승인 기획만으로 완료가 보장되지 않는 추가 Major**다.

C03/P16 사진 과실 크기·촬영 조건 통제, 새 사진과 동일 학습 모델의 연결선, 평가가 실측이 아니라는 인수조건. C11 직선 기울기와 절편 모두 변화 가능. C34 Label 사용 여부/학습 파라미터와 Clustering 구분. Video Group Split의 원본 영상 외 동일 제품·설비 그룹 명확화. 55장 120분은 리허설 검증 필요.

## 8. Planner에게 전달할 수정 사항

AUD-01~04. 승인 기획의 55장 ID/시간 배정과 새 Storyboard에 구체 수락 기준을 반영한다. 원본 자료를 Reviewer가 수정하지 않는다.

## 9. Builder가 직접 수정할 사항

AUD-05·06·08~16. 수정은 지역 HTML·Figure·CSS/JS에 국한하고 Manifest/Outline 제목/번호 동기화 여부를 재확인한다.

## Issue 세부 기록 (모두 Open)

### AUD-01 — Major — Planner — Open

대상: I02,I13,C04,C35,C43,C44. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: 중복 6장 통합. 독립 장만 제거하고 사람시각 사례, 학습단위, 임계값 비교 등 고유 정보 보존.

근거/상태: Approved 55장에 구조적 해결안 존재.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-02 — Major — Planner — Open

대상: C11,C12,C13. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: XOR 실습에서 |t|를 ReLU 설명 전에 사용. 선형 합성 한계→ReLU→비선형 XOR 시연으로 재배치. |t|=ReLU(t)+ReLU(-t) 명시.

근거/상태: Approved에서 순서 변경 계획.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-03 — Major — Planner — Open

대상: C14,C15. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: CNN 전체 Architecture보다 Local Connectivity의 필요성을 먼저 설명하고 얼룩말 패턴을 사과 결함과 연결.

근거/상태: Approved에서 C15→C14.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-04 — Major — Planner — Open

대상: I02 주변,C27. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: AI⊃ML⊃DL과 CV 문제 영역 구분, 디코딩 Frame의 시간축 T×H×W×3 부족. Video Group Split 전 영상·제품·설비 그룹 선행.

근거/상태: Approved 신규 ai-ml-dl-cv, video-frames.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-05 — Minor — Builder — Open

대상: C07,C09. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: 퍼셉트론 일반식 w1*x1+w2*x2+b와 공유 W 특수예시, w2=1 고정 실습의 차이를 Figure에 표기.

근거/상태: 현행 본문은 구분하나 시각 이해 확인.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-06 — Minor — Builder — Open

대상: C11. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: 두 Affine 층 합성의 최종 선형 결정 경계는 기울기뿐 아니라 위치도 바뀔 수 있다. 해당 표현 정정.

근거/상태: z=W2(W1*x1+x2+b1)+x1+b2.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-08 — Major — Builder — Open

대상: C03. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: 비교 사진의 크기/구도를 통제하고 학습 사진+Label→Training→같은 Model+새 사진→Inference→Prediction을 연결선으로 나타낼 것.

근거/상태: 최신 main HTML에서 독립 새 입력 추론 노드 부족. 기존 리뷰의 Crop 관찰은 현행 캡처 미검증.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-09 — Major — Builder — Open

대상: C34. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: 공통 Freeze Feature를 중앙에 크게, 좌우 Label 유무·학습 Head와 군집의 차이를 주 메시지로 부각.

근거/상태: 콘텐츠 기술적으로 적절; Figure 과밀 여부는 실렌더 필요.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-10 — Major — Builder — Open

대상: C23,C33. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: SqueezeNet feature 단계별 원본/채널 대응, Transfer Learning 외부 Figure 차단 fallback, Freeze/Head 연결을 실제 브라우저 검증.

근거/상태: 오류 확정이 아니라 실험·자산 시각 검증 필요.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-11 — Major — Builder — Open

대상: I05,I06,I08,C09,C11,C29,C37,C44. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: Pixel/해상도/슬라이더/Gradient/임계값 초기화와 변경을 1920,1366 해상도에서 실행.

근거/상태: HTML만으로 실행 통과 주장 금지.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

### AUD-12 — Minor — Builder — Open

대상: C37–C44. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: Score를 확률로 단정하지 말고 교육용 100건을 동일 Score 배열에서 집계; Validation 선택 후 Test 고정 평가 구분.

근거/상태: 수치상 TP18,FN2,FP4,TN76 일치.

영향 및 재검증: 해당 슬라이드와 전후 학습 흐름, 1920×1080 및 1366×768 화면에서 화살표·글자·레이아웃 확인, 수치·기능의 독립 재계산. 상태는 Open이며 실제 적용 후에만 Resolved/Verified로 갱신.

## 보완 Issue — 최신 HTML에 근거한 추가 지적 (모두 Open)

### AUD-13 — Major / Builder: C33 선행 슬라이드 오참조

현재 전역 46 / C33 `transfer`; `docs/vision_ai_course.html`에서 'Course 11의 얼룩말 CNN 구조'라고 적지만 현재 C11은 XOR이다. 초보자가 관련 CNN 설명을 찾지 못하는 명백한 참조 오류다. P45에서 숫자 참조를 제거하고 P20의 `cnn-overview` Concept 기준으로 다시 연결한다. 재검증은 새 Manifest와 실제 Deep Link를 대조한다. **상태 Open**.

### AUD-14 — Major / Builder: C14·C33 원격 CNN Figure 의존

`docs/vision_ai_course.html`의 `lf-cnn-architecture`가 외부 Developers Breach 배너를 참조한다. 차단 시 사과→Conv→Classification 폴백은 ReLU·Pool·Tensor Shape·학습 대상 Weight를 생략하므로 학습 목표를 충분히 지원하지 못한다. P20/P45에서 Conv→ReLU→Pool→Conv→GAP→Head의 로컬 도식을 같은 모양으로 공유하고 차단 상태에서 확인한다. **상태 Open**.

### AUD-15 — Major / Builder: C31 CNN Gradient 역방향 연결

C31 `cnn-training`의 Forward·Backward가 두 묶음으로 나뉘어, Loss→Gradient→Optimizer의 Weight 업데이트 결과가 Conv Kernel/Head에 돌아가는 방향이 사진/노드/화살표로 연결되지 않는다. P43에서 실제 학습 대상 Weight로 도착하는 역화살표와 Freeze 예외를 요구한다. 1920×1080/1366×768 실렌더로 종점을 검증한다. **상태 Open**.

### AUD-16 — Major / Planner·Builder: P20→P21→P28 교육 흐름 복귀

승인 55장에선 P20 CNN 전체 구조 직후 P21부터 퍼셉트론·Gate를 설명하고 P28 Kernel로 돌아오므로 새 개념을 처음 접한 수강생에겐 별도 주제로 보일 수 있다. P20에서 'CNN의 Weight·활성화 원리'를 예고하고 P27 마무리에서 P20 Conv를 다시 확대한다는 브리지 문구/도식 Highlight를 추가한다. 별도 장 추가는 불필요하다. **상태 Open**.

### AUD-17 — Major / Builder: C16 JPEG Crop과 인공 5×5 행렬의 구분

C16 `kernel`에서는 실제 사과 사진의 85×85 ROI에서 교육용 5×5 정수로 이어진다. 숫자 자체는 JPEG에서 읽은 값이 아님을 캡션에 기록했지만 연속 화살표 때문에 직관적으로 동일 데이터라 오독할 수 있다. P28에서 교육용 가상 입력 표기와 한 위치의 9곱/합→−6을 Figure 내부에 넣는다. 재검증은 사진 Crop과 행렬의 실측 관계가 없음을 초보자에게 설명할 수 있는지로 판단한다. **상태 Open**.

## 10. 검증 범위와 검증하지 못한 사항

검증 완료: main Manifest와 59개 실제 HTML Section Concept ID·제목 대조; 운영안 TWO_HOUR_LECTURE_PLAN.md, PROJECT_GUIDE.md, HTML_DESIGN_RULES.md, assets/SOURCES.md, 기존 reviews/CURRENT_REVIEW_REPORT.md, 승인 기획 Branch Storyboard의 구조 참조; 핵심 숫자 직접 재계산; 전체 선후 흐름 정적 분석.

**미검증:** 59×2=118개의 Chromium 실제 화면 육안 비교(1920×1080,1366×768), 최신 GitHub Pages 캐시/커밋 동기화, asset 원본 Figure의 수치/선 연결·Crop·대비, 이미지 로드/Console, 모든 Interactive 계산/Reset·키보드, 외부 Figure fallback, 실제 120분 리허설. 과거 CI와 리뷰의 스크린샷은 당시 버전의 참고 자료로만 취급한다. 재검증은 scripts/verify_two_hour_course.py, scripts/verify_learning_routes.py, scripts/audit_visual_slides.py 실행 및 각 출력물 검토를 권장한다. 55장 구현 후에는 110개 화면을 다시 확인해야 한다.
