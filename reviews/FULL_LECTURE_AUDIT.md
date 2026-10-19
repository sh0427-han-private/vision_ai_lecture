# Vision AI FULL LECTURE AUDIT

검수일: 2026-10-19 KST | 기준: main 실제 HTML/Manifest | 범위: Intro 13 + Course 46 = **59장**, 120분.

Manifest version: 20261019-arithmetic-rule-vision-learning. Source blob: manifest b939a7bfa7fa1d0a09c13d770300195b31df5651, intro 5bd3c23b5dca748bb54a4b0123e9ae9ca1405b0e, course c2f59fe33f23f4bf1f3997976782f67a669dba01. 승인 기획: planning/vision-ai-120min-storyboard-draft-20261019의 planning/SLIDE_STORYBOARD.md (55장 Approved, 실제 구현 전).

**판정: 정적 콘텐츠 CONDITIONAL PASS / 실제 발표 화면 NOT VERIFIED.** 기술 수치 Critical 오류는 발견하지 못했으나 59장 전체 브라우저 렌더는 시행하지 않았다. 이 보고서의 '유지'는 화면/그림의 최종 PASS가 아니다. 과거 보고서는 대조자료이지 최신 검증의 대체가 아니다.

## 1. 전체 59장 전수 검수표

각 행은 현재 전역/로컬 번호, Concept ID, 실제 제목, 교육 필요성, 기술적 정확성과 전후 연결·문제 근거, 사진/Figure 판정, 조치, 승인 55장 해결 여부, 우선순위를 명시한다. 개별 핵심 메시지는 제목과 기술 근거 열에 기술하였다. 이미지/화살표의 실제 겹침·가독성은 모두 미검증이다.

