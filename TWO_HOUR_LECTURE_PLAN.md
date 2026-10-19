# Vision AI 기초강의 · 원리 이해 중심 120분 운영안

> **현행 공개 강의 기준 (2026-10-18 개편): Intro 13장 + 통합 42장 = 전체 55장.** `docs/two_hour_manifest.json`을 정답으로 사용한다.  
> 이전 50장 강의 운영안/검토서의 슬라이드 번호는 현재와 다르다.  
> 강의 전체 질문: **“사과 사진에서 작은 갈색 반점을 어떻게 찾고, 다른 사진에서도 믿을 수 있을까?”**

## 1. 강의 목표와 전체 답변

**Vision AI 원리 이해(A안)**가 목표다. 수강생은 설명용 사과 사례를 통해 다음을 자신의 말로 답할 수 있어야 한다.

1. **왜 필요한가?** 사람의 반복적인 검사·위치 확인·영역 분석을 영상으로 지원한다.
2. **왜 어려운가?** 사진의 Pixel은 조명/회전/크기/가림에 따라 변하지만, Task에서 중요한 의미는 안정적으로 찾아야 한다.
3. **무엇을 할 것인가?** 유무·위치·모양·어떤 결과가 필요한지 먼저 결정하고, Task별 모델·Label을 선택한다.
4. **어떻게 계산·학습하는가?** CNN은 Kernel·Feature Map·Task Head를 통해 예측한다. 학습에서는 Loss의 Gradient로 Weight를 바꾼다.
5. **왜 믿어도 되는가?** 새 개체/촬영 조건을 분리한 데이터에서 놓친 결함·오알람과 Task별 지표를 확인한다.

직접 AI 학습 코드 작성·최신 모델 세부 수식·모든 Architecture 암기는 목표가 아니다. **Task 종류와 CNN의 계산 원리**를 구분한다. 최신 모델에는 CNN 이외의 구조도 있으므로 CNN을 모든 Vision AI 모델의 유일한 구조로 설명하지 않는다.

## 2. 2시간 진행 구성

| 구간 | 슬라이드 | 분 | 핵심 질문과 Figure | 자연스러운 다음 연결 |
|---|---|---:|---|---|
| 필요성, 사람의 이해와 숫자 | Intro 1–8 | 14 | 사과 결함 질문 → 사람이 보는 장면 → **Vision AI 활용** → Pixel/RGB/해상도 | “왜 사진만 있으면 어렵나?” |
| 어려움과 결정적인 차이 | Intro 9–13 | 10 | 기존 사과 원본을 조명·회전·가림으로 변환, 클래스 다양성, **어려움 종합** | “무슨 출력을 원해야 중요한 특징인지 정할까?” |
| 지금의 Vision AI / Task / 모델·Label | Course 1–5 | 10 | Class/Box/Mask, **규칙→학습모델→범용 사전학습**, 지도학습, 모델 선택, **유무·위치·영역 데이터** | “그 모델의 가장 기초적인 계산은?” |
| 신경망·비선형성 | Course 6–10 | 16 | 퍼셉트론 Wx+b·Step, AND/XOR, ReLU, Affine층의 한계 | “이 숫자 계산을 이미지에 효율적으로 적용하려면?” |
| **CNN 핵심 원리** | **Course 11–20** | **32** | 사진→Feature Map→Head, Kernel 한 칸/이동, 공유, Channel, Stride/Padding/Pooling, 실측 채널, Task Head | “학습에 필요한 데이터는 무엇일까?” |
| 데이터와 Label | Course 21–25 | 11 | 정상/결함×밝음/어두움, Group Split, 전처리/증강 | “Kernel Weight를 어떻게 바꾸나?” |
| 학습·일반화 | Course 26–32 | 13 | 숫자 1Step 학습, Loss, 추론 차이, **CNN 전체 학습 아키텍처**, 전이학습, Batch/Epoch, 과적합 | “Loss 감소가 실제 검사 성공을 보장할까?” |
| 평가 | Course 33–37 | 9 | Threshold, 혼동행렬, 불균형, Precision/Recall, IoU | “새 촬영조건에서 무엇을 놓치는가?” |
| 원리 회수 | Course 38–42 | 5 | 같은 사과 사진으로 Task→Model/Label→CNN→학습→오류검사 돌아보기 | “이 결과를 왜 믿어야 하는가?” |

**전체 강의 120분**으로 구성하며 별도 질의응답(Q&A) 구간은 배정하지 않습니다. 각 구간의 시간은 예상치이며 실제 발표 리허설로 조정합니다.

## 3. Course 새 장 번호

