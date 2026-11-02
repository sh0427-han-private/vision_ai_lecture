# 전체 AI/ML Curriculum · PART 00–14

> Draft v0.1 · **483개 concept ID / 661개 직접 선수 관계** · Independent Reviewer: PENDING. 실제 콘텐츠 구현을 의미하지 않는다.

## 설계 원칙

공통 기초(데이터, 수학, ML, DL) → Image Processing/CNN에서 Computer Vision·Anomaly·Video·Geometry·Time-series·MLOps로 분기한다. Dataset/Evaluation/Engineering은 각 경로에서 필요할 때 추가한다. PART 순서가 필수 선수지식의 직렬 순서는 아니다. 필수 관계는 [JSON](concepts.v1.json)을 정본으로 한다.

## PART별 범위와 최종 Gate

| PART | 분야 | 개념 수 | 완료 기준 |
|---|---|---:|---|
| 00 | Foundations | 44 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 01 | Machine Learning | 27 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 02 | Neural Networks | 36 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 03 | Digital Image | 42 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 04 | CNN | 29 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 05 | Vision Tasks | 27 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 06 | Anomaly Detection | 31 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 07 | Video AI | 29 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 08 | Geometry | 30 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 09 | Time-series | 29 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 10 | Dataset Design | 31 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 11 | Evaluation | 37 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 12 | MLOps | 37 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 13 | Engineering | 30 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |
| 14 | Advanced Research | 24 | 관련 입력·중간 처리·출력·한계를 대표 예제로 재현 |

## PART별 핵심 개념과 소개 순서

아래는 **초기 소개 순서**이고 직접 선행 개념은 [CONCEPT_CATALOG](CONCEPT_CATALOG.md)에 기재한다. 난이도는 같은 개념에서 단계별로 확장할 수 있다.

### PART 00 — Foundations

1. `f.artificial_intelligence` — Artificial Intelligence
2. `f.machine_learning` — Machine Learning
3. `f.deep_learning` — Deep Learning
4. `f.data` — 데이터
5. `f.sample` — Sample
6. `f.feature` — 특징
7. `f.label` — 정답 라벨
8. `f.dataset` — 데이터셋
9. `f.scalar` — 스칼라
10. `f.vector` — 벡터
11. `f.matrix` — 행렬
12. `f.tensor` — 텐서
13. `f.shape` — 형상
14. `f.dimension` — Dimension
15. `f.axis` — Axis
16. `f.broadcasting` — Broadcasting
17. `f.function` — Function
18. `f.linear_function` — Linear Function
19. `f.nonlinear_function` — Nonlinear Function
20. `f.sum` — Sum
21. `f.mean` — 평균
22. `f.variance` — 분산
23. `f.standard_deviation` — 표준편차
24. `f.statistics` — Statistics
25. `f.probability` — Probability
26. `f.probability_distribution` — Probability Distribution
27. `f.normal_distribution` — Normal Distribution
28. `f.conditional_probability` — Conditional Probability
29. `f.derivative` — Derivative
30. `f.partial_derivative` — Partial Derivative
31. `f.gradient` — 기울기
32. `f.chain_rule` — Chain Rule
33. `f.linear_algebra` — Linear Algebra
34. `f.dot_product` — 내적
35. `f.matrix_multiplication` — Matrix Multiplication
36. `f.distance_metric` — Distance Metric
37. `f.euclidean_distance` — 유클리드 거리
38. `f.cosine_similarity` — Cosine Similarity
39. `f.python` — Python
40. `f.numpy` — Numpy
41. `f.matplotlib` — Matplotlib
42. `f.array_indexing` — Array Indexing
43. `f.slicing` — Slicing
44. `f.data_type` — Data Type


### PART 01 — Machine Learning

