# Slidev 장별 참고자료와 그림 출처

슬라이드 발표자 노트에 적용한 원문과 해설을 기록했습니다. 다음 목록은 참고한 개념을 찾는 색인입니다. 표지와 소개 문구는 기존 강의에서 가져왔습니다. 대학 강의나 논문의 그림 원본을 새 덱에 복제하지 않았습니다.

- 사과 사진 두 장은 본 저장소의 교육용 생성 자산입니다. P01의 타원과 P14/P40의 박스 및 마스크는 직접 그린 설명용 주석입니다. P08의 동영상 프레임은 사진 한 장을 옮겨 보여 주는 시뮬레이션입니다. [기존 이미지 기록](../assets/SOURCES.md)
- P35는 저장소의 사과 사진을 실제 ImageNet 사전학습 SqueezeNet1.1에서 추론했습니다. 가중치 URL, 원본 해시, 전처리 및 출력 층·채널은 [계산 기록](figures/apple-feature-maps.json)에 기록했습니다. 이미지 실행 결과는 [재현 스크립트](scripts/render_feature_maps.py)로 다시 만들 수 있습니다.
- P20은 가상의 소형 구조, P28~34는 직접 검산하는 작은 행렬, P41~42는 1변수 회귀, P48~51은 교육용 100건입니다. 각 숫자를 만든 전제는 [강의 운영안](../TWO_HOUR_LECTURE_PLAN.md)과 [계산 코드](lesson/calculations.js)에서 확인할 수 있습니다.
- 로컬 한글 글꼴은 [Noto Sans KR Variable의 OFL-1.1 배포본](https://github.com/fontsource/fontsource/tree/main/fonts/variable/noto-sans-kr)을 사용합니다.

| 번호 | Concept | 제목 | 참고한 원문 |
| --- | --- | --- | --- |
| P01 | `start` | Vision AI란 무엇인가? | [MIT 6.S191, Lecture 3 Deep Computer Vision](https://introtodeeplearning.com/#schedule) · [University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위](https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf) |
| P02 | `ai-ml-dl-cv` | AI·ML·DL과 Computer Vision의 관계 | [MIT 6.S191, Lecture 1 Intro to Deep Learning](https://introtodeeplearning.com/#schedule) · [MIT 6.S191, Lecture 3 Deep Computer Vision](https://introtodeeplearning.com/#schedule) |
| P03 | `vision-value` | Vision AI가 필요한 이유 | [University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위](https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf) · [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) |
| P04 | `photo-numbers` | 사람의 의미 인식 vs Pixel 숫자 | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) |
| P05 | `gray` | 흑백 사진은 H × W 숫자 배열 | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) |
| P06 | `rgb` | RGB · Pixel당 세 숫자 | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) |
| P07 | `hwc` | RGB 이미지 전체는 H × W × 3 | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) · [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) |
| P08 | `video-frames` | 동영상은 시간순 RGB 이미지 여러 장 | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) |
| P09 | `resolution` | 해상도가 낮으면 작은 결함도 사라질까? | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) |
| P10 | `lighting` | 조명이 달라지면 Pixel 숫자도 변한다 | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) · [Geirhos 외, Shortcut learning in deep neural networks](https://www.nature.com/articles/s42256-020-00257-z) |
| P11 | `transform` | 회전·크롭·가림·흐림은 무엇을 바꿀까? | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) |
| P12 | `diversity` | 다르게 생겨도 같은 종류 | [Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리](https://link.springer.com/book/10.1007/978-3-030-34372-9) · [University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위](https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf) |
| P13 | `relevant-change` | 큰 변화보다 중요한 차이 | [Geirhos 외, Shortcut learning in deep neural networks](https://www.nature.com/articles/s42256-020-00257-z) |
| P14 | `task` | 같은 사진, 다른 질문과 정답 | [University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위](https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf) · [Lin 외, Microsoft COCO, 4절 객체 주석](https://arxiv.org/abs/1405.0312) |
| P15 | `rules` | 규칙 기반 · 답을 구하는 방법을 사람이 정한다 | 현행 강의의 설명과 교육용 예시 |
| P16 | `rules-image` | 이미지 판단 · 규칙을 어디까지 만들어야 할까? | [MIT 6.S191, Lecture 3 Deep Computer Vision](https://introtodeeplearning.com/#schedule) |
| P17 | `model-choice` | 사과 결함 검사 · 무엇부터 시도할까? | [MIT 15.773, Lecture 4 합성곱과 전이학습](https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/) · [PyTorch, ConvNet as fixed feature extractor](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) |
| P18 | `task-model-data` | 내 과제에 맞는 모델과 Label | [University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위](https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf) · [Lin 외, Microsoft COCO, 4절 객체 주석](https://arxiv.org/abs/1405.0312) |
| P19 | `cnn-why` | 왜 CNN인가? · 사과의 작은 특징 반복 탐색 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) |
| P20 | `cnn-overview` | CNN Architecture 전체 그림 · 사과 판정까지 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [MIT 15.773, Lecture 4 합성곱과 전이학습](https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/) |
| P21 | `perceptron` | 퍼셉트론 · 하나의 W와 b로 판정 | [위키독스 07-01 퍼셉트론, AND와 XOR](https://wikidocs.net/24958) |
| P22 | `and-rule` | AND Gate · 두 입력이 모두 1일 때 | [위키독스 07-01 퍼셉트론, AND와 XOR](https://wikidocs.net/24958) |
| P23 | `and-gate` | AND Gate · Weight와 Bias로 직선 이동 | [위키독스 07-01 퍼셉트론, AND와 XOR](https://wikidocs.net/24958) |
| P24 | `xor-rule` | XOR Gate · 입력이 다를 때만 1 | [위키독스 07-01 퍼셉트론, AND와 XOR](https://wikidocs.net/24958) |
| P25 | `nonlinear` | 비선형성 · 깊어져도 직선이면? | [MIT 6.S191, Lecture 1 Intro to Deep Learning](https://introtodeeplearning.com/#schedule) · [위키독스 07-01 퍼셉트론, AND와 XOR](https://wikidocs.net/24958) |
| P26 | `relu` | ReLU · 비선형성의 시작 | [MIT 6.S191, Lecture 1 Intro to Deep Learning](https://introtodeeplearning.com/#schedule) · [위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드](https://wikidocs.net/64066) |
| P27 | `xor-gate` | XOR · 선형층을 쌓아도 직선 하나 | [위키독스 07-01 퍼셉트론, AND와 XOR](https://wikidocs.net/24958) · [MIT 6.S191, Lecture 1 Intro to Deep Learning](https://introtodeeplearning.com/#schedule) |
| P28 | `kernel` | Kernel · 작은 영역의 가중합 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [MIT 15.773, Lecture 4 합성곱과 전이학습](https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/) · [Wang 외, CNN Explainer, II 및 IV절](https://arxiv.org/abs/2004.15004) · [위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드](https://wikidocs.net/64066) |
| P29 | `feature-map` | Feature Map · 같은 계산을 위치마다 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [Wang 외, CNN Explainer, II 및 IV절](https://arxiv.org/abs/2004.15004) |
| P30 | `sharing` | CNN · 지역 연결과 가중치 공유 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [Wang 외, CNN Explainer, II 및 IV절](https://arxiv.org/abs/2004.15004) |
| P31 | `channels` | RGB에서 Feature Channel까지 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드](https://wikidocs.net/64066) |
| P32 | `stride` | Stride · 계산 위치의 간격 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드](https://wikidocs.net/64066) |
| P33 | `padding` | Padding · 같은 입력, 다른 출력 크기 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드](https://wikidocs.net/64066) |
| P34 | `pool` | Max Pooling · 영역별 최댓값 | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드](https://wikidocs.net/64066) |
| P35 | `actual-map` | 실제 Feature Map · CNN 내부 반응 | [torchvision SqueezeNet1_1 weights 및 전처리](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.squeezenet1_1.html) · [Wang 외, CNN Explainer, II 및 IV절](https://arxiv.org/abs/2004.15004) |
| P36 | `backbone` | Backbone과 Task Head | [Stanford CS231n, Conv Layer 및 Pooling Layer](https://cs231n.github.io/convolutional-networks/) · [MIT 15.773, Lecture 4 합성곱과 전이학습](https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/) |
| P37 | `dataset` | 데이터셋 · 어떤 사진으로 배우나 | [Lin 외, Microsoft COCO, 4절 객체 주석](https://arxiv.org/abs/1405.0312) · [Geirhos 외, Shortcut learning in deep neural networks](https://www.nature.com/articles/s42256-020-00257-z) |
| P38 | `split` | Train · Validation · Test | [scikit-learn, Cross-validation iterators for grouped data](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data) · [scikit-learn, Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) |
| P39 | `leakage` | Video Group Split · 데이터 누출 방지 | [scikit-learn, Cross-validation iterators for grouped data](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data) |
| P40 | `augment` | Data Augmentation · 같은 정답, 다른 조건 | [MIT 6.S191, Lecture 3 Deep Computer Vision](https://introtodeeplearning.com/#schedule) · [scikit-learn, Cross-validation iterators for grouped data](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data) |
| P41 | `learn` | 모델 학습 · 오차를 줄이는 반복 | [MIT 6.S191, Lecture 1 Intro to Deep Learning](https://introtodeeplearning.com/#schedule) · [Stanford CS231n, Loss 및 Gradient descent](https://cs231n.github.io/optimization-1/) |
| P42 | `loss` | Loss · 틀린 정도를 줄이는 방향 | [Stanford CS231n, Loss 및 Gradient descent](https://cs231n.github.io/optimization-1/) · [MIT 6.S191, Lecture 1 Intro to Deep Learning](https://introtodeeplearning.com/#schedule) |
| P43 | `cnn-training` | CNN 학습 · 예측에서 Weight 갱신까지 | [MIT 6.S191, Lecture 1 Intro to Deep Learning](https://introtodeeplearning.com/#schedule) · [위키독스 07-05 역전파 이해하기](https://wikidocs.net/37406) |
| P44 | `infer` | Training과 Inference의 차이 | [MIT 6.S191, Lecture 1 Intro to Deep Learning](https://introtodeeplearning.com/#schedule) |
| P45 | `transfer` | 전이학습 · 특징은 고정하고 분류기만 학습 | [MIT 15.773, Lecture 4 합성곱과 전이학습](https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/) · [PyTorch, ConvNet as fixed feature extractor](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) |
| P46 | `cnn-learning-paths` | 같은 CNN 특징 · 지도와 비지도 활용 | [PyTorch, ConvNet as fixed feature extractor](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) |
| P47 | `overfit` | Overfitting · 새 데이터 일반화 | [Geirhos 외, Shortcut learning in deep neural networks](https://www.nature.com/articles/s42256-020-00257-z) |
| P48 | `threshold` | Score Threshold · 판정 기준 | [scikit-learn, Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) |
| P49 | `confusion` | Confusion Matrix · 100건 평가 | [scikit-learn, Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) |
| P50 | `imbalance` | Accuracy의 함정 · 모두 정상이라면? | [scikit-learn, Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) |
| P51 | `metrics` | Precision과 Recall | [scikit-learn, Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) |
| P52 | `iou` | IoU · 박스 겹침 비율 | [Lin 외, Microsoft COCO, 4절 객체 주석](https://arxiv.org/abs/1405.0312) · [COCO API, computeIoU](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py) |
| P53 | `workflow` | Vision AI 원리 · 한 장으로 연결 | [MIT 6.S191, Lecture 3 Deep Computer Vision](https://introtodeeplearning.com/#schedule) |
| P54 | `project-iterate` | 실패 사진이 알려 주는 것 | [Geirhos 외, Shortcut learning in deep neural networks](https://www.nature.com/articles/s42256-020-00257-z) · [scikit-learn, Cross-validation iterators for grouped data](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data) · [scikit-learn, Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) |
| P55 | `project-check` | Vision AI 원리 · 무엇을 설명할 수 있나? | 현행 강의의 설명과 교육용 예시 |
