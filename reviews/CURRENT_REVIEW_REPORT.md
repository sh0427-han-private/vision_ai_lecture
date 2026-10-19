# CURRENT REVIEW REPORT — Rule-based vs Machine Learning (P15–P16)

- 검수일: 2026-10-19 (KST)
- 검수자: 독립 Reviewer
- 최종 판정: **CONDITIONAL PASS**
- 대상: 통합 강의 Course 2 / Course 3, 전역 15 / 16, Concept ID **rules / rules-image**
- 기준: Builder PR #113의 HEAD **b44de7bc897a275b098623a7c52529bff02d314a**
- 비교 기준 main: **d52f42c0dcfdc60daf51ff69927e2345802fa2da**
- 승인 기획: planning/vision-ai-120min-storyboard-draft-20261019의 planning/SLIDE_STORYBOARD.md, **Approved P15–P16**
- 검수 상태: 코드·콘텐츠 정적 분석 및 CI가 촬영한 실제 Chromium 스크린샷의 **독립 육안 검토 완료**. Reviewer가 Builder HEAD에서 별도로 Chromium 실행하거나 배포 Pages를 직접 검증한 것은 아님.

## 1. 종합 평가

C02의 1+1, 2+1 → 공통 f(a,b)=a+b → 2, 3 Figure는 기술적으로 정확하며 입문자에게 핵심 개념을 직관적으로 전달한다. C03도 Rule-based를 불가능한 기술로 단정하지 않고, 단순 색 조건의 예외와 지도학습의 Label·Weight 학습, 새 조건에 대한 독립 검증 필요성을 조건부로 제시한다. **Critical 기술 오류는 확인되지 않았다.**

그러나 C03 핵심 비교 사진의 **서로 다른 대상 크기와 구도**, **학습한 모델에서 새 사진의 예측으로 이어지는 연결 관계 누락**, **처음 등장하는 학습 용어·작은 Figure 설명 글씨**는 교육 목표에 실제로 영향을 준다. 수정 전에는 완전 PASS로 판정하지 않는다. 별도로 C04/C05 중복은 이미 승인된 전체 개편의 Planner 작업이며 이번 Builder PR에서 발생한 문제로 간주하지 않는다.

| 구분 | 판정 | 근거 |
|---|---|---|
| 수식·결과 | PASS | f(1,1)=2; f(2,1)=3; 한 규칙에 두 입력·두 출력의 연결 일치 |
| Rule-based/ML 개념 | PASS | Rule 설계 주체와 지도학습 Label·Weight 업데이트 구분, 단정·허위 실측 결과 없음 |
| P15 기초 교육 전달 | PASS | 입력 → 사람 정의 규칙 → 출력이 시각적으로 연결됨 |
| P16 핵심 Figure·초보자 이해 | CONDITIONAL | 정상 사진 구도 불일치, 새 사진→기존 Model→Prediction 연결 누락, 선행 용어 부담 |
| 화면 잘림/자산 | PASS (제공된 CI 결과와 스크린샷 범위) | 대상 4개 해상도별 스크린샷에서 주요 영역 잘림/겹침 발견 안 됨; CI 이미지 수 6개 |
| 최신 Builder HEAD 독립 실렌더 / Pages 배포 / 현장 리허설 | NOT VERIFIED | 직접 실행·최신 배포·4.5분 리허설 증거 없음 |

## 2. 범위·브랜치·변경 비교

