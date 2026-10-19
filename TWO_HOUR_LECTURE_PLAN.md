# Vision AI 초급 강의 · 최신 58장 운영 계획

> **현재 기준 2026-10-19:** Intro 13 + 통합 Vision AI Course 45 = **총 58장**. 총 120분 전부 설명 및 시연에 사용하며 별도 Q&A 구간 없음.
> 최종 강의 순서·슬라이드 제목의 기준은 `docs/two_hour_manifest.json`과 `docs/lecture_outline.js`.

## 1. 전체 질문과 교육 목표

**대표 사례:** “사진 속 사과의 작은 갈색 반점을 어떻게 찾아, 조명·회전이 바뀐 사진에서도 잘 판단할까?”

수강생은 이미지가 Pixel 숫자로 입력되고, CNN이 지역 특징을 계산하며, 데이터의 정답 Label로 Weight를 학습하고, 새 사진에서 Precision/Recall 등을 확인해야 한다는 인과관계를 설명할 수 있으면 충분합니다. 모델 코딩이나 모든 Architecture 암기는 목표가 아닙니다.

AND/XOR는 Vision AI의 별도 Task가 아니라 **왜 단층 퍼셉트론만으로 충분한 문제와 부족한 문제가 생기는지** 보여주는 계산 예시입니다.

## 2. 120분 슬라이드 구간

| 구간 | 최신 번호 | 분 | 수업에서 답하는 질문 |
|---|---|---:|---|
| Vision AI 필요성 및 컴퓨터의 입력 | Intro 1–8 | 14 | 왜 사진 검사가 필요하며 사진은 어떤 Pixel 숫자로 변환될까? |
| 이미지의 어려움 | Intro 9–13 | 10 | 같은 사과가 조명·크기·가림에 따라 왜 다르게 보일까? |
| Vision Task / 모델·Label | Course 1–5 | 10 | Class, Box, Mask 중 어떤 결과가 필요한가? |
| AND/XOR와 퍼셉트론·비선형성 | **Course 6–12** | **18** | 언제 뉴런 하나로 되고, 왜 XOR에는 비선형성이 필요할까? |
| CNN 계산과 특징 추출 | Course 13–23 | 30 | Kernel·Feature Map·Channel·Pooling은 어떤 역할을 할까? |
| 데이터셋 분할과 증강 | Course 24–27 | 10 | 정상/불량과 촬영 변화를 어떻게 독립적으로 구성할까? |
| 학습 · 지도와 비지도 활용 | Course 28–35 | 14 | 같은 CNN Feature를 지도 Classifier와 비지도 Clustering에 어떻게 사용할까? |
| 모델 평가 | Course 36–40 | 9 | 무엇을 놓쳤고 어떤 오류가 발생했나? |
| 첫 사과 사례로 회수 | Course 41–45 | 5 | 내가 해결할 Task·Label·Model·Metric을 설명할 수 있나? |

**총합: 120분.** 발표 시간은 실측 리허설 전에 정한 교육용 배분이다.

## 3. 퍼셉트론 → AND → XOR: 단계별 교수 흐름