- **1** Task의 의미와 Class/Box/Mask
- **2** 규칙 vs 지도학습: 사진 조건이 바뀌어도 같은 Label을 배우는 이유
- **3 [신규]** Vision AI가 발전한 방식: 규칙/Task별 학습 모델/범용 사전학습
- **4** 현재 모델 선택: 규칙·사전학습·추가 학습 중 무엇을 먼저 시험할지
- **5** 목적/모델/Label/데이터 선택: Classification, Detection, Segmentation
- **6–10** Perceptron → AND Gate → XOR Gate → ReLU → 비선형성
- **11–20** CNN 구조·Kernel·Feature Map·Weight Sharing·채널·Stride/Padding/Pooling·실제 Feature Map·Backbone/Head
- **21–25** 데이터·Train/Validation/Test·Group Split·Preprocessing/Augmentation
- **26–27** 학습 실습과 Loss/Gradient
- **28 [Figure 교체]** CNN의 Forward → Loss → Backward → Weight 갱신 구조
- **29** Training vs Inference: 학습 후 새 사진에 사용
- **30–32** 전이학습, Batch/Step/Epoch, Overfitting
- **33–37** Score Threshold, Confusion Matrix, Accuracy 함정, Precision/Recall, IoU
- **38–42** 원리 회수, 과제 질문, 교육용 임계값 결과, 실패 조건, 최종 복습

Intro는 **3번(필요성)**, **13번(왜 어려운가·종합)**을 새로 추가했다. Intro Pixel 6×6 클릭은 **5번**, 3채널 이해는 **6–7번**, 해상도는 **8번**, 촬영조건 변화는 **9–10번**이다.

## 4. 장별 강의 설명의 경계와 오해 방지

### 왜 중요하고 어려운가 (Intro)

- 일상·산업에서 영상 기반 **반복 검사, 장면 내 위치 파악, 정밀 영역 분석**을 지원하는 목적을 먼저 보여 준다. 사과는 품질검사라는 대표 사례다.
- I9–10에서 **동일 사과 사진의 화면상 변환**으로 밝기·회전/크롭·가림을 비교한다. 실제 다른 카메라/각도에서 재촬영한 결과라고 주장하지 않는다. I11–12는 클래스 다양성과 중요한 결함 대비, I13은 한 줄로 왜 어려운지 설명한다.
- Pixel 수 vs RGB 채널 수를 구분한다. 가림·초점으로 정보가 없어진 경우 어떤 모델도 항상 정답을 보장할 수 없다.

### 현재의 모델과 데이터 선택 (Course 1–5)

- **Task = 원하는 출력의 형태**, **Model = 그 결과를 계산하는 방식**, **Label = 학습에 제공하는 정답**, **Dataset = 다양한 사례 모음**으로 구분.
- Classification(사진당 Class), Detection(결함마다 Box), Segmentation(결함 Mask) 세 종류로 비교한다.
- **YOLO 계열**은 여러 Task별 모델이 있고 **SAM 2**는 점·박스 등의 프롬프트로 이미지/영상 Mask를 예측할 수 있다. 그러나 자동으로 새 산업 결함의 정답 Label을 알려주는 만능 모델이 아니다.
- CNN은 이미지 모델의 근본 개념을 이해하기 위한 중심 소재이며, 오늘날 Transformer 기반 Vision Foundation Model도 있음을 설명한다. 별도 최신 모델 Architecture 수업으로 확장하지 않는다.

### CNN 계산과 학습

- C10의 큰 Architecture를 10초 보여 준 뒤, C11–19에서 “무슨 블록을 확대해서 보는가”를 직접 가리키며 설명한다.
- C11–12는 같은 교육용 5×5/3×3 숫자 (좌상단 −6, 다음 칸 12); 실제 사과 JPEG 숫자와 혼동하지 않는다.
- C28의 새 그림은 **사과 RGB → Kernel → Feature Map → Task Head → Prediction**(Forward)와 **Label + Prediction → Loss → Gradient/Optimizer → Weight 갱신**(Backward)을 두 층으로 보여준다. CNN 학습 전체가 꼭 그 특정 Tensor 크기/2 Class로 고정된 것은 아니다.
- C26의 수치 회귀는 CNN이 실제로 결함을 학습한 결과가 아니다. 가중치 갱신의 최소 개념 예시다.
- 학습 중 Gradient와 Weight를 바꾸지만 **추론**에서는 고정된 Weight로 새 사진을 분석한다.

### 평가

- 분류 교육용 100건 예시는 `TP18/FN2/FP4/TN76`로 동일하게 연결한다.
- Score 0.82는 불량 확률 82% 보장이 아니며, 같은 100건 기준 임계값 결과는 Validation 설명용이다.
- IoU는 위치/Mask 품질 지표의 개념 예로, 분류 Accuracy/Recall과 동일 지표가 아니다.

## 5. 검사·출처·배포