- PR: https://github.com/sh0427-han/vision_ai_lecture/pull/113 (open/draft, 미병합).
- Builder HEAD: https://github.com/sh0427-han/vision_ai_lecture/commit/b44de7bc897a275b098623a7c52529bff02d314a
- main 기준: https://github.com/sh0427-han/vision_ai_lecture/commit/d52f42c0dcfdc60daf51ff69927e2345802fa2da
- 비교: Builder가 main보다 **8 commits ahead / 0 behind**.
- 실제 변경 **3개 파일**: docs/rules_vs_learning.css (+172/-37), docs/vision_ai_course.html (+30/-22), scripts/verify_learning_routes.py (+15/-5). Manifest, Outline, 공통 CSS/JS, 이미지, Intro 및 다른 슬라이드의 실제 내용 변경 없음.
- 검토 문서: 승인 Storyboard P14~P18, TWO_HOUR_LECTURE_PLAN.md, PROJECT_GUIDE.md, HTML_DESIGN_RULES.md, AGENTS.md, assets/SOURCES.md, docs/two_hour_manifest.json, docs/lecture_outline.js, docs/vision_ai_course.html, docs/rules_vs_learning.css, docs/slide.css, docs/lesson.css, 기존 검수 2026-10-18의 3개 보고서, 2026-10-19 CNN 검수 기록, TODO_VISION_AI_LECTURE.md.
- 스토리보드는 위 **기획 브랜치**에서 확인하였다. 현재 main 59장과 승인된 미래 목표 55장(통합·삭제·신규 포함)을 동일 상태로 혼동하지 않는다.
- 현행 Manifest/Outline: Intro 13 + Course 46 = **59장**, Course 1=task, Course 2=rules, Course 3=rules-image, Course 4=vision-evolution, Course 5=model-choice. 대상 Concept ID·순서·제목이 실제 HTML과 일치한다.
- 기획상 전역 P15/P16은 현재 강의에서 각각 Course 2/3 = **전체 15/16**이다.

## 3. 기술적 정확성

### C02 / P15 — PASS

두 입력 1+1, 2+1은 하나의 사람이 명시한 결정적 함수 f(a,b)=a+b로 계산되고 출력이 각각 2, 3으로 연결된다. SVG의 두 합류선과 두 분기선도 해당 행에 연결된다. 인간이 정한 명시 규칙을 알고리즘으로 구현하는 접근을 올바르게 보여준다. **Rule-based는 오직 덧셈만 한다는 주장도, AI가 모든 문제에 필수라는 주장도 없다.** 승인 스토리보드의 우측 ✓ 표시는 별도로 없지만 각 출력의 입력 대응 라벨과 수치가 분명하므로 수정 필수사항으로 분류하지 않는다.

### C03 / P16 — 개념 PASS, 설명 Figure CONDITIONAL

좌측의 '갈색 Pixel 수 ≥ k → 불량?'은 **가능한 수동 규칙의 예시 질문**이지 실제 검증된 분류기나 측정 결과가 아니다. k와 갈색 범위/ROI가 정의되지 않아 참·거짓 예측을 수치 재현할 수 없지만, 실제 모델의 예측값을 주장하지 않기 때문에 **수치 오류로 간주하지 않는다.** 단순 전역 색 조건이 조명에 취약할 수 있다는 설명은 타당하며, 그렇다고 Rule-based 영상처리가 원천적으로 불가능한 것도 아니다. OpenCV의 전역/적응형 thresholding 사례도 이러한 조건부 설명과 부합한다.

우측은 명시적으로 **지도학습(Supervised Learning)**을 표기하고 같은 3개 입력의 정상/불량 Label을 제시한다. 목표·Label·모델 구조는 사람이 지정하고 데이터에서 Weight를 조정한다는 원리는 맞다. 'Prediction?'과 '결과는 미측정', 교육용 생성 사진/화면 밝기 변환 고지는 실측 성능 오인의 위험을 줄인다. 다만 우측에 나타낸 **지도학습은 Machine Learning 전체가 아니라 그 안의 한 방식**이다. 현재 명시 제목만으로 직접적인 오진술은 없으므로 별도 기술 오류는 기록하지 않는다.

독립 Validation/Test가 필요하다는 방향은 타당하다. 특히 Training에 쓴 사진의 라벨을 다시 맞히는 것으로 실제 일반화 성능을 판단해서는 안 된다. Validation은 보통 모델 선택/튜닝에, 최종 Test는 별도 최종 평가에 활용되며 같은 단계라는 뜻은 아니다. 자세한 역할은 현행 Course 26에서 설명한다.

참고: https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html 및 https://scikit-learn.org/stable/modules/cross_validation.html

## 4. 학습 흐름·난이도

