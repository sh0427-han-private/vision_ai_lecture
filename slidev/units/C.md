---
layout: lecture
lectureNumber: P19
concept: cnn-why
title: "왜 CNN인가? · 사과의 작은 특징 반복 탐색"
---

<LectureSlide number="P19" concept="cnn-why" title="왜 CNN인가? · 사과의 작은 특징 반복 탐색" lead="작은 반점이 사진의 왼쪽이나 오른쪽에 있어도 같은 종류의 작은 패턴을 찾아야 합니다." foot="같은 작은 가중치 세트를 여러 위치에 사용합니다.">
<AppleComparisons :cases="[[&quot;왼쪽으로 이동&quot;,&quot;같은 사진의 위치를 이동한 실습용 예시&quot;,{}],[&quot;기준 위치&quot;,&quot;같은 표면 패턴&quot;,{}],[&quot;오른쪽으로 이동&quot;,&quot;동일한 필터를 다시 사용&quot;,{}]]" frame />
<p class="featured-stat">작은 영역을 계산 → 창을 이동 → 같은 계산을 반복</p>
</LectureSlide>

<!--
픽셀마다 새 규칙을 만드는 대신 국소 연결과 가중치 공유가 왜 유용한지 설명합니다. 필터가 반점을 항상 검출한다는 실험은 아닙니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
-->

---
layout: lecture
lectureNumber: P20
concept: cnn-overview
title: "CNN Architecture 전체 그림 · 사과 판정까지"
---

<LectureSlide number="P20" concept="cnn-overview" title="CNN Architecture 전체 그림 · 사과 판정까지" lead="사과 사진이 특징값을 거쳐 정상·불량 점수로 바뀌는 전체 구조입니다." foot="이 그림은 강의용 가상 모델입니다.">
<NetworkDiagram />
</LectureSlide>

<!--
P28은 Conv A 같은 층 안의 한 위치를 확대합니다. P35는 별도 모델 SqueezeNet의 실제 특징을 봅니다. GAP은 채널별 공간 평균입니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- MIT 15.773, Lecture 4 합성곱과 전이학습: https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/
-->

---
layout: lecture
lectureNumber: P21
concept: perceptron
title: "퍼셉트론 · 하나의 W와 b로 판정"
---

<LectureSlide number="P21" concept="perceptron" title="퍼셉트론 · 하나의 W와 b로 판정" lead="두 입력에 같은 가중치 W를 쓰면, 값을 모아 더한 뒤 편향 b로 판정 기준을 조정할 수 있습니다." foot="한 장의 입문 예제입니다. 일반 퍼셉트론은 입력별로 다른 가중치를 쓸 수 있습니다.">
<ConceptCards :items="[[&quot;입력 둘&quot;,&quot;두 값을 작은 숫자로 둡니다.&quot;,&quot;x₁, x₂&quot;],[&quot;가중합&quot;,&quot;공유한 W로 입력을 곱한 뒤 b를 더합니다.&quot;,&quot;z = W(x₁+x₂)+b&quot;],[&quot;판정&quot;,&quot;z가 0 이상이면 1, 작으면 0&quot;,&quot;0 또는 1&quot;]]" flow />
</LectureSlide>

<!--
작은 가중합의 의미를 P20의 신경망과 연결합니다. 다음 결정 경계에서 다루는 Step 판정은 합성곱 뒤의 ReLU와 구별합니다.

참고
- 위키독스 07-01 퍼셉트론, AND와 XOR: https://wikidocs.net/24958
-->

---
layout: lecture
lectureNumber: P22
concept: and-rule
title: "AND Gate · 두 입력이 모두 1일 때"
---

<LectureSlide number="P22" concept="and-rule" title="AND Gate · 두 입력이 모두 1일 때" lead="두 입력의 값이 모두 1인 경우에만 정답이 1입니다." foot="네 점을 좌표에 찍으면 어떤 점을 분리해야 하는지 볼 수 있습니다.">
<LogicGate kind="and" />
</LectureSlide>

<!--
각 점에 표시된 값은 모델의 예측이 아닌 AND의 정답입니다. (1,1) 한 점만 선택하게 합니다.

참고
- 위키독스 07-01 퍼셉트론, AND와 XOR: https://wikidocs.net/24958
-->

---
layout: lecture
lectureNumber: P23
concept: and-gate
title: "AND Gate · Weight와 Bias로 직선 이동"
---

<LectureSlide number="P23" concept="and-gate" title="AND Gate · Weight와 Bias로 직선 이동" lead="직선 하나로 (1,1)과 나머지 세 점을 나눌 수 있습니다." foot="여기서는 z = W x₁ + x₂ + b의 부호를 사용합니다.">
<LogicGate kind="and" interactive />
</LectureSlide>

