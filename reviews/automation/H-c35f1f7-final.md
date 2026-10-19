# H구간(P53–P55) 수정 후 최종 독립 재검수 — PASS

- **최종 판정: PASS** (검수 범위 내 Critical 0, 미해결 Major 0; 신규 Minor H-04 1건은 미차단).
- **검수 일자:** 2026-10-19 (KST).
- **검수 고정 Builder SHA:** [`c35f1f7175788921f2a924f3ef1f4e0e552bb5e2`](https://github.com/sh0427-han/vision_ai_lecture/commit/c35f1f7175788921f2a924f3ef1f4e0e552bb5e2). 이 이후 `automation/approved-55-20261019`의 이동한 HEAD를 검수 기준으로 사용하지 않음.
- **소스 브랜치:** `automation/approved-55-20261019`; **기록 전용 Reviewer 브랜치:** `review/h-final-c35f1f7-20261019` (정확히 위 SHA에서 분기).
- **구간:** 승인 P53–P55 = 본강의 Course 40–42 (`workflow`, `project-iterate`, `project-check`), 3/3장, 2+1.5+1.5=5분.
- **원본 Reviewer 보고서:** [`review/h-4469656-20261019/reviews/automation/H-4469656.md`](https://github.com/sh0427-han/vision_ai_lecture/blob/review/h-4469656-20261019/reviews/automation/H-4469656.md), 보조 Chromium/Viewport 기록. 원본 판정 CONDITIONAL PASS·H-01/02/03 OPEN은 이력으로 보존.
- **참고:** 승인 `planning/SLIDE_STORYBOARD.md`, `planning/approved55.json`, `HTML_DESIGN_RULES.md`, `PROJECT_GUIDE.md`, `TWO_HOUR_LECTURE_PLAN.md`, `assets/SOURCES.md`, `docs/two_hour_manifest.json`, `docs/lecture_outline.js`, 고정 SHA의 HTML/CSS/JS와 브라우저 스크립트.

## 1. 기존 Issue 해결 판정

| Issue / 담당 | 원래 원인 | 수정 후 독립 확인 | 최종 상태 |
|---|---|---|---|
| **H-01 Major / Builder** | P54 배경 대조가 실제 배경 변경 없이 사진 바깥 테두리만 달랐음 | `docs/vision_ai_course.html` P54에서 `matte`/`grid` SVG는 동일 JPEG, `viewBox=300 85 450 450`, 동일 `<clipPath>` path/원본 960×640/결함 ROI circle 사용. 회색/격자 배경은 피사체 바깥 실제 픽셀에 합성됨. CI 렌더 + 별도 원본 PNG 픽셀 검산 확인. `교육용 합성·모델 예측 아님` 문구도 유지. | **CLOSED** |
| **H-02 Minor / Builder** | P53 생성 사진과 초록 ROI의 설명용 성격이 인접 표기되지 않았음 | `docs/vision_ai_course.html` P53의 사진 바로 밑에 `교육용 생성 사진 · 초록 ROI는 설명용 주석 / 모델 검출 결과 아님` 추가. 1920/1366 PNG에서 실제 노출 확인. 작은 폭에서는 `ROI는` 사이에 자동 줄바꿈이 생기지만 판독과 의미는 보존. | **CLOSED** |
| **H-03 Minor / Builder** | 기존 H Screenshot은 Canvas 비동기 Image.onload 완료를 기다리지 않아 미완성 이미지가 캡처될 위험 | `automation/check_group_browser.py`의 P54 특례: 두 Canvas `dataset.ready==='true'`, 각각 240×240/24×24, 픽셀 불투명도·비균일성 검사를 20초 timeout으로 기다림. 오류 시 `canvas_errors` 기록 및 캡처 생략. 고정 SHA CI 2뷰에서 모두 준비 완료, 캡처 성공. | **CLOSED** |

## 2. P54 배경 대조: 원본 PNG 기반 Reviewer 독립 픽셀 검산

- 증거: [H Chromium 성공 Run #39246424771](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424771) · [`approved-h-browser-qa` 아티팩트 #12183008736](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424771/artifacts/12183008736). 6개 전체 화면 PNG + 4개 분리 배경 SVG PNG + `report.json`을 **다운로드·열람**함.
- Builder CI가 생성한 `1920-background-{matte,grid}.png` 및 `1366-background-{matte,grid}.png`는 각각 동일 크기 200×200의 정밀 비교용 Chromium SVG 캡처임. Reviewer는 Python/Pillow, NumPy, CairoSVG 및 OpenCV를 사용해 **그 원본 PNG에 별도 픽셀 연산을 수행**함. 독립된 Chromium 재실행으로 오인하지 말 것.
- Figure 소스의 정확히 같은 clipping path를 CairoSVG로 200×200 raster mask화하고 완전불투명 영역을 2px erosion해 경계 안쪽만 비교했음. **피사체 내부 비교 픽셀 18,623개 중 바뀐 픽셀 0개** (두 뷰포트 모두). 녹색 ROI 중심 `(596,226)`의 렌더 RGB `(109,72,46)`도 양측 동일. 초록 원의 SVG outerHTML·반지름·중심, clip path, 원본 링크 모두 양쪽 일치.
- 마스크 바깥의 안쪽 경계를 제외한 **배경 영역 18,179개 픽셀 중 1,490개가 채널별 차이 최대치 >8** (8.20%). 전체 비교 PNG 픽셀 차이의 합집합은 3,312픽셀. 두 뷰포트에서 동일한 결과. 즉 **사과·ROI와 원본 사진 Crop/조명은 고정**하고, 바깥 배경의 실제 raster 픽셀은 다르게 렌더됨. JPEG 내부 측광 실험이나 실제 모델 실패 결과를 증명하는 그림은 아님.
- 주의: 클리핑 경계의 antialias blending까지 모든 화면 픽셀이 절대 동일하다고 주장하지 않음. 검사 영역은 마스크 내부 2px margin, ROI 중심, 외부 배경으로 정의함. 렌더는 둘 다 같은 SVG clip geometry 및 원본 image로 작성돼 피사체 내부 불변 조건을 충족함.
- Canvas 비교: 양 Viewport 모두 준비 상태 `true`, 240×240 **57,600/57,600 불투명 픽셀** 및 24×24 **576/576 불투명 픽셀**. 소스 `docs/approved_h.js`의 하나의 `drawImage(300,85,450,450)` Crop으로 두 크기를 생성하며 저해상도만 `image-rendering:pixelated`로 확대함.

## 3. 전수 P53–P55 교육·실화면 검수

| 계획 / 실제 | Concept | 기술·교육 내용 | 1920×1080 / 1366×768 Renderer 및 Figure | 판정 |
|---|---|---|---|---|
| **P53 / Course 40** | `workflow` | P52 IoU에서 사과 원리 복습으로 이동; Pixel→Task+Label→CNN→Training→독립 Eval 5노드 및 실제 4개 질문 연결. Train 학습/Val 선택/독립 Test 확인을 구분, Test 반복 최적화 금지. Caption 자료 성격 정확. | **2/2 PNG 직접 육안 확인**, 최소 fit 0.984. 1366에서도 사진·Caption·다섯 노드·선 연결 표시되고 잘림/겹침 없음. | **PASS** |
| **P54 / Course 41** | `project-iterate` | 조명/배경/해상도 세 가설을 실제 성능 주장 아닌 단일 조건 비교로 설명. 배경 SVG의 원본·마스크·ROI 동일, 외부 픽셀 변경. 조명 CSS 0.35는 표시 변환, Canvas 24·240은 동일 Crop. | **2/2 PNG 직접 육안 확인**, 최소 fit 0.943. 세 가설 Figure 및 배경 차이 확인, Canvas 2개 모두 완료. 배경 독립 정밀 픽셀 검산 통과. | **PASS** (H-04 Minor 별도) |
| **P55 / Course 42** | `project-check` | 4개 회수: H×W×3, Kernel/Map −6→12, 학습 예제 w0.5→1.7 Loss9→0.36, Recall 18/20=90%. 서로 다른 교육용 예제를 하나의 실측 모델로 주장하지 않음. | **2/2 PNG 직접 육안 확인**, 최소 fit 0.968. 4카드와 중앙 이미지, 자료 성격 주석 가독. `details` 상호작용은 전역 자동 회귀 PASS, 개별 수동 클릭은 미수행. | **PASS** |

- 전 화면 `report.json`: **6/6**, `contentBottomOverflow=0`, `contentRightOverflow=0`, `browserHorizontalOverflow=0`, `overlaps=[]`, `page_errors=[]`, `layout_issues=[]`, `canvas_errors=[]`; 최소 `fitScale=0.943`. 실제 PNG 육안 검토에서도 이미지 Crop 왜곡/누락·본문 또는 Footer 중첩·중요 내용 잘림 없음.
- 1920×1080에서 중앙 콘텐츠 좌우 여백은 넓지만 텍스트와 도식이 정상 노출됨; 1366×768 역시 발표용 핵심 숫자와 비교 결과가 읽힘. 모든 문장이 일반적인 학습자에게 충분히 이해됐는지의 실강의 검증은 아님.

## 4. 계약·회귀 및 CI

- 동일 SHA H CI Run [39246424771](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424771), Job `h-browser`: **SUCCESS**. 로그 `APPROVED55_FINAL_CONTRACT_PASS 55 slides; 120 minutes`, `FINAL_55_STATIC_QA_PASSED`, H 6 screens / 0 layout issues / 0 JS errors / minimum_fit 0.943, `TWO_HOUR_NAV_QA_PASSED`를 확인함.
- 자동 수행: `python automation/verify_approved_contract.py --final`, `python scripts/verify_two_hour_course.py`, `python automation/check_group_browser.py --group H ...`, `python scripts/verify_learning_routes.py`. 별도 Reviewer 로컬 체크아웃을 통한 재실행은 **NOT VERIFIED**로 구분하며, 위 실 실행 근거는 Builder가 정의한 GitHub CI임.
- 고정 SHA의 Manifest에는 **Intro 13 + Course 42 = 55**, 버전 `approved55-20261019-1`, 계획 총 120분; Outline 전역 번호 1–55. H는 Course 40–42 = P53–P55, 시간 **2+1.5+1.5=5분**. 최종 계약 및 경로/상호작용 CI 성공. 실제 120분 수업 리허설은 수행하지 않음.
- 선행 G 독립 보고서 [`G-4b79d63-final.md`](https://github.com/sh0427-han/vision_ai_lecture/blob/review/g-final-4b79d63-20261019/reviews/automation/G-4b79d63-final.md): **PASS**, G-01/G-02 CLOSED. `4b79d63..c35f1f7` 파일 diff는 H HTML/CSS, H QA 스크립트/워크플로, Progress뿐. G `docs/project_course.js`, G CSS, G 검사 원본은 변화 없음. **동일 SHA** 추가 G CI Run [39246424868](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424868): **SUCCESS**, `APPROVED_G_BROWSER_QA_PASSED {screens:10,interactive_checks:14}`로 G의 실화면·Threshold 회귀가 유지됨.
- CI 결과는 지정 SHA의 브라우저 테스트임. 공개 GitHub Pages의 실제 배포, A–F 전체 110화면 육안 전수, 실제 수업 120분 리허설, 브라우저별 호환성은 이 H 최종 검수에서 **NOT VERIFIED**. A–F 전체에 대한 PASS로 확대 해석하지 않음.

## 5. 새로 발견한 H-04 · Minor · Builder · OPEN — 배경 합성 Figure 메타데이터 불일치

- **근거 1:** `assets/SOURCES.md`, `Approved group H P53–P55` 절에는 P54 배경이 과거의 **`colored outer border`** 비교이고 '실제 배경 교체가 아니다'라는 옛 기록이 남음. 현재는 그 방식이 아니라 피사체 마스킹 후 외부 픽셀을 회색/격자 SVG로 재합성하는 방식임. 이 설명을 그대로 읽으면 Figure 제작 이력을 잘못 이해함.
- **근거 2:** `docs/vision_ai_course.html` P54의 `합성 A · 단색 배경`은 사진 바깥 배경에 실제로 얇은 가로/세로 선 4개가 그려져 있어 **완전 단색은 아님**. 1366/1920 PNG에서 이 선이 보임. '무늬 적은 배경' 등 정확한 명칭이 적절함.
- **영향:** Caption/자산 출처 문서의 세부 정합성이 저하됨. 다만 동일 피사체·ROI 및 배경 변화라는 핵심 교육적 메시지는 정확하며 실화면·컨트롤 테스트에 영향 없음. **Major 아님 / H PASS 차단하지 않음**.
- **수정 제안:** Builder가 `assets/SOURCES.md` P54 문단에 '동일 교육용 생성 사과의 SVG clipPath 마스킹, 회색선/격자 작업면의 배경 픽셀만 합성, ROI·조명·Crop 동일, 실제 재촬영 및 모델 예측 아님'으로 기술 업데이트. P54 합성 A figcaption을 '무늬 적은 배경' 등으로 변경하거나 실제 선을 제거해 단색과 일치시킬 것. 기존 H-01 처럼 테두리만 바꾸는 방식으로 회귀하지 말 것.
- **재검증:** SOURCES 문구와 현재 SVG 내용·Caption이 일치하는지 정적 재비교. Caption CSS 변경 시 1366 화면 1장 확인. Pixel mask/ROI·Canvas 불변 검증은 유지.

## 6. 완료 조건 및 권한

- **Reviewer 최종 결론:** H-01/02/03 모두 CLOSED, H구간 3/3, 두 해상도 6/6, 신규 미해결 Major/Critical 0. **PASS**. H-04는 향후 Builder 문서/라벨 정정 대상인 비차단 Minor.
- **독립성 수준:** GitHub Actions 실행/캡처는 고정 SHA의 Builder 스크립트가 수행. Reviewer는 그 artifact의 **원본 10 PNG와 JSON을 직접 확인**하고, 마스킹 기반 픽셀 검산을 **별도로 계산**함. 로컬 독립 Chromium 세션은 수행하지 않았다고 명시함.
- **변경 권한 준수:** 별도 Reviewer 브랜치에서 **이 보고서만 추가**. `docs/`, `assets/`, Planner 기획, 통합 Builder 브랜치, `main`, Pages 배포는 변경하지 않음. **main merge·배포 금지 및 미수행**.

## 증거 링크

- 고정 [Builder Commit c35f1f7](https://github.com/sh0427-han/vision_ai_lecture/commit/c35f1f7175788921f2a924f3ef1f4e0e552bb5e2)
- [H CI #39246424771 및 원본 PNG/JSON artifact](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424771/artifacts/12183008736)
- [G 회귀 CI #39246424868 및 artifact](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424868/artifacts/12182733802)
- [H 원본 독립 Reviewer 보고서](https://github.com/sh0427-han/vision_ai_lecture/blob/review/h-4469656-20261019/reviews/automation/H-4469656.md)
- [G 최종 PASS Reviewer 보고서](https://github.com/sh0427-han/vision_ai_lecture/blob/review/g-final-4b79d63-20261019/reviews/automation/G-4b79d63-final.md)