1. `ml.supervised_learning` — 지도학습
2. `ml.unsupervised_learning` — 비지도학습
3. `ml.self_supervised_learning` — Self Supervised Learning
4. `ml.semi_supervised_learning` — Semi Supervised Learning
5. `ml.classification` — Classification
6. `ml.regression` — Regression
7. `ml.binary_classification` — Binary Classification
8. `ml.multiclass_classification` — Multiclass Classification
9. `ml.multilabel_classification` — Multilabel Classification
10. `ml.feature_engineering` — Feature Engineering
11. `ml.linear_regression` — Linear Regression
12. `ml.logistic_regression` — Logistic Regression
13. `ml.decision_boundary` — Decision Boundary
14. `ml.linear_separability` — Linear Separability
15. `ml.underfitting` — Underfitting
16. `ml.overfitting` — Overfitting
17. `ml.bias_variance_tradeoff` — Bias Variance Tradeoff
18. `ml.generalization` — Generalization
19. `ml.train_validation_test_split` — 학습·검증·테스트 분할
20. `ml.cross_validation` — Cross Validation
21. `ml.data_leakage` — 데이터 누수
22. `ml.model_parameter` — Model Parameter
23. `ml.hyperparameter` — Hyperparameter
24. `ml.loss_function` — 손실 함수
25. `ml.evaluation_metric` — Evaluation Metric
26. `ml.gradient_descent` — 경사하강법
27. `ml.learning_rate` — Learning Rate


### PART 02 — Neural Networks

1. `dl.perceptron` — 퍼셉트론
2. `dl.and_or_xor` — And Or Xor
3. `dl.multilayer_perceptron` — Multilayer Perceptron
4. `dl.fully_connected_layer` — Fully Connected Layer
5. `dl.weight` — Weight
6. `dl.bias` — Bias
7. `dl.activation_function` — 활성화 함수
8. `dl.relu` — Relu
9. `dl.sigmoid` — Sigmoid
10. `dl.tanh` — Tanh
11. `dl.softmax` — Softmax
12. `dl.forward_propagation` — 순전파
13. `dl.backpropagation` — 역전파
14. `dl.neural_chain_rule` — Neural Chain Rule
15. `dl.cross_entropy` — Cross Entropy
16. `dl.binary_cross_entropy` — Binary Cross Entropy
17. `dl.mean_squared_error` — Mean Squared Error
18. `dl.mean_absolute_error` — Mean Absolute Error
19. `dl.sgd` — Sgd
20. `dl.momentum` — Momentum
21. `dl.adam` — Adam
22. `dl.adamw` — AdamW
23. `dl.batch` — Batch
24. `dl.iteration` — Iteration
25. `dl.epoch` — Epoch
26. `dl.batch_normalization` — Batch Normalization
27. `dl.dropout` — Dropout
28. `dl.weight_decay` — Weight Decay
29. `dl.early_stopping` — Early Stopping
30. `dl.learning_rate_scheduler` — Learning Rate Scheduler
31. `dl.residual_connection` — Residual Connection
32. `dl.representation_learning` — Representation Learning
33. `dl.transfer_learning` — Transfer Learning
34. `dl.fine_tuning` — Fine Tuning
35. `dl.model_training` — Model Training
36. `dl.computational_graph` — Computational Graph


### PART 03 — Digital Image

