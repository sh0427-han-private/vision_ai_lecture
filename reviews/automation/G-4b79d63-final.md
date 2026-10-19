# G구간(P48–P52) 최종 독립 재검수 — PASS

- **최종 판정:** **PASS — G구간 기술·수치·Figure·자동 브라우저 QA 범위**. Critical 0 / 미해결 Major 0 / 미해결 Minor 0.
- **검수일:** 2026-10-19 (KST).
- **저장소/통합 브랜치:** `sh0427-han/vision_ai_lecture` / `automation/approved-55-20261019`.
- **검수 기준 Builder 소스/QA SHA (고정):** `4b79d63ab422ac404dc91e45c7ff54ecd7ce3d8a`.
- **수정 구현 Commit:** `025d03679f570e3d2587b79ff263030e209b5e9f`; `4b79d63`은 G Chromium 검증 스크립트의 SVG 텍스트 추출 오류만 교정.
- **기존 Reviewer 원본:** [`reviews/automation/G-d27e160c.md`](https://github.com/sh0427-han/vision_ai_lecture/blob/review/g-d27e160c-20261019/reviews/automation/G-d27e160c.md), 고정 원본 `d27e160cdec960cdb7c9b056ee5112b4051ac896`, 판정 **CONDITIONAL PASS** (Critical 0, Major G-01 하나, Minor G-02 하나). 원본 보고서는 보존.
- **본 보고서 독립 브랜치:** `review/g-final-4b79d63-20261019` (검수 기준 SHA에서 분기). 본 파일만 기록하며 HTML/CSS/JS/스토리보드에는 쓰기 없음.
- **검수 범위:** 승인 계획 P48–P52 = `docs/vision_ai_course.html` Course 35–39; Concept ID `threshold, confusion, imbalance, metrics, iou`. **5/5장, 10분**.
- **기준 문서:** `planning/SLIDE_STORYBOARD.md`, `HTML_DESIGN_RULES.md`, `PROJECT_GUIDE.md`, `TWO_HOUR_LECTURE_PLAN.md`, `docs/two_hour_manifest.json`, `docs/lecture_outline.js`, `assets/SOURCES.md`, 원본 G 보고서 및 변경 Commit.
- **증거 출처:** [성공한 Chromium GitHub Actions Run 39239754107](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39239754107) 및 [10 PNG + report.json 아티팩트 12180258476](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39239754107/artifacts/12180258476). 실행 로그에 `APPROVED_G_BROWSER_QA_PASSED {"head":"4b79d63ab422ac404dc91e45c7ff54ecd7ce3d8a","screens":10,"interactive_checks":14}` 기록. Reviewer는 아티팩트 ZIP을 회수해 PNG 10장과 JSON 수치를 별도 열람·분석함.

## 1. Issue closure

| Issue | 최초 증거·영향 | 수정 확인 | 최종 상태 / 담당 / 재검증 |
|---|---|---|---|
| **G-01 Major** | P48 histogram의 실제 Score 분포가 승인된 100건 multiset과 다름. 기존 그래프 눈금 0–30으로 50건 bin 표시 불가 | `docs/project_course.js:6–13`: 승인된 7개 Score/Label 구간을 100개 배열로 재구성. `renderHistogram`: 실제 peak에서 `axisMax = max(50, ceil(peak/10)*10)`, `unit=160/axisMax` 계산. 표·막대·지표 모두 `scores`에서 재집계. CI DOM 10 bins(합100), 최고50건 막대 위치 범위 및 세 임계값 검사 통과. 실제 P48 2해상도 캡처에서 0.2:50, 0.4:28, 0.6:9, 0.8:13 및 기준선 표시 확인 | **CLOSED / Builder 해결·Reviewer 재검증 완료**. 다음 G JS 변경 시 동일 100건·3 threshold·SVG bounds/마커/Reset 회귀 실행 |
| **G-02 Minor** | P52 GT 녹색이 P14 GT 파란색과 불일치해 의미 색상 일관성 저하 | `docs/vision_ai_course.html`의 P52 사진 및 수치 격자 두 GT 외곽선·채움이 `#187c9a`. `docs/approved_g.css`의 `.g55-iou .g55-pos` 파란색. Prediction 주황 `#c17b27` 유지, 중첩 음영 구분. CI P14 파란색 참조 및 P52 두 GT/Pred box/legend 계산색 확인; P52 두 캡처 육안 확인 | **CLOSED / Builder 해결·Reviewer 재검증 완료**. GT/Predict 색상·범례, 대조도 및 IoU 산술을 재검증 |

### 독립 수치 검산 — P48

`docs/project_course.js`에 실제 구현된 분포를 기준으로 Reviewer가 별도로 Python에서 100건을 재구성해 계산함:

| Label | Score | Count |
|---|---:|---:|
| 실제 불량(1) | 0.8 / 0.6 / 0.4 | 11 / 7 / 2 = **20** |
| 실제 정상(0) | 0.8 / 0.6 / 0.4 / 0.2 | 2 / 2 / 26 / 50 = **80** |

| Threshold (`score >= t`) | TP | FN | FP | TN | 합계 | Precision | Recall |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.30 | 20 | 0 | 30 | 50 | 100 | 40.0% | 100.0% |
| 0.50 | 18 | 2 | 4 | 76 | 100 | 81.8% | 90.0% |
| 0.70 | 11 | 9 | 2 | 78 | 100 | 84.6% | 55.0% |

실제 분포는 0.2×50(정상), 0.4×28(불량2+정상26), 0.6×9(불량7+정상2), 0.8×13(불량11+정상2). 분포 히스토그램·Threshold 마커와 네 혼동행렬 칸의 의미가 일치. 0.50 기본값으로 P49/P51 고정 예시가 연결됨. **교육용 구성 Score**이며 확률로 보정된 값이나 실제 추론 성능이 아니라는 Caption이 유지됨.

## 2. 전수 재검수: 5/5

| 전역 P | 물리 Course | Concept | 기술·교육 흐름 | Figure / 출처 | 1920×1080 및 1366×768 / 기능 | 판정 |
|---|---:|---|---|---|---|---|
| **P48** | 35 | `threshold` | 실제 Score 100개 재계산 PASS. P47 새 데이터 일반화 → Validation에서 threshold 선택 → P49 고정 평가로 전개. FP/FN trade-off·비확률 Score 명시 | 0.2/0.4/0.6/0.8 bin 각각 50/28/9/13; 전체 20 불량/80 정상. 눈금 0–50과 기준 0.50 line이 실제 데이터와 정합. 자체 SVG·JS | **2/2 스크린 PASS**, 1366×768 `fitScale=0.913`, 화면 overflow 없음. CI threshold 변경·Home/End·Enter/클릭 Reset·DOM/막대/표 동기화 **14 상태 assertion PASS** | **PASS** |
| **P49** | 36 | `confusion` | `Threshold 0.50` 참조: TP18/FN2/FP4/TN76, Accuracy `(18+76)/100=94%`. 정답 행 / 예측 열 구분 정확 | 2×2 HTML Figure, 정답 20·80과 찾은/놓친 값 일치 | **2/2 스크린 PASS**; CI 네 count 검사, 눈에 띄는 잘림·겹침 없음 | **PASS** |
| **P50** | 37 | `imbalance` | 모두 정상 예측 기준: Accuracy 80%, 불량 Recall 0%. P49 94%와 대비하며 불균형 평가의 함정 설명 | 실제 눈에 보이는 100칸 중 놓친 불량 20칸, HTML 교육용 자체 구성 | **2/2 스크린 PASS**; CI `100 spans / 20 pf-miss` 검사; 가독성·배치 양호 | **PASS** |
| **P51** | 38 | `metrics` | 동일 t0.50에서 Precision `18/(18+4)=81.8%`, Recall `18/(18+2)=90%`. P49의 고정 참조 명확 | 22점(18 TP+4 FP), 20점(18 TP+2 FN) 분모가 보이는 Figure | **2/2 스크린 PASS**; CI `22/20` DOM 검사, 두 비교 Figure 가독성 양호 | **PASS** |
| **P52** | 39 | `iou` | Class 판정과 위치 정확도 구분 → P53 전체 흐름 회수. 수치 별도 격자 GT(1,1)~(6,7), Pred(1,3)~(6,9), 각 면적30, 교집합20, 합집합40, **IoU 0.5** 검산 PASS | 동일 AI 생성 사과 사진은 위치 설명용(실측 예측 아님), 정수 좌표 예제는 별도 산술. GT 파랑/예측 주황/겹침 중첩 구분. 출처 `assets/SOURCES.md` | **2/2 스크린 PASS**, SVG `image` 정상 디코딩, P14와 GT 색 일관성 확인. 잘림·겹침 없음 | **PASS** |

## 3. Chromium 실행 및 Reviewer 육안 검토 증거

- **실제 실행 주체:** GitHub Actions `Approved G P48-P52 browser re-review` (run `39239754107`, head SHA `4b79d63...`), Ubuntu Playwright Chromium Headless Shell 156. Job `g-browser`의 checkout / 설치 / 브라우저 테스트 / artifact 업로드 단계 **SUCCESS**. Browser 스크립트 `scripts/verify_approved_g_browser.py`.
- **실제 캡처:** `1920x1080_{threshold,confusion,imbalance,metrics,iou}.png` 및 `1366x768_{threshold,confusion,imbalance,metrics,iou}.png` **총10개**. Reviewer가 성공 Run에서 ZIP을 다운로드하고 모든 PNG를 이미지/몽타주로 눈으로 비교함.
- **실제 JSON 근거:** `report.json`에는 10개의 `screens`, 14개의 `interactions`, `issues=[]`, `page_errors=[]`, `console_errors=[]`. 모든 화면의 `contentBottomOverflow=0`, `contentRightOverflow=0`, `browserHorizontalOverflow=0`. P52 이미지 `loaded:true` 각각 확인.
- **이미지 및 Figure 검수:** P48은 1366에서도 SVG 50건 막대·표·메트릭·문구가 모두 보이며 왜곡/클리핑 없음. P49–P51 숫자·색상·분모 연결 명확. P52 실선 GT 파란색, 점선 Pred 주황색, 5×4 겹침 및 IoU 0.5 기호 가독성 확인. 두 화면에서 제목·Footer·본문 분리됨.
- **독립성 구분:** **테스트/렌더 실행 = Builder 작성 CI에서 실제 실행됨, GitHub 로그와 artifact로 관찰**; **Reviewer 수치 계산 = 별도 Python 독립 실행**; **Reviewer 화면 판독 = CI가 생성한 원본 PNG를 직접 열어 독립 시각 검수**. Reviewer가 고정 SHA 전체 저장소를 재클론해 두 번째 독립 Chromium 세션을 직접 수행한 것은 아님(로컬 외부 GitHub DNS 불가). 이를 독립 실행으로 과장하지 않음.
- **실패 이력:** `025d036`의 초기 CI run `39239565086` 실패는 SVG `inner_text()` assertion 문제. `4b79d63`에서 테스트 한 줄을 SVG `text_content()`로 수정한 후 성공. 그 사이 G 강의 콘텐츠의 JS/HTML/CSS 변경 없음.

## 4. 회귀 범위 / 55장 계약

- `025d036..4b79d63`: 변경은 **`scripts/verify_approved_g_browser.py`의 1행 치환만**이며 강의 코드/자산 변화 없음.
- `4b79d63..07ddcb273a72ef5cf6d6869388017f2ba27dae42`(조사 시점 통합 브랜치 HEAD): 변경은 **`automation/PROGRESS.md`의 G CI 증거 기록만**, G 콘텐츠 변경 없음. 검수 기준은 그럼에도 **`4b79d63`에 고정**.
- `d27e160c..4b79d63` 구간은 H 최종 슬라이드·Manifest/Outline 55장 정리와 G 후속 수정이 함께 포함됨. G 검수 범위 밖인 H/A–F 전체 렌더를 PASS로 확장하지 않음.
- 고정 SHA Manifest: Intro **13**, Course **42**, 총 **55**. G `threshold/confusion/imbalance/metrics/iou` = Course **35–39** = 전역 P48–P52, Outline도 전역 **48–52**. Block time `26+10+23+22+9+15+10+5=120분`, G **10분**. 검수 기준의 G 수·순서 불일치 없음.
- HTML source/JS/CSS, 고정 SHA manifest·outline, 스토리보드와 원본 Reviewer 보고서를 독립 대조. 다만 **55장 전체 Python 계약 실행, A–F/H 전수 회귀 렌더, 모든 TOC/Deep Link 조작**은 이 G 후속 검수의 직접 실행 범위를 벗어나며 **NOT VERIFIED**.
- **배포 환경 GitHub Pages, 학습자 실사용, 120분 현장 리허설:** **NOT VERIFIED**. CI 화면은 작업 SHA의 Chromium 결과이며 공개 Pages 검수 결과로 대체하지 않음.

## 5. 최종 Gate

- **G 최종 결론: PASS**, 검수 커버리지 **5/5장, 10/10화면** (CI 실제 화면 아티팩트 + Reviewer 수동 시각 확인), G-01 **CLOSED**, G-02 **CLOSED**. 이번 검수에서 신규 Critical/Major/Minor 없음.
- **Builder 필수 G 잔여 수정:** 없음. G 소스가 추가 변경되면 해당 Commit에서 동일 Threshold/Histo/Reset/IoU/two-view QA 재실행.
- **Planner:** G구간 삭제/통합/순서 재설계 권고 없음. 전역 A–H 최종 계약/학습 리허설은 별도 최종 Gate.
- **Reviewer 권한:** 이 보고서 이외의 강의 구현 파일 변경 없음. **main Merge / GitHub Pages 배포 금지 및 미수행**.
