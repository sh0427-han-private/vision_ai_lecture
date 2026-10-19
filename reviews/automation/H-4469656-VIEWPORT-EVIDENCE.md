# H구간 P53–P55 독립 검수 — 고정 SHA 실제 화면·실행 증거 보충

> 2026-10-19 KST. **기존 판정 보고서**: [H-4469656.md](H-4469656.md). 기존 정적 검수 결과와 Issue를 삭제하거나 소급 변경하지 않고, 추가로 **실제로 실행·관찰한 범위만** 기록한 후속 증거다.

## 0. 불변 검수 기준 및 판정

- **Builder 원본**: `automation/approved-55-20261019`의 `4469656244e55476b2c0e8ca2a1344a9710a29db`만 대상으로 한다. 원본 이후 G 수정분, Builder 브랜치 HEAD, `main`, Pages의 현재 배포본은 검수 기준에 반영하지 않는다.
- **Reviewer 브랜치**: `review/h-4469656-20261019`. 추가 GitHub Actions 워크플로·QA 스크립트·Markdown 보고서는 Reviewer 측 검증 수단이며, Builder HTML/CSS/JS/스토리보드 수정이 아니다.
- **현재 H 판정**: **CONDITIONAL PASS**. 기술·교육 흐름과 실제 두 뷰포트의 레이아웃·Canvas·내비게이션 검증 통과. **Critical 0 / Major 1 OPEN(H-01) / Minor 2 OPEN(H-02/H-03)**. Major Figure의 의미 전달 문제는 두 뷰포트의 PNG에서 재확인했으므로 전체 시각적 품질 최종 PASS 아님.
- **증거**: [성공한 CI 39242347432](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39242347432) / Reviewer CI HEAD `8ff7c45c53fa0fac951e2321c771f2be06772dc4` / [스크린샷+JSON+로그 Artifact #12182495001](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39242347432/artifacts/12182495001). 해당 실행은 `git diff --name-only 4469656... HEAD -- docs planning automation`의 불변성 검사부터 성공함.

## 1. 독립 실행 QA — 무엇을 실제로 확인했는가

| 구분 | 실행/관찰 결과 | 근거 |
|---|---|---|
| 승인 55장 최종 계약 | **PASS** | `automation/verify_approved_contract.py --final`: `APPROVED55_FINAL_CONTRACT_PASS 55 slides; 120 minutes` |
| 독립 수치·Figure 소스 검사 | **PASS** | `scripts/verify_two_hour_course.py`: `FINAL_55_STATIC_QA_PASSED` (합성곱/모양/학습·평가지표·분할·자산·공유 모델 등) |
| 전체 이동·핵심 Interaction | **PASS** | `scripts/verify_learning_routes.py`: `TWO_HOUR_NAV_QA_PASSED: 55 slides, TOC, legacy redirects, chapter boundary, real training update, threshold recalculation, review answer, no JS errors` |
| H 실화면 | **6/6 PASS (기술적 표시 검사)** | `reviews/automation/h_chromium_qa.py`, `1920×1080` 3장 및 `1366×768` 3장, PNG 직접 육안 확인 |
| H fit/overflow | **PASS** | 6뷰 fit = 1,1,1,1,1,0.968(최소 0.968); 모든 Content Bottom/Right/Browser Horizontal Overflow 0; JS `page_errors=[]`, `failures=[]` |
| P54 이미지 Raster | **PASS** | 각 뷰포트에서 실제 Canvas `240×240`=57,600 opaque 픽셀, `24×24`=576 opaque 픽셀. 양쪽 `data-ready=true`, 색상 범위 존재, 화면에서 서로 다른 샘플링 확인 |
| P55 조작·구간 이동 | **PASS** | 두 뷰포트 `details` 열기/닫기, 키보드 Course42→41→42 이동 확인; 네 답 카드 DOM 순서 `pixel/feature/learn/evaluate` |
| 55장 × 2해상도 전체 캡처/120분 실측/Pages 본 운영 | **NOT VERIFIED** | H 6뷰만 본 턴에서 독립 PNG 확인. 55장의 110뷰 실화면 전수, 강의 리허설 및 공개 사이트는 이 CI 성공에 포함되지 않음 |

**자료의 의미**: GitHub Actions가 고정 소스를 Checkout하고 Playwright Chromium으로 화면을 렌더한 것이며, Reviewer가 성공 CI의 6개 PNG와 `report.json`을 별도로 열어 육안 검사했다. Builder가 주장한 소스 PASS만 받아들인 것이 아니다. 이 성공 실행의 6개 PNG가 앞선 부분성공 실행의 PNG와 **픽셀 단위 동일**함도 이미지 비교로 확인했다.

## 2. 6개 화면의 직접 관찰

| 승인/실제 | 1920×1080 | 1366×768 | 콘텐츠·Figure 시각 판정 |
|---|---|---|---|
| **P53 / Course40 / workflow** | 제목·사과 ROI·5단 흐름과 네 설계 질문·점선 연결·마지막 Test 경고 모두 표시, 잘림 0 | 동일. 네 질문이 노드 2·2·4·5로 연결되는 실제 선 확인. 노드/텍스트 겹침 0 | 시각 흐름 **PASS**. 단 사과 초록 원은 실제 Model Detection처럼 보일 여지가 있는 **H-02 Minor** 근접 캡션 보완 필요 |
| **P54 / Course41 / project-iterate** | 조명·배경·해상도의 3열, 6개 사진/Canvas와 관찰→가설→추가 비교, 생성·비실측 고지 가시적 | 동일. 비교 이미지 자르기/텍스트 잘림 없음. 24×24 확대는 실제로 블록 픽셀로 보임 | **H-01 Major OPEN**, 실제 화면에서 배경 카드 좌우의 사과/배경 사진은 **완전히 동일**하고 청록 테두리만 다름. 밝기·해상도와 달리 배경 변화 현상을 실질적으로 설명하지 못함 |
| **P55 / Course42 / project-check** | 중심 원본 사진과 좌상 Pixel, 우상 Kernel, 좌하 Learning, 우하 Recall 카드 및 가상 수치 주석 모두 표시 | 동일. 가운데 Class/Mask Label은 좁은 폭으로 여러 줄이지만 잘리지 않음; 네 카드 정상 정렬 | 시각/숫자 **PASS**. `Recall=18/20=90%`, Kernel 첫 `−6` 다음 `12`, 회귀 예 `w:0.5→1.7; L:9→0.36`의 선행 예제 대응 유지 |

이 캡처는 모두 고정 원본을 대상으로 생성됐고, 조명이 어두워진 이미지와 24픽셀 확대는 교육용 **표시 변환**이지 실제 모델 오류·측정 결과가 아니다. P54 중간 배경 카드는 **테두리 표시**만 한 것이다.

## 3. Builder에게 요청하는 최소 수정·재검증 조건

1. **H-01 / Major / P54** — `docs/vision_ai_course.html`의 배경 카드 및 `docs/approved_h.css`의 `.h55-background svg`에서 외곽선 추가만 하는 방식은 배경 변수를 보여주지 못한다. 피사체 사과/결함 ROI/크기와 조명은 동일하게 유지하고 실제 **배경 픽셀만 다른 교육용 합성 이미지 두 개**를 대응시킨다. '합성 통제 비교·실제 모델 실패/예측 아님'을 사진 가까이에 명시. 두 뷰포트 PNG에서 배경 차이·ROI 통제·사진/레이블 크기를 재확인.
2. **H-02 / Minor / P53** — 같은 생성 사과 사진 및 초록 ROI 원 근처에 '교육용 생성 사진 · 원은 설명용 주석 · 모델 검출 결과 아님'을 가독성 있는 Caption으로 표기. 두 뷰포트에서 확인.
3. **H-03 / Minor / 표준 스크린샷 검사** — `automation/check_group_browser.py`의 P54 캡처는 `data-ready=true`인 두 Canvas를 기다리도록 보완. Reviewer 전용 `reviews/automation/h_chromium_qa.py`는 실제로 로딩 완료/픽셀을 검증해 본 H 검수에는 미완료 노출이 없지만 Builder 표준 툴 수정은 별도 필요.

**재검증은 반드시 Builder가 제시하는 새 수정 Commit을 별도 후속 대상으로 지정해야 한다.** 현 `4469656`의 Issue를 현재 Builder HEAD가 바뀌었다는 이유만으로 닫거나 이 보고서를 기존 소급 PASS로 변환하지 않는다. G Reviewer의 `G-01 Major`(Score 분포 계약), `G-02 Minor`(GT 색 일관성)도 H PASS로 자동 종결하지 않는다.

## 4. 검수 범위와 제한

- 승인 P53–P55 **3/3장(100%)**, **H의 6/6 두 화면**을 실제 독립 렌더링 이미지로 검사. Manifest/Outline은 실제 HTML·승인 계획과 전역 55/55 순서 일치, H 시간 2+1.5+1.5=5분, 전 구간 26+10+23+22+9+15+10+5=120분으로 확인.
- 기획 `approved55.json`의 화면용 제목 축약 9건(P01, P05–P11, P17)은 전체 Concept ID/순서 오류가 아닌 별도 기존 표기 정합성 참고사항. H 제목 3개는 일치.
- **독립 H 화면 6장 이외** 전 슬라이드 110-view 브라우저 육안 전수, 교육 대상자의 실제 학습 이해도, 강의 120분 리허설, 현재 `main`/Pages 화면은 **NOT VERIFIED**. 이 작업에서 `main` Merge·Pages 배포는 수행하지 않는다.