1. `img.digital_image` — 디지털 이미지
2. `img.pixel` — 픽셀
3. `img.rgb` — RGB
4. `img.bgr` — BGR
5. `img.image_resolution` — Image Resolution
6. `img.channel` — Channel
7. `img.bit_depth` — Bit Depth
8. `img.grayscale` — Grayscale
9. `img.hsv` — Hsv
10. `img.color_space` — Color Space
11. `img.image_tensor` — 이미지 텐서
12. `img.resize` — Resize
13. `img.crop` — Crop
14. `img.interpolation` — Interpolation
15. `img.region_of_interest` — Region Of Interest
16. `img.image_histogram` — Image Histogram
17. `img.gaussian_blur` — Gaussian Blur
18. `img.median_filter` — Median Filter
19. `img.sobel` — Sobel
20. `img.laplacian` — Laplacian
21. `img.edge_detection` — Edge Detection
22. `img.sharpening` — Sharpening
23. `img.noise` — Noise
24. `img.illumination` — Illumination
25. `img.reflection` — Reflection
26. `img.thresholding` — Thresholding
27. `img.binary_image` — Binary Image
28. `img.morphology` — Morphology
29. `img.erosion` — Erosion
30. `img.dilation` — Dilation
31. `img.opening` — Opening
32. `img.closing` — Closing
33. `img.contour` — Contour
34. `img.connected_component` — Connected Component
35. `img.distance_transform` — Distance Transform
36. `img.image_quality` — Image Quality
37. `img.blur_detection` — Blur Detection
38. `img.fft` — Fft
39. `img.dct` — Dct
40. `img.opencv` — OpenCV
41. `img.spatial_filter_kernel` — 공간 필터 커널
42. `img.video_frame` — Video Frame


### PART 04 — CNN

1. `cnn.local_connectivity` — Local Connectivity
2. `cnn.weight_sharing` — Weight Sharing
3. `cnn.kernel` — CNN 커널
4. `cnn.convolution` — 합성곱
5. `cnn.stride` — 스트라이드
6. `cnn.padding` — 패딩
7. `cnn.convolution_output_shape` — Convolution Output Shape
8. `cnn.feature_map` — 특징 맵
9. `cnn.feature_channel` — Feature Channel
10. `cnn.receptive_field` — Receptive Field
11. `cnn.pooling` — 풀링
12. `cnn.downsampling` — Downsampling
13. `cnn.feature_hierarchy` — Feature Hierarchy
14. `cnn.cnn_architecture` — CNN 구조
15. `cnn.backbone` — Backbone
16. `cnn.neck` — Neck
17. `cnn.head` — Head
18. `cnn.vgg` — Vgg
19. `cnn.resnet` — Resnet
20. `cnn.efficientnet` — Efficientnet
21. `cnn.feature_extraction` — Feature Extraction
22. `cnn.multi_scale_feature` — Multi Scale Feature
23. `cnn.feature_pyramid_network` — Feature Pyramid Network
24. `cnn.pretrained_backbone` — Pretrained Backbone
25. `cnn.transfer_learning` — Transfer Learning
26. `cnn.fine_tuning` — Fine Tuning
27. `cnn.dilated_convolution` — Dilated Convolution
28. `cnn.group_convolution` — Group Convolution
29. `cnn.depthwise_separable_convolution` — Depthwise Separable Convolution


### PART 05 — Vision Tasks

1. `task.image_classification` — Image Classification
2. `task.object_detection` — Object Detection
3. `task.semantic_segmentation` — Semantic Segmentation
4. `task.instance_segmentation` — Instance Segmentation
5. `task.panoptic_segmentation` — Panoptic Segmentation
6. `task.bounding_box` — Bounding Box
7. `task.polygon` — Polygon
8. `task.binary_mask` — Binary Mask
9. `task.confidence_score` — Confidence Score
10. `task.intersection_over_union` — Intersection Over Union
11. `task.non_maximum_suppression` — Non Maximum Suppression
12. `task.one_stage_detector` — One Stage Detector
13. `task.two_stage_detector` — Two Stage Detector
14. `task.yolo_architecture` — Yolo Architecture
15. `task.yolov8_detection` — YOLOv8 Detection
16. `task.yolov8_segmentation` — YOLOv8 Segmentation
17. `task.yolo_classification` — Yolo Classification
18. `task.small_object_detection` — Small Object Detection
19. `task.feature_pyramid` — Feature Pyramid
20. `task.mask_postprocessing` — Mask Postprocessing
21. `task.unet` — Unet
22. `task.segment_anything_model` — Segment Anything Model
23. `task.sam2` — SAM2
24. `task.grounding_dino` — Grounding DINO
25. `task.open_vocabulary_detection` — Open Vocabulary Detection
26. `task.object_localization` — Object Localization
27. `task.precision_recall_tradeoff` — Precision Recall Tradeoff


