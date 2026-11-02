# Concept Catalog · 483개 초기 등록

> [concepts.v1.json](concepts.v1.json)이 정본. **전체 상태 Related**, 즉 교육과정 후보로 등록. 기존 슬라이드 링크는 현장 구현/실험 증거와 다르다. 독립 Reviewer PENDING.

## 레코드 스키마

`id` 고유 ID · `title/title_ko` 영문/한국어 표제 · `part/chapter` 소유 PART · `level` 난이도 · `prerequisites` 직접 선수 · `next_topics` 역방향 간선 · `advanced_topics` 선택 심화 · `applications` 프로젝트 후보 · `status` 실무 증거 · `legacy_slide` 기존 물리 Deep Link · `references` 근거 URL.

- Level: Foundation/Basic/Intermediate/Advanced/Research.
- Status: Related(후보) → Reviewed(검토) / Implemented(소스 검증) / Experimented(재현 가능한 실험 기록 확인). 상태는 난이도와 무관.
- `title_ko`가 영문과 같은 등록 항목은 향후 한국어 표준 용어 검토 대상.
- 아직 모든 페이지를 만들지 않았으므로 ID가 곧 방문 가능한 새 URL은 아니다.

## 전체 고유 개념

| ID | Title | Level | 직접 선수 ID | 기존 강의 Deep Link | 연결 프로젝트 후보 |
|---|---|---|---|---|---|
| `f.artificial_intelligence` | Artificial Intelligence | Foundation | — | — | — |
| `f.machine_learning` | Machine Learning | Foundation | — | — | — |
| `f.deep_learning` | Deep Learning | Foundation | — | — | — |
| `f.data` | 데이터 / Data | Foundation | — | — | — |
| `f.sample` | Sample | Foundation | `f.data` | — | — |
| `f.feature` | 특징 / Feature | Foundation | `f.sample` | — | — |
| `f.label` | 정답 라벨 / Label | Foundation | `f.sample` | — | — |
| `f.dataset` | 데이터셋 / Dataset | Foundation | `f.sample` | — | — |
| `f.scalar` | 스칼라 / Scalar | Foundation | — | — | — |
| `f.vector` | 벡터 / Vector | Foundation | `f.scalar` | — | — |
| `f.matrix` | 행렬 / Matrix | Foundation | `f.vector` | — | — |
| `f.tensor` | 텐서 / Tensor | Foundation | `f.matrix` | — | — |
| `f.shape` | 형상 / Shape | Foundation | `f.tensor` | — | — |
| `f.dimension` | Dimension | Foundation | `f.tensor` | — | — |
| `f.axis` | Axis | Foundation | `f.tensor` | — | — |
| `f.broadcasting` | Broadcasting | Foundation | `f.shape`, `f.axis` | — | — |
| `f.function` | Function | Foundation | — | — | — |
| `f.linear_function` | Linear Function | Foundation | `f.function` | — | — |
| `f.nonlinear_function` | Nonlinear Function | Foundation | `f.function` | — | — |
| `f.sum` | Sum | Foundation | — | — | — |
| `f.mean` | 평균 / Mean | Foundation | `f.sum`, `f.sample` | — | — |
| `f.variance` | 분산 / Variance | Foundation | `f.mean` | — | — |
| `f.standard_deviation` | 표준편차 / Standard Deviation | Foundation | `f.variance` | — | — |
| `f.statistics` | Statistics | Foundation | `f.mean`, `f.variance` | — | — |
| `f.probability` | Probability | Foundation | — | — | — |
| `f.probability_distribution` | Probability Distribution | Foundation | `f.probability` | — | — |
| `f.normal_distribution` | Normal Distribution | Foundation | `f.probability_distribution` | — | — |
| `f.conditional_probability` | Conditional Probability | Foundation | `f.probability` | — | — |
| `f.derivative` | Derivative | Foundation | `f.function` | — | — |
| `f.partial_derivative` | Partial Derivative | Foundation | `f.derivative` | — | — |
| `f.gradient` | 기울기 / Gradient | Foundation | `f.partial_derivative`, `f.vector` | — | — |
| `f.chain_rule` | Chain Rule | Foundation | `f.derivative` | — | — |
| `f.linear_algebra` | Linear Algebra | Foundation | `f.vector`, `f.matrix` | — | — |
| `f.dot_product` | 내적 / Dot Product | Foundation | `f.vector` | — | — |
| `f.matrix_multiplication` | Matrix Multiplication | Foundation | `f.matrix`, `f.dot_product` | — | — |
| `f.distance_metric` | Distance Metric | Foundation | `f.vector` | — | — |
| `f.euclidean_distance` | 유클리드 거리 / Euclidean Distance | Foundation | `f.distance_metric` | — | — |
| `f.cosine_similarity` | Cosine Similarity | Foundation | `f.dot_product`, `f.distance_metric` | — | — |
| `f.python` | Python | Foundation | — | — | — |
| `f.numpy` | Numpy | Foundation | `f.python`, `f.tensor` | — | — |
| `f.matplotlib` | Matplotlib | Foundation | `f.python` | — | — |
| `f.array_indexing` | Array Indexing | Foundation | `f.tensor` | — | — |
| `f.slicing` | Slicing | Foundation | `f.array_indexing` | — | — |
| `f.data_type` | Data Type | Foundation | — | — | — |
| `ml.supervised_learning` | 지도학습 / Supervised Learning | Basic | `f.dataset`, `f.label` | — | — |
| `ml.unsupervised_learning` | 비지도학습 / Unsupervised Learning | Basic | `f.dataset` | — | — |
| `ml.self_supervised_learning` | Self Supervised Learning | Basic | `ml.unsupervised_learning` | — | — |
| `ml.semi_supervised_learning` | Semi Supervised Learning | Basic | `ml.supervised_learning`, `ml.unsupervised_learning` | — | — |
| `ml.classification` | Classification | Basic | `ml.supervised_learning` | — | — |
| `ml.regression` | Regression | Basic | `ml.supervised_learning` | — | — |
| `ml.binary_classification` | Binary Classification | Basic | `ml.classification` | — | — |
| `ml.multiclass_classification` | Multiclass Classification | Basic | `ml.classification` | — | — |
| `ml.multilabel_classification` | Multilabel Classification | Basic | `ml.classification` | — | — |
| `ml.feature_engineering` | Feature Engineering | Basic | `f.dataset` | — | — |
| `ml.linear_regression` | Linear Regression | Basic | `ml.regression`, `f.linear_function` | — | — |
| `ml.logistic_regression` | Logistic Regression | Basic | `ml.binary_classification`, `f.nonlinear_function` | — | — |
| `ml.decision_boundary` | Decision Boundary | Basic | `ml.classification`, `f.linear_function` | — | — |
| `ml.linear_separability` | Linear Separability | Basic | `ml.decision_boundary` | — | — |
| `ml.underfitting` | Underfitting | Basic | `f.dataset` | — | — |
| `ml.overfitting` | Overfitting | Basic | `ml.underfitting` | `docs/vision_ai_course.html#slide-34` | — |
| `ml.bias_variance_tradeoff` | Bias Variance Tradeoff | Basic | `ml.overfitting` | — | — |
| `ml.generalization` | Generalization | Basic | `ml.overfitting` | — | — |
| `ml.train_validation_test_split` | 학습·검증·테스트 분할 / Train Validation Test Split | Basic | `f.dataset`, `ml.supervised_learning` | `docs/vision_ai_course.html#slide-25` | — |
| `ml.cross_validation` | Cross Validation | Basic | `ml.train_validation_test_split` | — | — |
| `ml.data_leakage` | 데이터 누수 / Data Leakage | Basic | `ml.train_validation_test_split` | `docs/vision_ai_course.html#slide-26` | — |
| `ml.model_parameter` | Model Parameter | Basic | `ml.linear_regression` | — | — |
| `ml.hyperparameter` | Hyperparameter | Basic | `ml.model_parameter` | — | — |
| `ml.loss_function` | 손실 함수 / Loss Function | Basic | `ml.supervised_learning`, `f.function` | `docs/vision_ai_course.html#slide-29` | — |
| `ml.evaluation_metric` | Evaluation Metric | Basic | `ml.loss_function` | — | — |
| `ml.gradient_descent` | 경사하강법 / Gradient Descent | Basic | `f.gradient`, `ml.loss_function` | — | — |
| `ml.learning_rate` | Learning Rate | Basic | `ml.gradient_descent` | — | — |
| `dl.perceptron` | 퍼셉트론 / Perceptron | Intermediate | `f.vector`, `ml.supervised_learning` | `docs/vision_ai_course.html#slide-8` | — |
| `dl.and_or_xor` | And Or Xor | Intermediate | `dl.perceptron`, `ml.linear_separability` | — | — |
| `dl.multilayer_perceptron` | Multilayer Perceptron | Intermediate | `dl.perceptron`, `dl.activation_function` | — | — |
| `dl.fully_connected_layer` | Fully Connected Layer | Intermediate | `dl.perceptron`, `f.matrix_multiplication` | — | — |
| `dl.weight` | Weight | Intermediate | `dl.perceptron` | — | — |
| `dl.bias` | Bias | Intermediate | `dl.perceptron` | — | — |
| `dl.activation_function` | 활성화 함수 / Activation Function | Intermediate | `f.nonlinear_function`, `dl.perceptron` | — | — |
| `dl.relu` | Relu | Intermediate | `dl.activation_function` | `docs/vision_ai_course.html#slide-13` | — |
| `dl.sigmoid` | Sigmoid | Intermediate | `dl.activation_function` | — | — |
| `dl.tanh` | Tanh | Intermediate | `dl.activation_function` | — | — |
| `dl.softmax` | Softmax | Intermediate | `dl.activation_function`, `f.probability` | — | — |
| `dl.forward_propagation` | 순전파 / Forward Propagation | Intermediate | `dl.fully_connected_layer`, `dl.activation_function` | — | — |
| `dl.backpropagation` | 역전파 / Backpropagation | Intermediate | `dl.neural_chain_rule`, `ml.loss_function` | — | — |
| `dl.neural_chain_rule` | Neural Chain Rule | Intermediate | `f.chain_rule`, `dl.computational_graph` | — | — |
| `dl.cross_entropy` | Cross Entropy | Intermediate | `ml.loss_function`, `f.probability` | — | — |
| `dl.binary_cross_entropy` | Binary Cross Entropy | Intermediate | `dl.cross_entropy`, `ml.binary_classification` | — | — |
| `dl.mean_squared_error` | Mean Squared Error | Intermediate | `ml.loss_function`, `f.mean` | — | — |
| `dl.mean_absolute_error` | Mean Absolute Error | Intermediate | `ml.loss_function`, `f.mean` | — | — |
| `dl.sgd` | Sgd | Intermediate | `ml.gradient_descent`, `dl.backpropagation` | — | — |
| `dl.momentum` | Momentum | Intermediate | `dl.sgd` | — | — |
| `dl.adam` | Adam | Intermediate | `dl.momentum` | — | — |
| `dl.adamw` | AdamW | Intermediate | `dl.adam` | — | — |
| `dl.batch` | Batch | Intermediate | `f.dataset` | — | — |
| `dl.iteration` | Iteration | Intermediate | `dl.batch`, `dl.sgd` | — | — |
| `dl.epoch` | Epoch | Intermediate | `dl.iteration` | — | — |
| `dl.batch_normalization` | Batch Normalization | Intermediate | `dl.forward_propagation`, `f.mean`, `f.variance` | — | — |
| `dl.dropout` | Dropout | Intermediate | `dl.multilayer_perceptron` | — | — |
| `dl.weight_decay` | Weight Decay | Intermediate | `dl.sgd` | — | — |
| `dl.early_stopping` | Early Stopping | Intermediate | `ml.overfitting`, `ml.train_validation_test_split` | — | — |
| `dl.learning_rate_scheduler` | Learning Rate Scheduler | Intermediate | `ml.learning_rate` | — | — |
| `dl.residual_connection` | Residual Connection | Intermediate | `dl.multilayer_perceptron` | — | — |
| `dl.representation_learning` | Representation Learning | Intermediate | `dl.multilayer_perceptron` | — | — |
| `dl.transfer_learning` | Transfer Learning | Intermediate | `dl.representation_learning`, `ml.train_validation_test_split` | — | — |
| `dl.fine_tuning` | Fine Tuning | Intermediate | `dl.transfer_learning`, `dl.sgd` | — | — |
| `dl.model_training` | Model Training | Intermediate | `dl.forward_propagation`, `dl.backpropagation`, `dl.sgd` | — | — |
| `dl.computational_graph` | Computational Graph | Intermediate | `dl.forward_propagation` | — | — |
| `img.digital_image` | 디지털 이미지 / Digital Image | Basic | `f.data` | — | — |
| `img.pixel` | 픽셀 / Pixel | Basic | `img.digital_image` | `docs/intro.html#slide-5` | — |
| `img.rgb` | RGB | Basic | `img.pixel` | `docs/intro.html#slide-6` | — |
| `img.bgr` | BGR | Basic | `img.rgb` | — | — |
| `img.image_resolution` | Image Resolution | Basic | `img.pixel` | — | — |
| `img.channel` | Channel | Basic | `img.rgb` | — | — |
| `img.bit_depth` | Bit Depth | Basic | `img.pixel`, `f.data_type` | — | — |
| `img.grayscale` | Grayscale | Basic | `img.pixel` | — | — |
| `img.hsv` | Hsv | Basic | `img.rgb` | — | — |
| `img.color_space` | Color Space | Basic | `img.rgb` | — | — |
| `img.image_tensor` | 이미지 텐서 / Image Tensor | Basic | `img.rgb`, `f.tensor` | `docs/intro.html#slide-7` | — |
| `img.resize` | Resize | Basic | `img.image_resolution` | — | — |
| `img.crop` | Crop | Basic | `img.image_tensor` | — | — |
| `img.interpolation` | Interpolation | Basic | `img.resize` | — | — |
| `img.region_of_interest` | Region Of Interest | Basic | `img.crop` | — | Case A (candidate) |
| `img.image_histogram` | Image Histogram | Basic | `img.pixel`, `f.statistics` | — | — |
| `img.gaussian_blur` | Gaussian Blur | Basic | `img.spatial_filter_kernel`, `f.normal_distribution` | — | — |
| `img.median_filter` | Median Filter | Basic | `img.spatial_filter_kernel`, `f.statistics` | — | — |
| `img.sobel` | Sobel | Basic | `img.spatial_filter_kernel` | — | — |
| `img.laplacian` | Laplacian | Basic | `img.spatial_filter_kernel` | — | — |
| `img.edge_detection` | Edge Detection | Basic | `img.sobel` | — | — |
| `img.sharpening` | Sharpening | Basic | `img.spatial_filter_kernel` | — | — |
| `img.noise` | Noise | Basic | `img.digital_image` | — | — |
| `img.illumination` | Illumination | Basic | `img.digital_image` | — | — |
| `img.reflection` | Reflection | Basic | `img.digital_image` | — | — |
| `img.thresholding` | Thresholding | Basic | `img.grayscale` | — | — |
| `img.binary_image` | Binary Image | Basic | `img.thresholding` | — | — |
| `img.morphology` | Morphology | Basic | `img.binary_image` | — | — |
| `img.erosion` | Erosion | Basic | `img.morphology` | — | — |
| `img.dilation` | Dilation | Basic | `img.morphology` | — | — |
| `img.opening` | Opening | Basic | `img.erosion`, `img.dilation` | — | — |
| `img.closing` | Closing | Basic | `img.erosion`, `img.dilation` | — | — |
| `img.contour` | Contour | Basic | `img.binary_image` | — | — |
| `img.connected_component` | Connected Component | Basic | `img.binary_image` | — | — |
| `img.distance_transform` | Distance Transform | Basic | `img.binary_image`, `f.euclidean_distance` | — | — |
| `img.image_quality` | Image Quality | Basic | `img.digital_image` | — | — |
| `img.blur_detection` | Blur Detection | Basic | `img.edge_detection` | — | — |
| `img.fft` | Fft | Basic | `f.linear_algebra`, `img.digital_image` | — | — |
| `img.dct` | Dct | Basic | `img.fft` | — | — |
| `img.opencv` | OpenCV | Basic | `img.image_tensor`, `f.python` | — | — |
| `img.spatial_filter_kernel` | 공간 필터 커널 / Spatial Filter Kernel | Basic | `f.matrix`, `img.pixel` | — | — |
| `img.video_frame` | Video Frame | Basic | `img.digital_image` | `docs/intro.html#slide-8` | — |
| `cnn.local_connectivity` | Local Connectivity | Intermediate | `img.image_tensor` | — | — |
| `cnn.weight_sharing` | Weight Sharing | Intermediate | `cnn.local_connectivity` | — | — |
| `cnn.kernel` | CNN 커널 / Kernel | Intermediate | `img.spatial_filter_kernel`, `cnn.weight_sharing` | `docs/vision_ai_course.html#slide-15` | — |
| `cnn.convolution` | 합성곱 / Convolution | Intermediate | `cnn.kernel`, `img.image_tensor`, `f.dot_product` | — | — |
| `cnn.stride` | 스트라이드 / Stride | Intermediate | `cnn.convolution` | `docs/vision_ai_course.html#slide-19` | — |
| `cnn.padding` | 패딩 / Padding | Intermediate | `cnn.convolution` | `docs/vision_ai_course.html#slide-20` | — |
| `cnn.convolution_output_shape` | Convolution Output Shape | Intermediate | `cnn.stride`, `cnn.padding`, `f.shape` | — | — |
| `cnn.feature_map` | 특징 맵 / Feature Map | Intermediate | `cnn.convolution`, `cnn.convolution_output_shape` | `docs/vision_ai_course.html#slide-16` | — |
| `cnn.feature_channel` | Feature Channel | Intermediate | `cnn.feature_map`, `img.channel` | — | — |
| `cnn.receptive_field` | Receptive Field | Intermediate | `cnn.convolution`, `cnn.feature_map` | — | — |
| `cnn.pooling` | 풀링 / Pooling | Intermediate | `cnn.feature_map` | `docs/vision_ai_course.html#slide-21` | — |
| `cnn.downsampling` | Downsampling | Intermediate | `cnn.pooling` | — | — |
| `cnn.feature_hierarchy` | Feature Hierarchy | Intermediate | `cnn.feature_map`, `cnn.downsampling` | — | — |
| `cnn.cnn_architecture` | CNN 구조 / CNN Architecture | Intermediate | `cnn.feature_hierarchy`, `dl.relu`, `dl.fully_connected_layer` | `docs/vision_ai_course.html#slide-7` | — |
| `cnn.backbone` | Backbone | Intermediate | `cnn.cnn_architecture` | `docs/vision_ai_course.html#slide-23` | — |
| `cnn.neck` | Neck | Intermediate | `cnn.backbone` | — | — |
| `cnn.head` | Head | Intermediate | `cnn.backbone` | — | — |
| `cnn.vgg` | Vgg | Intermediate | `cnn.convolution` | — | — |
| `cnn.resnet` | Resnet | Intermediate | `cnn.cnn_architecture`, `dl.residual_connection` | — | — |
| `cnn.efficientnet` | Efficientnet | Intermediate | `cnn.convolution` | — | — |
| `cnn.feature_extraction` | Feature Extraction | Intermediate | `cnn.backbone`, `dl.representation_learning` | — | — |
| `cnn.multi_scale_feature` | Multi Scale Feature | Intermediate | `cnn.feature_hierarchy` | — | — |
| `cnn.feature_pyramid_network` | Feature Pyramid Network | Intermediate | `cnn.multi_scale_feature`, `cnn.neck` | — | — |
| `cnn.pretrained_backbone` | Pretrained Backbone | Intermediate | `cnn.backbone`, `dl.transfer_learning` | — | — |
| `cnn.transfer_learning` | Transfer Learning | Intermediate | `cnn.pretrained_backbone` | — | — |
| `cnn.fine_tuning` | Fine Tuning | Intermediate | `cnn.transfer_learning`, `dl.fine_tuning` | — | — |
| `cnn.dilated_convolution` | Dilated Convolution | Intermediate | `cnn.convolution` | — | — |
| `cnn.group_convolution` | Group Convolution | Intermediate | `cnn.convolution` | — | — |
| `cnn.depthwise_separable_convolution` | Depthwise Separable Convolution | Intermediate | `cnn.group_convolution` | — | — |
| `task.image_classification` | Image Classification | Intermediate | `ml.classification`, `img.image_tensor` | — | — |
| `task.object_detection` | Object Detection | Intermediate | `task.image_classification` | — | Case B (candidate) |
| `task.semantic_segmentation` | Semantic Segmentation | Intermediate | `task.image_classification` | — | — |
| `task.instance_segmentation` | Instance Segmentation | Intermediate | `task.semantic_segmentation`, `task.object_detection` | — | — |
| `task.panoptic_segmentation` | Panoptic Segmentation | Intermediate | `task.instance_segmentation`, `task.semantic_segmentation` | — | — |
| `task.bounding_box` | Bounding Box | Intermediate | `task.object_detection` | — | — |
| `task.polygon` | Polygon | Intermediate | `task.instance_segmentation` | — | — |
| `task.binary_mask` | Binary Mask | Intermediate | `img.binary_image`, `task.semantic_segmentation` | — | — |
| `task.confidence_score` | Confidence Score | Intermediate | `task.image_classification` | — | — |
| `task.intersection_over_union` | Intersection Over Union | Intermediate | `task.bounding_box` | — | — |
| `task.non_maximum_suppression` | Non Maximum Suppression | Intermediate | `task.bounding_box`, `task.confidence_score`, `task.intersection_over_union` | — | — |
| `task.one_stage_detector` | One Stage Detector | Intermediate | `task.object_detection`, `cnn.head` | — | — |
| `task.two_stage_detector` | Two Stage Detector | Intermediate | `task.object_detection`, `cnn.head` | — | — |
| `task.yolo_architecture` | Yolo Architecture | Intermediate | `task.one_stage_detector`, `cnn.feature_pyramid_network` | — | — |
| `task.yolov8_detection` | YOLOv8 Detection | Intermediate | `task.yolo_architecture` | — | — |
| `task.yolov8_segmentation` | YOLOv8 Segmentation | Intermediate | `task.yolov8_detection`, `task.instance_segmentation` | — | Case A (candidate), Case D (candidate) |
| `task.yolo_classification` | Yolo Classification | Intermediate | `task.image_classification`, `cnn.backbone` | — | — |
| `task.small_object_detection` | Small Object Detection | Intermediate | `task.object_detection`, `cnn.multi_scale_feature` | — | — |
| `task.feature_pyramid` | Feature Pyramid | Intermediate | `cnn.feature_pyramid_network` | — | — |
| `task.mask_postprocessing` | Mask Postprocessing | Intermediate | `task.binary_mask`, `img.morphology` | — | — |
| `task.unet` | Unet | Intermediate | `task.semantic_segmentation`, `cnn.cnn_architecture` | — | — |
| `task.segment_anything_model` | Segment Anything Model | Intermediate | `task.instance_segmentation`, `dl.representation_learning` | — | — |
| `task.sam2` | SAM2 | Intermediate | `task.segment_anything_model`, `img.video_frame` | — | — |
| `task.grounding_dino` | Grounding DINO | Intermediate | `task.object_detection`, `research.clip` | — | — |
| `task.open_vocabulary_detection` | Open Vocabulary Detection | Intermediate | `task.object_detection`, `research.clip` | — | — |
| `task.object_localization` | Object Localization | Intermediate | `task.bounding_box` | — | — |
| `task.precision_recall_tradeoff` | Precision Recall Tradeoff | Intermediate | `eval.precision`, `eval.recall` | — | — |
| `ad.normal_abnormal_definition` | Normal Abnormal Definition | Advanced | `f.dataset` | — | — |
| `ad.novelty_detection` | Novelty Detection | Advanced | `ad.normal_abnormal_definition`, `ml.unsupervised_learning` | — | — |
| `ad.outlier_detection` | Outlier Detection | Advanced | `ad.normal_abnormal_definition`, `f.statistics` | — | — |
| `ad.one_class_classification` | One Class Classification | Advanced | `ad.novelty_detection`, `ml.classification` | — | — |
| `ad.reconstruction_based_ad` | Reconstruction Based Ad | Advanced | `ad.normal_abnormal_definition`, `dl.representation_learning` | — | — |
| `ad.feature_distance_based_ad` | Feature Distance Based Ad | Advanced | `ad.normal_abnormal_definition`, `cnn.feature_extraction`, `f.euclidean_distance` | — | — |
| `ad.k_nearest_neighbor` | K Nearest Neighbor | Advanced | `ad.feature_distance_based_ad` | — | — |
| `ad.mahalanobis_distance` | Mahalanobis Distance | Advanced | `f.matrix`, `f.variance`, `ad.feature_distance_based_ad` | — | — |
| `ad.memory_bank` | 메모리 뱅크 / Memory Bank | Advanced | `ad.feature_vector`, `ad.nearest_neighbor_search` | — | Case C (candidate) |
| `ad.patch_embedding` | 패치 임베딩 / Patch Embedding | Advanced | `cnn.feature_map`, `ad.embedding` | — | — |
| `ad.patchcore` | 패치코어 / PatchCore | Advanced | `ad.patch_embedding`, `ad.memory_bank`, `ad.nearest_neighbor_search` | — | Case C (candidate) |
| `ad.coreset_selection` | Coreset Selection | Advanced | `ad.memory_bank`, `ad.k_nearest_neighbor` | — | — |
| `ad.padim` | PaDiM | Advanced | `ad.patch_embedding`, `ad.mahalanobis_distance` | — | — |
| `ad.spade` | Spade | Advanced | `ad.feature_distance_based_ad` | — | — |
| `ad.stfpm` | STFPM | Advanced | `ad.feature_distance_based_ad` | — | — |
| `ad.efficientad` | EfficientAD | Advanced | `ad.feature_distance_based_ad` | — | — |
| `ad.deep_svdd` | Deep Svdd | Advanced | `ad.one_class_classification` | — | — |
| `ad.autoencoder` | Autoencoder | Advanced | `dl.representation_learning` | — | — |
| `ad.draem` | DRAEM | Advanced | `ad.reconstruction_based_ad` | — | — |
| `ad.fastflow` | Fastflow | Advanced | `ad.feature_distance_based_ad` | — | — |
| `ad.reverse_distillation` | Reverse Distillation | Advanced | `ad.feature_distance_based_ad` | — | — |
| `ad.anomaly_score` | Anomaly Score | Advanced | `ad.normal_abnormal_definition` | — | — |
| `ad.anomaly_heatmap` | Anomaly Heatmap | Advanced | `ad.patch_embedding`, `ad.anomaly_score` | — | Case C (candidate) |
| `ad.threshold_calibration` | Threshold Calibration | Advanced | `ad.anomaly_score`, `eval.precision`, `eval.recall` | — | — |
| `ad.domain_shift` | Domain Shift | Advanced | `ad.normal_abnormal_definition`, `ml.generalization` | — | — |
| `ad.few_shot_anomaly_detection` | Few Shot Anomaly Detection | Advanced | `ad.novelty_detection` | — | — |
| `ad.industrial_anomaly_detection` | Industrial Anomaly Detection | Advanced | `ad.normal_abnormal_definition` | — | — |
| `ad.embedding` | Embedding | Advanced | `dl.representation_learning` | — | — |
| `ad.feature_vector` | Feature Vector | Advanced | `ad.embedding`, `f.vector` | — | — |
| `ad.feature_normalization` | Feature Normalization | Advanced | `ad.feature_vector`, `f.statistics` | — | — |
| `ad.nearest_neighbor_search` | Nearest Neighbor Search | Advanced | `ad.k_nearest_neighbor` | — | — |
| `vid.frames_per_second` | Frames Per Second | Intermediate | `img.video_frame` | — | — |
| `vid.frame_sampling` | Frame Sampling | Intermediate | `vid.frames_per_second` | — | — |
| `vid.temporal_stride` | Temporal Stride | Intermediate | `vid.frame_sampling` | — | — |
| `vid.temporal_window` | Temporal Window | Intermediate | `vid.frame_sampling` | — | — |
| `vid.video_level_aggregation` | Video Level Aggregation | Intermediate | `vid.cnn_feature_sequence` | — | — |
| `vid.cnn_feature_sequence` | CNN Feature Sequence | Intermediate | `vid.temporal_window`, `cnn.feature_extraction` | — | — |
| `vid.recurrent_neural_network` | Recurrent Neural Network | Intermediate | `dl.multilayer_perceptron`, `vid.cnn_feature_sequence` | — | — |
| `vid.lstm` | LSTM | Intermediate | `vid.recurrent_neural_network` | — | — |
| `vid.gru` | GRU | Intermediate | `vid.recurrent_neural_network` | — | — |
| `vid.transformer` | Transformer | Intermediate | `dl.representation_learning`, `f.matrix_multiplication` | — | — |
| `vid.self_attention` | Self Attention | Intermediate | `vid.transformer` | — | — |
| `vid.positional_encoding` | Positional Encoding | Intermediate | `vid.transformer`, `vid.temporal_window` | — | — |
| `vid.temporal_transformer` | 시간적 트랜스포머 / Temporal Transformer | Intermediate | `vid.self_attention`, `vid.positional_encoding`, `vid.cnn_feature_sequence` | — | Case B (candidate) |
| `vid.three_dimensional_cnn` | Three Dimensional CNN | Intermediate | `cnn.convolution`, `vid.temporal_window` | — | — |
| `vid.convlstm` | Convlstm | Intermediate | `vid.lstm`, `cnn.convolution` | — | — |
| `vid.videomae` | Videomae | Intermediate | `vid.transformer`, `ml.self_supervised_learning` | — | — |
| `vid.video_classification` | Video Classification | Intermediate | `vid.video_level_aggregation`, `ml.classification` | — | Case B (candidate) |
| `vid.video_anomaly_detection` | Video Anomaly Detection | Intermediate | `vid.video_classification`, `ad.normal_abnormal_definition` | — | — |
| `vid.optical_flow` | Optical Flow | Intermediate | `vid.frame_sampling`, `geom.coordinate_system` | — | — |
| `vid.object_tracking` | Object Tracking | Intermediate | `task.object_detection`, `vid.temporal_window` | — | — |
| `vid.temporal_smoothing` | Temporal Smoothing | Intermediate | `vid.video_level_aggregation` | — | — |
| `vid.consecutive_frame_decision` | Consecutive Frame Decision | Intermediate | `vid.temporal_window` | — | — |
| `vid.persistence` | Persistence | Intermediate | `vid.consecutive_frame_decision` | — | — |
| `vid.hysteresis` | Hysteresis | Intermediate | `vid.persistence` | — | — |
| `vid.event_detection` | Event Detection | Intermediate | `vid.persistence` | — | — |
| `vid.temporal_leakage` | Temporal Leakage | Intermediate | `vid.temporal_window`, `ml.data_leakage` | — | — |
| `vid.source_video_group_split` | 원본 영상별 그룹 분할 / Source Video Group Split | Intermediate | `vid.temporal_leakage` | — | — |
| `vid.temporal_attention` | Temporal Attention | Intermediate | `vid.self_attention`, `vid.temporal_window` | — | — |
| `vid.video_decoding` | Video Decoding | Intermediate | `img.video_frame` | — | — |
| `geom.coordinate_system` | Coordinate System | Advanced | `f.vector` | — | — |
| `geom.geometric_transformation` | Geometric Transformation | Advanced | `geom.coordinate_system`, `f.matrix` | — | — |
| `geom.affine_transformation` | Affine Transformation | Advanced | `geom.geometric_transformation` | — | — |
| `geom.perspective_transformation` | Perspective Transformation | Advanced | `geom.geometric_transformation` | — | — |
| `geom.homography` | Homography | Advanced | `geom.perspective_transformation`, `f.matrix_multiplication` | — | Case E (candidate) |
| `geom.camera_calibration` | Camera Calibration | Advanced | `geom.homography` | — | — |
| `geom.camera_intrinsics` | Camera Intrinsics | Advanced | `geom.camera_calibration` | — | — |
| `geom.camera_extrinsics` | Camera Extrinsics | Advanced | `geom.camera_calibration` | — | — |
| `geom.lens_distortion` | Lens Distortion | Advanced | `geom.camera_intrinsics` | — | — |
| `geom.circle_geometry` | Circle Geometry | Advanced | `geom.coordinate_system` | — | — |
| `geom.ellipse_geometry` | Ellipse Geometry | Advanced | `geom.circle_geometry` | — | Case E (candidate) |
| `geom.ellipse_fitting` | 타원 피팅 / Ellipse Fitting | Advanced | `geom.ellipse_geometry`, `geom.least_squares` | — | Case D (candidate) |
| `geom.least_squares` | 최소제곱법 / Least Squares | Advanced | `f.matrix`, `f.mean` | — | — |
| `geom.closed_form_solution` | 닫힌해 / Closed Form Solution | Advanced | `geom.least_squares`, `f.linear_algebra` | — | — |
| `geom.eigenvalue_eigenvector` | Eigenvalue Eigenvector | Advanced | `f.matrix_multiplication` | — | — |
| `geom.singular_value_decomposition` | Singular Value Decomposition | Advanced | `f.matrix_multiplication` | — | — |
| `geom.principal_component_analysis` | Principal Component Analysis | Advanced | `geom.singular_value_decomposition`, `f.variance` | — | — |
| `geom.ransac` | Ransac | Advanced | `geom.least_squares`, `f.probability` | — | — |
| `geom.robust_fitting` | Robust Fitting | Advanced | `geom.ransac` | — | — |
| `geom.median_absolute_deviation` | Median Absolute Deviation | Advanced | `f.statistics` | — | — |
| `geom.subpixel_edge_detection` | Subpixel Edge Detection | Advanced | `img.edge_detection`, `geom.coordinate_system` | — | — |
| `geom.polygon_geometry` | Polygon Geometry | Advanced | `task.polygon` | — | — |
| `geom.mask_geometry` | Mask Geometry | Advanced | `task.binary_mask` | — | — |
| `geom.contour_smoothing` | Contour Smoothing | Advanced | `img.contour` | — | — |
| `geom.boundary_refinement` | Boundary Refinement | Advanced | `geom.contour_smoothing`, `geom.subpixel_edge_detection` | — | Case A (candidate) |
| `geom.radial_edge_scanning` | Radial Edge Scanning | Advanced | `geom.ellipse_geometry`, `geom.boundary_refinement` | — | Case D (candidate) |
| `geom.angle_bin_outlier_removal` | Angle Bin Outlier Removal | Advanced | `geom.radial_edge_scanning`, `geom.median_absolute_deviation` | — | — |
| `geom.camera_geometry` | Camera Geometry | Advanced | `geom.camera_intrinsics`, `geom.camera_extrinsics` | — | — |
| `geom.residual_analysis` | Residual Analysis | Advanced | `geom.least_squares`, `f.variance` | — | — |
| `geom.algebraic_vs_geometric_distance` | Algebraic Vs Geometric Distance | Advanced | `geom.ellipse_fitting`, `f.euclidean_distance` | — | — |
| `ts.time_series` | Time Series | Intermediate | `f.data` | — | — |
| `ts.trend` | Trend | Intermediate | `ts.time_series` | — | — |
| `ts.seasonality` | Seasonality | Intermediate | `ts.time_series` | — | — |
| `ts.measurement_noise` | Measurement Noise | Intermediate | `ts.time_series` | — | — |
| `ts.moving_average` | Moving Average | Intermediate | `ts.time_series`, `f.mean` | — | — |
| `ts.moving_median` | 이동 중앙값 / Moving Median | Intermediate | `ts.time_series`, `f.statistics` | — | Case F (candidate) |
| `ts.standard_deviation` | Standard Deviation | Intermediate | `f.standard_deviation`, `ts.time_series` | — | — |
| `ts.z_score` | Z Score | Intermediate | `ts.standard_deviation` | — | — |
| `ts.robust_statistics` | Robust Statistics | Intermediate | `ts.moving_median` | — | — |
| `ts.median_absolute_deviation` | Median Absolute Deviation | Intermediate | `ts.robust_statistics` | — | — |
| `ts.interquartile_range` | Interquartile Range | Intermediate | `ts.robust_statistics` | — | — |
| `ts.static_threshold` | Static Threshold | Intermediate | `ts.time_series` | — | — |
| `ts.adaptive_threshold` | Adaptive Threshold | Intermediate | `ts.moving_median`, `ts.static_threshold` | — | — |
| `ts.step_change_detection` | 계단형 변화 감지 / Step Change Detection | Intermediate | `ts.moving_median`, `ts.static_threshold` | — | Case F (candidate) |
| `ts.change_point_detection` | Change Point Detection | Intermediate | `ts.time_series`, `ts.step_change_detection` | — | — |
| `ts.persistence_rule` | Persistence Rule | Intermediate | `ts.step_change_detection` | — | Case F (candidate) |
| `ts.baseline_update` | Baseline Update | Intermediate | `ts.moving_median` | — | — |
| `ts.baseline_freeze` | 기준선 고정 / Baseline Freeze | Intermediate | `ts.baseline_update`, `ts.persistence_rule` | — | — |
| `ts.cusum` | Cusum | Intermediate | `ts.change_point_detection` | — | — |
| `ts.ewma` | Ewma | Intermediate | `ts.moving_average` | — | — |
| `ts.page_hinkley` | Page Hinkley | Intermediate | `ts.change_point_detection` | — | — |
| `ts.bayesian_change_point_detection` | Bayesian Change Point Detection | Intermediate | `ts.change_point_detection`, `f.conditional_probability` | — | — |
| `ts.pelt` | Pelt | Intermediate | `ts.change_point_detection` | — | — |
| `ts.concept_drift` | Concept Drift | Intermediate | `ts.change_point_detection`, `ml.generalization` | — | — |
| `ts.data_drift` | Data Drift | Intermediate | `ts.time_series` | — | — |
| `ts.false_alarm_control` | False Alarm Control | Intermediate | `ts.persistence_rule`, `eval.false_positive` | — | — |
| `ts.online_detection` | Online Detection | Intermediate | `ts.change_point_detection` | — | — |
| `ts.change_magnitude` | Change Magnitude | Intermediate | `ts.step_change_detection` | — | — |
| `ts.rolling_window` | Rolling Window | Intermediate | `ts.moving_average` | — | — |
| `data.image_annotation` | Image Annotation | Intermediate | `img.digital_image`, `f.label` | — | — |
| `data.labelme` | Labelme | Intermediate | `data.image_annotation` | — | — |
| `data.labelimg` | Labelimg | Intermediate | `data.image_annotation` | — | — |
| `data.label_studio` | Label Studio | Intermediate | `data.image_annotation` | — | — |
| `data.bounding_box_annotation` | Bounding Box Annotation | Intermediate | `data.image_annotation`, `task.bounding_box` | — | — |
| `data.polygon_annotation` | Polygon Annotation | Intermediate | `data.image_annotation`, `task.polygon` | — | — |
| `data.mask_annotation` | Mask Annotation | Intermediate | `data.image_annotation`, `task.binary_mask` | — | — |
| `data.coco_format` | Coco Format | Intermediate | `data.bounding_box_annotation` | — | — |
| `data.yolo_format` | Yolo Format | Intermediate | `data.bounding_box_annotation` | — | — |
| `data.auto_labeling` | Auto Labeling | Intermediate | `data.image_annotation`, `task.object_detection` | — | — |
| `data.dataset_cleaning` | Dataset Cleaning | Intermediate | `f.dataset` | — | — |
| `data.data_augmentation` | Data Augmentation | Intermediate | `f.dataset`, `ml.train_validation_test_split` | — | — |
| `data.mosaic` | Mosaic | Intermediate | `data.data_augmentation` | — | — |
| `data.mixup` | Mixup | Intermediate | `data.data_augmentation` | — | — |
| `data.cutmix` | Cutmix | Intermediate | `data.data_augmentation` | — | — |
| `data.class_imbalance` | Class Imbalance | Intermediate | `f.dataset`, `ml.classification` | — | — |
| `data.weighted_sampling` | Weighted Sampling | Intermediate | `data.class_imbalance` | — | — |
| `data.hard_negative_mining` | Hard Negative Mining | Intermediate | `data.class_imbalance`, `eval.false_positive` | — | — |
| `data.group_split` | 그룹 분할 / Group Split | Intermediate | `ml.train_validation_test_split` | — | — |
| `data.group_k_fold` | Group K Fold | Intermediate | `data.group_split`, `ml.cross_validation` | — | — |
| `data.temporal_split` | Temporal Split | Intermediate | `data.group_split`, `vid.temporal_window` | — | — |
| `data.data_leakage` | Data Leakage | Intermediate | `data.group_split`, `ml.data_leakage` | — | — |
| `data.domain_generalization` | Domain Generalization | Intermediate | `data.group_split`, `ml.generalization` | — | — |
| `data.ablation_study` | Ablation Study | Intermediate | `ml.evaluation_metric`, `ml.train_validation_test_split` | — | — |
| `data.reproducibility` | Reproducibility | Intermediate | `ml.train_validation_test_split` | — | — |
| `data.random_seed` | Random Seed | Intermediate | `data.reproducibility` | — | — |
| `data.dataset_versioning` | Dataset Versioning | Intermediate | `data.reproducibility` | — | — |
| `data.experiment_tracking` | Experiment Tracking | Intermediate | `data.reproducibility` | — | — |
| `data.label_quality` | Label Quality | Intermediate | `data.image_annotation` | — | — |
| `data.dataset_provenance` | Dataset Provenance | Intermediate | `data.reproducibility` | — | — |
| `data.annotation_holes` | Annotation Holes | Intermediate | `data.mask_annotation`, `data.polygon_annotation` | — | — |
| `eval.confusion_matrix` | 혼동행렬 / Confusion Matrix | Intermediate | `ml.classification`, `ml.evaluation_metric` | — | — |
| `eval.true_positive` | True Positive | Intermediate | `eval.confusion_matrix` | — | — |
| `eval.true_negative` | True Negative | Intermediate | `eval.confusion_matrix` | — | — |
| `eval.false_positive` | False Positive | Intermediate | `eval.confusion_matrix` | — | — |
| `eval.false_negative` | False Negative | Intermediate | `eval.confusion_matrix` | — | — |
| `eval.accuracy` | Accuracy | Intermediate | `eval.confusion_matrix` | — | — |
| `eval.precision` | 정밀도 / Precision | Intermediate | `eval.true_positive`, `eval.false_positive` | — | — |
| `eval.recall` | 재현율 / Recall | Intermediate | `eval.true_positive`, `eval.false_negative` | — | — |
| `eval.f1` | F1 | Intermediate | `eval.precision`, `eval.recall` | — | — |
| `eval.sensitivity` | Sensitivity | Intermediate | `eval.recall` | — | — |
| `eval.specificity` | Specificity | Intermediate | `eval.true_negative`, `eval.false_positive` | — | — |
| `eval.roc_curve` | Roc Curve | Intermediate | `eval.recall`, `eval.specificity` | — | — |
| `eval.roc_auc` | Roc Auc | Intermediate | `eval.roc_curve` | — | — |
| `eval.precision_recall_curve` | Precision Recall Curve | Intermediate | `eval.precision`, `eval.recall` | — | — |
| `eval.pr_auc` | Pr Auc | Intermediate | `eval.precision_recall_curve` | — | — |
| `eval.threshold_sweep` | Threshold Sweep | Intermediate | `eval.confusion_matrix` | — | — |
| `eval.intersection_over_union` | Intersection Over Union | Intermediate | `task.intersection_over_union` | — | — |
| `eval.mean_average_precision` | Mean Average Precision | Intermediate | `eval.precision_recall_curve`, `eval.intersection_over_union` | — | — |
| `eval.map50` | Map50 | Intermediate | `eval.mean_average_precision` | — | — |
| `eval.map50_95` | Map50 95 | Intermediate | `eval.mean_average_precision` | — | — |
| `eval.dice_coefficient` | Dice Coefficient | Intermediate | `task.binary_mask` | — | — |
| `eval.boundary_iou` | Boundary IoU | Intermediate | `eval.intersection_over_union`, `task.binary_mask` | — | — |
| `eval.average_symmetric_surface_distance` | Average Symmetric Surface Distance | Intermediate | `geom.boundary_refinement` | — | — |
| `eval.hausdorff_distance` | Hausdorff Distance | Intermediate | `geom.boundary_refinement` | — | — |
| `eval.hd95` | Hd95 | Intermediate | `eval.hausdorff_distance` | — | — |
| `eval.mean_absolute_error` | Mean Absolute Error | Intermediate | `dl.mean_absolute_error` | — | — |
| `eval.mean_squared_error` | Mean Squared Error | Intermediate | `dl.mean_squared_error` | — | — |
| `eval.root_mean_squared_error` | Root Mean Squared Error | Intermediate | `eval.mean_squared_error` | — | — |
| `eval.statistical_significance` | Statistical Significance | Intermediate | `f.probability`, `ml.evaluation_metric` | — | — |
| `eval.mann_whitney_u` | Mann Whitney U | Intermediate | `eval.statistical_significance` | — | — |
| `eval.effect_size` | Effect Size | Intermediate | `eval.statistical_significance` | — | — |
| `eval.confidence_interval` | Confidence Interval | Intermediate | `eval.statistical_significance` | — | — |
| `eval.bootstrap` | Bootstrap | Intermediate | `eval.confidence_interval` | — | — |
| `eval.error_analysis` | Error Analysis | Intermediate | `eval.confusion_matrix` | — | — |
| `eval.slice_based_evaluation` | Slice Based Evaluation | Intermediate | `eval.error_analysis` | — | — |
| `eval.calibration` | Calibration | Intermediate | `eval.confidence_interval`, `task.confidence_score` | — | — |
| `eval.uncertainty_estimation` | Uncertainty Estimation | Intermediate | `eval.calibration` | — | — |
| `ops.model_export` | Model Export | Advanced | `dl.model_training` | — | — |
| `ops.pytorch` | PyTorch | Advanced | `dl.model_training` | — | — |
| `ops.onnx` | ONNX | Advanced | `ops.model_export` | — | — |
| `ops.onnx_runtime` | ONNX Runtime | Advanced | `ops.onnx` | — | Case G (candidate) |
| `ops.tensorrt` | Tensorrt | Advanced | `ops.onnx`, `ops.cuda` | — | — |
| `ops.triton_inference_server` | Triton Inference Server | Advanced | `ops.onnx_runtime`, `ops.batch_inference` | — | Case G (candidate) |
| `ops.static_shape` | Static Shape | Advanced | `f.shape`, `ops.onnx` | — | — |
| `ops.dynamic_shape` | Dynamic Shape | Advanced | `ops.static_shape` | — | — |
| `ops.batch_inference` | Batch Inference | Advanced | `dl.batch` | — | — |
| `ops.latency` | Latency | Advanced | `ops.model_export` | — | — |
| `ops.throughput` | Throughput | Advanced | `ops.latency` | — | — |
| `ops.gpu_memory` | GPU Memory | Advanced | `dl.model_training` | — | — |
| `ops.cuda` | CUDA | Advanced | `f.python` | — | — |
| `ops.model_versioning` | Model Versioning | Advanced | `ops.model_export` | — | — |
| `ops.data_versioning` | Data Versioning | Advanced | `data.dataset_versioning` | — | — |
| `ops.experiment_tracking` | Experiment Tracking | Advanced | `data.experiment_tracking` | — | — |
| `ops.airflow` | Airflow | Advanced | `ops.ml_pipeline` | — | — |
| `ops.directed_acyclic_graph` | Directed Acyclic Graph | Advanced | `ops.ml_pipeline` | — | — |
| `ops.kafka` | Kafka | Advanced | `ts.online_detection` | — | Case F (candidate), Case G (candidate) |
| `ops.object_storage` | Object Storage | Advanced | `f.data` | — | — |
| `ops.s3` | S3 | Advanced | `ops.object_storage` | — | — |
| `ops.minio` | Minio | Advanced | `ops.object_storage` | — | Case G (candidate) |
| `ops.rtsp` | RTSP | Advanced | `vid.video_decoding` | — | Case G (candidate) |
| `ops.ffmpeg` | FFmpeg | Advanced | `vid.video_decoding` | — | — |
| `ops.timestamp` | Timestamp | Advanced | `img.video_frame` | — | — |
| `ops.ntp` | NTP | Advanced | `ops.timestamp` | — | — |
| `ops.clock_drift` | Clock Drift | Advanced | `ops.ntp` | — | — |
| `ops.logging` | Logging | Advanced | `eng.logging` | — | — |
| `ops.monitoring` | Monitoring | Advanced | `ops.logging` | — | — |
| `ops.alert_system` | Alert System | Advanced | `ops.monitoring` | — | — |
| `ops.ml_pipeline` | Ml Pipeline | Advanced | `dl.model_training`, `ops.model_export` | — | — |
| `ops.model_drift_monitoring` | Model Drift Monitoring | Advanced | `ops.monitoring`, `ts.data_drift` | — | — |
| `ops.ci_cd` | Ci Cd | Advanced | `eng.continuous_integration`, `ops.model_versioning` | — | — |
| `ops.model_registry` | Model Registry | Advanced | `ops.model_versioning` | — | — |
| `ops.preprocessing_contract` | Preprocessing Contract | Advanced | `img.image_tensor`, `ops.model_export` | — | — |
| `ops.inference_contract` | Inference Contract | Advanced | `ops.preprocessing_contract` | — | — |
| `ops.observability` | Observability | Advanced | `ops.monitoring` | — | — |
| `eng.python_project_structure` | Python Project Structure | Basic | `f.python` | — | — |
| `eng.virtual_environment` | Virtual Environment | Basic | `f.python` | — | — |
| `eng.package_management` | Package Management | Basic | `eng.virtual_environment` | — | — |
| `eng.dependency_management` | Dependency Management | Basic | `eng.package_management` | — | — |
| `eng.jupyter_notebook` | Jupyter Notebook | Basic | `f.python` | — | — |
| `eng.modular_design` | Modular Design | Basic | `eng.python_project_structure` | — | — |
| `eng.configuration_management` | Configuration Management | Basic | `eng.modular_design` | — | — |
| `eng.logging` | Logging | Basic | `eng.python_project_structure` | — | — |
| `eng.exception_handling` | Exception Handling | Basic | `eng.python_project_structure` | — | — |
| `eng.unit_testing` | Unit Testing | Basic | `eng.modular_design` | — | — |
| `eng.integration_testing` | Integration Testing | Basic | `eng.unit_testing` | — | — |
| `eng.regression_testing` | Regression Testing | Basic | `eng.integration_testing` | — | — |
| `eng.git` | Git | Basic | `eng.python_project_structure` | — | — |
| `eng.github` | Github | Basic | `eng.git` | — | — |
| `eng.branch` | Branch | Basic | `eng.git` | — | — |
| `eng.commit` | Commit | Basic | `eng.branch` | — | — |
| `eng.pull_request` | Pull Request | Basic | `eng.commit`, `eng.github` | — | — |
| `eng.code_review` | Code Review | Basic | `eng.pull_request` | — | — |
| `eng.documentation` | Documentation | Basic | `eng.python_project_structure` | — | — |
| `eng.reproducible_experiment` | Reproducible Experiment | Basic | `data.reproducibility`, `eng.dependency_management` | — | — |
| `eng.multi_agent_workflow` | Multi Agent Workflow | Basic | `eng.code_review` | — | — |
| `eng.planner` | Planner | Basic | `eng.multi_agent_workflow` | — | — |
| `eng.builder` | Builder | Basic | `eng.planner` | — | — |
| `eng.reviewer` | Reviewer | Basic | `eng.builder` | — | — |
| `eng.agent_orchestration` | Agent Orchestration | Basic | `eng.multi_agent_workflow` | — | — |
| `eng.independent_review` | Independent Review | Basic | `eng.code_review`, `eng.reviewer` | — | — |
| `eng.research_reproduction` | Research Reproduction | Basic | `eng.reproducible_experiment` | — | — |
| `eng.version_control` | Version Control | Basic | `eng.git` | — | — |
| `eng.test_fixture` | Test Fixture | Basic | `eng.unit_testing` | — | — |
| `eng.continuous_integration` | Continuous Integration | Basic | `eng.integration_testing`, `eng.github` | — | — |
| `research.vision_transformer` | 비전 트랜스포머 / Vision Transformer | Research | `vid.self_attention`, `img.image_tensor` | — | — |
| `research.self_supervised_representation_learning` | Self Supervised Representation Learning | Research | `ml.self_supervised_learning`, `dl.representation_learning` | — | — |
| `research.contrastive_learning` | Contrastive Learning | Research | `research.self_supervised_representation_learning` | — | — |
| `research.dino` | DINO | Research | `research.contrastive_learning`, `research.vision_transformer` | — | — |
| `research.dinov2` | DINOv2 | Research | `research.dino` | — | — |
| `research.clip` | CLIP | Research | `research.contrastive_learning`, `research.vision_transformer` | — | — |
| `research.foundation_models` | Foundation Models | Research | `research.self_supervised_representation_learning` | — | — |
| `research.multimodal_learning` | Multimodal Learning | Research | `research.foundation_models` | — | — |
| `research.open_set_recognition` | Open Set Recognition | Research | `ml.classification` | — | — |
| `research.out_of_distribution_detection` | Out Of Distribution Detection | Research | `ad.novelty_detection`, `research.open_set_recognition` | — | — |
| `research.continual_learning` | Continual Learning | Research | `dl.fine_tuning` | — | — |
| `research.domain_adaptation` | Domain Adaptation | Research | `ad.domain_shift` | — | — |
| `research.model_compression` | Model Compression | Research | `dl.model_training` | — | — |
| `research.quantization` | Quantization | Research | `research.model_compression` | — | — |
| `research.pruning` | Pruning | Research | `research.model_compression` | — | — |
| `research.knowledge_distillation` | Knowledge Distillation | Research | `research.model_compression` | — | — |
| `research.probabilistic_modeling` | Probabilistic Modeling | Research | `f.probability_distribution` | — | — |
| `research.variational_inference` | Variational Inference | Research | `research.probabilistic_modeling` | — | — |
| `research.advanced_anomaly_detection` | Advanced Anomaly Detection | Research | `ad.patchcore`, `research.self_supervised_representation_learning` | — | — |
| `research.recent_computer_vision_research` | Recent Computer Vision Research | Research | `research.vision_transformer` | — | — |
| `research.attention_mechanism` | Attention Mechanism | Research | `vid.self_attention` | — | — |
| `research.masked_image_modeling` | Masked Image Modeling | Research | `research.vision_transformer`, `ml.self_supervised_learning` | — | — |
| `research.distillation_loss` | Distillation Loss | Research | `research.knowledge_distillation`, `ml.loss_function` | — | — |
| `research.benchmarking` | Benchmarking | Research | `eval.error_analysis`, `data.reproducibility` | — | — |

## 출처·실무 상태 검증

프로젝트 Case A–G는 연결 예시이며 운영 완료·실험 성능을 보장하지 않는다. 지표는 Dataset/Split/Preprocessing/Metric/Settings/Run log/Commit 확인 뒤만 기록한다. 논문·코드·저자 주장·우리의 해석을 구분한다. 연구 논문 URL은 개별 노드의 `references` 에서 관리한다.