- **Intro 13 → C01:** 조명·회전·가림으로 픽셀이 변한다 → 사과의 결함 유무/위치/영역 중 무엇을 답할지 고른다는 전환은 자연스럽다.
- **C01 → C02:** '무엇을 예측할까(Task/Label)?'에서 '판단 방법을 누가 정할까?'로 질문을 전환한다. C01은 Label과 Prediction의 차이도 먼저 설명하므로 C03의 사용은 선행된다.
- **C02 → C03:** 명시된 덧셈 규칙에서 조건과 예외가 많은 이미지로 전환하여 왜 데이터로 판단 기준을 만들 수 있는지 도입한다. 목표에 적절하다.
- **C03 → C04 → C05:** C04가 규칙/Task별 학습/사전학습을 다시 나열하고 C05가 실제 선택을 반복한다. Approved 55장 기획은 C04 내용을 C05로 통합할 계획이므로, 현재 구현에서 남은 중복을 **별도 Planner 범위**로 기록한다.
- **선행 용어:** C03에는 Weight, Training, Inference, Validation/Test가 이미 표시되지만, Weight는 C07, 데이터 분할은 C26, 상세 Training/Inference는 C32에서 설명한다. C03 단독으로 두 경로의 핵심 구별은 가능하나 이 용어의 의미까지 습득했다고 평가하기는 어렵다. 초보자 Figure의 한글 중심 설명 보완 필요(ISSUE-RML-03).

## 5. 실제 Figure·디자인·기능 증거

### 실제 확인한 자료

- 범위 전용 Chromium 성공: https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39206617799 ; 4개 PNG와 checks.json: https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39206617799/artifacts/12165594181
- 기존 탐색/인터랙션/118뷰 전수 QA 성공: https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39207002383 ; 전체 스크린샷과 issues.json: https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39207002383/artifacts/12165637912
- 제공된 캡처를 Reviewer가 독립적으로 열어 **C02/C03 각각 1920×1080, 1366×768**, Intro 13 및 C01/C04/C05의 1366×768 인접 화면을 육안 대조했다.
- 대상 4뷰는 checks.json에서 fit=1, C03의 각 뷰에서 이미지 로드 6개. 시각적으로 대상 슬라이드에 텍스트 잘림·중요 요소 겹침 발견 안 됨. C02의 계층·색·연결선은 양호.
- 전수 issues.json에는 대상 C02/C03 이슈가 없으나, **다른 슬라이드 C11 0.871, C34 0.848의 shrink**가 1366×768에서 기록되어 있다. 이들은 이번 두 장의 신규 문제에 포함하지 않는다.
- 캡처 시점은 범위 QA 8709848727d71684a47a396650da6bfc9438b842, 전수 QA 5feae4f6b61086b4c74e51c18eb17798b086d83c. 이후 최종 b44de7b까지 변경된 파일은 회귀 테스트 및 임시 workflow 정리이며 대상 HTML/CSS의 추가 변경은 확인되지 않는다.
- **주의:** 위의 화면은 Builder CI에서 렌더링한 결과를 독립적으로 해석한 것이다. Reviewer 자신이 현재 HEAD의 Chromium을 별도 실행한 독립 렌더 테스트나 GitHub Pages 최신 배포 테스트와 동일시하지 않는다. Pages의 main은 아직 이 미병합 PR을 반영하지 않는다.

### 시각 평가

C02는 입력 두 줄·공유 규칙 한 개·결과 두 줄의 방향성과 수치가 명확하고 스타일도 기본 청회색/녹색과 일치한다. C03은 양쪽 동일한 3개 경로 비교와 실험 아님 고지를 갖추었고 화면 밖으로 넘치지 않는다. 하지만 3번째 '어두운 정상' 사과는 다른 이미지 구도/크롭으로 **화면을 거의 채우는 큰 과실**이며 앞의 두 결함 사과와 크기가 현저히 달라 객관적인 밝기/결함 비교를 방해한다. 또한 1920 캡처에서 우측 긴 h3가 두 줄로 줄바꿈되어 두 패널 사진의 가로 대응선이 어긋난다(ISSUE-RML-01). 1366 화면 일부 설명 텍스트는 12–14px 수준으로 발표실 원거리 가독성을 장담하기 어렵다(ISSUE-RML-03).

