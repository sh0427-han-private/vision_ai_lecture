# Visual / Reference Sources

강의 자료의 출처와 사용 원칙을 기록합니다.

## 원칙

1. 외부 Figure를 그대로 복사하기보다 가능한 경우 직접 다시 그린 교육용 Diagram을 사용합니다.
2. 외부 자료를 참고해 재구성한 경우 원 출처 링크를 기록합니다.
3. 외부 사진을 추가할 경우 License와 원본 URL을 기록합니다.
4. 출처가 불명확한 이미지는 강의자료에 포함하지 않습니다.

## 현재 직접 제작한 Diagram

- `vision_ai_pipeline.svg`
- `sensor_overview.svg`
- `image_as_numbers.svg`
- `ai_ml_dl.svg`
- `supervised_tasks.svg`
- `perceptron.svg`
- `linear_vs_nonlinear.svg`
- `training_loop.svg`
- `dataset_split.svg`
- `ml_workflow.svg`
- `human_feature_to_cnn.svg`
- `cnn_flow.svg`
- `intro_question_apple.svg`
- `intro_human_vs_computer.svg`
- `supervised_unsupervised_industry.svg`
- `vision_tasks_comparison.svg`
- `and_xor_linear_separability.svg`
- `linear_layers_collapse.svg`
- `apple_visual_variations.svg`

## 2026-09 도표 재구성

- `docs/assets/*.svg`: 41개 도표를 1200×600 좌표계로 재구성.
- 사과 이미지: 이 프로젝트에서 AI로 생성한 교육용 이미지.
  `docs/assets/vision_task_apple_reference.jpg` (960×640).
  실사 촬영이나 실제 검사 데이터가 아님.
- 사과의 검출 박스, 분할 마스크, 0.98 점수는 설명용 예시이며 모델 추론 결과가 아님.
- RGB 숫자는 해당 JPG를 디코딩한 픽셀에서 직접 취득.
  밝기·크기·가림 변형은 SVG에서 만든 도식적 시뮬레이션.
- Noto Sans CJK KR Regular의 사용 글리프만 WOFF로 부분 집합화해 SVG에 내장.
  원본: https://github.com/notofonts/noto-cjk
  라이선스: SIL Open Font License 1.1 (`assets/NOTO_FONT_LICENSE.txt`).
- SVG를 HTML `img`로 사용할 때 외부 이미지 로딩이 제한되므로 JPG를 data URL로 내장.
  근거: https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image
- 생성: `scripts/rebuild_visuals.py --font <NotoSansCJKkr-Regular.otf>`
- 검증: `scripts/verify_visuals.py` (선택: `--render-dir <directory>`)

### 레이아웃 및 내용 검증 기준

1. 텍스트는 실제 글꼴 폭으로 줄바꿈하고 지정한 박스 높이를 초과하면 생성을 중단.
2. 사진·폰트를 포함한 도표 내부 리소스는 외부 네트워크에 의존하지 않음.
3. 합성곱: 5×5 / kernel 3×3 / stride 1 / padding 0 → 3×3 출력.
4. Batch: 10장 / batch_size 4 / drop_last=False → 4+4+2, 총 3 step.
5. 원본 이미지와 예시 annotation을 구분하고, AI 생성 이미지임을 명시.

## Intro Sensor 생성 이미지

- Intro 9 / 10의 사진형 장면은 이 프로젝트에서 AI로 생성한 교육용 이미지입니다.
- 실제 제품 사진, 실제 LiDAR scan, 실제 열화상 측정 데이터가 아닙니다.
- Intro 9 / 10은 2172 × 724 해상도의 AI 생성 원본 PNG를 Repository에 직접 저장해 사용합니다.
- 외부 이미지 서버나 runtime base64 조립에 의존하지 않고 `docs/assets/generated/*_hd.png`를 HTML에서 직접 참조합니다.
- Intro 9 비교 이미지: RGB 거리 장면 / LiDAR 실내 공간 scan / IR 전기 설비 열화상.
- 기존 Intro 10 합성 이미지는 RGB / IR 영역의 시각 예시로만 재사용하며, LiDAR 생활 예시는 별도 로봇청소기 생성 이미지를 사용합니다.

## AI 기초 참고 자료 (기존)

### WikiDocs — 딥 러닝 파이토치 교과서
https://wikidocs.net/book/2788

다음 입문 내용을 참고해 Vision AI 강의 흐름에 맞게 재구성했습니다.

- Machine Learning Workflow
- Data Splitting
- Linear Regression / Gradient Descent / Autograd
- Mini Batch / Batch Size / Epoch / Iteration
- Classification / Regression
- Supervised Learning
- Perceptron / MLP / XOR
- Backpropagation
- Overfitting

## CNN 관련 논문

### VGG
https://arxiv.org/abs/1409.1556

### ResNet
https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html

## Intro / Sensor References

### OpenCV Mat - The Basic Image Container
https://docs.opencv.org/4.10.0/d6/d6d/tutorial_mat_the_basic_image_container.html

### Intel RealSense D400 Documentation
https://dev.intelrealsense.com/docs/multiple-depth-cameras-configuration%C2%A0

### Event-based Vision: A Survey
https://arxiv.org/abs/1904.08405


## AI Basics 시각자료 개편

다음 자산은 이 프로젝트에서 초보자 강의용으로 직접 재구성한 SVG입니다.

- `docs/assets/optimizer_loss_landscape.svg`
- `docs/assets/activation_relu_boundary.svg`
- `docs/assets/backpropagation_visual.svg`
- `docs/assets/data_leakage_visual.svg`
- `docs/assets/group_split_visual.svg`
- `docs/assets/and_xor_linear_separability.svg`
- `docs/assets/rule_vs_ml.svg`
- `docs/assets/overfit_leakage.svg`
- `docs/assets/ml_workflow.svg`

개념 관계와 흐름을 전달하는 용도이므로 논문 Figure를 복제하지 않고 강의용으로 단순화했습니다.


## Intro 원근감 / LiDAR 생활 예시 생성 이미지

