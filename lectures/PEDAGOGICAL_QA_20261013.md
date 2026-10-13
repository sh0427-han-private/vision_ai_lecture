# Vision AI 강의: 개념·수치·Figure 연결성 점검 (2026-10-13)

## 이번 수정 범위

- 기존 강의의 전체 99장과 강의 흐름은 유지
- **AI Basics**: Perceptron 기본(7장), AND/XOR(11장) 그림 재구성
- **Vision AI**: Convolution(21장), Feature Map(22장), Feature Map/Channel(23장) 그림 재구성
- *주의:* Vision AI의 표지 포함 실제 웹 페이지 기준 번호를 사용했습니다. Manifest 번호는 표지 제외이므로 1씩 작습니다.
- **Backpropagation**(AI Basics 27장)은 지난 교정의 Chain Rule 계산 그래프를 유지하고, 그 수치의 수학적 일관성을 추가 확인

## 교정 전후의 교육적 차이

| 개념 | 이전 그림의 한계 | 개편 기준 | 반영 SVG |
|---|---|---|---|
| Perceptron | 입력·가중합·출력의 정량 연결이 약함 | 입력 0.5/1.0 → Weighted Sum 0.3 → Threshold → 출력 1을 따라가도록 구성 | `lesson_perceptron_numeric_flow.svg` |
| AND/XOR | 데이터 점의 분리 가능성 시각화는 있었으나 참/거짓 대응이 약함 | 출력 1/0을 같은 색으로 표시, AND 분리 직선과 XOR 불가능성을 같은 축으로 비교 | `lesson_and_xor_separability.svg` |
| Convolution | 같은 연산을 숫자로 확인할 수 있으나 바로 다음 장과 별도 설명 | 5×5 입력·3×3 커널·전체 3×3 출력값을 일치시키고 첫 칸 계산을 직접 표기 | `lesson_convolution_calculated.svg` |
| Feature Map | 임의 Feature Map 예시로 넘어가 수치적 연속성이 약함 | 직전 출력값 `[-6,12,16; -6,8,15; -4,2,7]`을 **같은 위치·같은 수치**로 색상 대응 | `lesson_featuremap_numeric_continuation.svg` |
| 다채널 Conv | 출력 Channel 생성 원리가 블록/설명 위주 | RGB의 3개 입력 Channel, 필터당 3×3×3 가중치, 64개 필터→64개 출력 Map으로 구분 | `lesson_multichannel_filter_to_maps.svg` |

## 직접 확인한 값

- Perceptron: `0.5×0.2 + 1.0×0.8 − 0.6 = 0.3`, 임계값 0에 대한 출력은 `1`.
- AND: `x₁+x₂≥1.5`이면 출력 1. 4개의 이진 입력 가운데 `(1,1)`만 1.
- XOR: `(0,1)`과 `(1,0)`일 때만 출력 1. **단일 직선으로 선형 분리 불가능**.
- Convolution: 입력 5×5에 커널 `[[1,0,-1],[1,0,-1],[1,0,-1]]`을 적용, Stride 1·Padding 0·Bias 0. 첫 원소는 `(1−3)+(4−6)+(7−9)=-6`. 출력은 `[[-6,12,16],[-6,8,15],[-4,2,7]]`. 커널 반전 없는 일반적인 CNN식 cross-correlation 예시.
- Feature Map: 위 9개 출력값을 그대로 그렸으며, 음수값이 존재합니다. **ReLU는 적용하지 않은 상태**.
- 다채널 출력: 입력 `224×224×3`, 크기 3×3×3인 필터가 64개라면 총 Weight `3×3×3×64=1728`, Bias `64`, 총 Parameter `1792`. Stride 1·Padding 1이면 출력은 `224×224×64`. 화면에는 교육용 HWC 순서를 사용합니다.
- Backpropagation(기존 개선분): `x=2,y=4,w=1,b=0`, `L=(wx+b-y)^2=4`. `dL/dw=-8`, `dL/db=-4`; SGD `η=.1` 1회 이후 `w'=1.8,b'=.4`, `L'=0` (동일 샘플에 대한 1단계 결과).

## 보장 범위 및 유의사항

이번 수치들은 **교육용 합성값**이며 실제 학습된 Weight·실험 모델 출력이 아닙니다. 각 SVG는 브라우저에서 확대 가능한 벡터 그림입니다. 수학적 연속성은 `scripts/verify_curriculum_overhaul.py`에서 자동 검사합니다.

전체 99장에 대한 브라우저 레이아웃 검사는 기존 `scripts/audit_visual_slides.py`와 GitHub Actions `Visual QA - full lecture`에서 수행합니다. 후속 5개 그림의 브라우저 결과는 워크플로 실행 기록을 확인해야 합니다. SVG 내부 선·글자의 물리적 투사 가독성은 프로젝터 환경에 따라 달라질 수 있습니다.

## 다음 개편 후보

Linear Layer의 비선형 활성화, 데이터 누수와 Group Split, 정밀도·재현율의 현장 의사결정, CNN 입력 Channel에서 학습 가능한 Kernel까지의 연결성을 같은 기준으로 점검합니다.
