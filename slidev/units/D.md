---
layout: lecture
lectureNumber: P28
concept: kernel
title: "Kernel · 작은 영역의 가중합"
---

<LectureSlide number="P28" concept="kernel" title="Kernel · 작은 영역의 가중합" lead="작은 창과 커널에서 같은 위치의 숫자를 곱하고 모두 더하면 출력 한 칸이 됩니다." foot="가상 사과 CNN의 합성곱을 작게 떼어낸 단일 채널 교육용 계산입니다.">
<WindowLab />
</LectureSlide>

<!--
첫 창의 세 행 합 −2, −2, −2를 더해 −6을 확인합니다. P20의 Conv와 연결해 이 작은 계산이 어디에 속하는지 보여줍니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- MIT 15.773, Lecture 4 합성곱과 전이학습: https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/
- Wang 외, CNN Explainer, II 및 IV절: https://arxiv.org/abs/2004.15004
- 위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드: https://wikidocs.net/64066
-->

---
layout: lecture
lectureNumber: P29
concept: feature-map
title: "Feature Map · 같은 계산을 위치마다"
---

<LectureSlide number="P29" concept="feature-map" title="Feature Map · 같은 계산을 위치마다" lead="같은 커널을 옆으로 옮기면 다른 위치의 반응을 계산합니다. 그 값들을 위치별로 놓으면 특징 맵이 됩니다." foot="앞 장과 같은 5×5 입력·3×3 커널을 사용합니다.">
<WindowLab mode="feature-map" />
</LectureSlide>

<!--
왼쪽 위 −6을 확인한 후 오른쪽 12를 누릅니다. 수강생에게 그 값의 입력 창을 직접 가리키게 합니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- Wang 외, CNN Explainer, II 및 IV절: https://arxiv.org/abs/2004.15004
-->

---
layout: lecture
lectureNumber: P30
concept: sharing
title: "CNN · 지역 연결과 가중치 공유"
---

<LectureSlide number="P30" concept="sharing" title="CNN · 지역 연결과 가중치 공유" lead="같은 커널을 여러 위치에 쓰면, 한 번 학습한 패턴을 사진의 여러 부분에서 반복해서 찾을 수 있습니다." foot="P28의 입력 창에서 각 위치의 숫자는 달라도 커널 값은 같습니다.">
<ConceptCards :items="[[&quot;위치 A&quot;,&quot;첫 번째 영역에서 가중합을 계산&quot;,&quot;−6&quot;],[&quot;같은 가중치&quot;,&quot;오른쪽 한 칸으로 이동해도 필터 값은 유지&quot;,&quot;3×3 커널&quot;],[&quot;위치 B&quot;,&quot;두 번째 영역에서 가중합을 계산&quot;,&quot;12&quot;]]" flow />
</LectureSlide>

<!--
국소 연결은 계산이 창 안의 값만 본다는 뜻이고, 가중치 공유는 여러 위치에서 같은 필터를 쓴다는 뜻입니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- Wang 외, CNN Explainer, II 및 IV절: https://arxiv.org/abs/2004.15004
-->

---
layout: lecture
lectureNumber: P31
concept: channels
title: "RGB에서 Feature Channel까지"
---

<LectureSlide number="P31" concept="channels" title="RGB에서 Feature Channel까지" lead="RGB 입력에서는 한 필터가 세 채널의 같은 위치를 읽고, 각각의 가중합을 합쳐 출력 한 채널을 만듭니다." foot="시각화에는 출력 채널 두 개만 예로 들었습니다.">
<ConceptCards :items="[[&quot;입력&quot;,&quot;세 채널에서 같은 공간 위치의 창을 읽습니다.&quot;,&quot;H×W×3&quot;],[&quot;필터 두 개&quot;,&quot;각 필터는 R·G·B 방향으로 이어지는 가중치를 갖습니다.&quot;,&quot;3×3×3 × 2&quot;],[&quot;출력&quot;,&quot;필터 하나마다 특징 맵 한 장이 만들어집니다.&quot;,&quot;H′×W′×2&quot;]]" flow />
</LectureSlide>

<!--
RGB 세 채널 자체가 출력 특징 세 장이라는 오해를 피합니다. 편향을 쓴다면 필터마다 하나가 더해집니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- 위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드: https://wikidocs.net/64066
-->