- `docs/assets/generated/intro_perspective_cat_generated.svg`
  - AI로 생성한 교육용 이미지의 사진 영역을 Crop해 사용.
  - Camera 가까이의 고양이가 크게, 멀리 있는 사람이 작게 보이는 원근감 예시.
  - 실제 촬영 사진이나 측정 데이터가 아님.
- `docs/assets/generated/intro_lidar_robot_vacuum_generated.svg`
  - AI로 생성한 로봇청소기 LiDAR 공간 스캔 장면.
  - 자동차 이미지는 포함하지 않으며, 로봇청소기의 공간 맵핑 예시에만 사용.
  - 실제 LiDAR Point Cloud 측정 결과가 아니라 교육용 시각화임.
- 두 SVG는 생성 이미지 WebP를 내부에 그대로 포함하며 외부 이미지 서버에 의존하지 않습니다.


## Paper-style 기본 학습 Figure

- `docs/assets/supervised_unsupervised_industry.svg`
  - Supervised / Unsupervised Learning을 Feature Space scatter plot으로 비교.
  - 지도학습은 Label과 Decision Boundary, 비지도학습은 unlabeled sample과 Cluster structure를 표현.
- `docs/assets/classification_regression.svg`
  - Classification은 discrete class와 Decision Boundary, Regression은 continuous target과 fitted function으로 표현.
- 두 Figure 모두 특정 논문의 Figure를 복제한 것이 아니라, 학술 논문에서 흔히 사용하는 축·점·경계선 중심의 시각 문법을 강의용으로 재구성한 도표입니다.


## Beginner-first AI Basics 재구성

2026-09-25 개편에서는 처음 AI를 배우는 학생이 개념을 순서대로 연결할 수 있도록 다음 교육용 SVG를 새로 만들거나 전면 재작성했습니다.

- `docs/assets/perceptron.svg`
- `docs/assets/weight_bias_intuition.svg`
- `docs/assets/and_xor_linear_separability.svg`
- `docs/assets/neural_network_layers.svg`
- `docs/assets/linear_layers_collapse.svg`
- `docs/assets/activation_relu_boundary.svg`
- `docs/assets/feature_representation.svg`
- `docs/assets/loss_intuition.svg`
- `docs/assets/gradient_intuition.svg`
- `docs/assets/optimizer_loss_landscape.svg`
- `docs/assets/training_loop.svg`
- `docs/assets/backpropagation_visual.svg`
- `docs/assets/training_inference.svg`
- `docs/assets/batch_epoch.svg`
- `docs/assets/kfold_visual.svg`

특정 논문의 Figure를 복제하지 않았으며, Neural Network / Optimization 교과서에서 일반적으로 사용하는 Node, Layer, Loss landscape, Gradient, Decision Boundary 표현을 입문 강의용으로 단순화했습니다.


## Beginner-first Vision AI 재구성

2026-09-25 개편에서는 Vision AI 입문자가 Task와 CNN 계산을 단계적으로 연결할 수 있도록 다음 교육용 SVG를 새로 만들거나 전면 재작성했습니다.

- `docs/assets/iou_visual.svg`
- `docs/assets/cnn_why_local.svg`
- `docs/assets/kernel_pattern_detector.svg`
- `docs/assets/convolution_visual.svg`
- `docs/assets/stride_padding_downsampling.svg`
- `docs/assets/feature_maps.svg`
- `docs/assets/cnn_hierarchy.svg`
- `docs/assets/cnn_training.svg`
- `docs/assets/backbone_head.svg`
- `docs/assets/transfer_learning.svg`
- `docs/assets/vision_task_selection.svg`
- `docs/assets/vision_project_pipeline.svg`

특정 논문의 Figure를 복제하지 않았으며, Computer Vision 교재와 논문에서 일반적으로 사용하는 Convolution, Kernel, Feature Map, Receptive Field, Backbone/Head 표현을 초보자 강의용으로 단순화했습니다.


## Shortcut Learning 참고

### Geirhos et al. — Shortcut Learning in Deep Neural Networks
https://www.nature.com/articles/s42256-020-00257-z

- Nature Machine Intelligence, 2020.
- 표준 평가에서는 잘 작동하지만 더 어려운 실제 조건에서 전이되지 않는 decision rule을 Shortcut 관점으로 설명합니다.
- 강의의 `docs/assets/shortcut_learning.svg`는 논문 Figure를 복제하지 않고, 배경색과 Class가 우연히 연관된 Toy Example로 개념을 재구성한 교육용 Diagram입니다.
- AI Basics에서는 Shortcut Learning과 Data Leakage의 차이를 설명하고, Vision AI에서는 높은 Score가 사람이 기대한 Feature 사용을 보장하지 않는다는 운영 관점으로 연결합니다.


## 고해상도 생성 Lecture Figure — 2026-09-27

다음 자산은 ChatGPT에서 강의 목적에 맞게 생성한 뒤, 제목 중복을 줄이기 위해 Figure 영역을 Crop하고 WebP로 저장한 교육용 이미지입니다.

- `docs/assets/generated/lecture/intro_human_vs_computer.webp`
- `docs/assets/generated/lecture/intro_perspective.webp`
- `docs/assets/generated/lecture/intro_sensor_modalities.webp`
- `docs/assets/generated/lecture/ai_perceptron.webp`
- `docs/assets/generated/lecture/ai_leakage_shortcut.webp`
- `docs/assets/generated/lecture/vision_task_selection.webp`
- `docs/assets/generated/lecture/vision_convolution.webp`
- `docs/assets/generated/lecture/vision_backbone_head.webp`
- `docs/assets/generated/lecture/vision_transfer_learning.webp`

사용 원칙:
- 실제 촬영·실측·실제 Model 추론 결과가 아니라 강의용 시각화입니다.
- 당시 생성 Convolution Figure는 전체 Feature Map 값의 오류가 확인되어 2026-10-06 개편에서 사용을 중단했습니다. 현재 계산 그림은 아래 검증된 SVG를 사용합니다.
- LiDAR Figure는 자동차 예시 없이 로봇청소기와 실내 공간 Scan 예시만 사용합니다.
- AI / Machine Learning / Deep Learning / Computer Vision의 포함관계는 생성 이미지보다 정확성이 중요한 Diagram이므로 기존 `ai_ml_dl.svg`를 유지합니다.
- Repository 내부 WebP를 직접 참조하며 외부 이미지 Host나 Runtime base64 조립에 의존하지 않습니다.