### PART 06 — Anomaly Detection

1. `ad.normal_abnormal_definition` — Normal Abnormal Definition
2. `ad.novelty_detection` — Novelty Detection
3. `ad.outlier_detection` — Outlier Detection
4. `ad.one_class_classification` — One Class Classification
5. `ad.reconstruction_based_ad` — Reconstruction Based Ad
6. `ad.feature_distance_based_ad` — Feature Distance Based Ad
7. `ad.k_nearest_neighbor` — K Nearest Neighbor
8. `ad.mahalanobis_distance` — Mahalanobis Distance
9. `ad.memory_bank` — 메모리 뱅크
10. `ad.patch_embedding` — 패치 임베딩
11. `ad.patchcore` — 패치코어
12. `ad.coreset_selection` — Coreset Selection
13. `ad.padim` — PaDiM
14. `ad.spade` — Spade
15. `ad.stfpm` — STFPM
16. `ad.efficientad` — EfficientAD
17. `ad.deep_svdd` — Deep Svdd
18. `ad.autoencoder` — Autoencoder
19. `ad.draem` — DRAEM
20. `ad.fastflow` — Fastflow
21. `ad.reverse_distillation` — Reverse Distillation
22. `ad.anomaly_score` — Anomaly Score
23. `ad.anomaly_heatmap` — Anomaly Heatmap
24. `ad.threshold_calibration` — Threshold Calibration
25. `ad.domain_shift` — Domain Shift
26. `ad.few_shot_anomaly_detection` — Few Shot Anomaly Detection
27. `ad.industrial_anomaly_detection` — Industrial Anomaly Detection
28. `ad.embedding` — Embedding
29. `ad.feature_vector` — Feature Vector
30. `ad.feature_normalization` — Feature Normalization
31. `ad.nearest_neighbor_search` — Nearest Neighbor Search


### PART 07 — Video AI

1. `vid.frames_per_second` — Frames Per Second
2. `vid.frame_sampling` — Frame Sampling
3. `vid.temporal_stride` — Temporal Stride
4. `vid.temporal_window` — Temporal Window
5. `vid.video_level_aggregation` — Video Level Aggregation
6. `vid.cnn_feature_sequence` — CNN Feature Sequence
7. `vid.recurrent_neural_network` — Recurrent Neural Network
8. `vid.lstm` — LSTM
9. `vid.gru` — GRU
10. `vid.transformer` — Transformer
11. `vid.self_attention` — Self Attention
12. `vid.positional_encoding` — Positional Encoding
13. `vid.temporal_transformer` — 시간적 트랜스포머
14. `vid.three_dimensional_cnn` — Three Dimensional CNN
15. `vid.convlstm` — Convlstm
16. `vid.videomae` — Videomae
17. `vid.video_classification` — Video Classification
18. `vid.video_anomaly_detection` — Video Anomaly Detection
19. `vid.optical_flow` — Optical Flow
20. `vid.object_tracking` — Object Tracking
21. `vid.temporal_smoothing` — Temporal Smoothing
22. `vid.consecutive_frame_decision` — Consecutive Frame Decision
23. `vid.persistence` — Persistence
24. `vid.hysteresis` — Hysteresis
25. `vid.event_detection` — Event Detection
26. `vid.temporal_leakage` — Temporal Leakage
27. `vid.source_video_group_split` — 원본 영상별 그룹 분할
28. `vid.temporal_attention` — Temporal Attention
29. `vid.video_decoding` — Video Decoding


### PART 08 — Geometry

