# Vision AI 73장: 유명 논문·강의·공식 원본 Figure 활용 매핑

> 2026-10-16 · **설계/조사 문서**입니다. 여기서 '후보'는 원본 이미지 파일 URL·권리·표시 가능성을 확인하기 전 단계이며 현재 공개 강의 슬라이드가 변경되었다는 의미가 아닙니다.

## 판단 기준

- **16번 CNN 얼룩말 원본 채택 때 좋았던 점**: 실제 사례로 설명하는 큰 한 장의 Figure, 단계가 한눈에 드러나는 구조, 핵심만 담은 한국어 설명.
- 영어로 된 원본 Figure를 사용하더라도 설명은 **한국어 중심**으로 하고 필요한 기술 용어에 한해 영문을 함께 씁니다.
- 원본 Figure가 예쁘더라도 입력/출력/모델 버전이 달라 현재 설명과 충돌하면 사용하지 않습니다.
- 실제 사진·인터랙티브 자료가 있는 슬라이드는 이유 없이 벡터 그림으로 대체하지 않습니다.
- 수학/Pixel 숫자표/Kernel 값은 시각자료만 믿지 않고 **계산을 재현해 검증**합니다.
- ResNet/U-Net 개별 모델 구조, ViT/Tracking/Depth 등은 현재 입문 강의에 추가하지 않습니다.
- 먼저 기존 **총 73장** 구조를 유지하며 Figure의 적합성부터 평가합니다. 새 슬라이드는 꼭 필요한 경우에만 추가합니다.

## 작업 우선순위 (초기 제안)

| 우선순위 | 대상 슬라이드 | 활용 자료 | 판단 포인트 |
|---|---|---|---|
| 1 | Vision AI Task 선택 | Distill Feature Visualization (R12) | 추상적인 '층이 깊어질수록'을 실제 특징 이미지로 보여 줌 |
| 1 | 51번 (Shortcut) | Grad-CAM (R13) + Geirhos (R24) | 객체 대신 배경에 반응하는 문제 등 시각적 오해 수정 |
| 1 | 10~11번 (Filtering/경계) | OpenCV 원본 예제 (R06/R07) | 필터 전후 사진을 그림만 보고 이해 가능하게 구성 |
| 2 | Classification · 이미지 전체 분류 | CNN Explainer (R10/R11), CS231n (R03), D2L (R08/R09) | Figure의 실제 Kernel 위치·Feature Map·값 대응 |
| 2 | 29~32번 (YOLO) | YOLO 논문과 Ultralytics (R16~R21) | Class/Box/Score/Label/학습의 관계를 원본 그림 중심 설명 |
| 2 | 44~46번 (전이학습) | PyTorch, Shortcut Learning (R23/R24) | Freeze/Fine-tune 과현장 환경 변화 |
| 3 | Detection · 위치와 종류 찾기 | Ultralytics Metrics (R22) | Threshold/Precision/Recall/IoU를 같은 사례로 묶기 |
| 유지 | 1~5번, 16번, 28번, 33번 등 | 이미 좋은 사진·원본·인터랙티브 | 설명에 오류가 있는 경우만 수리 |

## 통합 강의 54장 매핑

