# Vision AI 55장 / 120분 — Final Integration QA (Reviewer)

> **판정: CONDITIONAL PASS (최종 PASS 아님) / main Merge: HOLD**
>
> 작성일: 2026-10-19 KST · Reviewer 고정 소스 SHA: `f5e0ac56de7582465bf3e91af91321942f5c10b8` · Source: `automation/approved-55-20261019` · 기록 전용: `review/final-55-f5e0ac5-20261019`.
>
> 검수 중 GitHub 계정명이 `sh0427-han`에서 `sh0427-han-private`로 변경됨. 동일 repository ID **1380693126** 및 동일 고정 SHA를 확인하고 canonical 경로로 기록. 새 저장소나 별도 fork를 검수한 것이 아님.

## 0. Executive decision and non-negotiable verification boundary

- **알려진 Critical 0 / 알려진 미해결 Major 0**. 승인된 55장, 120분, Concept ID, Manifest, Outline, 로컬 경로 및 핵심 수치의 새로운 오류는 발견하지 못함.
- **잔여 확인된 Minor 2건:** `A-R1` P04 photo/grid 선택 셀 대응의 교육적 보강, `H-04` P54 Caption 및 `assets/SOURCES.md`의 배경 합성 메타데이터 불일치. 새 문서 품질 Minor `FINAL-DOC-01` 1건(구버전 PROGRESS/TODO 상태 문구) 등록. 미확인 항목은 결함으로 단정하지 않음.
- **전수 55/55 정적 구조 및 기획 비교 = 독립 수행**. 55개의 슬라이드 본문 각각이 해당 구간 최종 독립 검수 SHA의 HTML과 **byte-for-byte 동일**함을 원격 GitHub 파일 비교로 확인함.
- **110/110 화면은 각 구간의 과거 고정 SHA에서 축적된 Reviewer 판독 증거**임. **이번 최종 SHA에서 새로 실행·열람한 110개 화면은 0/110 (NOT VERIFIED)**. 특히 기존 A–F 화면 94개를 현 SHA에서 다시 열어본 것은 아님. 최신 Chromium CI는 바로 이전 *강의 구현 동일* SHA `c35f1f7`의 G10+H6=**16/110** 및 공통 경로 테스트만 실행. 따라서 최종 110-screen same-SHA gate를 완료했다고 주장할 수 없음.
- 화면/기능/수치의 구간 검수 PASS는 **검수 당시 SHA**에 대한 증거. Reviewer의 이번 작업에는 Chromium 신규 실행, Python 원본 스크립트 직접 실행, 실제 강의 리허설, 공개 Pages 검사가 없음. 해당 항목은 각각 NOT VERIFIED.
- **결정:** 현재 강의 내용은 주요 기능·수치 범위에서 병합 후보이지만, 요청된 동일 SHA 110장×2 전체 화면과 A–F 회귀를 독립적으로 재판독하지 못했으므로 최종 통합 QA는 CONDITIONAL PASS. **main Merge/배포 비권고**. PASS는 마지막 QA Gate 완료 후 다시 판정.

## 1. Snapshot, baseline, and source hierarchy