## 기본 그림 + 상세 Figure 개편 — 2026-10-06

- `docs/assets/lesson/`: AI Basics와 Vision AI에서 실제 사용하는 그림.
- `docs/assets/lesson/manifest.json`: 슬라이드 번호·개념·설명 수준·자산 경로.
- 쉬운 기본 그림 뒤에 계산 그래프, 수식, Tensor 크기, 공간 연산 조건을 담은 상세 Figure를 배치.
- 특정 논문 Figure를 복제하지 않고 직접 작성한 SVG. 색은 기본 설명과 상세 설명에서 동일하게 사용.
- 사과 사진은 기존 AI 생성 교육용 이미지. Box·Mask·점수는 실제 모델 출력이 아닌 설명용 예시.
- AND 경계 `x1+x2=1.5`, XOR의 두 경계, Gradient 방향, 합성곱 전체 출력, RGB 전체 필터 합산을 교정.
- 5×5 합성곱 예시의 출력: `[[-6,12,16],[-6,8,15],[-4,2,7]]`.
- RGB 입력 224×224×3, 필터 64개, Kernel 3×3, Stride 1, Padding 1 → 224×224×64.
- Backbone의 고양이/컵 생성 그림 대신 동일한 사과 사진과 결함 annotation을 사용.
- `vision_convolution.webp`, `vision_backbone_head.webp`는 배포 슬라이드에서 사용하지 않음.
- 기존 SVG의 중복 제목을 제거한 context 자산은 원본에서 파생. 데이터는 그림 안에 포함하고 외부 요청을 사용하지 않음.

### 근거 자료

- Stanford CS231n, Optimization: https://cs231n.github.io/optimization-1/
  - Loss의 Gradient와 반대 방향으로 Parameter를 갱신하는 경사하강법.
- Stanford CS231n, Backpropagation: https://cs231n.github.io/optimization-2/
  - 계산 그래프에서 Chain Rule로 Gradient를 역방향 계산.
- Stanford CS231n, Neural Networks: https://cs231n.github.io/neural-networks-1/
  - Layer, 비선형 Activation, ReLU와 표현력.
- Stanford CS231n, CNN: https://cs231n.github.io/convolutional-networks/
  - Local connectivity, Weight sharing, 공간 출력 크기, Feature Map.
- PyTorch Conv2d: https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html
  - Cross-correlation, Channel 합산, Weight shape와 Stride/Padding 조건.
- PyTorch Transfer Learning: https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
  - 고정된 특징 추출기와 Fine-tuning의 구분.
- scikit-learn Model Selection: https://scikit-learn.org/stable/modules/cross_validation.html
  - Train/Test 분리, 교차검증, Group 단위 검증.
- scikit-learn Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html
  - Confusion Matrix, Accuracy, Precision, Recall, F1.

### 생성과 검증

- 생성: `python scripts/build_lesson_revision.py`
- 검증: `python scripts/verify_lesson_revision.py`
- HTML 슬라이드 수·연속 번호·자산 경로, SVG XML·내부 리소스 참조, 합성곱·Gradient·AND·IoU·평가지표 수치 검증.
- 두 챕터 전용 `docs/lesson.css`로 레이아웃 적용. Intro의 공통 CSS/JS는 변경하지 않음.

## 2026-10-06 전문 강의용 사진 자산

- ChatGPT Image Generation으로 생성한 사과·오렌지 사진형 자산과 촬영 조건 비교 이미지: `docs/assets/generated/`. 교육용 합성 이미지이며 실제 관측 데이터나 모델 실험 결과가 아닙니다. 상세 용도와 생성 명세는 해당 폴더 `README.md`에 기록했습니다.
- 사진 파일을 기반으로 지도/비지도학습, 신경망 입력, Dataset 촬영 조건, 계층적 Feature, Shortcut Learning 그림을 재구성했습니다. 수식·텐서·계산값은 기존 검증 가능한 SVG 방식으로 유지했습니다.

## Loss / Gradient / Optimizer 재구성 (2026-10-06)

- 개념 출처: Stanford CS231n Optimization — https://cs231n.github.io/optimization-1/ . Loss를 줄이는 가중치 탐색, Gradient와 경사하강법 설명을 참고했습니다.
- 모든 숫자·곡선은 `scripts/build_loss_optimizer_figures.py`에서 직접 계산한 단일 샘플 회귀 예시입니다. x=2, y=4, b=0, 초기 w=1; L(w)=(2w−4)²; Gradient=8w−16. 실제 학습 실험 결과나 모델 Benchmark가 아닙니다.
- Optimizer는 기본 SGD로 고정하고 학습률 0.025/0.1/0.3만 비교합니다. 업데이트 t=0~3을 표시하며, 증가 예시의 세로축은 0~34로 별도 표기합니다. Momentum·Weight Decay는 사용하지 않습니다.
- SVG는 NumPy/Matplotlib로 생성하며 글꼴 윤곽을 포함합니다. 재생성 환경에는 Noto Sans CJK KR 글꼴이 필요합니다. 예측값을 비교하는 Loss 그림과 가중치를 비교하는 Loss 곡선의 가로축을 구분합니다.

## Alzubaidi et al. (2021) 기반 보강

