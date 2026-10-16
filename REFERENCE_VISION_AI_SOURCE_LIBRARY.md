# Vision AI 초보 강의 · 논문/대학 강의/공식 Figure 소스 라이브러리

> 조사일: 2026-10-16 · 버전: 1차 큐레이션 (대표 28건)
> 현재 공개 강의는 **Intro 19장 + Vision AI 통합 53장(총 72장)**. 자료 자체를 현재 강의의 보충 근거로 사용하며, 모든 논문 또는 Figure를 무차별적으로 강의에 삽입하지 않습니다.

## 사용 목적

- 이 문서는 **원본/공식 1차 출처 → 적합한 한글 설명 → 해당 슬라이드**를 연결하기 위한 출처 후보 저장소입니다.
- 기존의 이해하기 쉬운 사과 사진, 픽셀 계산, 인터랙티브 자료를 가능한 한 유지합니다.
- 원본 Figure가 적합하면 그 그림을 우선 검토하고, 긴 영문 문구는 한글 부제와 간결한 한글 설명으로 보완합니다.
- 그림에 붙일 출처는 논문 제목/저자/연도, Figure 번호 또는 강의명/페이지, 원본 URL을 남깁니다.
- `ResNet`, `U-Net`, `ViT` 등의 개별 모델 아키텍처 심화 단원은 초보자 본강의에 추가하지 않습니다. CNN → YOLO의 핵심과 데이터/평가 중심입니다.

## 1차 핵심 참고문헌 및 Figure 후보