<!--
기본 W=1, b=−1.2에서 정답 네 개를 확인합니다. W는 기울기, b는 x₂ 절편 위치에 영향을 줍니다. 값 조작은 학습을 실행하는 과정이 아닙니다.

참고
- 위키독스 07-01 퍼셉트론, AND와 XOR: https://wikidocs.net/24958
-->

---
layout: lecture
lectureNumber: P24
concept: xor-rule
title: "XOR Gate · 입력이 다를 때만 1"
---

<LectureSlide number="P24" concept="xor-rule" title="XOR Gate · 입력이 다를 때만 1" lead="입력이 서로 다를 때만 정답이 1입니다. 좌표 그림에서는 같은 정답이 대각선에 놓입니다." foot="XOR의 정답 두 집합 사이에 직선 하나를 그어 봅니다.">
<LogicGate kind="xor" />
</LectureSlide>

<!--
(0,1)과 (1,0)이 1임을 확인합니다. 선을 움직인다는 가정에서 항상 한 점 이상이 잘못 분류됨을 관찰합니다.

참고
- 위키독스 07-01 퍼셉트론, AND와 XOR: https://wikidocs.net/24958
-->

---
layout: lecture
lectureNumber: P25
concept: nonlinear
title: "비선형성 · 깊어져도 직선이면?"
---

<LectureSlide number="P25" concept="nonlinear" title="비선형성 · 깊어져도 직선이면?" lead="중간에 비선형 연산이 없으면, 가중합과 편향을 여러 번 적용해도 하나의 가중합과 편향으로 합칠 수 있습니다." foot="분류 점수에 문턱값 하나를 적용하면 경계는 직선 하나입니다.">
<ConceptCards :items="[[&quot;첫 층&quot;,&quot;입력을 한 번 변환&quot;,&quot;u = 2x + 1&quot;],[&quot;둘째 층&quot;,&quot;첫 층 출력을 다시 변환&quot;,&quot;v = 3u + 2&quot;],[&quot;한 번에 계산&quot;,&quot;두 식을 이어 하나의 식으로 표현&quot;,&quot;v = 6x + 5&quot;]]" flow />
</LectureSlide>

<!--
정확한 용어는 편향을 포함한 아핀 변환입니다. 엄밀한 증명 대신 숫자 대입을 보여줍니다. 직선 경계 설명은 이진 점수의 경우입니다.

참고
- MIT 6.S191, Lecture 1 Intro to Deep Learning: https://introtodeeplearning.com/#schedule
- 위키독스 07-01 퍼셉트론, AND와 XOR: https://wikidocs.net/24958
-->

---
layout: lecture
lectureNumber: P26
concept: relu
title: "ReLU · 비선형성의 시작"
---

<LectureSlide number="P26" concept="relu" title="ReLU · 비선형성의 시작" lead="ReLU는 음수를 0으로 놓고, 0 이상의 값은 그대로 통과시킵니다." foot="이 꺾이는 규칙 때문에 층들의 조합이 더 다양한 경계를 표현할 수 있습니다.">
<ConceptCards :items="[[&quot;음수&quot;,&quot;0으로 바뀝니다.&quot;,&quot;−3 → 0&quot;],[&quot;0&quot;,&quot;그대로입니다.&quot;,&quot;0 → 0&quot;],[&quot;양수&quot;,&quot;그대로입니다.&quot;,&quot;2 → 2&quot;]]" />
<p class="featured-stat">ReLU(t) = max(0, t)</p>
</LectureSlide>

<!--
다음 장에서 두 ReLU 출력을 합해 |t|를 만들 수 있음을 보여줍니다. ReLU 한 개만으로 XOR를 푼다는 인상을 주지 않습니다.

참고
- MIT 6.S191, Lecture 1 Intro to Deep Learning: https://introtodeeplearning.com/#schedule
- 위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드: https://wikidocs.net/64066
-->

---
layout: lecture
lectureNumber: P27
concept: xor-gate
title: "XOR · 선형층을 쌓아도 직선 하나"
---

<LectureSlide number="P27" concept="xor-gate" title="XOR · 선형층을 쌓아도 직선 하나" lead="직선 하나로는 XOR를 나누기 어렵지만, 두 ReLU를 조합하면 두 경계 사이의 영역을 만들 수 있습니다." foot="ReLU(t) + ReLU(−t) = |t|입니다. 이 실습은 그 결과를 이용합니다.">
<LogicGate kind="xor" interactive />
</LectureSlide>

<!--
직선 하나에서 3/4만 맞는 것을 확인하고 ReLU 조합을 누릅니다. 기본 조합에서는 t=x₁+x₂−1에 대해 |t|≤0.5를 만족하는 띠가 정답 두 점을 포함합니다.

참고
- 위키독스 07-01 퍼셉트론, AND와 XOR: https://wikidocs.net/24958
- MIT 6.S191, Lecture 1 Intro to Deep Learning: https://introtodeeplearning.com/#schedule
-->
