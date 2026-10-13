# Core 경로 독립성 및 Figure 접근성 추가 QA

검토일: 2026-10-13 · 대상: GitHub Pages 전체 99장 / 핵심 79장

## 발견된 핵심 학습 경로 설명 단절

1. **Vision AI / Median 필터 (Manifest 13번, 웹 14장)**
   - 이전 설명은 "다음 장에서 3×3 비교"를 예고했다.
   - 핵심 모드는 다음 장인 *필터 비교* (Manifest 14번, 심화)을 건너뛰기 때문에 초보자가 예고한 내용을 볼 수 없었다.
   - 개선: 주변 3×3 값을 크기순으로 정렬한 중앙값을 선택한다는 설명을 해당 핵심 장만으로 이해할 수 있게 수정. 심화 장의 실제 계산과 비교 도식은 그대로 보존.

2. **Vision AI / Feature Map (Manifest 21번, 웹 22장)**
   - 이전 설명과 SVG 헤더는 "직전 Convolution에서 계산한…"을 전제했다.
   - 핵심 모드는 직전 *Convolution* (Manifest 20번, 심화)을 건너뛰므로 정확한 계산이 갑자기 등장하는 문제였다.
   - 개선: "5×5 입력 → 3×3 필터를 한 칸씩 이동 → 위치별 3×3 출력 반응"을 **이 장 안에서** 설명. 기존 정확한 출력값 -6/12/16/-6/8/15/-4/2/7과 심화 계산은 변경하지 않음.

3. **AI Basics / 클래스 불균형 (Manifest 41번, 웹 42장)**
   - 핵심 모드에서 *Accuracy와 F1* 심화 장이 건너뛰어진다.
   - 개선: Accuracy는 전체 정답률이고 F1은 Precision·Recall의 조화평균이라는 최소 개념을 클래스 불균형 핵심 장에 추가. 별도 100건 계산 도식은 심화 과정에 유지.

## 그림 자체를 설명하는 대체 텍스트 개선

기존 강의에서는 많은 `img alt`가 슬라이드 제목과 동일했다. 아래 12개 기술 도식에 대해 핵심 수치·모델 역할·데이터 그룹의 구조가 읽히는 문장으로 수정했다.

- Perceptron 수치 계산
- AND·XOR 선형 분리 가능성
- ReLU 입력·출력
- Video Group Split (A/B/C)
- 100건 혼동행렬
- Precision·Recall
- Accuracy·F1
- Convolution 결과가 Feature Map이 되는 과정
- Backbone과 Task Head의 분리
- Receptive Field 3×3/5×5/7×7
- Freeze vs Fine-tuning
- CNN Feature Hierarchy

실제 HTML 및 강의 재생성 스크립트 `scripts/build_lesson_revision.py`의 `FIGURE_ALT_DESCRIPTIONS`에 반영하여 재생성 이후에도 유지되도록 했다.

## 다시 발생하지 않도록 추가한 자동 검증

- `scripts/verify_curriculum_overhaul.py`
  - 핵심 슬라이드의 물리적 이전/다음 장이 심화이고 건너뛰어지는 경우, `직전`, `다음 장`, `이전 장` 등에 의존하지 않는지 검사.
  - 중요 12개 기술 도식의 `img alt`가 구체적 설명 길이를 갖는지 검사.
  - 원래의 슬라이드 수, 이미지 자산, 계산값 검사도 유지.
- `scripts/verify_learning_routes.py`
  - 핵심 모드에서 Median 웹 14장과 Feature Map 웹 22장을 직접 열어 모호한 지시어가 남지 않았는지 확인.
  - 두 화면의 JPEG 캡처를 `visual_audit_output/core_continuity_*.jpg`에 기록.
- `scripts/audit_visual_slides.py`
  - 1920×1080 및 1366×768의 198개 화면 전수 렌더링을 유지.

## 수정 범위와 품질 주장에 대한 제한

99장/79장의 전체 학습 경로와 기존 번호·그림 수치·기본 16:9 강의 레이아웃은 유지했다. 이번 작업은 건너뛰기 경로의 설명 의존성 및 일부 핵심 그림의 접근성을 개선한 것이며, 모든 기존 개념 도식의 의미 정확성이나 모바일·프로젝터에서의 실제 가독성 전체를 검증한 것은 아니다.