|현재 전역 / 로컬 / Concept ID|기존 제목·핵심 메시지|교육 필요성|기술·전후 연결·문제 및 추가 조치|사진/Figure 품질|권고|55장 계획|우선순위|
|---|---|---|---|---|---|---|---|
|1 / I01 / start|AI와 시각의 출발점|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|2 / I02 / scene|사람의 시각 · 장면 이해|독립 장 불필요, 정보 보존|사람 시각 사례는 I03 필요성으로 흡수|이미지/그림 DOM 확인; 육안 미검증|통합|해결|Minor|
|3 / I03 / vision-value|Vision AI가 필요한 이유|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|4 / I04 / photo-numbers|사람의 의미 인식 vs Pixel 숫자|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|5 / I05 / gray|사진에서 밝기 숫자로|학습 목표상 필요|0–255 밝기/round/clipping은 타당; 클릭 6×6 실제 값 미실행|이미지/그림 DOM 확인; 육안 미검증|유지·검증|유지|—|
|6 / I06 / rgb|RGB · Pixel당 세 숫자|학습 목표상 필요|RGB 3채널 입력은 적절; 클릭 좌표/원본 pixel 값 미실행|이미지/그림 DOM 확인; 육안 미검증|유지·검증|유지|—|
|7 / I07 / hwc|RGB 이미지와 숫자 배열|학습 목표상 필요|640×960×3=1,843,200 일치|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|8 / I08 / resolution|해상도에 따른 정보 차이|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|9 / I09 / lighting|조명·색감에 따른 Pixel 변화|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|10 / I10 / transform|회전·크기·가림·흐림에 따른 변화|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|11 / I11 / diversity|다르게 생겨도 같은 종류|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|12 / I12 / relevant-change|큰 변화보다 중요한 차이|학습 목표상 필요|지정 결함은 구별하고 촬영 변화에는 견고해야 한다는 목표 명확|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|13 / I13 / vision-challenge|Vision AI는 왜 어려울까?|독립 장 불필요, 정보 보존|I09–12의 조명·가림·변화 재설명|이미지/그림 DOM 확인; 육안 미검증|통합|해결|Minor|
|14 / C01 / task|같은 사진, 다른 질문과 정답|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|15 / C02 / rules|규칙 기반 · 답을 구하는 방법을 사람이 정한다|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|16 / C03 / rules-image|이미지 판단 · 규칙을 어디까지 만들어야 할까?|학습 목표상 필요|비교 사과의 촬영구도 통제·새 사진→동일 Model→예측 연결 불명확; 조건식 if brown_pixels = k 구문도 개선|이미지/그림 DOM 확인; 육안 미검증|수정|부분|Major|
|17 / C04 / vision-evolution|지금 Vision AI는 어디까지 왔나?|독립 장 불필요, 정보 보존|규칙/모델/사전학습 소개가 C05와 중복|이미지/그림 DOM 확인; 육안 미검증|통합|해결|Minor|
|18 / C05 / model-choice|첫 선택 · 어떤 모델을 쓸까?|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|그림 형태/육안 미검증|유지|유지|—|
|19 / C06 / task-model-data|내 과제에 맞는 모델과 Label|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|20 / C07 / perceptron|퍼셉트론 · 하나의 W와 b로 판정|학습 목표상 필요|동일 W 두 입력은 일반 뉴런이 아닌 특수 예시; 일반식과 대비|이미지/그림 DOM 확인; 육안 미검증|수정|부분|Minor|
|21 / C08 / and-rule|AND Gate · 두 입력이 모두 1일 때|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|그림 형태/육안 미검증|유지|유지|—|
|22 / C09 / and-gate|AND Gate · Weight와 Bias로 직선 이동|학습 목표상 필요|C07의 동일 Weight와 다른 w₂=1 고정 설정을 시각적으로 구분|이미지/그림 DOM 확인; 육안 미검증|수정|부분|Minor|
|23 / C10 / xor-rule|XOR Gate · 입력이 다를 때만 1|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|그림 형태/육안 미검증|유지|유지|—|
|24 / C11 / xor-gate|XOR · 선형층을 쌓아도 직선 하나|학습 목표상 필요|ReLU 전에 비선형 /t/ 사용; 직선의 위치 변경을 기울기 변경으로 축소 서술|이미지/그림 DOM 확인; 육안 미검증|이동·수정|부분|Major|
|25 / C12 / relu|ReLU · 비선형성의 시작|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|26 / C13 / nonlinear|비선형성 · 깊어져도 직선이면?|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|27 / C14 / cnn-overview|CNN Architecture · 사진에서 분류까지|개념 필요, 선행순서 조정|CNN 이유 C15보다 전체 Architecture C14가 앞섬|이미지/그림 DOM 확인; 육안 미검증|이동|해결|Major|
|28 / C15 / cnn-why|왜 CNN인가? · 특징을 모아 얼룩말을 알아보기|개념 필요, 선행순서 조정|CNN 전체 구조에 앞서 지역 특징 필요성 설명 권장|이미지/그림 DOM 확인; 육안 미검증|이동|해결|Major|
|29 / C16 / kernel|Kernel · 작은 영역의 가중합|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|30 / C17 / feature-map|Feature Map · 같은 계산을 위치마다|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|그림 형태/육안 미검증|유지|유지|—|
|31 / C18 / sharing|CNN · 지역 연결과 가중치 공유|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|32 / C19 / channels|RGB에서 Feature Channel까지|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|33 / C20 / stride|Stride · 계산 위치의 간격|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|그림 형태/육안 미검증|유지|유지|—|
|34 / C21 / padding|Padding · 같은 입력, 다른 출력 크기|학습 목표상 필요|Padding0 1×1=45; Padding1 출력 12/21/16,27/45/33,24/39/28 정확|그림 형태/육안 미검증|유지|유지|—|
|35 / C22 / pool|Max Pooling · 영역별 최댓값|학습 목표상 필요|4×4→2×2 MaxPool 결과 6,4,7,9 정확|그림 형태/육안 미검증|유지|유지|—|
|36 / C23 / actual-map|실제 Feature Map · CNN 내부 반응|학습 목표상 필요|실측 SqueezeNet feature의 stage, channel, 정규화·입력 사진 대응 실렌더 검증 필요|이미지/그림 DOM 확인; 육안 미검증|유지·검증|미확인|Minor|
|37 / C24 / backbone|Backbone과 Task Head|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|38 / C25 / dataset|데이터셋 · 어떤 사진으로 배우나|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|39 / C26 / split|Train · Validation · Test|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|40 / C27 / leakage|Video Group Split · 데이터 누출 방지|학습 목표상 필요|Video Frame의 시간축 도입 없이 Video Group Split 등장|이미지/그림 DOM 확인; 육안 미검증|수정|해결|Major|
|41 / C28 / augment|Data Augmentation · 같은 정답, 다른 조건|학습 목표상 필요|Train-only 증강과 Box/Mask 보정 원칙 명시|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|42 / C29 / learn|모델 학습 · 오차를 줄이는 반복|학습 목표상 필요|단일 x=2,y=4,w=.5; Loss9 교육용 예제, JS 단계 미실행|그림 형태/육안 미검증|유지·검증|유지|—|
|43 / C30 / loss|Loss · 틀린 정도를 줄이는 방향|학습 목표상 필요|Gradient=-12, w'=1.7, Loss'=0.36 정확|그림 형태/육안 미검증|유지|유지|—|
|44 / C31 / cnn-training|CNN 학습 · 예측에서 Weight 갱신까지|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|45 / C32 / infer|Training과 Inference의 차이|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|46 / C33 / transfer|전이학습 · 특징은 고정하고 분류기만 학습|학습 목표상 필요|외부 Figure 차단 시 fallback과 Freeze/Update 표시 브라우저 확인 필요|이미지/그림 DOM 확인; 육안 미검증|유지·검증|미확인|Minor|
|47 / C34 / cnn-learning-paths|같은 CNN 특징 · 지도와 비지도 활용|학습 목표상 필요|Freeze Backbone 공유+지도 Head 학습/비지도 군집 그림의 학습 목표를 우선 강조|이미지/그림 DOM 확인; 육안 미검증|수정|부분|Major|
|48 / C35 / training-log|Batch · Step · Epoch|독립 장 불필요, 정보 보존|Batch/Step/Epoch를 C29 노트로 흡수, 10장/4장=3step 보존|그림 형태/육안 미검증|통합|해결|Minor|
|49 / C36 / overfit|Overfitting · 새 데이터 일반화|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|50 / C37 / threshold|Score Threshold · 판정 기준|학습 목표상 필요|TP18 FN2 FP4 TN76 같은 100건; Score는 실제 확률 아님, 집계 JS 미실행|그림 형태/육안 미검증|유지·검증|유지|—|
|51 / C38 / confusion|Confusion Matrix · 100건 평가|학습 목표상 필요|TP18 FN2 FP4 TN76, 정확도94% 일치|그림 형태/육안 미검증|유지|유지|—|
|52 / C39 / imbalance|Accuracy의 함정 · 모두 정상이라면?|학습 목표상 필요|전부 정상 예측 Accuracy80%, 불량 Recall0% 일치|그림 형태/육안 미검증|유지|유지|—|
|53 / C40 / metrics|Precision과 Recall|학습 목표상 필요|Precision 18/22=81.8%, Recall18/20=90% 정확|그림 형태/육안 미검증|유지|유지|—|
|54 / C41 / iou|IoU · 박스 겹침 비율|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|55 / C42 / workflow|Vision AI 원리 · 한 장으로 연결|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|56 / C43 / project-brief|첫 과제를 위한 네 가지 질문|독립 장 불필요, 정보 보존|과제 정의 네 질문이 C42 워크플로와 중복|이미지/그림 DOM 확인; 육안 미검증|통합|해결|Minor|
|57 / C44 / project-run|실행 결과 확인 · 임계값과 오류 수|독립 장 불필요, 정보 보존|C37 임계값 실습과 100건 재집계 중복|그림 형태/육안 미검증|통합|해결|Minor|
|58 / C45 / project-iterate|실패 사진이 알려 주는 것|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|
|59 / C46 / project-check|Vision AI 원리 · 무엇을 설명할 수 있나?|학습 목표상 필요|현행 인과 흐름과 핵심 설명은 정적 검토상 대체로 적절; 상세 이미지·실화면 미검증|이미지/그림 DOM 확인; 육안 미검증|유지|유지|—|