- Alzubaidi et al., Review of deep learning: concepts, CNN architectures, challenges, applications, future directions, Journal of Big Data 8, 53 (2021). https://doi.org/10.1186/s40537-021-00444-8
- Fig. 3의 특징 설계/학습 비교, Fig. 7의 CNN 흐름, CNN architectures의 연결 원리, Fig. 20의 Residual 연결, Loss·Regularization·Imbalanced data 절을 강의 흐름에 맞춰 재구성했습니다. 원본 Figure를 복제하지 않았습니다. `survey_*.svg`는 직접 작성한 도표이며 성능 측정 결과가 아닙니다.
- 자동 특징 학습: LeCun, Bengio & Hinton, Deep learning (2015). https://www.nature.com/articles/nature14539
- VGG: Simonyan & Zisserman. https://arxiv.org/abs/1409.1556
- Inception: Szegedy et al. https://openaccess.thecvf.com/content_cvpr_2015/html/Szegedy_Going_Deeper_With_2015_CVPR_paper.html
- ResNet: He et al. https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html
- Dropout: Srivastava et al. https://jmlr.org/papers/v15/srivastava14a.html
- Dropout의 매 Forward 샘플링 및 추론 동작: https://docs.pytorch.org/docs/stable/generated/torch.nn.Dropout.html
- CE와 클래스 가중치: https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html
- Conv Shape: https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html
- 정규화 및 Early Stopping: https://cs231n.github.io/neural-networks-2/
- 비교 그림의 사과는 기존 `apple_studio_preview.png` 생성 사진을 재사용했습니다. CE는 정답을 고정한 단일 샘플 L=−ln(p)의 직접 계산이며, CNN Shape와 Residual 숫자도 설명용 예시입니다.
- 생성: `scripts/build_survey_figures.py` 또는 전체 `scripts/build_lesson_revision.py`. 논문과 슬라이드의 대응·주의점은 `lectures/PAPER_REVIEW_2021.md`에 기록했습니다.

## Szeliski 3장 Image Processing 기반 보강 (2026-10-06)

- Richard Szeliski, Computer Vision: Algorithms and Applications, 1판, 3장.
  저자 공식 안내: https://szeliski.org/Book/1stEdition.htm
- Brown 강의용 3장 PDF: https://mesh.brown.edu/engn1610/szeliski/03-ImageProcessing.pdf
  이 주소의 응답 실패로 2010-09-03 교재 초안 본문을 대조했습니다.
  대학 미러: https://www.cs.ccu.edu.tw/~damon/tmp/SzeliskiBook_20100903_draft.pdf
- `processing_*.svg` 7종은 원문 Figure를 복제한 그림이 아닙니다. 기존 AI 생성 사과
  사진과 합성 잡음·이진 Mask를 실제로 필터링한 결과 및 직접 작성한 계산 도표입니다.
- Pixel/이웃 연산(3.1–3.2), Gaussian·Sobel(3.2), 중앙값(3.3.1),
  형태학(3.3.2), 축소·다중 해상도(3.5.2–3.5.3)를 강의용으로 재구성했습니다.
- OpenCV 공식 설명으로 대조: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
  https://docs.opencv.org/4.x/d5/d0f/tutorial_py_gradients.html
  https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
  https://docs.opencv.org/4.x/d4/d1f/tutorial_pyramids.html
- 생성: `scripts/build_image_processing_figures.py` (NumPy/Pillow/SciPy).
  출처·계산 조건·현재 페이지: `lectures/SZELISKI_IMAGE_PROCESSING_REVIEW.md`.

## Intro 3 흑백 사진과 밝기 행렬 (2026-10-07)

- 기존 사과 사진을 재사용: Intro 2의 vision_task_apple_reference.jpg와 같은 사진이 포함된 docs/assets/task_classification.svg에서 읽습니다.
- Pillow로 Grayscale L(8-bit 1채널)로 변환하고 BOX 평균으로 12열×8행에 축소합니다. 중간 Pixel 영상과 오른쪽 숫자 행렬은 같은 96개 값을 사용합니다.
- 초록 테두리는 4행 6열(1부터 세는 위치), 밝기 97을 세 패널에서 연결합니다. 원본 사진의 테두리는 축소 Pixel에 대응하는 영역입니다.
- 사진 패널은 표시용 JPEG로 압축합니다. 숫자는 압축 전 원본에서 축소한 실제 8-bit 값입니다.
- 생성: scripts/build_intro_grayscale.py. 자산: docs/assets/intro_grayscale_values.svg. 외부 Figure를 복제하지 않습니다.

### Intro 3 해상도·순서 수정 (2026-10-07)

- 가로·세로를 각각 4배 늘려 48열×32행, 총 1,536개 값을 표시합니다.
- 사진 → 흰 배경의 동일한 색 숫자 → Pixel별 밝기 영상 순서입니다. 중앙 숫자 행렬과 오른쪽 영상은 432×288의 같은 화면 크기이며 동일한 배열을 사용합니다.
- 이전 4행 6열 강조는 제거했습니다. 숫자 영역에는 값에 따른 배경색·글자색·굵기 차이가 없습니다. 오른쪽 영상은 무손실 PNG와 최근접 표시를 사용합니다.
- 이전 12×8 설명은 앞선 수정 기록입니다. 현재 입력은 32×48×1입니다. 개별 숫자는 그림을 선택해 원본 SVG를 확대하여 확인할 수 있습니다.

### Intro 3 동일한 크기와 숫자 밝기 그림 (2026-10-11)

- 세 패널 모두 360×240이며 상단과 하단을 정렬했습니다. 원본 사진의 3:2 비율을 유지합니다.
- 중앙은 흰 배경에 검정 숫자 1,536개입니다. 오른쪽도 같은 48열×32행 숫자로만 구성합니다.
- 오른쪽의 각 값 v는 글자색 RGB(v,v,v)로 표시합니다. 배경은 흰색이며 셀 채움이나 사진/Pixel PNG를 겹치지 않습니다. 수치는 그대로이고 글자색만 바뀝니다.
- 이전 PNG 밝기 영상 구현은 교체되었습니다. 0은 검정, 255는 흰색 글자입니다. 높은 값의 글자는 흰 배경에 가까워 옅게 보입니다.
- 실제 사진에서 계산한 밝기 값의 시각화이며 모델 실험 결과가 아닙니다. 확대 링크로 각 숫자를 확인할 수 있습니다.


## Pixel·Noise·Spatial Filtering 신규 도식 (2026-10-13)