1. `geom.coordinate_system` — Coordinate System
2. `geom.geometric_transformation` — Geometric Transformation
3. `geom.affine_transformation` — Affine Transformation
4. `geom.perspective_transformation` — Perspective Transformation
5. `geom.homography` — Homography
6. `geom.camera_calibration` — Camera Calibration
7. `geom.camera_intrinsics` — Camera Intrinsics
8. `geom.camera_extrinsics` — Camera Extrinsics
9. `geom.lens_distortion` — Lens Distortion
10. `geom.circle_geometry` — Circle Geometry
11. `geom.ellipse_geometry` — Ellipse Geometry
12. `geom.ellipse_fitting` — 타원 피팅
13. `geom.least_squares` — 최소제곱법
14. `geom.closed_form_solution` — 닫힌해
15. `geom.eigenvalue_eigenvector` — Eigenvalue Eigenvector
16. `geom.singular_value_decomposition` — Singular Value Decomposition
17. `geom.principal_component_analysis` — Principal Component Analysis
18. `geom.ransac` — Ransac
19. `geom.robust_fitting` — Robust Fitting
20. `geom.median_absolute_deviation` — Median Absolute Deviation
21. `geom.subpixel_edge_detection` — Subpixel Edge Detection
22. `geom.polygon_geometry` — Polygon Geometry
23. `geom.mask_geometry` — Mask Geometry
24. `geom.contour_smoothing` — Contour Smoothing
25. `geom.boundary_refinement` — Boundary Refinement
26. `geom.radial_edge_scanning` — Radial Edge Scanning
27. `geom.angle_bin_outlier_removal` — Angle Bin Outlier Removal
28. `geom.camera_geometry` — Camera Geometry
29. `geom.residual_analysis` — Residual Analysis
30. `geom.algebraic_vs_geometric_distance` — Algebraic Vs Geometric Distance


### PART 09 — Time-series

1. `ts.time_series` — Time Series
2. `ts.trend` — Trend
3. `ts.seasonality` — Seasonality
4. `ts.measurement_noise` — Measurement Noise
5. `ts.moving_average` — Moving Average
6. `ts.moving_median` — 이동 중앙값
7. `ts.standard_deviation` — Standard Deviation
8. `ts.z_score` — Z Score
9. `ts.robust_statistics` — Robust Statistics
10. `ts.median_absolute_deviation` — Median Absolute Deviation
11. `ts.interquartile_range` — Interquartile Range
12. `ts.static_threshold` — Static Threshold
13. `ts.adaptive_threshold` — Adaptive Threshold
14. `ts.step_change_detection` — 계단형 변화 감지
15. `ts.change_point_detection` — Change Point Detection
16. `ts.persistence_rule` — Persistence Rule
17. `ts.baseline_update` — Baseline Update
18. `ts.baseline_freeze` — 기준선 고정
19. `ts.cusum` — Cusum
20. `ts.ewma` — Ewma
21. `ts.page_hinkley` — Page Hinkley
22. `ts.bayesian_change_point_detection` — Bayesian Change Point Detection
23. `ts.pelt` — Pelt
24. `ts.concept_drift` — Concept Drift
25. `ts.data_drift` — Data Drift
26. `ts.false_alarm_control` — False Alarm Control
27. `ts.online_detection` — Online Detection
28. `ts.change_magnitude` — Change Magnitude
29. `ts.rolling_window` — Rolling Window


### PART 10 — Dataset Design