## 2. 강의 전체 스토리라인의 구조적 문제

I09~I13의 변화 사례 반복, C03~C05 방법 선택 중복, C11~C13 비선형성 순서, C14/C15 CNN 구조의 동기 역전, C42~C44 마무리 중복이 핵심이다. 독립 장의 삭제를 곧 개념 삭제로 간주하면 안 된다. 아래 AUD-01~04를 구조 개선의 기준으로 사용한다.

## 3. 기술적으로 부정확하거나 오해 가능한 내용

검증된 계산: RGB 640×960×3=1,843,200; AND z=0.5(x1+x2)-0.7 의 00/01/10/11 출력 0/0/0/1; XOR 대각 1은 직선 하나로 분리 불가. Padding 입력 1..9, all-ones 3×3 kernel에서 Padding0 45, Padding1 출력 [[12,21,16],[27,45,33],[24,39,28]]. MaxPool 2×2 stride2 출력 [[6,4],[7,9]]. 회귀 x=2, y=4, w=.5, L=(wx-y)^2: L=9, dL/dw=-12, lr=.1, w'=1.7, 예측 3.4, L'=.36. TP18 FN2 FP4 TN76: Accuracy94%, Precision18/22=81.8%, Recall18/20=90%. 전부 정상 가상 모델의 Accuracy80%, Recall0%. **Critical 계산 오류 확인 없음.** 기술적 정정은 AUD-05~07 및 12 참고.

