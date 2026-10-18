# 원리 중심 강의 TODO 후속 구현 · 2026-10-18

기준 main `1264f23`에서 `improve/principles-todo` 브랜치로 작업했다. 공개 구성은 Intro 11장 + Course 39장, 110분 + 질의 10분을 유지한다. 제목·번호·manifest·목차는 변경하지 않았다. **아래 검증은 작업 브랜치의 로컬 결과이며, main 병합·공개 배포·현장 리허설 완료를 의미하지 않는다.**

## 반영

- P0-01/02: 실제 사과 ROI `(550,185,85,85)` 확대와 별도의 교육용 5×5 배열, 3×3 Kernel, −6 계산을 연결. 두 인접 입력 창과 −6/12 출력 위치를 표시하고 RGB 축소판/Mask와 구별한다.
- P0-03/04: 의자·균열 대신 기존 생성 사과 두 장을 재사용. 갈색 반점 기준을 Intro→Task→Dataset에 유지하고 정상/불량 × 밝음/어두움의 2×2를 표시한다. 독립 원본과 화면 밝기 변환을 명시한다.
- P1-01~04: 모델 선택은 규칙/사전학습/Label+학습의 출력 비교로 변경. CNN 구조의 공간 H/W·채널 C와 선택적 축소를 명시. RGB에서 두 3×3×3 필터로 직접 분기하는 SVG를 작성했다. Stride 시작 위치 9/4곳, Pooling 네 영역의 색상 대응을 추가했다. Padding의 별도 입력·가중치·0 경계는 확인 후 유지했다.
- P1-05/06: Pixel·RGB·해상도 실제 브라우저 검증. 강아지 실측 CNN 자료를 쓰는 이유와 일부 채널/전체 Tensor의 차이를 명시. Backbone은 같은 갈색 반점의 Class/Box/Mask로 연결한다. 전처리·증강의 실제 사진 출처와 Label 보존 설명을 유지한다.
- P1-07/08: Threshold부터 같은 교육용 100건을 사용. TP/FN/FP/TN의 색과 용어를 일치시킨 표, Precision/Recall 분모를 보여주는 점 배열, 동적 2×2 혼동행렬과 FN/FP 막대에 동일 계산을 연결한다. IoU는 다른 Task의 영역 지표로 유지한다.
- P1-09: 마지막 복습은 입력·특징·학습·평가 4질문으로 변경. 실패 사진은 가설임을 명시하고 배경 테두리를 실제 배경 교체로 오인하지 않게 설명했다. 작업명세는 기존 사진+4질문 도식을 유지한다.
- 출처는 외부 원본 사진에만 유지. 새 도식은 HTML/SVG이며 외부 이미지를 추가하지 않았다. 기존 CSS 중 교체로 미사용된 count/kernel-pair 규칙을 정리했다.

## 검증 근거

| 검사 | 결과 |
|---|---|
| `verify_curriculum_overhaul.py` | PASS, 기존 참고 강의 포함 구조·자산·SVG·수치·출처 검사 |
| `verify_two_hour_course.py` | PASS, 50장·110+10분·선행 개념·Kernel/Padding/Pooling 재계산 |
| `verify_intro_pixel_interactive.py` | PASS, 12×8 실제 수치·6×6 클릭/밝기/재설정·JPEG RGB 샘플링·160×90/320×180/640×360 축소 |
| `verify_learning_routes.py` | PASS, 50개 실제 목차 링크·50장 다음/이전·구버전 URL·학습 버튼·임계값·복습 펼침·390px 목차/키보드·JS 예외 0 |
| `audit_visual_slides.py` | PASS, 1920×1080 + 1366×768, 총 100화면, 문제 0, 최저 fitScale 0.93 |
| JS syntax / DOM IDs / diff whitespace | PASS |

브라우저는 시스템 Chromium(`/usr/bin/chromium`)을 사용했다. Playwright의 `executable_path`를 주입하는 환경 helper로 저장소 검사 스크립트를 실행했다. 기존 Pixel QA의 사라진 만화 아이콘/옛 문구 assertion은 현재 실제 의미 라벨에 맞췄으며, 픽셀 수치 비교는 유지했다. 탐색 QA에는 모든 목차 클릭·역방향 이동·동적 막대 값 검증을 추가했다. 키보드는 목차 버튼의 포커스를 벗어난 뒤 슬라이드에서 검사한다(버튼에 초점이 있으면 슬라이드 이동을 무시하는 기존 동작).

임계값별 실제 브라우저 결과:

| Threshold | TP | FN | FP | TN | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| 0.30 | 20 | 0 | 30 | 50 | 40.0% | 100.0% |
| 0.50 | 18 | 2 | 4 | 76 | 81.8% | 90.0% |
| 0.70 | 11 | 9 | 2 | 78 | 84.6% | 55.0% |

[렌더 조사 JSON](evidence/2026-10-18-principles-todo/report.json), [문제 목록(빈 배열)](evidence/2026-10-18-principles-todo/issues.json), 같은 폴더의 8개 contact sheet를 보존한다. 100개 개별 스크린샷은 현재 작업환경 `/workspace/.onboarding/vision-ai/principles-todo-20261018/screenshots/`에 보존했다. 핵심 변경 장 C9/10/18/37은 1366px 원본 화면도 직접 확인했다.

## 남은 외부 단계

- `gh pr list --repo sh0427-han/vision_ai_lecture --limit 1`는 `https://api.github.com/graphql: Forbidden`으로 실패했다. GitHub PR API 접근이 막혀 PR 생성/병합은 수행하지 못했다. 토큰이 없다고 단정하거나 요청하지 않았다.
- 브랜치를 게시한 뒤 PR→Merge→main 재조회→Pages 성공 및 공개 파일 검증이 필요하다. main 직행 push로 지정된 PR 절차를 대체하지 않는다.
- 120분 실제 강의와 초보 수강생의 4질문 답변 확인은 사람이 참여하는 리허설이므로 미완료다. 시간 배분의 정적 합계 검증으로 대체하지 않는다.
