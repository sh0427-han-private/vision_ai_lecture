# Vision AI Lecture · 성능 평가와 Backbone/Transfer 강의 개선 (2026-10-13)

## 적용 대상 및 의도

기존 웹 강의 99장을 유지하면서 AI Basics의 임계값·혼동행렬·Precision·Recall·Accuracy·F1 4장과 Vision AI의 Backbone/Head 2장·Transfer Learning/Freeze-Fine-tuning 2장, 총 **8개 Figure**를 교체했습니다.

- `docs/assets/lesson/lesson_threshold_score_decision.svg`
- `docs/assets/lesson/lesson_confusion_100cases.svg`
- `docs/assets/lesson/lesson_precision_recall_sharedcase.svg`
- `docs/assets/lesson/lesson_accuracy_f1_same100.svg`
- `docs/assets/lesson/lesson_backbone_head_roles.svg`
- `docs/assets/lesson/lesson_backbone_tensor_head_options.svg`
- `docs/assets/lesson/lesson_transfer_pretraining_to_task.svg`
- `docs/assets/lesson/lesson_transfer_freeze_vs_finetune.svg`

## 1. 동일 평가 데이터의 수치 연결

100개 샘플 평가에서 양성(Class 1)은 '불량'입니다.

| 항목 | 계산 | 값 |
|---|---|---|
| TP | 실제 불량 중 불량 판정 | 18 |
| FN | 실제 불량 중 정상 판정 | 2 |
| FP | 실제 정상 중 불량 판정 | 4 |
| TN | 실제 정상 중 정상 판정 | 76 |
| Precision | TP/(TP+FP) | 18/22 = 81.818…% |
| Recall | TP/(TP+FN) | 18/20 = 90.0% |
| Accuracy | (TP+TN)/100 | 94/100 = 94.0% |
| F1 | 2TP/(2TP+FP+FN) | 36/42 = 85.714…% |

Threshold 설명에 사용하는 '0.82'라는 **별도의 단일 예시 점수**는 위 100개 평가의 한 샘플이라고 주장하지 않습니다. Threshold가 바뀌면 판정·혼동행렬·Precision·Recall·F1이 함께 바뀔 수 있습니다. Threshold는 Validation에서 선택하고 독립 Test로 성능을 검증합니다.

별도의 불균형 예시는 '정상 95/불량 5' 또는 '불량이 1%일 때 모두 정상 예측' 등을 설명하기 위해 존재합니다. 동일 100개 혼동행렬의 실제 불량 비율 20%와 혼동하지 않게 강의에서 데이터 구성을 구분합니다.

## 2. Tensor와 모델 구조

예시 Backbone은 입력 224×224×3에서 공간 크기가 112×112 → 56×56 → 28×28 → 14×14로 감소하는 단순 구조입니다. 각 단계의 채널 수 64,128,192,256은 설계 예시이며 모든 Backbone의 필수 규격이 아닙니다.

Backbone이 특징을 추출한다는 일반적 역할과 Task Head가 최종 출력을 만드는 역할을 구분합니다.
- Classification: 분류 점수 (예: Pooling → Class logits)
- Detection: Box·Class·Score (Neck / detection head 사용 가능)
- Segmentation: Pixel Mask (Decoder / segmentation head 사용 가능)

세 Task Head는 **서로 다른 모델 구조의 선택 사례**로 그렸습니다. 하나의 모델이 반드시 세 출력을 동시에 만든다는 뜻은 아닙니다.

## 3. Transfer Learning

- 사전학습: 기존 데이터의 학습 Weight를 얻음
- 새 Task: Backbone Weight를 초기값으로 재사용하고 새 Head를 구성
- Freeze: Backbone Weight 고정, 새 Head 업데이트
- Fine-tuning: 일부 또는 전체 Backbone Weight 및 Head 업데이트

어느 쪽이 우수한지는 새 데이터의 양·도메인 차이·Validation/Test 결과로 판단하며, 항상 개선된다고 보장하지 않습니다.

## 4. 기술 검수 및 제작상의 한계

- `scripts/verify_curriculum_overhaul.py`에 동일 혼동행렬 100건, 분수·F1, Threshold 예시, Backbone의 출력 크기 예시와 SVG 연결 검사 추가
- `scripts/build_lesson_revision.py`, `docs/assets/lesson/manifest.json` 및 배포 HTML을 동기화
- `.github/workflows/visual-audit.yml`은 1920×1080 및 1366×768에서 전체 99장을 캡처합니다.

모든 새 도식은 계산·모델 역할을 설명하기 위한 **편집 가능한 SVG**입니다. 실제 관측 데이터, 모델 파라미터, 실험 성능을 나타내는 것은 아닙니다. 자동 HTML 레이아웃 검사는 SVG 내부 모든 요소의 간섭을 완전히 검출하지 않으므로, 해당 스크린샷을 추가 확인해야 합니다.

## 최종 브라우저 및 교육 Figure 검수 기록

- 최종 배포 페이지: https://sh0427-han.github.io/vision_ai_lecture/
- 1920×1080 및 1366×768, 99장씩 총 **198화면** Chromium 자동 렌더링 성공.
- 최종 시각 QA: https://github.com/sh0427-han/vision_ai_lecture/actions/runs/38346982908
- 결과: 자동 감지 문제 레코드 **0건**, 최소 fitScale **0.95**.
- 수정 대상 8개 웹 슬라이드(표지 포함): AI Basics 38–41, Vision AI 32–33 및 37–38.
- 1366×768의 각 슬라이드 실제 캡처를 확인함. 최초 기본 Backbone은 Conv 단계 숫자가 너무 작았으므로 기존 사과 사진을 사용한 **입력 사진 → 공통 Backbone → Task Head 세 가지 선택 예시**의 큰 그림으로 재수정하고 다시 캡처 확인.
- 전후 개편은 내용의 의미나 평가 건수를 바꾸지 않는 시각 교정임. 99장 전체 수식의 전문적 감수, 실제 프로젝터·모바일 렌더링, 임의 글꼴 대체까지 완전히 보증하는 것은 아님.