| ID | 분야 | 1차 출처 링크 | 강의에 가져올 핵심 | 용도 | 우선순위 |
|---|---|---|---|---|---|
| R01 | 종합 입문 | [Szeliski (2022), Computer Vision: Algorithms and Applications 2e](https://szeliski.org/Book/) | 카메라/Pixel/이미지 변화·필터·검출의 큰 그림 | 배경·이론 기준 | 중 |
| R02 | 대학 강의 | [Stanford CS231n (2025) 공식 강의 일정 및 강의 슬라이드](https://cs231n.stanford.edu/2025/schedule.html) | Image Classification/CNN/Detection의 입문 강의 흐름과 강의 Figure 후보 | 강의 전개와 슬라이드 Figure 후보 | 상 |
| R03 | 대학 강의 | [Stanford CS231n — Convolutional Neural Networks](https://cs231n.github.io/convolutional-networks/) | 3D 채널·필터·Weight Sharing·Pooling·FC의 관계 | CNN 도식 후보 | 상 |
| R04 | 대학 강의 | [MIT 6.S191 Introduction to Deep Learning (OCW 2026 강의 정보)](https://ocw.mit.edu/courses/6-s191-introduction-to-deep-learning-january-iap-2020/) | 컴퓨터가 보는 이미지 → 필터 추출 → CNN 입문 | 스토리·강의 슬라이드 후보 | 상 |
| R05 | 대학 강의 | [MIT 15.773 (2024) — CNN, Computer Vision & Transfer Learning](https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/lists/lecture-notes/) | CNN·전이학습 슬라이드와 Convolution 계산 XLSX | 원본 계산/강의 Figure 후보 | 상 |
| R06 | 공식 튜토리얼 | [OpenCV — Smoothing Images / 2D Filtering](https://docs.opencv.org/4.12.0/d4/d13/tutorial_py_filtering.html) | Mean/Gaussian/Median 등 필터별 결과·노이즈 변화 | 원본 처리 사진 및 재계산 | 상 |
| R07 | 공식 튜토리얼 | [OpenCV — Sobel Derivatives](https://docs.opencv.org/4.12.0/d2/d2c/tutorial_sobel_derivatives.html) | 경계(밝기 변화)와 Sobel 영상 예시 | 원본 경계 시각화 | 상 |
| R08 | 공개 교재 | [Dive into Deep Learning — Chapter 7 CNN](https://d2l.ai/chapter_convolutional-neural-networks/index.html) | Kernel 학습·Stride/Padding/Channel·Pooling | 수학적 계산 근거 | 상 |
| R09 | 공개 교재 | [Dive into Deep Learning — Convolutions for Images](https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html) | 밝은/어두운 패치와 경계 반응값이 연결되는 예시 | 정확한 배열 예제 | 상 |
| R10 | 상호작용/논문 | [CNN Explainer (Georgia Tech Polo Club)](https://poloclub.github.io/cnn-explainer/) | 이미지→Kernel→Feature Map과 연산 단계를 시각적으로 연결 | 구조·계산 참고 | 상 |
| R11 | 논문 | [Wang et al., CNN Explainer, IEEE TVCG (2020)](https://poloclub.github.io/papers/20-vis-cnnexplainer.pdf) | 층 전체 보기 + 위치별 필터 연산 + 숫자식 결합 | 시각 설명 설계 참고 | 상 |
| R12 | 시각화 논문 | [Olah et al., Feature Visualization, Distill (2017)](https://distill.pub/2017/feature-visualization/) | CNN 얕은 층 패턴과 깊은 층 특징의 차이 | **원본 특징 시각화 이미지 후보** | 상 |
| R13 | 논문 | [Selvaraju et al., Grad-CAM, ICCV (2017)](https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html) | 어디를 근거로 예측했는지 Heatmap 비교 | 시각적 검증 예시 | 중 |
| R14 | 논문/데이터 | [Deng et al., ImageNet, CVPR (2009)](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf) | 레이블 종류/데이터셋 규모/사전학습 개념 | 이미지 레이블 참고 | 중 |
| R15 | 논문/데이터 | [Lin et al., Microsoft COCO (2014)](https://arxiv.org/abs/1405.0312) | 일상 사진의 실제 객체 박스/마스크 주석 | Label 종류 설명 원본 사례 | 상 |
| R16 | 원 논문 | [Redmon et al., You Only Look Once, CVPR (2016)](https://openaccess.thecvf.com/content_cvpr_2016/html/Redmon_You_Only_Look_CVPR_2016_paper.html) | 한 번에 Class + Bounding Box 예측하는 검출 원리 | YOLO 핵심 원본 Figure 후보 | 상 |
| R17 | 공식 문서 | [Ultralytics — YOLO Architecture Explained](https://docs.ultralytics.com/ko/guides/yolo-architecture) | Backbone → Neck → Head, 다중 크기 특징 | YOLO 구조 그림 후보 | 상 |
| R18 | 공식 문서 | [Ultralytics — Object Detection](https://docs.ultralytics.com/tasks/detect) | Class + Box + Confidence 출력, 검출 Task | YOLO 박스 예시 원본 | 상 |
| R19 | 공식 문서 | [Ultralytics — Classification](https://docs.ultralytics.com/ko/tasks/classify) | 이미지 전체 Class를 예측하는 분류 전용 Task | Classify/Detect 비교 | 상 |
| R20 | 공식 문서 | [Ultralytics — Detection Dataset Format](https://docs.ultralytics.com/datasets/detect) | 한 개 박스 정답: class cx cy w h (정규화) | 실제 YOLO Label 표현 | 상 |
| R21 | 공식 강의 | [Ultralytics Academy — Train Your First YOLO](https://academy.ultralytics.com/courses/train-your-first-yolo) | 데이터 수집/Label → Train → Predict → Val | 실습 워크플로와 그림 | 상 |
| R22 | 공식 문서 | [Ultralytics — YOLO Performance Metrics](https://docs.ultralytics.com/ko/guides/yolo-performance-metrics) | IoU/Precision/Recall/mAP/Confusion Matrix 해석 | 평가 수치의 근거 | 상 |
| R23 | 공식 튜토리얼 | [PyTorch — Transfer Learning for Computer Vision](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial) | Freeze vs Fine-tune/사전학습 가중치/새 Task | 시각적 워크플로·실습 근거 | 상 |
| R24 | 논문 | [Geirhos et al., Shortcut Learning, Nature MI (2020)](https://www.nature.com/articles/s42256-020-00257-z) | 배경/색 등 잘못된 단서를 학습할 위험 | 일반화 실패 사례 | 상 |
| R25 | 공식 문서 | [scikit-learn — GroupShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html) | 같은 Video/LOT이 Train/Test 양쪽에 섞이는 누출 방지 | 그룹 분할 논리 근거 | 중 |
| R26 | 외부 원본 | [Developers Breach — Convolutional Neural Network (얼룩말)](https://developersbreach.com/convolution-neural-network-deep-learning/) | 입력 이미지 → CNN Feature → Classifier | 현재 16번에서 **원본 그대로 사용 중** | 상 |
| R27 | 외부 그림 | [Electronics (2024), YOLOv8 Figure 1](https://doi.org/10.3390/electronics13224411) | YOLOv8 Backbone/Neck/Head 세부 아키텍처 | 현재 28번 원본 Figure 사용 중 | 중 |
| R28 | 참고 구조 | [Dragon1 — Convolutional Neural Networks Definition](https://www.dragon1.com/terms/convolutional-neural-networks-definition) | Input/Convolution/ReLU/Pooling/FC/Output의 대표 단계 | 기존 CNN 강의용 SVG 제작 기준 | 중 |

## 수집·활용 전 주의사항

- **R01**: 온라인 교재 링크. 전자책 PDF 재게시 제한을 명시함
- **R02**: 각 강의별 슬라이드 원본 및 저작권 표시 확인 후 사용
- **R03**: 수치와 예제를 강의용 한국어로 설명
- **R04**: 강의 슬라이드 사용할 때 해당 강의 표기 지침 확인
- **R05**: Lecture 03B·04와 XLSX 참고
- **R06**: 원본 Figure는 출처 표기; 수치 처리 조건은 직접 재검산
- **R07**: Gradient 절댓값과 실제 방향 결과를 혼동하지 않기
- **R08**: 직접 계산 예제로 재현하고 원본 출처 병기
- **R09**: 교재는 CNN 실습에서 주로 cross-correlation 연산 사용
- **R10**: 상호작용을 캡처하기보다 설명에 필요한 Figure만 선별
- **R11**: 논문 Figure와 외부 원본 이미지 출처 기록
- **R12**: 자체 도식/텍스트 CC BY 4.0(별도 표시된 제3자 Figure 제외)
- **R13**: Class Activation Map을 실제 결함 위치/근거라고 단정하지 않기
- **R14**: 모델 학습용 데이터·그림 저작권은 별개
- **R15**: 데이터셋 개별 이미지 권리 확인 필요
- **R16**: 2016년 원 YOLO는 현대 Ultralytics 버전 구조와 구별
- **R17**: 버전별 세부 모듈은 본강의에서 생략
- **R18**: Confidence를 검증된 정확도/확률로 잘못 설명하지 않기
- **R19**: Detection과 다른 학습 Label/Head를 사용
- **R20**: 좌표 0~1 정규화 여부 표시
- **R21**: 모델 이름/버전 업데이트 가능하므로 공식 예제와 고정 버전 구분
- **R22**: 분류 Confusion Matrix와 검출 TP 판정 조건 분리
- **R23**: 예시에 등장하는 ResNet은 도구일 뿐 본강의에 독립 아키텍처 강의 미추가
- **R24**: 실제 모델 행동 Figure면 실험 조건 함께 소개
- **R25**: 개별 프레임 랜덤 분할과 대조
- **R26**: 외부 서버 직접 로드: 사내망 차단 시 기존 로컬 SVG 대체
- **R27**: 현재 논문 속 구현 한정; 모든 YOLO 공통 구성도로 오해하지 않기
- **R28**: 전형적 분류 CNN 예시이며 YOLO 검출 Head와 다름

## 출처 재사용과 정확성

1. **출처 표기와 원본 이미지 복제 허가는 동일하지 않습니다.** 그림을 공개 GitHub Pages에 복제해 호스팅할 때는 원문에 표시된 라이선스/사용 조건을 확인합니다. 원본 페이지 링크와 원본 자체를 iframe/hotlink하는 방식도 사이트 정책/네트워크/브라우저 정책의 영향을 받습니다. 라이선스를 확인하지 않은 그림을 무조건 공개 저장소로 복사하지 않습니다.
2. 예시 출처: Distill(자체 Figure의 CC BY 4.0), Szeliski 교재(전자책 개인 사용용 PDF 재게시 제한), Computer Vision Foundation 논문(논문 접근 가능하지만 저작권은 저자/권리자에게 남음).
3. 원본 Figure는 **해당 Figure 번호와 실제 이미지 URL 확인 이후** 강의 슬라이드에 적용합니다. 본 표의 링크는 검토용 **문헌 URL**이며 아직 모든 이미지의 직접 파일 링크를 검증한 것은 아닙니다.
4. 추출 이미지가 아니라 실제 실험 결과처럼 보이는 그림에는 반드시 **개념도 / 재구성 / 실제 추론 아님** 여부를 표시합니다.
5. 외부 서버 이미지 로드가 차단될 수 있으므로 GitHub Pages에는 가능한 한 저장소 내부 fallback을 사용합니다.
6. 각 그림에서 CNN 특징(Convolution, Pooling, Feature Map), YOLO Detect 학습(Class + Box), 분류 CNN(Class only)을 서로 혼동하지 않습니다.
7. 본 라이브러리는 특정 시점의 **선별 자료 목록**이며, 모든 Computer Vision 논문과 강의자료를 망라한 목록은 아닙니다. 새로운 자료는 검증 후 계속 추가합니다.

## 다음 작업으로 연결

자세한 적용 우선순위·슬라이드별 매칭은 [REFERENCE_SLIDE_SOURCE_MAP.md](REFERENCE_SLIDE_SOURCE_MAP.md)를 참고합니다.
강의 반영 단계: (1) 외부 원본 Figure 후보와 직접 이미지 URL 검증 → (2) 한국어 제목/설명·실제 사례 매칭 → (3) 최소 범위 Branch + PR → (4) 1920×1080/1366×768 렌더링 확인 → (5) merge/Pages 검증.