| 슬라이드 | 현재 메시지 | 주요 출처 ID | 활용할 구체적 시각자료 | 상태 | 초보자 관점 메모 |
|---|---|---|---|---|---|
| 1 | 필요한 결과부터 정하면 Vision Task가 정해집니다 | R15 · R18 · R19 | 기존 사과/정답 도식 유지 | 유지 | 같은 이미지에서 세 Task 목적 대비 |
| 2 | 이미지 전체의 상태나 종류를 예측합니다 | R19 | 실제 이미지 전체 Label 예시 보강 | 유지 | Classify 원본 Figure는 전체-클래스 관계 확인 |
| 3 | 객체나 결함의 위치를 사각형으로 찾습니다 | R18 | 실제 Detect 박스 예시와 병치 후보 | 후보 | YOLO 공식 사진 결과와 비교 |
| 4 | Segmentation · Pixel 단위 분할 | R15 | Mask 원본 주석 사진 참고 | 후보 | Pixel Mask와 Box 차이만 강조 |
| 5 | 같은 사진, 다른 정답 형태 | R15 · R18 · R19 | 기존 동일 사과·Task 변형 3종 유지 | 유지 | 동일 대상/다른 라벨 장점 보존 |
| 6 | AI · 머신러닝 · 딥러닝의 관계 | R02 · R04 | AI·ML·DL 기존 관계 그림 유지 | 유지 | 대학 강의의 개념 순서만 참고 |
| 7 | 규칙 기반과 데이터 학습 | R02 · R04 | 규칙 vs 학습 기존 그림 유지 | 유지 | 한글로 간단히 보완 |
| 8 | Pixel 연산과 주변 영역 연산 | R06 · R08 | 이웃 연산 실제 계산 그림 보존 | 유지 | 독립 Pixel vs Neighborhood |
| 9 | 이동하는 3×3 Kernel | R06 · R09 | 기존 Kernel 연산·수치 보존 | 유지 | 행렬 값과 결과 재검산 |
| 10 | Mean · Gaussian · Median 비교 | R06 | OpenCV Mean·Gaussian·Median 원본 처리사진 조사 | 후보 | 원본 필터 처리 사진/실제 수치 대응 |
| 11 | Sobel · 밝기 변화와 경계 | R07 | OpenCV Sobel 원본 Before/After 조사 | 후보 | 밝기 변화→경계 반응 이미지 |
| 12 | Spatial Filtering에서 CNN으로 | R06 · R09 | 필터→CNN 전환 슬라이드 한글 해설 | 보완 | 고정 Kernel↔학습 Kernel |
| 13 | Perceptron · 가중합과 Bias | R03 · R04 | 입력·Weight·출력 계산 유지 | 유지 | 현재 난이도 유지 |
| 14 | Neural Network · 층별 계산 | R02 · R04 | 신경망 기본 그림 유지 | 유지 | Layer와 Weight 관계 직관적으로 |
| 15 | ReLU · 비선형 활성화 | R03 · R08 | ReLU 값 계산 시각화 유지 | 유지 | 비선형성이 필요한 이유 |
| 16 | CNN 아키텍처 · 특징 추출과 분류 | R26 | 사용자가 지정한 얼룩말 원본 Figure 유지 | 유지 | 왼쪽 특징 추출 / 오른쪽 분류 강조 |
| 17 | CNN 기본 블록 · Conv · BN · ReLU | R03 · R10 · R11 | CNN Explainer 단계별 구조 후보 검토 | 후보 | Conv·BN·ReLU 도식은 순서 일반화 주의 |
| 18 | CNN · 지역 연결과 가중치 공유 | R03 · R11 | 공유 Kernel의 이동 Figure 조사 | 후보 | 하나의 Weight 세트가 위치마다 반복 |
| 19 | Kernel 위치별 반응 | R09 | 동일 필터·서로 다른 Patch의 수치 비교 | 보완 | 원문 계산값과 현재 그림 검산 |
| 20 | 숫자 배열에서 Feature Map까지 | R09 · R10 | CNN Explainer Feature Map 연산 Figure 후보 | 후보 | 작은 영역→한 Pixel 계산 확대 |
| 21 | RGB 입력과 출력 Channel | R03 · R08 | RGB 채널↔출력 Feature Map 구조 참조 | 보완 | 3채널 입력 Kernel과 2D 출력 관계 |
| 22 | Stride · 이동 간격과 출력 크기 | R08 | D2L Stride 그림과 수치 비교 | 보완 | Output shape 검산 |
| 23 | Padding · 가장자리 계산 | R08 | D2L Padding 원본 예시 검사 | 보완 | 경계 계산 영역 크기 |
| 24 | Max Pooling · 공간 정보 축소 | R08 | D2L Pooling Before/After Figure 조사 | 후보 | Pooling vs Gaussian Downsampling 주의 |
| 25 | 실제 CNN Feature Map · 층별 반응 | R02 · R03 · R08 | ImageNet 사전학습 SqueezeNet1.1의 실제 3단계 활성화 지도(동일 강아지 입력) | 완료 | 실제 공간별 Feature Map / 채널별 상대값 |
| 26 | Feature Visualization · 층별 학습 패턴 | R03 · R12 | Stanford CS231n 원본 VGG-16 Feature Visualization | 완료 | 특징을 자극하는 패턴과 실제 Feature Map 구분 |
| 27 | Backbone과 Task Head | R03 · R16 | Backbone/Head 역할 설명 유지 | 유지 | CNN 공통 Feature와 task 출력 분리 |
| 28 | 고정 필터와 학습 필터 | R07 · R08 · R17 | 고정 Sobel과 학습 Filter 대비 | 보완 | 사람이 정한 값 ↔ 학습한 값 |
| 29 | YOLO 구조 · Backbone / Neck / Head | R17 · R27 | 기존 YOLOv8 원본 Figure 유지 | 유지 | 과도한 모듈 강의 피하기 |
| 30 | YOLO Detection · Class / Box / Score | R16 · R18 | 공식 YOLO 실제 검출 이미지 후보 | 후보 | Class·Box·Score 실제 샘플은 추론 출처 명확히 |
| 31 | YOLO Task · Classify / Detect / Segment | R18 · R19 | Classify/Detect/Segment 비교 기존 사과 재사용 | 유지 | Task별 출력 형식이 다름 |
| 32 | YOLO 검출 학습 · 종류와 위치 | R16 · R18 | 신규 한글 Class+Box 학습 그림 유지 | 유지 | YOLO 검출은 분류만 학습 X |
| 33 | YOLO 데이터·Label·검증 | R20 · R21 | YOLO Dataset Label 실물 1줄 예시 보완 | 보완 | class cx cy w h 정규화 |
| 34 | 모델 학습 · 오차를 줄이는 반복 | R08 · R21 | 기존 학습 Interactive 유지 | 유지 | Weight는 Gradient가 수정 |
| 35 | Loss · 예측과 정답의 차이 | R04 · R05 | Loss와 정답 비교 계산 유지 | 유지 | 학습 loss vs 성능지표 구분 |
| 36 | Forward · Gradient · Weight 갱신 | R04 · R05 | Forward/Backward 과정 한글 해설 | 보완 | 실제 학습 오차를 이용한 업데이트 |
| 37 | Training과 Inference의 차이 | R04 · R21 | Training vs Inference 그림 유지 | 유지 | 언제 Weight가 변경되는지 |
| 38 | Batch · Iteration · Epoch | R21 | Batch/Epoch 실습 예시 유지 | 유지 | 10장/Batch4 예시처럼 수치 검증 |
| 39 | CNN Filter 가중치 학습 | R08 · R11 | 학습 Kernel Weight를 그림에 표현 | 보완 | CNN Kernel이 학습되는 과정 |
| 40 | 데이터셋 · 촬영 조건과 Label | R01 · R24 | 현장 변화(조명/시점/가림) 기존 사진 유지 | 유지 | 현장 이미지가 실감 남 |
| 41 | Train · Validation · Test | R21 · R25 | Train/Val/Test 구분 설명 유지 | 유지 | 독립 데이터 기준 설명 |
| 42 | Video Group Split · 데이터 누출 방지 | R25 | Video/LOT 그룹 분할 사례 강화 | 보완 | 동일 촬영 그룹이 Train/Test로 새면 누출 |
| 43 | Preprocessing · 입력 규격 맞추기 | R21 | Letterbox/Resize 예시·이미지 유지 | 유지 | 비율과 패딩 구분 |
| 44 | Data Augmentation · 조건 변화 만들기 | R21 | Augmentation 실제 사진 비교 유지 | 유지 | Label 함께 변형 주의 |
| 45 | Transfer Learning · 사전학습 활용 | R23 | PyTorch 전이학습 본문 Figure 선별 | 후보 | 사전학습→내 Task Fine-tune |
| 46 | Freeze와 Fine-tuning | R23 | Freeze/Unfreeze 구조 유지 | 유지 | 기존 Backbone / Task Head 사용 |
| 47 | Overfitting · 새 데이터 일반화 | R24 | Shortcut 학습 실제 사례 Figure 선별 | 후보 | 학습 점수와 현장 성능 불일치 |
| 48 | Score Threshold · 판정 기준 | R22 | Confidence threshold 예시 유지 | 유지 | 점수≠성공확률 |
| 49 | Confusion Matrix · 100건 평가 | R22 | Confusion Matrix 한글·수치 보존 | 유지 | TP/FP/FN/TN 실제 동일 조건 |
| 50 | Precision과 Recall | R22 | Precision/Recall 수치 예시 보존 | 유지 | 검출 문제에도 다른 Matching 조건 필요 |
| 51 | IoU · 박스 겹침 비율 | R22 | IoU 실제 Box 중첩 Figure 후보 | 후보 | 교집합/합집합 이미지 |
| 52 | Grad-CAM · 클래스별 판단 근거 | R13 · R24 | Grad-CAM/Shortcut 실제 원본 Figure 후보 | 최우선 | 높은 점수≠옳은 근거 직관화 |
| 53 | Vision AI 프로젝트 전체 흐름 | R21 · R24 | 운영 Loop 기존 한글 그림 유지 | 유지 | 현장 실패 수집→재평가 |
| 54 | 운영 데이터와 재학습 | R21 · R24 | 기존 재학습/모니터링 결론 유지 | 유지 | 성능 변화는 환경·운영까지 감안 |