| Course | 핵심 메시지 | 발표자가 연결할 질문 |
|---|---|---|
| **6 · 퍼셉트론** | 뉴런 하나의 동일 Weight 예시 z=W(x₁+x₂)+b를 그림으로 보여주고 W,b 한 개씩 설명. 일반 뉴런은 입력별 Weight가 다를 수 있음. Step으로 0/1 출력 | “뉴런 하나로 어떤 논리 규칙을 표현할 수 있을까요?” |
| **7 · AND Gate 규칙** | 0/1 두 입력 모두 1일 때만 1. 네 입력 (00,01,10,11)을 시각적으로 비교. 동일 Weight를 쓰는 퍼셉트론 한 개로 구현 가능 | “Weight와 Bias를 조절하면 경계가 어떻게 바뀔까요?” |
| **8 · AND 실습** | x₂의 Weight는 1로 고정하고 W,b를 바꿔 결정 직선의 **기울기와 위치**를 조절. 기본 예시 AND 정답 4/4 | “그렇다면 입력이 서로 다를 때만 1인 규칙도 직선 하나로 분리할 수 있을까요?” |
| **9 · XOR Gate 규칙** | 둘 중 **정확히 하나가 1**일 때만 1. 정답 1이 (0,1)와 (1,0)에 대각선으로 놓임 | “AND와 다르게 왜 뉴런 하나로 표현이 어려울까요?” |
| **10 · XOR 실습** | 선형 두 층도 최종 **하나의 직선**; 비선형 활성화 추가로 XOR 패턴을 구현 | “그 직선을 꺾는 활성화가 무엇일까요?” |
| **11 · ReLU** | 음수를 0으로 바꾸는 꺾임 | “비선형 함수를 중간에 넣으면 어떤 점이 달라질까요?” |
| **12 · 선형층 합성의 한계** | 비선형성 없이는 깊어져도 하나의 Affine 변환과 같음 | “이미지의 지역 특징을 이런 뉴런으로 효율적으로 배우려면?” |

AND는 정답을 정의한 논리 기능이고, Step 퍼셉트론은 이를 구현하는 수치 모델이다. 뉴런 개수와 입력별 Weight 개수는 다르다는 점을 명확히 구분한다. 단층 신경망이라는 설명도 가장 단순한 뉴런 하나의 구현 예시로 제한한다.

AND/XOR의 새로운 개념 장표에는 외부 이미지 없이 직접 구성한 네 가지 0/1 입력 그림을 사용한다. **녹색 결과가 1, 회색 결과가 0**이며, 설명용 표와 별개로 모델을 실제 학습한 결과로 소개하지 않는다.

## 4. 이후 슬라이드 번호(최신 Course)

- **C13** CNN Architecture, **C14** CNN을 쓰는 이유(얼룩말 예시), **C15** Kernel, **C16** Feature Map, **C17** Weight Sharing, **C18** RGB/Feature Channel
- **C19** Stride, **C20** Padding, **C21** Max Pooling, **C22** 실제 Feature Map 일부, **C23** Backbone/Task Head
- **C24–27** Dataset, Train/Validation/Test, Group Split, Data Augmentation
- **C28–35** 학습 수치 예제, Loss, CNN Forward/Backward, 추론, 전이학습, **지도/비지도 특징 활용(C33)**, Batch/Epoch, Overfitting
- **C36–40** Score Threshold, Confusion Matrix, Accuracy 함정, Precision/Recall, IoU
- **C41–45** Vision AI 업무 과제 구성·검증·개선·마무리

## 5. 수치·데이터·실험 설명 원칙

- AND 설명 규칙: (00→0, 01→0, 10→0, 11→1), 단일 Step 퍼셉트론으로 구현 가능.
- XOR 설명 규칙: (00→0, 01→1, 10→1, 11→0), 단일 직선 불가능. 뒤 C10의 비선형 예시는 `|t|=ReLU(t)+ReLU(−t)`를 사용하며 단일 ReLU 하나의 계산 결과라고 설명하지 않음.
- C15–16 Kernel/Feature Map의 5×5 입력 및 3×3 출력 수치는 동일한 교육용 예시. 사과 JPEG의 실제 픽셀 계산이라고 주장하지 않음.
- C20 Padding: 동일 입력 3×3, 3×3 Kernel, Stride1을 비교해 Padding0 출력 1×1 vs Padding1 출력 3×3.
- C28 학습의 1차원 회귀는 **Gradient 설명용**이지 실제 CNN 결함 학습 측정치가 아님.
- C37–40의 교육용 평가 데이터는 동일한 100건 Cohort로 연결하고 Test 실제 측정 결과로 포장하지 않음.
- 실제 강아지 SqueezeNet Feature Map 등 외부 실측 예시에는 출처 및 대상 모델·사진을 구분. 사내망을 고려해 직접 재구성 그림은 로컬 CSS/HTML을 사용.

## 6. 검증·배포 조건