1. `data.image_annotation` — Image Annotation
2. `data.labelme` — Labelme
3. `data.labelimg` — Labelimg
4. `data.label_studio` — Label Studio
5. `data.bounding_box_annotation` — Bounding Box Annotation
6. `data.polygon_annotation` — Polygon Annotation
7. `data.mask_annotation` — Mask Annotation
8. `data.coco_format` — Coco Format
9. `data.yolo_format` — Yolo Format
10. `data.auto_labeling` — Auto Labeling
11. `data.dataset_cleaning` — Dataset Cleaning
12. `data.data_augmentation` — Data Augmentation
13. `data.mosaic` — Mosaic
14. `data.mixup` — Mixup
15. `data.cutmix` — Cutmix
16. `data.class_imbalance` — Class Imbalance
17. `data.weighted_sampling` — Weighted Sampling
18. `data.hard_negative_mining` — Hard Negative Mining
19. `data.group_split` — 그룹 분할
20. `data.group_k_fold` — Group K Fold
21. `data.temporal_split` — Temporal Split
22. `data.data_leakage` — Data Leakage
23. `data.domain_generalization` — Domain Generalization
24. `data.ablation_study` — Ablation Study
25. `data.reproducibility` — Reproducibility
26. `data.random_seed` — Random Seed
27. `data.dataset_versioning` — Dataset Versioning
28. `data.experiment_tracking` — Experiment Tracking
29. `data.label_quality` — Label Quality
30. `data.dataset_provenance` — Dataset Provenance
31. `data.annotation_holes` — Annotation Holes


### PART 11 — Evaluation

1. `eval.confusion_matrix` — 혼동행렬
2. `eval.true_positive` — True Positive
3. `eval.true_negative` — True Negative
4. `eval.false_positive` — False Positive
5. `eval.false_negative` — False Negative
6. `eval.accuracy` — Accuracy
7. `eval.precision` — 정밀도
8. `eval.recall` — 재현율
9. `eval.f1` — F1
10. `eval.sensitivity` — Sensitivity
11. `eval.specificity` — Specificity
12. `eval.roc_curve` — Roc Curve
13. `eval.roc_auc` — Roc Auc
14. `eval.precision_recall_curve` — Precision Recall Curve
15. `eval.pr_auc` — Pr Auc
16. `eval.threshold_sweep` — Threshold Sweep
17. `eval.intersection_over_union` — Intersection Over Union
18. `eval.mean_average_precision` — Mean Average Precision
19. `eval.map50` — Map50
20. `eval.map50_95` — Map50 95
21. `eval.dice_coefficient` — Dice Coefficient
22. `eval.boundary_iou` — Boundary IoU
23. `eval.average_symmetric_surface_distance` — Average Symmetric Surface Distance
24. `eval.hausdorff_distance` — Hausdorff Distance
25. `eval.hd95` — Hd95
26. `eval.mean_absolute_error` — Mean Absolute Error
27. `eval.mean_squared_error` — Mean Squared Error
28. `eval.root_mean_squared_error` — Root Mean Squared Error
29. `eval.statistical_significance` — Statistical Significance
30. `eval.mann_whitney_u` — Mann Whitney U
31. `eval.effect_size` — Effect Size
32. `eval.confidence_interval` — Confidence Interval
33. `eval.bootstrap` — Bootstrap
34. `eval.error_analysis` — Error Analysis
35. `eval.slice_based_evaluation` — Slice Based Evaluation
36. `eval.calibration` — Calibration
37. `eval.uncertainty_estimation` — Uncertainty Estimation


### PART 12 — MLOps

1. `ops.model_export` — Model Export
2. `ops.pytorch` — PyTorch
3. `ops.onnx` — ONNX
4. `ops.onnx_runtime` — ONNX Runtime
5. `ops.tensorrt` — Tensorrt
6. `ops.triton_inference_server` — Triton Inference Server
7. `ops.static_shape` — Static Shape
8. `ops.dynamic_shape` — Dynamic Shape
9. `ops.batch_inference` — Batch Inference
10. `ops.latency` — Latency
11. `ops.throughput` — Throughput
12. `ops.gpu_memory` — GPU Memory
13. `ops.cuda` — CUDA
14. `ops.model_versioning` — Model Versioning
15. `ops.data_versioning` — Data Versioning
16. `ops.experiment_tracking` — Experiment Tracking
17. `ops.airflow` — Airflow
18. `ops.directed_acyclic_graph` — Directed Acyclic Graph
19. `ops.kafka` — Kafka
20. `ops.object_storage` — Object Storage
21. `ops.s3` — S3
22. `ops.minio` — Minio
23. `ops.rtsp` — RTSP
24. `ops.ffmpeg` — FFmpeg
25. `ops.timestamp` — Timestamp
26. `ops.ntp` — NTP
27. `ops.clock_drift` — Clock Drift
28. `ops.logging` — Logging
29. `ops.monitoring` — Monitoring
30. `ops.alert_system` — Alert System
31. `ops.ml_pipeline` — Ml Pipeline
32. `ops.model_drift_monitoring` — Model Drift Monitoring
33. `ops.ci_cd` — Ci Cd
34. `ops.model_registry` — Model Registry
35. `ops.preprocessing_contract` — Preprocessing Contract
36. `ops.inference_contract` — Inference Contract
37. `ops.observability` — Observability