## Intro 19장 참고 매핑

| Intro | 기존 슬라이드 메시지 | 주요 출처 ID | 적용 원칙 |
|---|---|---|---|
| 1 | AI와 시각의 출발점 | R01 · R02 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 2 | 사람의 시각 · 장면 이해 | R01 · R02 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 3 | 일상 속 Vision 기술 | R01 · R02 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 4 | 사진 속 객체 인식 | R01 · R08 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 5 | 사람의 의미 인식 vs Pixel 숫자 | R01 · R08 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 6 | 조명·색감에 따른 Pixel 변화 | R01 · R08 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 7 | 시점·회전·가림·초점 변화 | R01 · R08 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 8 | 위치 변화와 Pixel 배열 | R01 · R08 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 9 | RGB · Pixel당 세 숫자 | R01 · R08 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 10 | RGB 이미지와 숫자 배열 | R01 · R08 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 11 | 해상도와 Pixel 수 | R01 · R04 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 12 | 해상도에 따른 정보 차이 | R01 · R04 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 13 | 시각 이해 · What과 Where | R01 · R04 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 14 | 2D 이미지와 3D 공간의 모호함 | R01 · R04 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 15 | 밝기값 3D 표시 vs 실제 거리 | R01 · R24 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 16 | 외우는 Pixel, 학습하는 Pattern | R01 · R24 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 17 | Vision AI · Pixel에서 결과까지 | R01 · R24 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 18 | 센서별 입력 데이터 비교 | R01 · R24 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |
| 19 | 우리 주변의 Vision Sensor | R01 · R24 | 기존 사과·Pixel 도식 유지, 참고 Figure는 근거와 비교만 |