- 기존 외부 Borromini 회랑 사진은 Intro 새 활용 슬라이드에도 원출처를 직접 표기. 직접 가져온 외부 Figure는 인접 출처를 표시하고 자체 도식/변형에 참고 문헌을 장식처럼 추가하지 않는다.
- 55장 Title/Subtitle/Figure/Takeaway 체계와 `data-concept`, TOC, 수치, 로컬 이미지 경로를 동기화해야 한다.
- `python scripts/verify_curriculum_overhaul.py`, `python scripts/verify_two_hour_course.py`, `python scripts/verify_learning_routes.py`, `python scripts/audit_visual_slides.py`를 수행하여 총 **110개 뷰(1920×1080, 1366×768)** 검사.
- 실제 Pages URL을 최신 Commit으로 확인, 이미지 로딩과 JS 이벤트를 확인. 공개 렌더 검사를 정적 검사와 혼동하지 않는다.
- 전체 콘텐츠 리뷰 및 남은 문제는 [54장 내용·흐름 재검토서](reviews/2026-10-18_VISION_AI_54_SLIDE_FLOW_REVIEW.md)에 기록하고, 활성 TODO는 [TODO_VISION_AI_LECTURE.md](TODO_VISION_AI_LECTURE.md)를 따른다.

## 기술적 참고 자료

- Ultralytics 공식 <https://docs.ultralytics.com/tasks/>: Classification/Detection/Segmentation 등 Task 구분과 모델 선택 예시.
- Meta FAIR SAM 2 공식 <https://ai.meta.com/research/sam2/>: 이미지·영상에서 promptable segmentation 및 사전학습의 활용 범위.

**중요:** 링크는 모델 기능의 사실 확인을 위한 자료이며, 새 강의에 외부 이미지를 복제해서 사용한 것은 아니다.


## 2026-10-19 · 현재 슬라이드 수정 적용

- **I13:** 원본 사과 사진과 밝기·회전·가림 CSS 적용 위치를 통일하였다. 원본 사진의 실제 카메라 시점 변환이라고 설명하지 않는다.
- **C5:** Anomaly Detection 제외. Classification/Detection/Segmentation 세 선택지를 한눈에 비교.
- **C6–10:** 퍼셉트론 → AND의 진리표와 한 직선 → XOR 진리표와 직선 불가능 → ReLU → 비선형 층의 의미.
- **C11:** 과거 발표에 사용했던 얼룩말 CNN 구조 원본 Figure를 출처와 함께 다시 사용. 사내망 원본 로딩 실패 시 로컬 자체 CNN 구조로 대체.
- **C12–13:** 한 Kernel이 5×5 입력을 3×3 Feature Map으로 바꾸는 동일 예제; C14–15는 왜 Weight를 공유하고 여러 필터 Channel을 만드는지 설명.
- **C17–18:** 같은 3×3 입력에서 Padding=0/1의 출력 1×1/3×3 비교; Pooling은 강한 반응 유지와 공간 축소 목적을 먼저 설명.
- **C24–25:** Preprocessing/Augmentation을 동일 사과 사진의 본문 HTML 비교로 전환. 브라우저 표시 변화와 실제 학습용 이미지 저장은 구분.
- **C28:** 복잡한 화살표 교차를 제거하고 Forward / Backward 두 줄로 정렬.
- **C30:** 동일 CNN 구조에서 Feature Extractor는 Freeze하고 Classification Head만 학습하는 사례를 파란색/초록색으로 비교.
- 새 스크린샷 55×2=110장 및 실제 Pages 로딩 검증은 별도 확인이 필요하다.


## 2026-10-19 · Gate 인터랙티브 실습 및 Q&A 삭제 (최신)

- 별도 질의응답 시간 **0분**: 55장 강의 내용과 마지막 원리 복습까지 **120분 모두 강의에 사용**합니다.
- Course 7 AND: Weight w₁·w₂와 Bias를 막대 슬라이더로 이동. 단일 결정 직선과 네 입력의 예측 결과, 정답 4건 중 맞힌 개수가 즉시 갱신됩니다.
- Course 8 XOR: Layer 1의 뉴런 2개(각 Weight 2개 + Bias 1개) / Layer 2의 출력뉴런(Weight 2개 + Bias 1개) = **총 9개의 Weight/Bias 슬라이더**. 은닉층 **Step 사용 / 활성화 없음** 토글을 제공해 두 선형층을 쌓아도 XOR를 직선 하나로 분리할 수 없음을 보여 줍니다. Step을 켜면 두 뉴런의 경계가 XOR를 분리합니다.
- 동일 개념을 뒤의 ReLU/비선형성 설명에 연결합니다. Gate 시연 시간을 11→16분으로 늘리고 데이터·학습·CNN에 추가 시간을 배분해 전체 **120분**을 맞췄습니다.
- 인터랙션 코드: `docs/interactive_gates.js`, 디자인: `docs/interactive_gates.css`. 두 페이지 새 Figure에 국소 적용. CDN 의존 없음.