- Repository: [`sh0427-han-private/vision_ai_lecture`](https://github.com/sh0427-han-private/vision_ai_lecture); originally [legacy address](https://github.com/sh0427-han/vision_ai_lecture) redirects following owner rename.
- Fixed source: [`f5e0ac56de7582465bf3e91af91321942f5c10b8`](https://github.com/sh0427-han-private/vision_ai_lecture/commit/f5e0ac56de7582465bf3e91af91321942f5c10b8). Parent [`c35f1f7`](https://github.com/sh0427-han-private/vision_ai_lecture/commit/c35f1f7175788921f2a924f3ef1f4e0e552bb5e2). `c35f1f7..f5e0ac5` changes **only** `automation/H_REVIEWER_FIX_QA.md`, `automation/PROGRESS.md`; HTML/CSS/JS/Manifest/asset and test scripts unchanged.
- Normative: `planning/SLIDE_STORYBOARD.md`, `planning/approved55.json`, `TWO_HOUR_LECTURE_PLAN.md`, `PROJECT_GUIDE.md`, `HTML_DESIGN_RULES.md`, `AGENTS.md`, `assets/SOURCES.md`.
- Implementation: `docs/intro.html`, `docs/vision_ai_course.html`, `docs/two_hour_manifest.json`, `docs/lecture_outline.js`, relevant `docs/*.css`, `docs/*.js`, `docs/assets/`.
- Earlier reference-only: `reviews/CURRENT_REVIEW_REPORT.md`, `reviews/FULL_LECTURE_AUDIT.md`, `TODO_VISION_AI_LECTURE.md`, `automation/PROGRESS.md`. Older 59/58/54-slide numbering is **not** current 55-slide order.

### A–H final independent review lineage

| 구간 | 전역 범위 | 장수 | 과거 2-view 기본 화면 | 최종 baseline | 실제 수동/CI 증거 | 구간 결론 |
|---|---|---:|---:|---|---|---|
| A | P01–P13 | 13 | 26 | `2280772` | 개별 화면 26개 + 보강 8개; 실수치/ROI 검수 | Critical0 / Major0 / Minor A-R1 |
| B | P14–P18 | 5 | 10 | `b803380` | 10+2 화면; P16 텍스트 박스 재실측 | Critical0 / Major0 |
| C | P19–P27 | 9 | 18 | `fc8d463` | 18+2 화면; AND/XOR 키보드/Reset | Critical0 / Major0 |
| D | P28–P36 | 9 | 18 | `ae99806` | 18+2 화면; 24 Matrix/Window 재계산 | Critical0 / Major0 |
| E | P37–P40 | 4 | 8 | `39e9cc5` | 8 화면; 분할·GT 변환 검산 | Critical0 / Major0 |
| F | P41–P47 | 7 | 14 | `219e2ba` | 14+2 화면; 학습/Reset/Arrow endpoint | Critical0 / Major0 |
| G | P48–P52 | 5 | 10 | `4b79d63` | 10 PNG/JSON Reviewer 검토; c35f1f7 CI 재실행 | Critical0 / Major0 |
| H | P53–P55 | 3 | 6 | `c35f1f7` | 6 PNG+4 SVG crop; Reviewer 픽셀 검산 | Critical0 / Major0 / Minor H-04 |

최종 보고서 참조:

- **A:** [reviews/automation/A-2280772.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/automation/approved-55-20261019/reviews/automation/A-2280772.md)
- **B:** [reviews/automation/B-b803380.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/automation/approved-55-20261019/reviews/automation/B-b803380.md)
- **C:** [reviews/automation/C-fc8d463.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/automation/approved-55-20261019/reviews/automation/C-fc8d463.md)
- **D:** [reviews/automation/D-ae99806.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/automation/approved-55-20261019/reviews/automation/D-ae99806.md)
- **E:** [reviews/automation/E-39e9cc5.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/automation/approved-55-20261019/reviews/automation/E-39e9cc5.md)
- **F:** [reviews/automation/F-219e2ba.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/automation/approved-55-20261019/reviews/automation/F-219e2ba.md)
- **G:** [reviews/automation/G-4b79d63-final.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/review/g-final-4b79d63-20261019/reviews/automation/G-4b79d63-final.md)
- **H:** [reviews/automation/H-c35f1f7-final.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/review/h-final-c35f1f7-20261019/reviews/automation/H-c35f1f7-final.md)
- H 최초 Issue 보고서 [H-4469656.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/review/h-4469656-20261019/reviews/automation/H-4469656.md); G 최초 Issue 보고서 [G-d27e160c.md](https://github.com/sh0427-han-private/vision_ai_lecture/blob/review/g-d27e160c-20261019/reviews/automation/G-d27e160c.md). 이전 판정·근거는 덮어쓰지 않음.

## 2. Independent contract and consistency check — PASS (static)

고정 SHA의 계획 JSON, 실제 HTML, Manifest, Outline을 동일 요청에서 재조회해 개별 순서/제목/ID/시간을 직접 교차 비교한 결과:

| 검사 | 기대 | 관찰 | 판정 |
|---|---|---|---|
| 슬라이드 개수 | Intro13 + Course42 | **13 + 42 = 55** | PASS |
| 고유 Concept | 55개, 중복 0 | **55개**, 중복 0 | PASS |
| 계획↔HTML↔Manifest↔Outline | 전역1–55, 순서·타이틀·물리 번호 | **불일치 0** | PASS |
| 각 그룹·시간 | A26 B10 C23 D22 E9 F15 G10 H5 | **120분**, 플랜 개별 분 합도120 | PASS |
| Manifest duration/teaching/discussion | 120/120/0 | **120/120/0** | PASS |
| HTML 상대 `src/href` 파일 경로 | 누락 0 | **172 참조, 고유53, 누락0** (현재 Git Tree 451항목) | PASS |
| A–H 구간 보고서 이후 HTML 본문 | 동일 또는 재검수 필요 | **13+5+9+9+4+7+5+3 = 55/55 구간 본문 완전 동일** | PASS |
| 최종 SHA 신규 CI | 실제 해당 SHA 워크플로 | SHA f5e0ac5 등록된 Actions run **0건** | NOT VERIFIED |
| 실제 120분 교수 시간 | 120분 실측 | 배정표만 검증, 실측 없음 | NOT VERIFIED |

정적 계약 검사는 숫자나 DOM의 완전한 기술 의미/독해 수준/실제 브라우저 가시성을 보장하지 않음.

### Global narrative and prerequisite progression

1. **A→B (P13→P14):** 사과 사진에서 무의미한 촬영변화와 중요한 결함 차이를 구분한 뒤, 동일 사진의 Class/Box/Mask GT 질문을 정의. 선행 Pixel/HWC 존재.
2. **B→C (P18→P19):** 정답·Task·Model 선택을 정의한 다음 국소 패턴 탐색에 왜 CNN이 필요한지 연결. C는 CNN 전체 그림부터 제시한 후 뉴런·AND/XOR·비선형성을 설명하여 역참조 부담을 낮춤.
3. **C→D (P27→P28):** XOR 비선형 실습에서 CNN Conv의 실제 Window/Kernel로 복귀. 한 뉴런과 하나의 필터, 단일 채널 토이와 전체 CNN을 혼동하지 않도록 구분.
4. **D→E (P36→P37):** Backbone/Head가 어떤 특징을 계산하는지 설명한 뒤 무엇을 학습시키는지(사진/Label/분할)를 도입.
5. **E→F (P40→P41):** Train-only Augmentation 및 독립 Split → 실제 한 단계 Gradient Update → CNN Weight·Inference·Transfer·Overfit 순서.
6. **F→G (P47→P48):** 새 조건에서 일반화 필요성 → Validation의 Threshold 조절 → 고정 조건의 Confusion/Precision/Recall/IoU. 점수는 교육용이지 모델 성능 실측값이 아님.
7. **G→H (P52→P53):** 측정의 위치 정확도부터 전체 Pixel→Task→CNN→Train→독립 Evaluate를 회수, 세 가지 가설 비교 후 네 설명 질문으로 마침.

**구조적 Critical/Major 중복·선행지식 누락:** 현재 보고서·DOM·스토리보드의 검증 범위에서는 새로 확인하지 못함. 실제 비전공 학습자 이해도·한 장당 발표 시간은 NOT VERIFIED; Planner의 구조 변경은 현시점 권고하지 않음.

## 3. Whole-course slide register — all 55 included

이 표의 **「구간 PASS」는 각 구간 최종 독립 Reviewer의 판정과 현재 슬라이드 본문 정적 동일성에 기반**한다. 현재 SHA의 신규 독립 Chromium 렌더 PASS를 의미하지 않는다. `NV`=NOT VERIFIED. 각 표 행은 계획번호/실제 물리번호/Concept/시간/수치·Figure 원리/대표 자산/화면 증거/Issue/권고를 기록한다. 파일은 P01–P13=`docs/intro.html`, P14–P55=`docs/vision_ai_course.html`; 상대 이미지 파일은 `docs/assets/` 하위. 교육적 기술 검수는 각 원본 구간 보고서가 상세 근거임.

| Plan | 실제 | Concept | 분 | 설명·수치·Figure 핵심 검토 | 주요 Figure 로컬 파일 또는 렌더 | 1920/1366 | 잔여 Issue | 조치/통합 상태 |
|---|---|---|---:|---|---|---|---|---|
| P01 | Intro 1 | `start` | 1.5 | 교육용 사과 사진→분석→설명용 ROI; 실제 모델 예측 아님 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P02 | Intro 2 | `ai-ml-dl-cv` | 2 | AI⊃ML⊃DL와 Computer Vision 응용 분야 분리 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P03 | Intro 3 | `vision-value` | 2 | 반복 검사→후보→사람 검증; 100장은 가상 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P04 | Intro 4 | `photo-numbers` | 2 | 원본 전체→실제 12×8 Grayscale 숫자; 셀 연결은 Minor A-R1 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | Minor A-R1 | 구간 PASS / 최종 재렌더 NV |
| P05 | Intro 5 | `gray` | 2.5 | 6×6 실제 값·계산·밝기 Reset; 사진 미리보기 근사 고지 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P06 | Intro 6 | `rgb` | 2 | RGB Pixel 좌표·값·색 견본 일치; 생성 이미지 고지 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P07 | Intro 7 | `hwc` | 2 | 640×960×3=1,843,200 Channel 값; C≠물리 깊이 | HTML·Canvas | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P08 | Intro 8 | `video-frames` | 2 | 1초 30fps, Frame 시간축/T×H×W×3; 합성 이동 고지 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P09 | Intro 9 | `resolution` | 2.5 | 160/320/640 해상도 동일 결함 ROI 포함; 정보 복원 주장 없음 | HTML·Canvas | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P10 | Intro 10 | `lighting` | 2 | 동일 ROI 밝기 변화: 원본[88,57,29]×0.45/1.6 계산 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P11 | Intro 11 | `transform` | 2 | 회전·크롭·가림·흐림 변환을 각각 비교 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P12 | Intro 12 | `diversity` | 1.5 | 품종 변화와 정상/결함 Label 구분 | generated/apple_studio_preview.png, vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P13 | Intro 13 | `relevant-change` | 2 | 정상/불량×밝기 교차로 판단에 필요한 변화 강조 | generated/apple_studio_preview.png, vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P14 | Course 1 | `task` | 2 | 동일 ROI의 Class/Box/Mask GT 차이; 예측과 혼동 없음 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P15 | Course 2 | `rules` | 2 | 단일 Python add 규칙에 입력(1,1)/(2,1)→2/3 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P16 | Course 3 | `rules-image` | 2.5 | 손작성 규칙 vs Label 학습; 새 사진/같은 모델/평가 연결 | vision_task_apple_reference.jpg, generated/apple_studio_preview.png | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P17 | Course 4 | `model-choice` | 1.5 | 규칙→기존 결함 모델→추가학습 선택, 각 분기 독립 평가 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P18 | Course 5 | `task-model-data` | 2 | Task별 Label 부담; Class≠Box≠Mask | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P19 | Course 6 | `cnn-why` | 2.5 | 국소 결함 특징·가중치 공유/위치 반복, 개념 Map 고지 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P20 | Course 7 | `cnn-overview` | 2.5 | 64×64×3→Conv8→Pool→Conv16→GAP→Dense2, 1,426 Parameter | HTML·Canvas | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P21 | Course 8 | `perceptron` | 2 | 두 입력 공유 W와 b, 한 뉴런≠한 Weight | HTML·Canvas | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P22 | Course 9 | `and-rule` | 2 | AND 진리표 및 z=.5(x₁+x₂)−.7 값/경계 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P23 | Course 10 | `and-gate` | 2.5 | AND W·b 슬라이더, 예측/정답/경계/Reset | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P24 | Course 11 | `xor-rule` | 2 | XOR 대각 양성 예시와 한 직선의 분리 불가 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P25 | Course 12 | `nonlinear` | 2.5 | Affine 층 합성의 선형성, ReLU 전 필요성 제시 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P26 | Course 13 | `relu` | 2 | Identity/ReLU의 음수/양수 응답; 단독 ReLU XOR 미해결 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P27 | Course 14 | `xor-gate` | 5 | XOR 선형3/4→비선형4/4; |t|의 두 ReLU 구성과 Reset | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P28 | Course 15 | `kernel` | 4 | 5×5 입력·3×3 Kernel의 9개 곱 합 −6; 사진/토이 분리 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P29 | Course 16 | `feature-map` | 3 | 9개 Sliding Window와 [[−6,12,16],[−6,8,15],[−4,2,7]] | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P30 | Course 17 | `sharing` | 1.5 | 지역 연결·Weight Sharing; 1,048,576 vs 9 Parameter(편향 제외) | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P31 | Course 18 | `channels` | 2.5 | RGB 3채널×두 3×3×3 Kernel→Feature Map 2개 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P32 | Course 19 | `stride` | 2.5 | Stride1의 3×3→Stride2의 2×2; 샘플 값−6,16,−4,7 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P33 | Course 20 | `padding` | 2.5 | Padding0/1의 크기/합; Zero Padding 출력 중심 45 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P34 | Course 21 | `pool` | 2 | 2×2 Max Pool→[[6,4],[7,9]]; Channel 유지/공간 감소 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P35 | Course 22 | `actual-map` | 1 | 실제 SqueezeNet Map; 강아지·사과 모형 분리, fresh inference 미수행 | lesson/cnn_squeezenet_actual_feature_maps.png | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P36 | Course 23 | `backbone` | 3 | Backbone 출력 특징 vs Class/Box/Mask Head의 요구 정보 구분 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P37 | Course 24 | `dataset` | 2.5 | 정상/불량×조명 교차, Shortcut/관찰과 가상 구분 | generated/apple_studio_preview.png, vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P38 | Course 25 | `split` | 2 | 1000건 700/150/150 분할, Train/Val/Test 역할 분리 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P39 | Course 26 | `leakage` | 2.5 | 영상/객체 그룹 A/B/C 중복 배제, Leakage 설명 | vision_task_apple_reference.jpg, generated/apple_studio_preview.png | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P40 | Course 27 | `augment` | 2 | 사진+GT 동일 기하 변환; 밝기 Label 불변·Train만 증강 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P41 | Course 28 | `learn` | 2.5 | 회귀 Weight 한 단계: 0.5→1.7, Loss9→0.36 및 Reset | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P42 | Course 29 | `loss` | 2 | Gradient−12, learning rate .1→w1.7, 손실 계산 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P43 | Course 30 | `cnn-training` | 3 | Forward→Loss→Backward→Optimizer→ConvA/B/Head 파라미터 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P44 | Course 31 | `infer` | 1.5 | Train은 Weight Update, Inference는 고정 Weight Forward만 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P45 | Course 32 | `transfer` | 2 | Head-only vs Fine-tune 업데이트 대상, 로컬 모델 도식 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P46 | Course 33 | `cnn-learning-paths` | 2 | 공통 Frozen Backbone 특징→지도 Classifier/비지도 K-means | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P47 | Course 34 | `overfit` | 2 | Train/Validation Loss 추세; 가상 곡선/과적합 가설 고지 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P48 | Course 35 | `threshold` | 3 | 동일 100건 Score 분포(50/28/9/13), Threshold/지표 동기 | 인라인 SVG/HTML | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P49 | Course 36 | `confusion` | 2 | t=.5의 TP18 FN2 FP4 TN76와 Accuracy94% | HTML·Canvas | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P50 | Course 37 | `imbalance` | 1 | 모두 정상 예측의 Accuracy80%·불량 Recall0% | HTML·Canvas | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P51 | Course 38 | `metrics` | 2.5 | Precision18/22=81.8%, Recall18/20=90% | HTML·Canvas | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P52 | Course 39 | `iou` | 1.5 | GT Box/Pred Box 30/30, 겹침20, IoU20/40=.5 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P53 | Course 40 | `workflow` | 2 | Pixel→Task+Label→CNN→Training→독립 Evaluation 5단계; ROI 출처 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |
| P54 | Course 41 | `project-iterate` | 1.5 | 조명/배경/해상도 통제 비교; Subject/ROI 동일·외부 픽셀 변경; H-04 라벨 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | Minor H-04 | 구간 PASS / 최종 재렌더 NV |
| P55 | Course 42 | `project-check` | 1.5 | H×W×3, Map −6→12, w/Loss, Recall90% 네 개별 예제 회수 | vision_task_apple_reference.jpg | 2/2 기존 증거¹ | 없음 | 구간 PASS / 최종 재렌더 NV |

¹ 화면 '2/2 기존 증거': A–F = 구간 최종 Reviewer가 해당 baseline에서 Chromium PNG 직접 열람 (원래 리포트에 증거 경로 기록); G/H = 성공 Actions 아티팩트 PNG를 Reviewer가 별도로 직접 판독. 해당 검수의 **기본 합계 110화면**. 이번 보고서 작성에서 원본 PNG 110개를 새로 받아 각각 시각 검사한 것은 아니며, 고정 SHA 재실행 증거가 아님. 실화면 물리장치·모바일·프로젝터 원거리 시력 검사 역시 제외.

## 4. Numeric and diagram checks — independently recomputed representative invariants

### Image/architecture/activation

- P07: **640×960=614,400 Pixel**, RGB 총 **1,843,200 Channel 값**.
- P20: ConvA `(3×3×3+1)×8=224`; ConvB `(3×3×8+1)×16=1,168`; Dense `(16+1)×2=34`; 총 **1,426 trainable parameters** (bias 포함). ReLU/Pool/GAP 자체 trainable Parameter=0. Feature shapes은 64×64×3→64×64×8→32×32×8→32×32×16→16→2.
- P22: `z=0.5(x1+x2)-0.7`; (0,0),(0,1),(1,0),(1,1)의 z는 `-0.7,-0.2,-0.2,0.3`; Step≥0이면 `0,0,0,1`. P24–P27의 XOR는 단일 Affine으로 분리 불가. 일반 합성 `W2(W1x+b1)+b2=(W2W1)x+(W2b1+b2)` 정확.
- P28–29: 동일 5×5 입력 및 세 행 [1,0,−1] Kernel의 Cross-correlation 계산값은 **[[-6,12,16],[-6,8,15],[-4,2,7]]**. P32 Stride2=**[[-6,16],[-4,7]]**.
- P33: 3×3 `[[1,2,3],[4,5,6],[7,8,9]]`, ones Kernel, ZeroPadding1 ⇒ **[[12,21,16],[27,45,33],[24,39,28]]**; 중심45. P34 2×2 MaxPool ⇒ **[[6,4],[7,9]]**.
- P41–42: `x=2,y=4,w=.5` ⇒ 초기 Loss`(wx−y)²=9`, Gradient`2(wx−y)x=−12`, `η=.1` ⇒ **w'=1.7**, 예측3.4, Loss'=**0.36**.
- P48 고정 데이터 레이블20 불량/80 정상. 점수 bin `0.2:50, 0.4:28, 0.6:9, 0.8:13` 총 100; Threshold 0.30에서 (TP20,FN0,FP30,TN50), 0.50에서 (18,2,4,76), 0.70에서 (11,9,2,78). 0.50 Precision **81.818…%**, Recall **90%**, Accuracy **94%**. Score를 calibration된 probability로 단정하지 않음.
- P52 별도 두 Box 각 면적30, 교집합20, 합집합40 ⇒ IoU **0.5**. H의 네 회고 수치는 상이한 **교육용 예시**들을 연결하는 것이며 한 CNN의 실측 결과라고 주장하지 않음.

본 회차에서 위 수치는 별도 JavaScript 산술로 재계산. 구간 리뷰는 표시 Matrix 값/화살표·ROI/DOM을 독립 비교했지만 이번 회차 **모든 외부 SVG의 픽셀 수준·선 좌표·가독성을 55장 전체 재감사하지 않았음**(해당 전수 Figure 재육안 = NOT VERIFIED).

### P54 synthetic background, photo and canvas

- 최신 [H Reviewer 재검수](https://github.com/sh0427-han-private/vision_ai_lecture/blob/review/h-final-c35f1f7-20261019/reviews/automation/H-c35f1f7-final.md)의 **마스크 내부 18,623 Pixel 중 변경 0**, 외부 배경 18,179 Pixel 중 차이>8인 Pixel 1,490, ROI 중심 `(596,226)` 색 동일. 이는 H Reviewer가 Builder CI PNG 원본에 **추가 독립 픽셀 연산**을 수행한 결과이며 본 회차 새 Chromium 촬영 아님.
- H 구현의 `docs/approved_h.js`는 단일 사진 `drawImage(source,300,85,450,450,...)`로 240²/24² Canvas 생성; 둘 모두 readiness 완료 후 캡처하도록 `automation/check_group_browser.py`가 기다림. CI 두 뷰의 Canvas ready/opaque/nonuniform 확인. 차이 비교는 ROI·Apple 내부가 아닌 합성 배경이라는 한정된 명제가 성립.
- **H-04는 남음:** 배경 단색 Caption과 실제 미세 선무늬의 차이, 오래된 `assets/SOURCES.md`의 'colored outer border' 기록이 현재 masked-background 합성과 불일치.

## 5. Browser, functional, CI and provenance evidence — source of execution explicit

| 범위 | CI/test/수동 검증 | 결과 | 주체·판정 |
|---|---|---|---|
| A 13×2=26 | Chromium 개별 PNG/Intro Pixel 계산+Reset/ROI; 이후 P09 보정, P03/05/06 caption 재검사 | 보고서 PASS | 이전 A Reviewer **실행+육안**; 현재 SHA 재촬영 NV |
| B 5×2=10 | 이미지 대응/모델 flow, P16 overflow 재렌더 | 보고서 PASS | 이전 B Reviewer **실행+육안**; 현재 SHA 재촬영 NV |
| C 9×2=18 | CNN/AND/XOR 값·presets/keyboard/Reset | 보고서 PASS | 이전 C Reviewer **실행+육안**; 현재 SHA 재촬영 NV |
| D 9×2=18 | 24 displayed matrices/9 windows/PNG 실패 fallback | 보고서 PASS | 이전 D Reviewer **실행+육안**; fresh SqueezeNet 추론 NV |
| E 4×2=8 | split/Ground Truth/augmentation 실제 DOM·SVG | 보고서 PASS | 이전 E Reviewer **실행+육안**; 현재 SHA 재촬영 NV |
| F 7×2=14 | 1-step/8-step/Reset, six update arrows, offline Transfer rendering | 보고서 PASS | 이전 F Reviewer **실행+육안**; 현재 SHA 재촬영 NV |
| G 5×2=10 | 10 PNG, threshold 14 assertions, Score/IoU | [Run 39246424868](https://github.com/sh0427-han-private/vision_ai_lecture/actions/runs/39246424868) SUCCESS at `c35f1f7` | Builder CI 실행 + G Reviewer PNG 분석; 새 f5e0 SHA 실행 NV |
| H 3×2=6 | 6 PNG, 4 background crop PNG, readiness, 55/120 계약 | [Run 39246424771](https://github.com/sh0427-han-private/vision_ai_lecture/actions/runs/39246424771) SUCCESS at `c35f1f7` | Builder CI 실행 + H Reviewer PNG 분석; 새 f5e0 SHA 실행 NV |
| Cross-deck nav | `scripts/verify_learning_routes.py`: 55 TOC, Deep Link, chapter, training, threshold, P55 details | `TWO_HOUR_NAV_QA_PASSED` | Builder CI **실행**, 이번 Reviewer 로컬 실행 NV |
| Static curriculum | `automation/verify_approved_contract.py --final` + `scripts/verify_two_hour_course.py` | `APPROVED55_FINAL_CONTRACT_PASS`; `FINAL_55_STATIC_QA_PASSED` | Builder CI 실행; **본 Reviewer 자체 JSON/HTML 대조도 PASS** |
| 110 same-SHA viewport | f5e0ac5의 새 1920/1366 ×55 | **0/110 이번 회차 직접 재촬영·열람** | **NOT VERIFIED** |
| Real classroom | 약120분 실제 강의, 비전공자 comprehension, 투사 거리 | 미수행 | **NOT VERIFIED** |
| Public GitHub Pages | main merge 이후 빌드/이동/에셋 | 수행·검사 없음 | **NOT VERIFIED**, user forbids merge |

**CI 로그 직접 재확인:** H `h-browser` Job118039343410: static 55/120, H6 / 0 layout issues / 0 page errors / minimum fit .943 / 0 canvas errors / navigation PASS. G `g-browser` Job118039343935: 10 screens, 14 interaction checks PASS. 둘 모두 head=`c35f1f7175788921f2a924f3ef1f4e0e552bb5e2`. `f5e0ac5` 자체로 등록된 Actions run은 0건. 두 SHA 사이 교육 구현·검사 스크립트는 변하지 않으므로 두 CI 결과는 관련성 높은 이전 SHA 증거이되, 같은 SHA 실행이라고 표기하지 않음.

**현재 코드 정적 동작 확인:** `docs/slide.js`의 ArrowRight/PageDown/Space→next, ArrowLeft/PageUp→previous, Home/End, 페이지 경계 Intro13↔Course1, Hash Deep Link, `docs/lecture_sidebar.js`의 TOC 링크·Esc·focus·inert, `docs/interactive_gates.js`의 AND/XOR, `docs/interactive_lessons.js`의 Pixel/Train, `docs/project_course.js`의 Threshold/Reset, `docs/approved_h.js`의 Canvas readiness를 확인. 현재 회차에서 직접 클릭·키보드 이벤트 실행은 NV; G/H CI와 해당 A/C/F 이전 Reviewer 동작 결과에서 확인.

**회귀 범위:** A–H 보고서 각각의 기준 SHA에서 고정 SHA까지 각 구간 HTML `<section class="slide">…</section>` 원문은 55/55 동일. `4b79d63..f5e0ac5` 변경 6파일은 H HTML/CSS, H QA workflow/script 및 인계문서만. `approved_h.css` 규칙은 `.h55…` 스코프이며 `approved_h.js`는 H용 두 Canvas만 선택. 동일 `c35f1f7`의 G10 재실행은 PASS. **하지만 공동 JS/CSS의 실제 모든 과거 동작 결과를 재현한 A–F 94개 고정 SHA 신규 캡처는 없음**.

**Image provenance:** 실제 사과는 로컬 교육용 생성 원본, P14 Box/Mask는 GT 설명 주석, P35 실제 SqueezeNet Feature Map은 별도의 강아지 사진·사전학습 모델·정규화된 결과, P48–P51 가상 100건 Score, P54 통제 합성 배경, H 회고의 회귀값은 독립 토이 데이터. 타 모델·사진 사이 비교가 같은 실험으로 해석되면 안 됨. 외부 Figure의 식별/출처는 `assets/SOURCES.md` 및 해당 구간 독립 검수의 범위에서 확인; 모든 55장의 출처 Caption을 이번 회차 새 스크린샷으로 재판독하지 못한 점은 NV. P54 설명 불일치는 H-04로 등록.

## 6. Historical issues: resolution and residual

| Issue | 심각도 | 담당 | 최종 상태 및 근거 | 재검증 조건 |
|---|---|---|---|---|
| A-01 / A-R0 | Major | Builder | **CLOSED**: P09 결함 ROI가 실제 반점 위치에 포함되도록 보정, P10 RGB 값 계산 | P09 세 Canvas ROI + 두 viewport |
| A-R1 | Minor | Builder | **OPEN**: P04 원본 사진과 12×8 Grid 중 선택 Cell 상호 강조 부재. 전체-사진 Downsample 자체는 정확 | 사진 Pixel과 Grid Cell 가시적 1:1 대응 표시 |
| A-R2 / A-R3 | Minor | Builder | **CLOSED**: P05 preview/수치 구분, P06 생성 사진 alt, P03 편집 메모 제거 | A-final 재검수 기록 |
| RML-01/02/03, B-R1 | Major | Builder | **CLOSED**: P16 과실 크기/촬영 조건, 학습·새 입력·동일 모델 연결, 국문 라벨·descendant overflow | B-final 두 화면/descendant 위치 |
| FLOW-01 | Major | Planner | **CLOSED**: P17 모델선택으로 중복 구조 통합 | P16→17→18 컨셉 점검 |
| AUD-02/03/05/06/14/16 (C/D) | 이전 Major | Builder | **기술적 CLOSED**: 선형/비선형 구분, 퍼셉트론, CNN 예제·로컬 architecture | C/D 최종 report, 필요시 재렌더 |
| D-R1 / AUD-17 | Minor/과거 Major | Builder | **CLOSED**: P35 캡션과 사진/입력 tensor 구분, 수치 Window | D-final 보고서 |
| E 분할/Leakage/Augmentation | 스토리보드 필수 | Builder | **PASS**: 새 A/B/C 그룹 중복 배제, Label 일치, Test 고정 | E 보고서 + 최종 route 체크 |
| AUD-09/10/13/14/15 (F 관련) | 과거 audit | Builder | **기술적 해결 근거 있음**: P43 ConvA/B/Head update, P45 Head/fine-tune, P46 supervised/unsupervised Frozen Backbone, P20 local architecture, P35 source metadata. 그러나 `automation/PROGRESS.md`의 과거 OPEN 표기는 업데이트되지 않음. **해당 과거 OPEN 자동 종결 처리 금지**; Tracker sync 필요 | F/D 실제 source·발표 화면 및 문서 update |
| AUD-01/04/11/12 | 과거 통합·Minor 항목 | Planner/Builder | **현재 정적 55/120·분할·핵심 인터랙션 증거 확보**. 110 동일 SHA 화면/실강의 검증 범위는 미완료이므로 **통합 검증 Gate OPEN / NOT VERIFIED** | 110 view 전수·필수 기능 재실행 |
| G-01 | Major | Builder | **CLOSED**: 100건 histogram/axis 실제 Score 재계산 | G 10 view + threshold 14 assertions |
| G-02 | Minor | Builder | **CLOSED**: P52 GT 청록·Prediction 주황색 P14와 일관 | G SVG/Caption |
| H-01 | Major | Builder | **CLOSED**: 테두리 변경→실제 합성 외부 배경 Pixel 변경, Apple/ROI 고정 | H 독립 Mask Pixel 산술 |
| H-02 / H-03 | Minor | Builder | **CLOSED**: P53 생성/ROI Caption 및 P54 Image.onload readiness | H 6 PNG + JSON |
| H-04 | Minor | Builder | **OPEN**: P54 Figure 설명과 SOURCES 이력 불일치 | 하단 세부 수정 |
| FINAL-DOC-01 | Minor | Builder/Planner(문서 정합성) | **OPEN 신규**: `automation/PROGRESS.md` 첫 상태표의 G final pending/H review pending, `TODO_VISION_AI_LECTURE.md` 상단 '현행59장'이 55 승인 Manifest와 모순됨. 이전 이력을 삭제할 필요 없이 최신 활성 상태와 구버전 이력을 분리할 것 | 문서 상단 55/120 및 A–H 최종 report link 일치 확인 |

이전 `reviews/CURRENT_REVIEW_REPORT.md`는 최신 55 최종보고서가 아닌 과거 Issue 근거임. 과거 OPEN을 무조건 현재 새 Critical/Major로 집계하지 않았고, 반대로 CI만으로 실강의/전체 화면 재검증이 해결됐다고 간주하지 않음.

## 7. Actionable residual findings

### A-R1 · Minor · Builder · P04

- **근거:** `docs/intro.html` `data-concept="photo-numbers"`; 12×8 수치가 원본 전체 Downsample임을 정확히 명시, 동일 원본 사진의 한 좌표 ↔ 특정 숫자 Cell의 선택/하이라이트 연결은 없음.
- **학습 영향:** 숫자 격자가 사진에서 유래함을 초보자가 추적하기 어려울 수 있음. 수식/데이터 왜곡이나 전체 Slide PASS 차단 이슈는 아님.
- **권고:** 선택 Cell을 클릭하면 해당 원본 사진의 대응 샘플 영역도 표시하거나, 하나의 정적 매칭 예시를 추가; 기존 Downsample 계산을 바꾸지 말 것.
- **재검증:** 1920/1366에서 선택 ROI와 숫자, 사진과 Grid의 대응/텍스트 가독성 확인.

### H-04 · Minor · Builder · P54

- **근거:** `assets/SOURCES.md`의 "Approved group H P53–P55"에서 P54를 colored outer border, 실제 배경 교체 아님으로 기술. 실제 `docs/vision_ai_course.html` P54는 같은 Apple에 clipPath로 외부 배경 pixel을 회색선/격자 합성. Figure '합성 A · 단색 배경'에는 얇은 선무늬가 포함됨.
- **영향:** 핵심 Apple/ROI 불변과 외부 배경 변경 결과는 정확. 그러나 실험 조건 설명/출처 메타데이터를 오해할 수 있음. **H PASS는 유지**.
- **수정:** `assets/SOURCES.md`를 '동일 생성 사과·동일 clipPath/ROI, 바깥 배경만 합성, 실측/Prediction 아님'으로 수정. '단색 배경'→'무늬가 적은 배경'으로 고치거나 실제 패턴 제거. 원래의 테두리만 바꾸는 오류로 회귀 금지.
- **재검증:** SVG 마스킹·Caption·SOURCES 설명 일치, 1366/1920 P54 화면.

### FINAL-DOC-01 · Minor · Builder + Planner(최신 상태 문서)

- **근거:** 최신 `automation/PROGRESS.md` 최초 표는 G 최종 Reviewer pending, H review pending을 유지하고, `TODO_VISION_AI_LECTURE.md` 상단은 59장/118화면을 활성 기준처럼 표시함. 최신 manifest/plan은 승인된 55장.
- **영향:** Merge 전에 잔여 과제를 잘못 선정하거나 오래된 Course 번호로 QA 가능.
- **수정:** 승인 55/120과 최종 A–H report 경로 및 Issue 최신 상태로 **현재 상태 섹션만** 교정, 과거 기록은 명시적으로 역사 영역에 보존.
- **재검증:** Intro13/Course42, 110화면 목표, 8구간 링크/Issue 목록의 상대 경로 확인.

### FINAL-GATE-01 · NOT VERIFIED / Final QA gate, not a proven content defect

- **현상:** `f5e0ac5`에서 새 Chromium 55×1920 및 55×1366 합계 **110개 화면을 같은 SHA로 생성/개별 육안 판독하지 못함**. 동일 SHA의 global interaction/keyboard/Reset 회귀 재실행도 미완료.
- **담당:** Builder가 같은 SHA(또는 Minor 변경 후 새로운 고정 SHA)의 CI에서 110 PNG/JSON, Canvas await, asset/console/overflow, nav/keyboard/Reset report를 생성; **Reviewer가 전체 110 PNG 각각 직접 확인**. CI PASS만으로 Figure 의미·오해 없음 결론 금지.
- **재검증:** 보고서에 55행 × 2뷰의 파일/검수자 판정, 수정 전후 SHA, 실패/차단 원인, 재검증 결과를 누락 없이 기록. A–F 회귀는 P04/09/16/20/27/29/35/41/43/45/48/54 특히 우선. 기존 110 화면 이력은 참고만.
- **한계:** 공개 Pages 실제 배포 확인은 main merge/배포 금지로 지금 수행하지 않음. 실제 120분 리허설/학습자 테스트는 별도 교육 검증 Gate.

## 8. Completion checklist and merge decision

| 조건 | 상태 |
|---|---|
| 승인 기획 ↔ HTML/Manifest/Outline, 55/120 | **PASS** |
| A–H 구간별 최종 독립 보고서 | **8/8 확인, 모두 구간 PASS** |
| 수식/주요 Tensor/Matrix/Threshold/IoU 계산 | **대표 독립 재계산 PASS; 모든 Figure 새 육안 NV** |
| A–H 기존 Critical/Major 해결 | **확인된 현재 미해결 Critical/Major 0**, 구버전 AUD 상태 재정리 필요 |
| G/H 최신 2뷰 CI + 전역 route/interaction | **관련 이전 SHA CI PASS**, 최종 SHA 새 실행 NV |
| 110/110 같은 SHA 화면 전수 캡처·독립 판독 | **NOT VERIFIED** |
| 실제 발표실 120분/초보자 사용성 | **NOT VERIFIED** |
| 공개 Pages/new main | **NOT VERIFIED / 사용자 지시로 미수행** |
| H-04, A-R1, FINAL-DOC-01 | **Minor OPEN**, 기능/기술 오류 확정 아님 |

**종합 판정: CONDITIONAL PASS (최종 PASS 아님).** 주요 기술적 결함은 현재 확보한 근거에서 확인되지 않았으나, 명시적으로 요구된 동일 SHA 전수 110화면 및 전체 회귀의 신규 독립 실화면 검증이 완료되지 않았으므로 **main Merge: HOLD / 비권고**, GitHub Pages 배포: **금지 유지**. 이 Gate가 통과하고 새 Critical/Major가 없을 때 최종 PASS를 부여할 수 있음. Planner는 전체 교육 흐름의 구조 변경보다 실제 강의 리허설 및 피드백을 우선; Builder는 화면/기능 증거와 문서 Minor를 정리.

**권한 준수:** 이 문서만 별도 Reviewer 브랜치에 추가. `docs/`, `assets/`, 승인 스토리보드, 통합 브랜치 및 `main` 수정·Merge·배포 없음.