## Figure 1장 적용 체크리스트

1. **원본 페이지**: 저자·논문·수업연도·정확한 Figure/슬라이드 번호를 적습니다.
2. **원본 파일 URL**: HTTP(S) 이미지 요청과 실제 픽셀을 검증한 뒤 등록합니다(표 URL을 바로 이미지 URL이라고 추정하지 않습니다).
3. **권리·재사용 조건**: 페이지에 표시된 이용 조건과 출처 필요사항을 기록하고, 불명확하면 해당 페이지 링크/강의용 독립 재구성을 우선합니다.
4. **맥락**: 논문 속 모델 버전, 이미지의 의미, 수치·색상 범례, Before/After 계산 조건을 확인합니다.
5. **한글 설명**: 제목=핵심 한 문장, 부제=그림을 보는 순서, 강조=학습자가 알아야 할 결론. 영어 단어는 필요한 기술 용어만 씁니다.
6. **실제 강의화면**: 16:9 슬라이드에서 원본이 충분히 크게 보이는지, 잘림/글자 겹침/외부 URL 차단이 없는지 검사합니다.
7. **GitHub 변경**: 브랜치 → 변경 → PR → 병합 → 최신 main 확인 → Actions/Pages 배포 확인.
8. **일괄변경 지양**: 최초 2~3장 샘플 적용 → 비교 평가 → 같은 기준으로 다음 묶음 적용.

## 레포지토리 연결

- 참고문헌의 상세 링크는 [REFERENCE_VISION_AI_SOURCE_LIBRARY.md](REFERENCE_VISION_AI_SOURCE_LIBRARY.md)에서 R01~R28로 조회합니다.
- 현재 공개 수업: https://sh0427-han.github.io/vision_ai_lecture/
- 교육용 원본 데이터 및 기타 기존 그림 인용 목록: [assets/SOURCES.md](assets/SOURCES.md).



## 2026-10-16 · 시범 적용 완료 후 검토 지점

| 슬라이드 | 실제 적용 | 확인해야 할 점 |
|---|---|---|
| Vision 10 | OpenCV Mean·Gaussian·Median 원본 처리영상 3종 + 기존 3×3 수치 예시 펼침 | 필터별 입력 조건 차이를 이해하는가? |
| Vision 11 | OpenCV Sobel 원본 사진·밝기·미분 원리 Figure + 기존 실제 Sobel 연산 펼침 | 밝기 변화가 왜 경계 단서인지 이해하는가? |
| Vision 25 | Distill GoogLeNet mixed4a/mixed5a의 최적화 패턴/실제 반응 이미지 비교 | Feature Visualization과 실제 Feature Map을 구분하는가? |
| Vision 51 | 분류 모델 Dog/Cat Class별 Grad-CAM 원본 3종 | 같은 사진에서 클래스별로 열지도가 왜 달라지는지 이해하는가? |

