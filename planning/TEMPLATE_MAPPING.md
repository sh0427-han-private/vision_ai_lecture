# Design Template Mapping — 8종 패턴 활용

> 레퍼런스: [sh0427-han/design-template-library](https://github.com/sh0427-han/design-template-library) (읽기 전용). 참조 규격: `DESIGN_SYSTEM.md`, `TEMPLATE_CATALOG.md`, `docs/REFERENCE_REUSE_WORKFLOW.md`, `docs/FIGURE_PRODUCTION_STANDARD.md`, `docs/DESIGN_COMPONENT_RECIPES.md`, `docs/REFERENCE_PAGE_SPECS.md`. 실제 원본 `templates/html/`을 확인한 설계. 신규 렌더링은 미수행.

| 패턴 | 원본 HTML | 학습 활용 | 보존할 구성 원리 | 새 학습 예제에서 재계산 |
|---|---|---|---|---|
| 01 Concept | `concept.html` | Pixel→RGB→Tensor, Feature | 동일 이미지/좌표의 확대·3채널 대응 | 다른 사진/ROI/크기/채널·값 |
| 02 Process | `process.html` | Train/Inference, YOLO 추론 | Input/Process/Output의 역할·화살표 정렬 | 단계/라벨/출력 종류·점수 |
| 03 Comparison | `comparison.html` | Supervised/Unsupervised, Mask/Box | 좌우 동일 기준, 준비/적용 단계 | 비교 조건/출력/불확실성 |
| 04 Step-by-Step | `step-by-step.html` | Convolution/Distance/Gradient | 같은 Input Patch→계산식→Output | 행렬 셀·연산·결과 값 |
| 05 Interactive | `interactive.html` | Kernel, Stride, Threshold, LR | 조작→예측/계산→표·그래프 동기화 | 원본 TP/FP·임계값·수치 |
| 06 Architecture | `architecture.html` | CNN, PatchCore, Transformer, Triton | 모듈·실제 Shape·연결선 | Conv×2/Flatten8192/3 Class 등 예제 수치 |
| 07 Experiment | `experiment.html` | Confusion Matrix, Boundary Metrics | GT/Pred 축·양성 정의, 지표 검산 | 원본 분류 수량·실험 조건 |
| 08 Executive Summary | `executive-summary.html` | 근거 있는 프로젝트 결과 요약 | 단위/비교 기준/변화율 | 실제 확인되지 않은 개선율·KPI |

## 적용 우선순위

첫 Slice는 01 Concept(Pixel·RGB), 04 Step-by-Step(Convolution), 02 Process(Feature Map), 06 Architecture(CNN), 교육적 가치가 확인되면 05 Interactive(Kernel/Stride)를 적용한다. 필수 패턴이 아닌 03/07/08은 비교·검증 사례가 생겼을 때 사용한다.

디자인 시스템에서 유지할 것은 White·정보 위계·Pretendard 선호·반응형/화살표/역할별 라벨의 의미다. 수치·사과 이미지·CNN의 2개 Block·3개 Output·고정 필터의 반응을 다른 주제로 무분별하게 복제하지 않는다. Reference #2/#3의 고정 필터는 학습된 CNN 특징 추론과 동일하지 않고, #6은 별도 SVG 모식도다.

## 도입 및 QA

- `docs/knowledge/assets/` 내부 네임스페이스로 CSS/JS를 구성하고 현행 `docs/slide.css`와의 충돌 방지.
- 상대경로와 정적 Pages(`./docs` artifact)에서 자산이 모두 접근 가능한지 확인.
- 폰트 파일/라이선스와 타 저장소 복사 사용 권한을 확인. 외부 CDN을 추가하지 않는다.
- HTML/SVG/JS의 숫자는 Python 독립 계산값과 비교. DOM 실제 bounding box로 Arrow/그림 정렬 확인.
- Reference의 과거 스크린샷은 신규 페이지의 실제 Chromium 검증 증거가 아니다.