- 참고 강의: Brown University CSCI1430, *Image Filtering* (2020) — https://cs.brown.edu/courses/csci1430/2020_Spring/lectures/2020Spring_02_ImageFiltering.pdf. 제공 PDF의 원문 페이지는 이번 작업에서 직접 열람·대조하지 못했으며, 수업 주제와 학습 흐름의 참고 자료입니다.
- 계산/개념 확인: OpenCV Filtering https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html · OpenCV Gradients https://docs.opencv.org/4.x/d5/d0f/tutorial_py_gradients.html
- 신규 SVG: `lecture_rgb_channel_stack.svg`, `lecture_2d_brightness_surface.svg`, `lecture_noise_outlier.svg`, `lecture_point_neighborhood.svg`, `lecture_kernel_slide.svg`, `lecture_mean_calculation.svg`, `lecture_filter_comparison.svg`, `lecture_sobel_concept.svg`.
- 수치 예시는 실제 관측값이 아니라 강의용 합성값입니다. 동일 3×3 배열의 합은 1053이고 Mean = 117, Gaussian = 2219/16 ≈ 138.69, Median = 100입니다.
- 2D 밝기 높이 그래프는 영상의 Pixel 밝기값을 세로축으로 표시한 개념도이며, 단안 카메라에서 측정된 깊이 맵이 아닙니다.
- 이전에 생성된 이미지 인포그래픽은 위치·숫자 대응을 보장하기 어려워 실제 교재에는 검증 가능한 독립 SVG 도식을 사용합니다. 그림은 Brown 원본 Figure를 복제하지 않았습니다.


## 2026-10-13 전체 강의 개편 이미지 계보

- `docs/assets/intro_grayscale_crop_6x6.svg`: 기존 `intro_grayscale_values.svg`의 48×32 밝기 배열에서 6×6 구간(행 10–15, 열 16–21, 0부터)을 추출해 동일 JPG의 위치 표시와 함께 재구성했습니다.
- `docs/assets/lesson/task_labels_three_outputs.svg`: 기존 `context_task_classification.svg`에 임베드된 강의용 사과 사진을 재사용하고 Class·Bounding Box·Pixel Mask의 세 라벨 형태를 직접 그렸습니다. Box/Mask는 개념적 오버레이이고 실제 수동 정밀 라벨이나 모델 출력이 아닙니다.
- `docs/assets/lesson/lecture_filter_to_cnn_bridge.svg`: 동일한 사과 사진과 고정 평균 커널(1/9)·학습 커널(w1..w9) 비교를 새로 구성했습니다. 학습 커널에는 실제 모델 Weight를 표기하지 않았습니다.
- 커널 이동은 동일한 5×5 배열에서 왼쪽 상단 ROI를 오른쪽으로 3번 옮긴 합 1045·1053·1055와 평균값 약 116.11·117·117.22를 표시합니다.
- 저장소에 있는 원본 필터 연산 Figure와 수치·라벨 Figure는 별개 예시이므로 임의의 학습/측정 결과로 설명하지 않습니다.


## 2026-10-13 추가 AI Basics 시각 교재

- `docs/assets/lesson/lesson_sgd_update_flow.svg`: 기존 x=2, y=4, w=1, b=0 고정 예시의 SGD 1회 갱신을 전/후 파이프라인으로 재구성. η=0.1, gradient=-8, w'=1.8, ŷ'=3.6, L'=0.16. 직접 작성한 벡터 도식이며 실제 모델 학습 성능 결과가 아님.
- `docs/assets/lesson/lesson_chain_rule_graph.svg`: 동일 x=2, y=4 예제에 학습 가능한 Bias를 추가. 초기 w=1,b=0, L=4. Chain Rule을 통해 dL/dŷ=-4, dL/dw=-8, dL/db=-4, SGD η=0.1 후 w'=1.8,b'=0.4 및 L'=0. 실제 계산을 표현한 교육용 SVG.
- 참고 개념: https://cs231n.github.io/optimization-1/ 와 https://cs231n.github.io/ (Stanford CS231n). 도식 구조와 수치는 독자적으로 설계·계산함.


## 2026-10-13 성능 평가 및 Transfer Learning 추가 Figure