## 6. 문제별 우선순위 및 수정 지침

### ISSUE-RML-01 · Major · C03 / 전역16 / rules-image · Builder · Open

- **파일/위치:** docs/vision_ai_course.html의 C03 좌우 .rl-photos 세 번째 .rl-photo-card--dark; docs/rules_vs_learning.css의 .rl-photo-card img (object-fit: cover) 및 .rl-photo-card--dark img; 자산 docs/assets/generated/apple_studio_preview.png.
- **실제 문제:** '어두운 정상'은 양쪽 모두 별도 생성 사과 사진을 크게 잘라 과실이 프레임 대부분을 차지한다. '밝은 불량'과 '어두운 불량'은 상대적으로 작은 전신 사과와 주변 배경이 보인다. 캡처에서도 정상 사과는 밝기·촬영 구도·과실 비율이 동시에 달라 보인다. P16의 '촬영 조건 변화 vs 결함 정답 유지' 메시지를 시각적으로 분리하기 어렵다.
- **근거/이유:** 같은 이미지 밝기 비교는 통제된 동일 ROI가 적합하며 정상 이미지와 불량 이미지를 동시에 비교할 때도 **대상 크기·중심 위치·배경 노출을 최대한 일치**시키는 편이 학습 혼동을 줄인다. assets/SOURCES.md의 두 원본을 유사 크기로 보여준다는 기존 설명 및 HTML_DESIGN_RULES.md의 정확한 Figure 관계 요구와도 어긋난다. 이것은 'ML 성능이 잘못되었다'는 문제가 아니라 **학습용 비교 이미지의 통제 부족**이다.
- **수정 권고:** 기존 로컬 자산을 유지하되 정상 이미지에 동일 대상 크기가 확보되도록 object-position/size 또는 명시적 Crop/이미지 컨테이너를 조정한다. 두 클래스의 결함 유무 외 구도 차이는 최소화하고, 어두움은 각 원본의 화면 밝기를 일관된 원칙으로 조절한다. 두 패널의 1~3번 사진은 서로 같은 처리 결과로 유지. 1920에서 우측 h3를 짧게 하거나 제목 행 높이를 일치시켜 대응 사진 3열의 y좌표도 맞춘다. 새로운 실사·측정 이미지를 생성했다고 주장하지 않는다.
- **영향:** C03 양쪽 사진 6개 및 전용 CSS 일부. 다른 슬라이드·공통 CSS/JS 변경 불필요.
- **재검증:** 각 해상도에서 3종 사진이 동일 순서·대응 좌표이며 과실 폭/높이/중심이 유사한지 2×3 비교 캡처를 육안 확인. 밝음·어두움 두 결함 사례의 반점 ROI가 가시적인지, 정상은 결함이라고 오해할 시각적 아티팩트가 없는지 확인.

### ISSUE-RML-02 · Major · C03 / 전역16 / rules-image · Builder · Open

- **파일/위치:** docs/vision_ai_course.html의 .rl-learning-path, 두 .rl-learning-line.
- **실제 문제:** 첫 줄은 '사진+정답 Label → Training → 학습된 Model', 둘째 줄은 별도의 'Inference → Prediction?'으로 표현된다. 그러나 첫 줄의 **학습된 Model에서 둘째 줄로 연결선이 없고**, Inference의 새 입력 사진도 별도의 Figure Node로 나타나지 않는다. 새 사진이 학습된 모델에 실제로 입력된다는 관계는 작은 문장에만 있다.
- **이유:** 입문자가 'Training은 Model 생성/파라미터 갱신, Inference는 **같은 Model**을 새 입력에 적용'한다는 핵심을 그림만으로 재구성하기 어렵다. 분리된 두 줄을 서로 다른 처리기로 오해할 수 있다.
- **수정 권고:** **정답 사진들 + Label → 학습(Training) → 학습된 Model**, 그리고 **새 사진 + 동일 Model → 적용(Inference) → 예측(Prediction, 미측정)**의 두 흐름을 시각적으로 연결한다. 학습된 Model을 두 단계가 공유하거나, 명확한 하향/분기 연결선을 만든다. 새 사진은 학습 샘플과 구별되는 교육용 입력이라는 표기를 추가하되 실제 훈련·예측 결과나 점수를 발명하지 않는다. Validation/Test는 별도 새 촬영 조건 데이터 평가로 두고 '추론 그림'과 '평가 확인'의 역할도 구분한다.
- **영향:** C03 우측 Figure DOM 및 스코프 CSS.
- **재검증:** 이미지와 화살표·노드의 관계만 읽고 수강생이 '학습에 쓴 정답 사진', '학습한 모델', '처음 보는 사진', '예측', '별도 평가'를 구분할 수 있는지 2명 이상에게 블라인드 질문. 두 해상도 캡처에서 연결선·라벨 겹침 없음 확인.

