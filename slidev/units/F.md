---
layout: lecture
lectureNumber: P41
concept: learn
title: "모델 학습 · 오차를 줄이는 반복"
---

<LectureSlide number="P41" concept="learn" title="모델 학습 · 오차를 줄이는 반복" lead="입력 2에서 목표가 4인 숫자 예시입니다. 학습 버튼을 누르면 가중치가 바뀌고 예측을 다시 계산합니다." foot="단순 회귀 실습입니다. 예측값은 사과 불량 점수가 아닙니다.">
<TrainingLab />
</LectureSlide>

<!--
시연 전 예측 1이 정답 4에 가까워지려면 W가 어느 쪽으로 바뀌어야 할지 묻습니다. 배치는 여러 학습 예를 묶는 단위이고, 에폭은 학습 데이터 한 바퀴입니다.

참고
- MIT 6.S191, Lecture 1 Intro to Deep Learning: https://introtodeeplearning.com/#schedule
- Stanford CS231n, Loss 및 Gradient descent: https://cs231n.github.io/optimization-1/
-->

---
layout: lecture
lectureNumber: P42
concept: loss
title: "Loss · 틀린 정도를 줄이는 방향"
---

<LectureSlide number="P42" concept="loss" title="Loss · 틀린 정도를 줄이는 방향" lead="손실은 예측과 정답이 얼마나 어긋났는지 수치로 보여줍니다. 기울기는 가중치를 움직일 방향을 알려줍니다." foot="여기서는 단순 회귀 예제의 제곱 오차를 사용합니다.">
<ConceptCards :items="[[&quot;예측과 정답&quot;,&quot;예측 1과 정답 4의 차이는 −3&quot;,&quot;오차 −3&quot;],[&quot;손실&quot;,&quot;차이를 제곱합니다.&quot;,&quot;(−3)² = 9&quot;],[&quot;가중치 갱신&quot;,&quot;기울기의 반대 방향으로 한걸음 이동&quot;,&quot;W 0.5 → 1.7&quot;]]" flow />
</LectureSlide>

<!--
초기 기울기는 −12, 학습률은 0.1입니다. 갱신 뒤 예측은 3.4, 손실은 0.36입니다. 실제 사과 분류에는 과제에 맞는 손실을 씁니다.

참고
- Stanford CS231n, Loss 및 Gradient descent: https://cs231n.github.io/optimization-1/
- MIT 6.S191, Lecture 1 Intro to Deep Learning: https://introtodeeplearning.com/#schedule
-->

---
layout: lecture
lectureNumber: P43
concept: cnn-training
title: "CNN 학습 · 예측에서 Weight 갱신까지"
---

<LectureSlide number="P43" concept="cnn-training" title="CNN 학습 · 예측에서 Weight 갱신까지" lead="작은 회귀 예제와 같은 흐름으로 CNN도 예측과 정답을 비교해 커널과 분류기의 가중치를 바꿉니다." foot="사진의 정답 라벨은 비교 기준입니다. 라벨에 기울기를 적용하지 않습니다.">
<NetworkDiagram mode="training" />
</LectureSlide>

<!--
순전파의 점수와 정답을 손실에 넣습니다. 역전파는 가중치별 기울기를 계산하고, Optimizer는 가중치를 갱신합니다. Conv A, Conv B, Head를 지도처럼 다시 찾습니다.

참고
- MIT 6.S191, Lecture 1 Intro to Deep Learning: https://introtodeeplearning.com/#schedule
- 위키독스 07-05 역전파 이해하기: https://wikidocs.net/37406
-->

---
layout: lecture
lectureNumber: P44
concept: infer
title: "Training과 Inference의 차이"
---

<LectureSlide number="P44" concept="infer" title="Training과 Inference의 차이" lead="학습에는 사진과 정답이 필요합니다. 추론에서는 학습이 끝난 가중치로 새 사진의 예측을 계산합니다." foot="둘 다 사진에서 예측을 계산하지만, 가중치 갱신은 학습 중에 합니다.">
<ConceptCards :items="[[&quot;학습&quot;,&quot;사진 → 예측 → 정답과 비교 → 가중치 갱신&quot;,&quot;사진 + 정답&quot;],[&quot;추론&quot;,&quot;새 사진 → 고정된 모델 → 예측&quot;,&quot;새 사진&quot;]]" />
</LectureSlide>

