# Learning Paths · 분기형 학습

> 초기 추천 읽기 순서. **실제 신규 HTML 페이지는 아직 없음**. 경로에서 생략된 직접·전이 선수 관계는 [Concept DAG](CONCEPT_DEPENDENCIES.md)로 보충한다.

## vertical_slice

1. `img.digital_image` — 디지털 이미지
2. `img.pixel` — 픽셀
3. `img.rgb` — RGB
4. `f.vector` — 벡터
5. `f.matrix` — 행렬
6. `f.tensor` — 텐서
7. `img.image_tensor` — 이미지 텐서
8. `img.spatial_filter_kernel` — 공간 필터 커널
9. `cnn.kernel` — CNN 커널
10. `cnn.convolution` — 합성곱
11. `cnn.feature_map` — 특징 맵
12. `cnn.pooling` — 풀링
13. `cnn.cnn_architecture` — CNN 구조


## cv

1. `img.image_tensor` — 이미지 텐서
2. `cnn.convolution` — 합성곱
3. `cnn.cnn_architecture` — CNN 구조
4. `task.object_detection` — Object Detection
5. `task.instance_segmentation` — Instance Segmentation
6. `task.yolov8_segmentation` — YOLOv8 Segmentation


## anomaly

1. `ad.normal_abnormal_definition` — Normal Abnormal Definition
2. `cnn.feature_extraction` — Feature Extraction
3. `ad.embedding` — Embedding
4. `ad.feature_vector` — Feature Vector
5. `ad.nearest_neighbor_search` — Nearest Neighbor Search
6. `ad.memory_bank` — 메모리 뱅크
7. `ad.patch_embedding` — 패치 임베딩
8. `ad.patchcore` — 패치코어
9. `ad.anomaly_heatmap` — Anomaly Heatmap


## video

1. `img.video_frame` — Video Frame
2. `vid.frames_per_second` — Frames Per Second
3. `vid.frame_sampling` — Frame Sampling
4. `vid.temporal_window` — Temporal Window
5. `vid.cnn_feature_sequence` — CNN Feature Sequence
6. `vid.self_attention` — Self Attention
7. `vid.temporal_transformer` — 시간적 트랜스포머
8. `vid.source_video_group_split` — 원본 영상별 그룹 분할


## geometry

1. `geom.coordinate_system` — Coordinate System
2. `geom.ellipse_geometry` — Ellipse Geometry
3. `geom.least_squares` — 최소제곱법
4. `geom.ellipse_fitting` — 타원 피팅
5. `geom.radial_edge_scanning` — Radial Edge Scanning
6. `geom.angle_bin_outlier_removal` — Angle Bin Outlier Removal


## timeseries

1. `ts.time_series` — Time Series
2. `ts.moving_median` — 이동 중앙값
3. `ts.static_threshold` — Static Threshold
4. `ts.step_change_detection` — 계단형 변화 감지
5. `ts.persistence_rule` — Persistence Rule
6. `ts.baseline_freeze` — 기준선 고정


## mlops

1. `vid.video_decoding` — Video Decoding
2. `ops.rtsp` — RTSP
3. `ops.ffmpeg` — FFmpeg
4. `ops.onnx` — ONNX
5. `ops.triton_inference_server` — Triton Inference Server
6. `ops.kafka` — Kafka
7. `ops.airflow` — Airflow



## 학습 경로 선택

입문: Data/Vector/Matrix/Tensor → Pixel/RGB/Image Tensor → CNN 수치 원리. CV: Classification/Detection/Segmentation, Label과 IoU. Anomaly: Patch Embedding/Memory Bank/Nearest Neighbor → Score/Heatmap. Video: FPS/T/Frame Sampling → GRU/Attention/Temporal Transformer와 Source Video Group Split. Geometry: 좌표·Edge·MAD·Ellipse. Time-series: Moving Median→Step Change→Persistence→Freeze. MLOps: RTSP/Decode→Preprocess→ONNX/Triton→Kafka/Storage/Monitoring.

**Vertical Slice 학습 Gate:** 4×4×3=48개의 **성분값**과 16 Pixel을 구분, 5×5 단일 채널/3×3 Kernel/S1/P0/D1 출력이 3×3임을 계산, `(N,Cin,H,W)`→`(N,Cout,Hout,Wout)` 구조를 설명하고, 고정 필터의 계산과 학습된 Kernel을 혼동하지 않는다.