### ISSUE-RML-03 · Major · C03 / 전역16 / rules-image · Builder · Open

- **파일/위치:** docs/vision_ai_course.html의 .rl-learning-step small/.rl-learning-check/.rl-pane-note; docs/rules_vs_learning.css의 해당 font-size 선언.
- **실제 문제:** 본 단원의 첫 머신러닝 도입 화면에 Weight, Training, Model, Inference, Prediction, Validation/Test가 밀집하고, 중요 단계 설명 일부는 1366×768에서 CSS 최소 **12px**(.rl-method-step small, .rl-learning-step small) 및 **13px**(.rl-learning-check)까지 낮아진다. Weight의 역할은 현행 C07, Train/Validation/Test는 C26, Training/Inference는 C32에서 자세히 배운다.
- **이유:** 수강생은 '규칙을 사람이 만드는가, 데이터로 조정하는가?'가 우선인데 상세 학습 사이클 용어가 새로 많이 들어와 주 메시지와 경쟁한다. 12–14px 보조 글자가 연결 관계를 설명하는 용도로 필수라면 1366 프로젝터에서 읽기 어렵다. HTML_DESIGN_RULES.md의 '직관→용어'·Figure annotation 약 18–22px/1920 참조 기준 및 한 장 한 메시지 원칙과 긴장이 있다.
- **수정 권고:** 기획에 포함된 Training·Weight·Validation/Test 개념을 삭제하는 대신 **한국어 설명을 앞세우고 용어는 괄호의 작은 두 번째 라벨**로 사용한다. 예: '정답 사진으로 기준 학습(Training)', '학습한 판단 모델', '새 사진으로 판정(Inference)', '처음 보는 사진으로 성능 확인(Validation/Test, 자세한 역할은 뒤에서)'. Weight는 '모델 내부 가중치(Weight)' 한 번만 간단히 연결한다. 영역별 글자 수/줄 수를 줄인 다음 Figure의 단계 키워드·주석 가독성을 높여 1366 화면에서 최소한 핵심 설명은 약 16px 이상 확보하도록 우선 조절하며, 화면 전체의 과도한 shrink 또는 영역 밀집을 초래하지 않는다.
- **영향:** C03 문구와 전용 CSS에 국한. 승인 스토리보드의 개념 범위와 2.5분 목표 유지.
- **재검증:** 본문만으로 Rule/ML 차이를 20초 이내에 말할 수 있는지 초보자 관점 확인. 1366×768 및 1920×1080에서 핵심 Figure 라벨의 computed font-size와 실제 캡처의 시인성, 영역 간 간섭 재확인.

### ISSUE-FLOW-01 · Major (기존 흐름 / 이번 PR 외) · C04–C05 / 전역17–18 / vision-evolution·model-choice · Planner · Open (승인 계획에 조치 예정)