## 4. 수정 또는 교체가 필요한 Figure

C03 우측 Training→Model→Inference 단절과 사진 통제(AUD-08)는 필수 Figure 개선. C34 Freeze Backbone에서 지도 Head/비지도 군집 대비의 시각적 우선순위(AUD-09). C23 실제 Feature Map stage와 채널 비교 및 C33 외부 원본 fallback(AUD-10). 단, 최신 1920×1080 및 1366×768 화면을 직접 확인하지 않았으므로 Crop/겹침/자산 실패를 이번 검수에서 확정했다고 주장하지 않는다.

## 5. 중복·불필요·누락 슬라이드

통합 대상 I02 scene, I13 vision-challenge, C04 vision-evolution, C35 training-log, C43 project-brief, C44 project-run 6장. 신규 ai-ml-dl-cv와 video-frames 2장. **59−6+2=55장**. 빠지는 정보는 기존 인접 장에 명시적으로 옮긴다.

## 6. 현재 55장 승인 계획으로 해결 가능한 문제

중복 여섯 개 제거 및 신규 두 장, CNN 필요성→전체 구조, XOR/활성화 순서, C37 임계값과 C44 실습 통합은 Approved 기획에 포함. 기획 승인 자체는 Builder 구현이나 화면 검증 완료를 뜻하지 않는다.

## 7. 승인 계획에 추가 반영이 필요한 문제

C03/P16 사진 과실 크기·촬영 조건 통제, 새 사진과 동일 학습 모델의 연결선, 평가가 실측이 아니라는 인수조건. C11 직선 기울기와 절편 모두 변화 가능. C34 Label 사용 여부/학습 파라미터와 Clustering 구분. Video Group Split의 원본 영상 외 동일 제품·설비 그룹 명확화. 55장 120분은 리허설 검증 필요.

## 8. Planner에게 전달할 수정 사항

AUD-01~04. 승인 기획의 55장 ID/시간 배정과 새 Storyboard에 구체 수락 기준을 반영한다. 원본 자료를 Reviewer가 수정하지 않는다.

## 9. Builder가 직접 수정할 사항

AUD-05~12. 수정은 지역 HTML·Figure·CSS/JS에 국한하고 Manifest/Outline 제목/번호 동기화 여부를 재확인한다.

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

### AUD-07 — Minor — Builder — Open

대상: C03. 파일: docs/intro.html 또는 docs/vision_ai_course.html (해당 Concept ID), 필요 시 해당 전용 CSS/JS; Planner 항목은 planning/SLIDE_STORYBOARD.md 및 docs/two_hour_manifest.json.

문제·수정 권고: 의사 Python 조건 if brown_pixels = k 는 비교식이 아님. >= k로 변경하거나 의사코드라고 표시.

근거/상태: 현재 설명용 미완성 코드 고지는 존재.

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

## 10. 검증 범위와 검증하지 못한 사항

검증 완료: main Manifest와 59개 실제 HTML Section Concept ID·제목 대조; 운영안 TWO_HOUR_LECTURE_PLAN.md, PROJECT_GUIDE.md, HTML_DESIGN_RULES.md, assets/SOURCES.md, 기존 reviews/CURRENT_REVIEW_REPORT.md, 승인 기획 Branch Storyboard의 구조 참조; 핵심 숫자 직접 재계산; 전체 선후 흐름 정적 분석.

**미검증:** 59×2=118개의 Chromium 실제 화면 육안 비교(1920×1080,1366×768), 최신 GitHub Pages 캐시/커밋 동기화, asset 원본 Figure의 수치/선 연결·Crop·대비, 이미지 로드/Console, 모든 Interactive 계산/Reset·키보드, 외부 Figure fallback, 실제 120분 리허설. 과거 CI와 리뷰의 스크린샷은 당시 버전의 참고 자료로만 취급한다. 재검증은 scripts/verify_two_hour_course.py, scripts/verify_learning_routes.py, scripts/audit_visual_slides.py 실행 및 각 출력물 검토를 권장한다. 55장 구현 후에는 110개 화면을 다시 확인해야 한다.
