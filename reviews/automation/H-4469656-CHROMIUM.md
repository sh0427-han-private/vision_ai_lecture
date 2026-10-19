# H구간(P53–P55) 독립 Chromium 실화면 추가 검수 — 고정 SHA 4469656

- 검수 대상 원본: `4469656244e55476b2c0e8ca2a1344a9710a29db` (**Builder HEAD를 따라가지 않음**)
- 기록 브랜치: `review/h-4469656-20261019`
- 최종 성공 GitHub Actions: [Pinned H Reviewer Chromium QA / 39242523440](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39242523440)
- 기존 정적 독립 검수 보고서: [H-4469656.md](H-4469656.md). 본 문서는 그 후속 **실제 브라우저 검수 증거**이며 H-01/H-02를 자동 종결하지 않음.
- 결론: **H구간 실행·화면 검수 PASS(지정한 자동 검사 및 6화면 프리뷰)**, **최종 콘텐츠 CONDITIONAL PASS** (Critical 0, Major 1, Minor 2). `main` merge·Pages 배포 승인 아님.

## 1. 실제 수행한 검증

GitHub Actions가 고정 SHA를 전체 fetch하여 `docs`, `planning`, `automation`에 Builder 기준 대비 변경이 **없음**을 확인했다. Reviewer 파일 및 CI만 추가했다. 실제 `docs/vision_ai_course.html`을 로컬 HTTP로 제공하고 Playwright/Chromium으로 캡처했으며 1920×1080, 1366×768에서 각각 P53/P54/P55 3장씩 **원본 PNG 6장**을 생성했다. 작은 JPEG preview로 변환해 6장 **독립 육안 검토**를 수행했다. 원본 PNG 및 구조/Canvas 측정 JSON은 Actions artifact `pinned-h-4469656-chromium`에 보존되며 현재 retention 14일이다.

| 검사 | 실측 결과 |
|---|---|
| `automation/verify_approved_contract.py --final` | **PASS**: Intro13 + Course42 = 55, 승인 순서, 120분, 기초 숫자/Asset |
| `scripts/verify_two_hour_course.py` | **PASS**: 모든 final 소스 연동 수치/모델/라벨·평가 지표 |
| `scripts/verify_learning_routes.py` | **PASS**: 목차·전역 경로·legacy URL·실습 경로·사용자 입력(전체 경로 회귀) |
| P53~P55 × 두 해상도 | **6/6 browser geometry PASS** |
| 최소 실제 auto-fit 비율 | **0.968** (검수 하한 0.90보다 큼) |
| Content right/bottom overflow 및 수평 스크롤 | 검수 설정 허용치 이내 **6/6 PASS** |
| JavaScript page errors | **0건** |
| P53 workflow node / question path | **5 / 4**, 2개 viewport 확인 |
| P54 Canvas 생성 | **두 viewport 모두 240² = 57,600픽셀, 24² = 576픽셀** 불투명 픽셀 채워짐; `data.ready=true` |
| P55 4답 카드 / `details` 토글 | **PASS**, Pixel→Feature→Learning→Evaluation, 열기·닫기 |
| P54↔P55 키보드 | **PASS**, ArrowLeft 후 ArrowRight 동작 |

## 2. 프리뷰 독립 시각 검토

| 슬라이드 | 1920×1080 | 1366×768 | 결과 |
|---|---|---|---|
| P53 | 원본 사과·5단계 흐름·연결 4개 한 화면 배치 | 다섯 노드와 하단 질문의 선/Label 판독 가능; 잘림·충돌 없음 | **시각 PASS**, 단 모델 비실측 사진·녹색 ROI Annotation Caption 부재 **H-02 Minor OPEN** |
| P54 | 조명·배경·해상도 3열 사진의 크기와 설명 구분 | 240↔24의 실제 저해상도 대비 선명, 텍스트·가설·검증안 모두 화면 안 | **시각 전달력 H-01 Major OPEN**: 배경은 사진 변경이 아니라 테두리 6px 표시뿐; 자동 화면 PASS로 콘텐츠 결함이 해소되는 것은 아님 |
| P55 | 사과 중앙 2×2 복습 카드·수치 분리 주석 보임 | Pixel·Feature·Learning·Evaluation 네 카드, Folded `details`, 하단 출처 성격 주석 가독 | **시각 PASS**, 클릭·키보드 테스트도 PASS |

**검수 방법 한계:** UI/레이아웃·글자 잘림은 실제 Chromium PNG와 그 **최대 너비 1280px JPEG 미리보기**를 통해 확인했다. 대형 화면의 모든 Pixel을 1:1 확대하여 검증했다거나 실제 청중의 원거리 판독을 실측했다고 주장하지 않는다. 브라우저 테스트는 실제 화면을 확인한 것이나 120분 수업 리허설/학생 이해도/배포 사이트의 동작과는 다르다.

## 3. 독립 Issue 처리

- **H-01 · Major · OPEN:** P54 배경 Figure는 윤곽선만 바뀌며 실제 배경 변화 비교가 아님. 같은 결함 사과 전경을 고정하고 배경만 다르게 합성한 교육용 Figure로 교체 필요. 실제 사진·모델 오분류라 주장 금지. 두 해상도에서 사진·캡션 다시 검증.
- **H-02 · Minor · OPEN:** P53 초록 ROI 원과 생성 사과 사진을 모델 출력 또는 실측 원본으로 오인하지 않도록 근접 Caption 추가. 두 해상도 가독성 재검증.
- **H-03 · Minor · Reviewer 증거에서는 회피/검증 완료, Builder 일반 캡처 스크립트는 OPEN:** 별도 `reviews/automation/h_chromium_qa.py`가 P54에서 두 Canvas가 `data.ready=true`로 바뀌기를 명시적으로 기다린 후 크기/픽셀을 확인하고 Screenshot을 찍음. 그러나 원래 `automation/check_group_browser.py`의 160ms 단순 지연은 수정하지 않았으므로 Builder 후속 조치 필요.

G구간의 G-01/G-02는 **별도 G 고정-SHA 검수**로 유지. 자동 검사 6장 PASS와 콘텐츠 Major 이슈는 서로 독립이며, **H 최종 합격·전55장 Verified·main 병합·공개 배포를 선언하지 않는다.**

## 4. 추적성

- 최종 성공 브라우저/정적 CI: https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39242523440
- 원본 H Builder SHA: https://github.com/sh0427-han/vision_ai_lecture/commit/4469656244e55476b2c0e8ca2a1344a9710a29db
- 브라우저 검수 소스: `reviews/automation/h_chromium_qa.py`
- 전용 CI: `.github/workflows/reviewer-h-qa.yml`
- 기존 검수 이슈: `reviews/automation/H-4469656.md`

**Reviewer 브랜치 외 강의자료, Planner 스토리보드 및 Builder 브랜치는 수정하지 않았다.**