- **파일/위치:** 현행 docs/vision_ai_course.html의 C04, C05; 승인 planning/SLIDE_STORYBOARD.md의 P17.
- **실제 문제:** C03이 이미 규칙과 지도학습 선택의 근거를 다룬 직후, C04에서 규칙·Task별 모델·사전학습 모델을 다시 소개하고 C05에서 같은 선택지를 다시 분류한다. 새로운 학습 성과가 줄어들어 10분 구간의 설명 밀도가 높아진다.
- **근거/이유:** 반복은 **현행 main에서도 존재하며 PR #113의 변경 범위가 아니다.** 승인된 55장 기획이 이미 'C04를 C05에 통합'한다고 명시했다. Builder에게 이번 P15/P16 작업에서 C04/C05를 임의로 삭제하도록 지시하면 범위 초과다.
- **수정 권고:** Planner의 55장 개편 시 P17 한 장으로 '규칙 가능? → 기존 결함 모델 적합? → 부족할 때 Label 수집·추가 학습? → 독립 검증'을 통합하고 중복 발전사/종류 나열을 정리한다. C03 수정과는 별도 작업으로 추적한다.
- **영향:** C04/C05 통합, 차후 Manifest/Outline·발표 시간·딥링크 조정. **이번 PR은 변경하지 않음.**
- **재검증:** 개편 Manifest의 P16→P17→P18이 개념 중복 없이 연결되고 총 55장/120분에 맞는지 별도 검수.

## 7. Planner / Builder 후속 작업

**Builder / 이번 PR의 필수 권고:** ISSUE-RML-01 → ISSUE-RML-02 → ISSUE-RML-03 순서로 국소 수정. 공통 CSS·JS, Manifest, 다른 슬라이드와 기획안은 변경하지 않는다. 수정 후 C02는 회귀가 없는지 확인하고 C03 두 viewport 재촬영, 6개 이미지 로딩·화살표·글자 영역 확인, 탐색/상호작용 QA를 수행한다.

**Planner / 별도 승인 작업:** ISSUE-FLOW-01은 이미 Approved 55장 개편의 P17에서 다룬다. 이번 Builder 두 장 PR의 범위를 넓혀 처리하지 않는다. 별도 55장 개편 작업과 그 검수에서 확인한다.

**자료 출처:** docs/assets/vision_task_apple_reference.jpg, docs/assets/generated/apple_studio_preview.png는 프로젝트의 교육용 생성 이미지. 새 외부 사진을 추가하지 않았고 화면상 밝기 변환을 사용한다. 해당 자산과 실측 데이터 구분은 assets/SOURCES.md에 기록되어 있다. 출처나 모델 성능 숫자를 새로 만들어내지 않는다.

## 8. 최종 판정 및 승인 조건

- **범위 내 판정: CONDITIONAL PASS** — Critical 0, **Major 3개 Open**(ISSUE-RML-01/02/03). 규칙·산술의 기술 내용 자체는 PASS이나 핵심 이미지 비교 및 모델 연결 관계와 선행 설명을 보완해야 한다.
- **범위 밖의 별도 Planner Major:** 1개 Open(ISSUE-FLOW-01), 기존 59장 구조 문제이며 이번 Builder 변경에서 발생하지 않음.
- **정적·스크린샷 기반 판단:** 대상 4뷰 실제 CI 캡처 육안 검토 완료, fit=1, 누락 이미지 및 잘림/겹침 미발견. 하지만 **최종 HEAD 직접 Chromium 실행, 공개 Pages 해당 PR 배포, 현장 4.5분 발표**는 NOT VERIFIED.
- **PASS 전환 조건:** 세 Builder Major 항목 수정; 새로운 변경 HEAD의 1920×1080/1366×768 두 장 브라우저 렌더에서 이미지/텍스트/흐름/Console/asset 재확인; 새 사진/정답/모델/평가 설명에 오해가 없는지 초보자 관점 재검토. 별도 전체 55장 Planner 개편 완료를 이 두 장의 코드 수정 조건으로 요구하지는 않는다.
- **이번 검수에서 수행하지 않은 것:** PR 승인/merge, Docs/HTML/CSS/JS/이미지 직접 수정, Pages 배포, 120분 리허설.

이 보고서는 제작자의 주장이나 CI 성공 여부만으로 교육 품질을 PASS 처리하지 않고, 실제 캡처를 독립 검토해 문제와 미검증 항목을 분리한다.