### PART 13 — Engineering

1. `eng.python_project_structure` — Python Project Structure
2. `eng.virtual_environment` — Virtual Environment
3. `eng.package_management` — Package Management
4. `eng.dependency_management` — Dependency Management
5. `eng.jupyter_notebook` — Jupyter Notebook
6. `eng.modular_design` — Modular Design
7. `eng.configuration_management` — Configuration Management
8. `eng.logging` — Logging
9. `eng.exception_handling` — Exception Handling
10. `eng.unit_testing` — Unit Testing
11. `eng.integration_testing` — Integration Testing
12. `eng.regression_testing` — Regression Testing
13. `eng.git` — Git
14. `eng.github` — Github
15. `eng.branch` — Branch
16. `eng.commit` — Commit
17. `eng.pull_request` — Pull Request
18. `eng.code_review` — Code Review
19. `eng.documentation` — Documentation
20. `eng.reproducible_experiment` — Reproducible Experiment
21. `eng.multi_agent_workflow` — Multi Agent Workflow
22. `eng.planner` — Planner
23. `eng.builder` — Builder
24. `eng.reviewer` — Reviewer
25. `eng.agent_orchestration` — Agent Orchestration
26. `eng.independent_review` — Independent Review
27. `eng.research_reproduction` — Research Reproduction
28. `eng.version_control` — Version Control
29. `eng.test_fixture` — Test Fixture
30. `eng.continuous_integration` — Continuous Integration


### PART 14 — Advanced Research

1. `research.vision_transformer` — 비전 트랜스포머
2. `research.self_supervised_representation_learning` — Self Supervised Representation Learning
3. `research.contrastive_learning` — Contrastive Learning
4. `research.dino` — DINO
5. `research.dinov2` — DINOv2
6. `research.clip` — CLIP
7. `research.foundation_models` — Foundation Models
8. `research.multimodal_learning` — Multimodal Learning
9. `research.open_set_recognition` — Open Set Recognition
10. `research.out_of_distribution_detection` — Out Of Distribution Detection
11. `research.continual_learning` — Continual Learning
12. `research.domain_adaptation` — Domain Adaptation
13. `research.model_compression` — Model Compression
14. `research.quantization` — Quantization
15. `research.pruning` — Pruning
16. `research.knowledge_distillation` — Knowledge Distillation
17. `research.probabilistic_modeling` — Probabilistic Modeling
18. `research.variational_inference` — Variational Inference
19. `research.advanced_anomaly_detection` — Advanced Anomaly Detection
20. `research.recent_computer_vision_research` — Recent Computer Vision Research
21. `research.attention_mechanism` — Attention Mechanism
22. `research.masked_image_modeling` — Masked Image Modeling
23. `research.distillation_loss` — Distillation Loss
24. `research.benchmarking` — Benchmarking



## 콘텐츠 확장

각 개념은 Why → Intuition → Definition → Mechanism → Mathematics → Implementation → Application → Limitations → Related 순서로 정리한다. 신규 필수 용어가 발생하면 중복 ID를 검사하고 적절한 PART에 추가하여 DAG·학습 경로를 함께 갱신한다. 학술 원문·실무 구현 근거 없는 수치나 SOTA 지위를 주장하지 않는다.