1. `scripts/verify_two_hour_course.py`: Intro 13 + Course 45, 목차 58개, Concept ID와 제목 동기화, 네 입력 조합 숫자 및 Task/Kernel/평가 관련 기존 검사.
2. `scripts/verify_learning_routes.py`: 최신 Concept ID로 AND 설명→퍼셉트론→AND 실습→XOR 설명→XOR 실습 이동, Slider·초기화 등 기존 회귀 테스트.
3. `scripts/audit_visual_slides.py`: 두 발표 해상도 **1920×1080 / 1366×768**, 전체 58×2=**116개 화면**에서 잘림·이미지·레이아웃·콘솔 확인.
4. Merge 후 `main` 실제 파일 재조회 및 Pages Workflow 최신 커밋 상태, 공개 사이트 실렌더/캐시 확인.
5. 리허설에서는 Gate 이해 18분/ CNN31분/총 120분 실현 가능성 확인.

**주의:** Connector 기반 정적 구조 검사와 118개 브라우저 실제 스크린샷 검증은 서로 다르다. 후자를 실행하지 않았다면 완료했다고 기록하지 않는다.


## 2026-10-19 · 퍼셉트론 입력선의 Weight와 후속 Gate 실습

- 일반 단일 퍼셉트론: z=w₁x₁+w₂x₂+b. 뉴런 1개, 입력 2개, Weight는 2개.
- 동일 Weight의 AND 예시: w₁=w₂=0.5, b=−0.7이면 z=0.5(x₁+x₂)−0.7이며 Step을 통해 0,0,0,1을 얻는다.
- AND 기울기 변경 실습: z=Wx₁+1·x₂+b는 두 번째 연결 Weight를 1로 고정했으며, 결정 직선 x₂=−Wx₁−b. 이것은 위의 동일 Weight 사례와 다른 AND 매개변수 설정이다.
- XOR 설명 실습: Layer1 t=W₁x₁+1·x₂+b₁, Layer2 z=W₂g(t)+1·x₁+b₂. 각각 추가 연결 Weight는 1로 고정되어 화면에서 조절하지 않는다. Layer마다 하나만 조절한다는 뜻이 실제 Weight가 하나뿐이라는 뜻은 아니다.


## 2026-10-19 · CNN Feature의 지도/비지도 비교

- **C6:** W(가중치) 1개와 b(편향) 1개만 노출한 공통 Weight 예시 `z=W(x₁+x₂)+b`. 그림은 두 입력에 같은 W를 쓰는 특별한 계산이며 보편적인 모든 퍼셉트론이 한 스칼라 Weight만 가진다는 뜻은 아니다.
- **C32→C33:** 같은 **고정된 사전학습 CNN**에서 추출한 Feature를 활용. (지도) 정답 Label을 사용해 Classification Head를 학습하고 정상/불량 예측. (비지도) 정답 Label 없이 K-means 등의 Clustering으로 이름 없는 그룹 A/B 발견.
- 지도/비지도 구분은 **학습할 때 정답 Label을 쓰는가, 학습 목표가 무엇인가**에 따른다. 단순히 Head를 교체해 모든 CNN이 지도/비지도로 전환되는 것은 아니고, Backbone 자체의 학습 방식과도 별개다.
- 최신 배정: CNN 원리 C13–23 **30분**, CNN 학습 C28–35 **14분**. 전체 **120분**.


## 2026-10-19 · Preprocessing 삭제에 따른 흐름 최신화

- 이전 C27 Preprocessing(Resize/Letterbox 비교)은 강의 범위에서 제외. **C24 Dataset → C25 데이터 분할 → C26 Video Group Split → C27 Data Augmentation → C28 학습**으로 바로 진행합니다.
- 데이터 학습에 필요한 최소한의 주의점(독립 분할, Train에서만 증강, Label 변경 시 정합성)은 기존 슬라이드에서 유지합니다.
- 이후 C33 CNN 지도/비지도 비교, C36–40 모델 평가, C41–45 업무 적용. 전체 58장/120분(별도 Q&A 없음).
