# Content Style Guide — Concept 페이지 제작 규약

> 이 문서는 신규 Knowledge Scroll 페이지를 위한 설계 문서다. 기존 55장 Slide에 대한 명시적인 수정 지시가 아니다. 현재 신규 페이지 **미구현**.

## 메타데이터

기본 스키마는 `planning/concepts.v1.json`의 고유 ID, PART, level, prerequisites, next_topics, advanced_topics, applications, status, legacy_slide, references. 웹 페이지의 제작 상태(`planned/draft/reviewed/published`)는 프로젝트 구현 검증 상태(`Related/Reviewed/Implemented/Experimented`)와 별도로 다룬다.

## 교육용 본문 흐름

| 순서 | 질문 | 필수 출력 |
|---|---|---|
| 01 Why | 이 방법이 필요한 이유는? | 해결할 문제/기존 방법의 한계 |
| 02 Intuition | 작은 숫자나 그림으로 어떻게 이해하나? | 직관적 Input→Output |
| 03 Definition | 전문 용어는 정확히 무엇인가? | 영문 명칭·한국어·개념 범위 |
| 04 Mechanism | 내부 단계는 어떻게 연결되나? | 실제 데이터 흐름/Shape |
| 05 Mathematics | 어떤 가정과 식으로 계산하나? | 기호·차원·단위·대입·중간·최종값 |
| 06 Implementation | 실행하면 같은 값이 나오나? | Python import/설정/입출력/실행법 |
| 07 Application | 산업 AI 과제에서 왜 쓰나? | 확인된 소스/실험 또는 '후보' 명시 |
| 08 Limitations | 무엇이 실패하며 비용은? | 계산량·메모리·오류/도메인 이동 |
| 09 Related | 학습을 어디로 확장하나? | 필수 선수, 다음, 선택 심화, 원문 |

기초 개념은 핵심 Figure 한 화면만으로 완결할 수 있다. 상세 수치/Architecture/Interactive는 필요한 경우 후속 페이지로 분할한다. 첫 노출의 전문 용어는 풀이하고, 약어의 첫 등장에는 영문 풀네임을 쓴다.

## 정확성 계약

- **예제:** 입력 텐서 Shape, dtype, 값의 범위, 배치·채널 순서, 단위를 명시한다.
- **CNN:** 단일 채널 입력 (5×5), 3×3 Kernel, stride=1, pad=0, dilation=1이면 Hout=Wout=3. 다중 채널 Weight는 PyTorch conventions에서 `(Cout,Cin,kH,kW)`(groups=1), Tensor는 `(N,Cin,H,W)`. CNN layer가 수행하는 상관 연산(cross-correlation)과 수학적 kernel-flipped convolution의 차이를 설명한다.
- **Shape:** `floor((H+2P-D(K-1)-1)/S)+1`. Channel 증가나 Feature Map 축소를 보편 법칙으로 표현하지 않고 각 설정·Stride·Pooling을 검증한다.
- **Gradient Demo:** 가중치 Slider 조작을 '실제 학습'이라고 부르지 않는다. 자동 미분/Optimizer step/파라미터 변화와 Loss 감소를 확인해야 학습 데모다.
- **데이터 신뢰성:** 교육용 고정 필터·Toy 입력·Synthetic 데이터·실제 모델 추론·현장 실측을 구분하여 화면에 명시한다. 근거 없는 정확도·수치 인용 금지.
- **Python/JS:** 단일 독립 계산과 브라우저 표시 값 및 SVG/Canvas 색·좌표를 대조. 반올림은 마지막 표시 단계에서만 적용. 0 나눗셈/NaN과 Input 경계 검사.

## 디자인 및 출처

흰색, Pretendard 참고, Navy 제목/Blue 단계 라벨, 최소 카드·그림자, 시각적 위계·한 핵심 메시지. 기존 `docs/slide.css`를 무조건 덮어쓰지 않고 신규 Knowledge namespace 사용. 아이콘·도형 대신 기술적 인과관계를 정확한 SVG/HTML/Canvas로 표현한다. 정확하지 않은 AI 생성 구조 그림을 모델 추론 결과로 내보내지 않는다.

원논문 → Official GitHub → Official Docs → 대학 강의 → 신뢰 가능한 해설 순서. 논문명, 저자/기관, 연도, 버전/commit, URL, 접근 날짜 기록. 인용 Figure는 출처와 라이선스, 수정 Figure는 **Adapted from**. 논문 주장/코드 동작/우리 실험/해석을 구별하고, 모델 비교는 Split/Metric/Compute/Preprocess/Version을 통제한다.

## 브라우저 품질

Viewport 1600×950, 1440×810, 1366×768, 1280×720에서 한글 폰트·줄바꿈·수식·넘침·겹침·선 연결을 확인. 실습은 클릭·터치·키보드 및 실패 입력 테스트. CSS/parser 정적 검사는 브라우저 실렌더와 별개이며, 이전 템플릿의 PASS를 현재 웹 페이지 PASS로 간주하지 않는다.