4개 슬라이드만 우선 수정하고, 다른 49개 Vision AI 슬라이드와 Intro 19장 그림은 그대로 유지합니다. 원본 이미지는 외부 링크이며 네트워크 접근 불가 시 기존 로컬 SVG가 표시됩니다.


## 2026-10-16 · Vision AI 25번 3단계 CNN Figure 반영

- 이전 Distill 2개 Layer의 연구 시각화로만 구성한 25번을 **기존 사과 원본 + 얕은층 + 중간층 + 깊은층**으로 교체했습니다. 사용자 피드백: 연구용 추상 Figure만으로는 교육 목적이 불명확했습니다.
- 새 Figure: `docs/assets/lesson/cnn_three_stage_apple_ko.svg`. 사과 사진은 기존 `lesson_cnn_feature_hierarchy.svg`에 내장된 동일한 사진을 그대로 재사용합니다. 사진의 새 복제본이나 외부 이미지 CDN은 필요하지 않습니다.
- 얕은층은 실제 고정 경계 강조 연산(학습된 CNN Filter 결과 아님)을 개념 예시로 보여주며, 중간층과 깊은층은 같은 사과에서 관찰 가능한 곡선·부분 형태와 그 조합을 명확한 주석으로 표시합니다. **세 패널은 실제 학습 모델의 Layer Activation이 아닌 교육용 도식**입니다.
- 기술 설명 근거: CS231n CNN 강의자료 (R03) 및 Distill Feature Visualization (R12). 실제 Feature Visualization 결과를 직접 측정한 것처럼 표기하지 않습니다.


## 2026-10-16 · Vision AI 25번 CS231n 원본 Figure 반영

- 현재 강의 25번: `docs/assets/lesson/cs231n_vgg16_feature_hierarchy_original.png` 원본 PNG와 한국어 3단계 해설(얕은층 Conv1_1 / 중간층 Conv3_2 / 깊은층 Conv5_3)을 사용합니다.
- 기존 사과 3단계 직접 제작 SVG 대신 실제 학습 특징 연구 시각화로 교체합니다. 원본 이미지는 변경하지 않았습니다. 그림 출처는 CS231n 2017 Lecture 5 Slide 37입니다.


## 2026-10-16 · 실제 Feature Map과 Feature Visualization 분리(현재)

- **Vision 25**: 사전학습된 torchvision SqueezeNet 1.1에 CS231n 원본 강아지 사진을 직접 입력해 계산한 실제 Feature Map. `docs/assets/lesson/cnn_squeezenet_actual_feature_maps.png`, `scripts/render_cnn_feature_maps.py`로 재현 가능. 네 채널을 선택하며 색은 각 채널별 상대 반응입니다.
- **Vision 26**: Stanford CS231n 2017 Lecture 5 Slide37 원본 VGG-16 Figure를 보존하고, 입력 사진의 실제 공간별 출력과 각 계층의 학습된 특징을 자극하는 패턴의 차이를 설명합니다.
- 두 Figure는 SqueezeNet1.1과 VGG-16으로 **다른 CNN**입니다. 같은 사진/같은 모델의 연속 Layer 출력으로 오해시키지 않습니다.
- Intro 19 + 통합 54 = 총 73장. 이후 번호·목차 일치와 브라우저 QA를 검증합니다.

## 2026-10-16 · 실사 계산 기반 5장 시각자료 및 73개 간결 제목

- Intro 19장과 통합 강의 54장 전부의 슬라이드 제목을 한 문장형 서술(~합니다/~입니다) 대신 짧은 개념형 제목으로 재작성했습니다. 목차에도 동일 제목을 사용합니다.
- Vision AI 22·23·24·43·44번은 같은 CS231n 강아지 원본 사진에 필터·Pooling·비율 조정·밝기/회전/가림을 실제 계산한 PNG를 사용합니다. 원래 정확한 행렬·개념 Figure는 각 슬라이드의 펼침 영역에 보존합니다.
- 25·26번의 실제 CNN Feature Map/연구 원본 특성 시각화, 10·11번의 OpenCV 원본, 52번의 Grad-CAM 원본은 유지합니다. 각 그림의 출처와 모델 계산 여부를 구분합니다.