- 성능 평가 4개 SVG (`lesson_threshold_score_decision.svg`, `lesson_confusion_100cases.svg`, `lesson_precision_recall_sharedcase.svg`, `lesson_accuracy_f1_same100.svg`): 사용자가 기존 강의에 제공한 합성 결과 TP 18/FN 2/FP 4/TN 76, 총 100건을 수치 변경 없이 직접 재시각화했습니다. Threshold의 0.82 사례는 독립적인 단일 예시입니다.
- 모델 구조 2개 SVG (`lesson_backbone_head_roles.svg`, `lesson_backbone_tensor_head_options.svg`): Backbone과 Classification/Detection/Segmentation Head를 비교하는 새 블록 다이어그램. 기본 구성도에 포함한 사과 사진은 동일 저장소의 `docs/assets/lesson/backbone_basic.svg` 내 강의용 사진을 재사용했습니다. 학습된 실제 Backbone의 특징을 측정한 시각화가 아닙니다.
- Transfer Learning 2개 SVG (`lesson_transfer_pretraining_to_task.svg`, `lesson_transfer_freeze_vs_finetune.svg`): Weight 재사용, 고정 및 갱신 경로를 직접 그린 설명용 개념도입니다. 특정 모델을 실제로 Fine-tuning한 성능 결과가 아닙니다.
- 구조 참고자료: [Stanford CS231n CNN](https://cs231n.github.io/convolutional-networks/) · [PyTorch Transfer Learning Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html). 링크는 개념적 참고이며, 원문의 Figure를 복제하지 않았습니다.
- 계산 검증: `scripts/verify_curriculum_overhaul.py`에서 동일한 100건의 Precision/Recall/Accuracy/F1과 Shape·Threshold 예시를 점검합니다.


## Intro 실제 사진 및 외부 교육 Figure (2026-10-14)

상세 변형 및 라이선스: [출처 페이지](../docs/assets/intro_photos/SOURCES.html).

- apple: Abhijit Tembhekar · CC BY 2.0 — https://commons.wikimedia.org/wiki/File:Red_Apple.jpg
- perspective: Livioandronico2013 · CC BY-SA 4.0 — https://commons.wikimedia.org/wiki/File:Forced_perspective_gallery_by_Francesco_Borromini.jpg
- lidar: Rebecca equator · CC BY-SA 4.0 — https://commons.wikimedia.org/wiki/File:Austin_Texas_LiDAR_Point_Cloud_(Highway_183).png
- robot: S. Winkvist · Public domain — https://commons.wikimedia.org/wiki/File:LIDAR_equipped_mobile_robot.jpg
- cctv: Neslihan Turan · CC0 — https://commons.wikimedia.org/wiki/File:Surveillance_camera.jpg
- thermal: MartinThoma · CC0 — https://commons.wikimedia.org/wiki/File:Thermal-image.jpg
- pcp: Meinard Müller / AudioLabs · PCP Unit 5 · MIT — https://www.audiolabs-erlangen.de/resources/MIR/PCP/PCP_05_vis.html

사진은 축소·WebP 변환. CC BY-SA 변환본은 동일 라이선스. PCP Figure는 MIT (동봉 원문 참조), 2D 패널만 크롭. 8/10/11 변형은 교육용이며 실제 재촬영/모델 예측이 아님.


## 2026-10-16 · CNN / YOLO 공개 논문 Figure 인용

공개 통합 강의의 CNN 구조 및 YOLO 구조 설명은 검증된 외부 학술 Figure 원본을 인용합니다. 두 Figure 모두 그대로 표시하며 크기만 반응형으로 조정합니다.

- **CNN 기본 구조 / Forward & Backpropagation**: Yamashita, Nishio, Do, et al., *Convolutional neural networks: an overview and application in radiology*, *Insights into Imaging* 9, 611–629 (2018), **Fig. 1**. 원문: https://doi.org/10.1007/s13244-018-0639-9 ; 이미지: https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs13244-018-0639-9/MediaObjects/13244_2018_639_Fig1_HTML.png ; 라이선스: https://creativecommons.org/licenses/by/4.0/ (CC BY 4.0). 일반적인 분류 CNN Figure로, YOLO 모델의 실제 Detection Head라고 주장하지 않습니다.
- **YOLOv8 Backbone / Neck / Head**: *Enhancing YOLOv8’s Performance in Complex Traffic Scenarios: Optimization Design for Handling Long-Distance Dependencies and Complex Feature Relationships*, *Electronics* 13(22), 4411 (2024), **Fig. 1**. 원문: https://doi.org/10.3390/electronics13224411 ; 이미지: https://www.mdpi.com/electronics/electronics-13-04411/article_deploy/html/images/electronics-13-04411-g001.png ; 라이선스: https://creativecommons.org/licenses/by/4.0/ (CC BY 4.0). 해당 그림은 YOLOv8 예시이며 모든 YOLO 버전의 세부 구조가 동일하다는 뜻이 아닙니다.
- 강의 화면의 외부 학술 Figure는 기관 네트워크에서 차단될 수 있으므로 이미지 로드 실패 시 원래 Repository에 있는 로컬 개념 SVG로 대체합니다. 출처 링크와 학술 자료 인용은 남습니다. 외부 Figure 로컬 영구 보관은 현재 수행하지 않았습니다.


## 2026-10-16 · Dragon1 기반 CNN 기본 구조 설명

- CNN 교육 흐름 참고: [Dragon1 — Convolutional Neural Networks Definition](https://www.dragon1.com/terms/convolutional-neural-networks-definition), 2026-10-16 확인. Input → Convolution → ReLU → Pooling → Flatten/Fully Connected → Output 순서로 전형적인 **분류 CNN**을 설명합니다.
- 논문 Figure 출처는 기존 Yamashita et al. (2018), *Insights into Imaging*, Fig. 1(CC BY 4.0)을 유지합니다. Dragon1 원본 이미지는 파일·재사용 권한이 확인되지 않아 복제하지 않았으며, 기사에 따라 단계 이름과 별도의 한국어 해설을 작성했습니다.
- 위 순서는 일반적인 CNN 분류 예시이며 실제 모델의 블록과 순서는 다를 수 있습니다. 특히 YOLO 검출 Head를 Flatten/FC 분류기와 동일시하지 않습니다.


## 2026-10-16 · CNN 구조 로컬 SVG로 완전 교체 (현재 공개 슬라이드)

- 파일: `docs/assets/lesson/cnn_dragon1_lecture.svg`. GitHub Pages의 통합 강의 16번 CNN 구조 슬라이드에서 직접 로딩합니다. 외부 이미지 서버 또는 CDN에 의존하지 않습니다.
- 개념·구조 참고: [Dragon1 — Convolutional Neural Networks Definition](https://www.dragon1.com/terms/convolutional-neural-networks-definition), Input → Convolution → ReLU → Pooling → Flatten / Fully Connected → Output.
- **직접 제작한 강의용 그림**입니다. Dragon1의 원본 이미지를 복제한 것이 아니라 입력 사과, Kernel/Feature Map, ReLU 변환, Pooling, Dense, 클래스 출력을 같은 순서로 다시 시각화했습니다.
- ReLU 예시에서는 음수를 0으로 변환하고 양수를 유지합니다. Max Pooling 예시는 `[[1,4],[3,7]] → 7`, 전체 출력 `[[7,6],[8,9]]`; 분류 점수 `92% + 5% + 3% = 100%`는 **임의의 교육용 값**이며 실제 모델 추론 결과가 아닙니다.
- 원문 Yamashita et al. Figure는 과거 강의 버전의 기록으로 보존하지만, 현재 16번 슬라이드는 **오직 로컬 SVG**만 로드합니다. Flatten / FC는 대표적인 분류 CNN의 예시이며 YOLO 검출 Head를 뜻하지 않습니다.


## 2026-10-16 · CNN 원본 얼룩말 Figure / YOLO 분류·박스 학습 출처
- CNN Figure: Swapna K E, Convolutional Neural Network | Deep Learning, Developers Breach (2020). 원문 https://developersbreach.com/convolution-neural-network-deep-learning/ ; 원본 Figure URL https://i0.wp.com/developersbreach.com/wp-content/uploads/2020/08/cnn_banner.png?fit=1200%2C564&ssl=1 . 그림 그대로 표시(외부 네트워크 접근 필요).
- YOLO Detect: https://docs.ultralytics.com/ko/tasks/detect ; Class와 Bounding Box 예측/학습. YOLO Classify: https://docs.ultralytics.com/tasks/classify ; 이미지 전체의 단일 클래스 예측과 학습.
- 자체 제작 한글 그림: docs/assets/lesson/yolo_class_box_training_ko.svg. 모델이 Class와 Box를 함께 학습한다는 개념 표현이며 실제 학습 결과 또는 YOLO 추론 출력은 아닙니다.



## 2026-10-16 · 논문·공식 자료 원본 Figure 시범 적용: Vision AI 10, 11, 25, 51

- **Vision 10 · OpenCV Smoothing Images**: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html ; Mean: https://docs.opencv.org/4.13.0/blur.jpg ; Gaussian: https://docs.opencv.org/4.13.0/gaussian.jpg ; Median: https://docs.opencv.org/4.13.0/median.jpg . **Median 예제는 원본에 점 잡음이 포함되고 Mean/Gaussian 예제와 입력 조건이 다름**. 원본을 그대로 인용하며 수치 비교는 기존 별도 3×3 Figure를 참조합니다.
- **Vision 11 · OpenCV Sobel Derivatives** (Ana Huamán): https://docs.opencv.org/4.x/d2/d2c/tutorial_sobel_derivatives.html ; Photo: https://docs.opencv.org/4.13.0/Sobel_Derivatives_Tutorial_Theory_0.jpg ; Intensity curve: https://docs.opencv.org/4.13.0/Sobel_Derivatives_Tutorial_Theory_Intensity_Function.jpg ; derivative curve: https://docs.opencv.org/4.13.0/Sobel_Derivatives_Tutorial_Theory_dIntensity_Function.jpg . 곡선은 경계 원리 설명용으로 원문에 수록된 것이며 이미지 전체에서 실제 측정한 결과는 아닙니다.
- **Vision 25 · Distill Feature Visualization**: Chris Olah, Alexander Mordvintsev, Ludwig Schubert (2017), https://distill.pub/2017/feature-visualization/ ; mixed4a Unit 97 optimized: https://distill.pub/2017/feature-visualization/images/diversity/mixed4a_97_optimized.png ; dataset: https://distill.pub/2017/feature-visualization/images/diversity/mixed4a_97_examples.jpg ; mixed5a Unit 9 optimized: https://distill.pub/2017/feature-visualization/images/diversity/mixed5a_9_optimized.png ; dataset: https://distill.pub/2017/feature-visualization/images/diversity/mixed5a_9_examples.jpg . 최적화 특징 이미지와 실제 강한 활성의 이미지 사례를 구분하고, Layer가 깊어짐에 따라 복합 패턴이 나타나는 한 가지 연구 사례로 소개합니다.
- **Vision 51 · Grad-CAM 비교**: Selvaraju et al., *Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization*, ICCV 2017, https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html ; 구현 및 원본 이미지: https://github.com/jacobgil/pytorch-grad-cam#classification ; input: https://raw.githubusercontent.com/jacobgil/pytorch-grad-cam/master/examples/dog_cat.jfif ; dog: https://raw.githubusercontent.com/jacobgil/pytorch-grad-cam/master/examples/resnet50_dog_gradcam_cam.jpg ; cat: https://raw.githubusercontent.com/jacobgil/pytorch-grad-cam/master/examples/resnet50_cat_gradcam_cam.jpg . 두 Heatmap은 **개/고양이 클래스에 각각 대응**하는 실제 Grad-CAM Classification 예제이며 별도의 Box/Masks나 설비 결함 탐지 결과가 아닙니다.
- 원본 자료를 **직접 URL로 표시**하고 사용된 원본 URL을 함께 연결합니다. 별도 다운로드/편집/재호스팅하지 않았습니다. 오프라인/사내망에서는 원래 로컬 Figure를 fallback으로 사용합니다.


## 2026-10-16 · Vision AI 25번: 얕은층 → 중간층 → 깊은층

- **교육용 Figure**: `docs/assets/lesson/cnn_three_stage_apple_ko.svg` (직접 제작한 SVG, 원본 사과 사진 재사용). 출처 사진은 기존 `docs/assets/lesson/lesson_cnn_feature_hierarchy.svg`에 이미 포함된 사과 사진입니다.
- **정확성**: 얕은층 경계 강조는 고정된 3×3 Laplacian 연산의 예시이며 특정 CNN의 실제 Kernel 또는 학습된 Feature Map이 아닙니다. 중간층의 곡선/껍질 무늬 강조선, 깊은층의 사과 형태 실루엣도 학습된 모델에서 실측한 시각화가 아니라 부분 특징과 복합 특징의 관계를 설명하기 위한 도식입니다.
- **설명 근거**: Stanford CS231n, *Convolutional Neural Networks*, https://cs231n.github.io/convolutional-networks/ (초기 Layer는 Edge/Color Blob, 깊은 Layer는 점차 복합적 Feature). Olah, Mordvintsev & Schubert, *Feature Visualization*, Distill (2017), https://distill.pub/2017/feature-visualization/ , DOI 10.23915/distill.00007. 본 수업 Figure에는 Distill 논문의 연구 시각화를 그대로 복사하지 않았습니다.
- 수업 메시지: 얕은층(경계·밝기) → 중간층(곡선·질감·부분 형태) → 깊은층(앞 특징의 복합 조합). 깊은층이 원본 전체 사진을 그대로 보거나 모든 뉴런이 하나의 명확한 의미를 학습하는 것은 아닙니다.


## 2026-10-16 · Vision 25: Stanford CS231n 원본 VGG-16 특징 시각화

- 원본 무수정 파일: `docs/assets/lesson/cs231n_vgg16_feature_hierarchy_original.png`. 저장한 PNG는 미러 원본과 Git Blob SHA `bb2d7a7033c7139bc68cd5fe619eba7b58ea71f3`이 동일하며, 외부 CDN 없이 수업에 표시됩니다.
- 강의 원문: Stanford CS231n, Fei-Fei Li · Justin Johnson · Serena Yeung, Lecture 5: Convolutional Neural Networks (2017), Slide 37, https://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture5.pdf .
- Figure 원 크레딧: Visualization of VGG-16 by Lane McIntosh. 관련 논문: Zeiler and Fergus, Visualizing and Understanding Convolutional Networks, ECCV 2014, https://cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf . VGG-16 아키텍처는 Simonyan and Zisserman (2014)을 인용한 CS231n 자료입니다.
- 동일 원본 PNG 미러: https://github.com/yganalyst/yganalyst.github.io/blob/master/assets/images/cs231n/4/convlayer_4.png .
- 주의: Conv1_1 · Conv3_2 · Conv5_3 그림은 강아지 한 장이 픽셀 단위로 층별 변환된 결과가 아니라, 각 층에서 학습된 특징을 시각화한 것입니다. 현재 25번 설명에는 이 차이를 명확히 적었습니다.
- 이전 자체 제작 사과 도식 `cnn_three_stage_apple_ko.svg`는 보존하지만 현재 25번 본문에서는 사용하지 않습니다.


## 2026-10-16 · Vision AI 25 실제 활성화 지도와 26 연구 시각화 구분

- **Vision 25 (실제 Activation)**: `docs/assets/lesson/cnn_squeezenet_actual_feature_maps.png`은 `scripts/render_cnn_feature_maps.py`에서 학습된 CNN으로 직접 계산한 실제 데이터입니다. 입력: CS231n Lecture5 Slide37 원본 Figure (`cs231n_vgg16_feature_hierarchy_original.png`)의 좌측 강아지 사진을 Cropping/Resize(224×224), ImageNet 정규화. Model: `torchvision.models.squeezenet1_1(weights=SqueezeNet1_1_Weights.IMAGENET1K_V1).eval()`, 실제 중간 Activation 추출: `features[1]` (111×111×64), `features[7]` (27×27×256), `features[12]` (13×13×512). 각 단계 4개 채널을 변화량 기준으로 선택했고 시각화 대비는 각 채널별 2–99 분위수 정규화하므로 **채널 간 절대값 비교는 불가**합니다. 재현 실행 환경: GitHub Actions `.github/workflows/generate-real-feature-maps.yml` (CPU PyTorch/torchvision + Noto CJK). 모델 문서: https://pytorch.org/vision/stable/models/generated/torchvision.models.squeezenet1_1.html
- **Vision 26 (Feature Visualization)**: 원본 CS231n 강의 Figure인 VGG-16 Conv1_1/Conv3_2/Conv5_3의 학습 특징 시각화. 원본: https://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture5.pdf . 이 이미지는 **Vision 25의 SqueezeNet Feature Map을 가공한 것이 아니며**, 동일 네트워크의 동일 입력 단계별 이미지 변화로 해석하지 않습니다.
- 핵심 수업 메시지: Feature Map은 입력 사진에서 각 채널의 공간 위치별 출력 값, Feature Visualization은 학습된 특정 Feature를 강하게 활성화하는 패턴을 보여 주는 별도의 분석입니다.

## 2026-10-16 · 실제 이미지 연산 기반 추가 Figure 5장 (Vision 22·23·24·43·44)

- **원본 실사 입력**: Stanford CS231n 2017 Lecture5 Slide37에서 이미 로컬 저장한 원본 강아지 사진을 Cropping/Resize해 사용했습니다. 출처 https://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture5.pdf . 사용 파일 `docs/assets/lesson/cs231n_vgg16_feature_hierarchy_original.png`.
- **재현 가능한 계산 코드**: `scripts/render_real_vision_examples.py` (Python NumPy + Pillow). `docs/assets/lesson/cnn_real_stride_dog.png`: 실제 Gray(224×224) 영상에서 3×3 Sobel Kernel, Padding 0, Stride 1→222×222, Stride 2→111×111; 비교할 때 반응 크기에 같은 값 범위를 적용합니다.
- `cnn_real_padding_dog.png`: 같은 Gray 입력에 3×3 Sobel / Stride1 사용; Padding0→222×222, Padding1→224×224. Padding1은 경계에 실제 0 값을 넣고 계산합니다.
- `cnn_real_maxpool_dog.png`: RGB 사진의 실제 Gray 값에 2×2 Max Pooling을 수행해 224×224→112×112→56×56. **CNN 내부 학습된 Feature Map 출력이라고 주장하지 않습니다.**
- `cnn_real_preprocess_dog.png`: 원본에서 실제 3:2 비율로 사진을 Crop한 뒤, 강제 320×320 Resize와 비율을 보존한 320×320 Letterbox (회색 Padding)을 직접 생성했습니다. 잘못된 가로세로 비율을 입력이라고 표기하지 않습니다.
- `cnn_real_augment_dog.png`: 같은 강아지 사진에 밝기 감소 0.58배, 실제 13도 회전, 부분 가림을 적용했습니다. 이미지 전체 Class는 유지되지만 검출 Box·Segmentation Mask에 기하학적 변화를 적용하면 Label도 함께 수정해야 합니다.
- 전제: 이미지 계산 모두 **고정 이미지 처리 연산**이며 사전학습 CNN 활성화 지도와는 다릅니다. 실제 사전학습 CNN의 Layer Feature Map은 별도 Vision 25번을 참고합니다. 원본 5장 도식은 그림 아래의 펼침 영역에 보존했습니다.
- 방법론 출처: OpenCV 공식 Filtering https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html ; Dive into Deep Learning CNN https://d2l.ai/chapter_convolutional-neural-networks/index.html ; PyTorch/Torchvision transforms https://docs.pytorch.org/vision/stable/transforms.html . 각 슬라이드 하단에 사진 출처와 재현 코드를 연결했습니다.