<!--
테스트는 정답을 알고 성능을 측정하는 절차입니다. 정답 없이 결과를 내는 추론과 개념상 구분합니다.

참고
- MIT 6.S191, Lecture 1 Intro to Deep Learning: https://introtodeeplearning.com/#schedule
-->

---
layout: lecture
lectureNumber: P45
concept: transfer
title: "전이학습 · 특징은 고정하고 분류기만 학습"
---

<LectureSlide number="P45" concept="transfer" title="전이학습 · 특징은 고정하고 분류기만 학습" lead="이미지에서 특징을 뽑는 사전학습 모델을 보존하고, 내 정상·불량 사진으로 작은 분류기만 학습할 수 있습니다." foot="고정하는 방법은 전이학습의 한 선택입니다. 새 환경에서는 검증으로 효과를 봅니다.">
<ConceptCards :items="[[&quot;새 사과 사진&quot;,&quot;내 과제의 정상·불량 라벨과 함께 준비&quot;,&quot;입력&quot;],[&quot;사전학습 Backbone&quot;,&quot;이미 학습한 특징을 고정해서 사용&quot;,&quot;Freeze&quot;],[&quot;새 분류 Head&quot;,&quot;사과 라벨에 맞춰 가중치를 갱신&quot;,&quot;Train&quot;]]" flow />
</LectureSlide>

<!--
입문 화면에서는 고정 특징 추출기를 보여줍니다. 전체 또는 일부를 미세조정하는 방법도 있다는 점은 필요할 때 노트로 설명합니다.

참고
- MIT 15.773, Lecture 4 합성곱과 전이학습: https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/
- PyTorch, ConvNet as fixed feature extractor: https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
-->

---
layout: lecture
lectureNumber: P46
concept: cnn-learning-paths
title: "같은 CNN 특징 · 지도와 비지도 활용"
---

<LectureSlide number="P46" concept="cnn-learning-paths" title="같은 CNN 특징 · 지도와 비지도 활용" lead="같은 고정 특징을 써도, 정답을 주면 클래스 구분을 학습하고 정답 없이 비슷한 점을 묶으면 군집을 얻습니다." foot="군집 이름은 ‘정상’이나 ‘불량’으로 자동 결정되지 않습니다.">
<ConceptCards :items="[[&quot;지도 학습&quot;,&quot;네 특징에 정상·불량 라벨을 붙이고 분류 기준을 맞춥니다.&quot;,&quot;라벨 있음&quot;],[&quot;비지도 활용&quot;,&quot;비슷한 특징끼리 두 묶음으로 나눠 패턴을 탐색합니다.&quot;,&quot;라벨 없음&quot;]]" />
</LectureSlide>

<!--
Torch 튜토리얼은 고정 특징 추출기를 뒷받침합니다. 군집은 자체 교육 예시입니다. 1차원 특징 [1,2,8,9]를 중심 1.5와 8.5에 가까운 두 그룹으로 묶는 예를 사용합니다.

참고
- PyTorch, ConvNet as fixed feature extractor: https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
-->

---
layout: lecture
lectureNumber: P47
concept: overfit
title: "Overfitting · 새 데이터 일반화"
---

<LectureSlide number="P47" concept="overfit" title="Overfitting · 새 데이터 일반화" lead="훈련에서 늘 같은 배경일 때, 모델이 반점보다 배경을 단서로 사용해 새 환경에서 틀릴 수 있습니다." foot="높은 훈련 점수가 다른 촬영 조건에서의 성능을 보장하지 않습니다.">
<AppleComparisons :cases="[[&quot;익숙한 조건&quot;,&quot;배경과 밝기가 익숙한 사진&quot;,{&quot;mode&quot;:&quot;mark&quot;}],[&quot;조건 변경&quot;,&quot;반점은 같고 화면만 어두워짐&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;filter&quot;:&quot;brightness(.48)&quot;}]]" />
<p class="featured-stat">새 촬영 조건과 사과 그룹을 따로 모아 성능을 확인</p>
</LectureSlide>

<!--
실제 모델 측정이나 절대 성능 숫자를 제시하는 화면은 아닙니다. 과제와 무관하지만 정답과 같이 나타나는 단서를 모델이 사용할 수 있다는 개념을 설명합니다.

참고
- Geirhos 외, Shortcut learning in deep neural networks: https://www.nature.com/articles/s42256-020-00257-z
-->