---
layout: lecture
lectureNumber: P32
concept: stride
title: "Stride · 계산 위치의 간격"
---

<LectureSlide number="P32" concept="stride" title="Stride · 계산 위치의 간격" lead="커널을 두 칸씩 옮기면 한 칸씩 이동하는 경우보다 계산하는 위치가 줄어듭니다." foot="이동 간격 2의 결과는 앞에서 얻은 특징 맵의 해당 위치들과 일치합니다.">
<WindowLab mode="stride" />
</LectureSlide>

<!--
강사 시연으로 1에서 2로 한 번 전환합니다. 네 값 −6,16,−4,7이 실제로 대응하는 원본 위치를 확인합니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- 위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드: https://wikidocs.net/64066
-->

---
layout: lecture
lectureNumber: P33
concept: padding
title: "Padding · 같은 입력, 다른 출력 크기"
---

<LectureSlide number="P33" concept="padding" title="Padding · 같은 입력, 다른 출력 크기" lead="테두리에 0을 덧붙이면 커널이 가장자리에서도 계산할 수 있습니다." foot="이 장은 앞선 창 이동 실습과 구분되는 3×3 입력의 합계 예제입니다.">
<WindowLab mode="padding" />
</LectureSlide>

<!--
패딩 0일 때 1×1의 45, 패딩 1일 때 3×3과 중앙 45를 비교합니다. 실제 경계 신호를 새로 얻는 것이 아니라 0으로 채운 것입니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- 위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드: https://wikidocs.net/64066
-->

---
layout: lecture
lectureNumber: P34
concept: pool
title: "Max Pooling · 영역별 최댓값"
---

<LectureSlide number="P34" concept="pool" title="Max Pooling · 영역별 최댓값" lead="Max Pooling은 작은 영역에서 가장 큰 값만 남겨 지도 크기를 줄입니다." foot="이 예에서는 2×2로 읽고 두 칸씩 이동합니다. 학습 가중치는 없습니다.">
<WindowLab mode="pool" />
</LectureSlide>

<!--
출력 6과 4를 눌러 두 영역을 비교합니다. 정보 요약의 대가로 영역 안의 정확한 위치나 작은 반응이 사라질 수 있습니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- 위키독스 11-01 합성곱 신경망, 필터와 패딩·스트라이드: https://wikidocs.net/64066
-->

---
layout: lecture
lectureNumber: P35
concept: actual-map
title: "실제 Feature Map · CNN 내부 반응"
---

<LectureSlide number="P35" concept="actual-map" title="실제 Feature Map · CNN 내부 반응" lead="사과 사진을 사전학습된 SqueezeNet에 넣고 세 층의 실제 중간값을 그림으로 바꿨습니다." foot="채널별 표시 밝기를 정규화했습니다. 층과 채널 사이에 색의 절대값을 비교할 수 없습니다.">
<FeatureEvidence />
</LectureSlide>

<!--
강의 저장소의 생성 사과를 실제 ImageNet 사전학습 SqueezeNet1.1에 입력했습니다. P20의 가상 모델을 실측한 결과는 아닙니다. 선택 채널·가중치·전처리와 이미지 해시를 자산 기록에 남겼습니다.

참고
- torchvision SqueezeNet1_1 weights 및 전처리: https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.squeezenet1_1.html
- Wang 외, CNN Explainer, II 및 IV절: https://arxiv.org/abs/2004.15004
-->

---
layout: lecture
lectureNumber: P36
concept: backbone
title: "Backbone과 Task Head"
---

<LectureSlide number="P36" concept="backbone" title="Backbone과 Task Head" lead="Backbone은 사진에서 특징을 뽑고, Head는 그 특징으로 과제에 맞는 답을 만듭니다." foot="여기서는 분류 Head가 사과 사진의 정상·불량 점수를 냅니다.">
<NetworkDiagram mode="backbone" />
</LectureSlide>

<!--
같은 특징 추출기 위에 과제가 달라지면 다른 헤드가 올 수 있음을 말합니다. 검출과 분할은 다른 과제의 예입니다.

참고
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
- MIT 15.773, Lecture 4 합성곱과 전이학습: https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/
-->
