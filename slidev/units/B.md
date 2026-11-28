---
layout: lecture
lectureNumber: P14
concept: task
title: "같은 사진, 다른 질문과 정답"
---

<LectureSlide number="P14" concept="task" title="같은 사진, 다른 질문과 정답" lead="같은 사진에서도 질문이 달라지면 AI가 내야 하는 답과 사람이 붙일 정답이 달라집니다." foot="분류는 사진 전체, 검출은 객체 위치, 분할은 픽셀 단위의 영역을 답으로 냅니다.">
<TaskExamples />
</LectureSlide>

<!--
먼저 사진이 정상인지 묻고, 그다음 어디가 불량인지 묻습니다. 세 항목을 눌러 정답의 형식이 어떻게 달라지는지 확인합니다.

참고
- University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위: https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf
- Lin 외, Microsoft COCO, 4절 객체 주석: https://arxiv.org/abs/1405.0312
-->

---
layout: lecture
lectureNumber: P15
concept: rules
title: "규칙 기반 · 답을 구하는 방법을 사람이 정한다"
---

<LectureSlide number="P15" concept="rules" title="규칙 기반 · 답을 구하는 방법을 사람이 정한다" lead="사람이 규칙을 정하면 같은 규칙으로 여러 입력을 처리할 수 있습니다." foot="규칙의 조건과 예외는 사람이 정의합니다.">
<ConceptCards :items="[[&quot;입력 ①&quot;,&quot;같은 더하기 규칙으로 계산합니다.&quot;,&quot;1 + 1&quot;],[&quot;사람이 정한 규칙&quot;,&quot;두 수를 더한 값을 돌려줍니다.&quot;,&quot;add(a, b)&quot;],[&quot;입력 ②&quot;,&quot;입력을 바꾸어도 규칙은 같습니다.&quot;,&quot;2 + 1&quot;]]" flow />
<p class="featured-stat">add(1, 1) = 2    ·    add(2, 1) = 3</p>
</LectureSlide>

<!--
더하기 함수 두 번 실행을 예로 듭니다. 사람이 설정한 규칙은 다음 장 사진에서 조건을 늘려야 할 수 있습니다.
-->

---
layout: lecture
lectureNumber: P16
concept: rules-image
title: "이미지 판단 · 규칙을 어디까지 만들어야 할까?"
---

<LectureSlide number="P16" concept="rules-image" title="이미지 판단 · 규칙을 어디까지 만들어야 할까?" lead="사진에서는 조명과 그림자 때문에 ‘갈색이면 불량’ 같은 규칙이 자주 예외를 만납니다." foot="데이터로 학습할 때도 사람이 정답의 뜻과 평가 기준을 정합니다.">
<AppleComparisons :cases="[[&quot;조명이 밝음&quot;,&quot;반점이 있는 불량 사진&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;zoom&quot;:true}],[&quot;조명이 어두움&quot;,&quot;같은 반점이 어두워짐&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;zoom&quot;:true,&quot;filter&quot;:&quot;brightness(.48)&quot;}]]" />
<ConceptCards :items="[[&quot;사람이 만든 규칙&quot;,&quot;갈색을 몇 픽셀부터 반점으로 볼지 정합니다.&quot;],[&quot;사진+정답으로 학습&quot;,&quot;조건이 다른 사진과 라벨을 주고 모델의 가중치를 갱신합니다.&quot;]]" />
</LectureSlide>

<!--
규칙 기반 방식도 촬영 조건이 일정하면 유효합니다. 기준은 새 조건에서 놓침과 오알람이 얼마나 달라지는지입니다.

참고
- MIT 6.S191, Lecture 3 Deep Computer Vision: https://introtodeeplearning.com/#schedule
-->

---
layout: lecture
lectureNumber: P17
concept: model-choice
title: "사과 결함 검사 · 무엇부터 시도할까?"
---

<LectureSlide number="P17" concept="model-choice" title="사과 결함 검사 · 무엇부터 시도할까?" lead="문제와 촬영 환경이 명확하면 가장 단순한 방법을 기준으로 삼아 성능을 확인할 수 있습니다." foot="어느 방법을 선택해도 이전에 보지 못한 사과에서 확인해야 합니다.">
<ConceptCards :items="[[&quot;간단한 규칙&quot;,&quot;촬영 조건이 일정하고 명확한 기준을 손으로 정할 수 있을 때&quot;],[&quot;기존 모델&quot;,&quot;새 사진으로 검증했을 때 필요한 결과를 이미 내는 경우&quot;],[&quot;추가 학습&quot;,&quot;내 결함이나 촬영 환경에서 기존 성능이 부족하고 정답 자료가 있을 때&quot;]]" />
</LectureSlide>

<!--
세 후보는 진화 단계가 아닙니다. 같은 문제에 대해 후보를 비교한 뒤 더 단순한 쪽으로 충분한지 확인합니다.

참고
- MIT 15.773, Lecture 4 합성곱과 전이학습: https://ocw.mit.edu/courses/15-773-hands-on-deep-learning-spring-2024/resources/mit15_773_s24_lec04_pdf/
- PyTorch, ConvNet as fixed feature extractor: https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
-->

---
layout: lecture
lectureNumber: P18
concept: task-model-data
title: "내 과제에 맞는 모델과 Label"
---

<LectureSlide number="P18" concept="task-model-data" title="내 과제에 맞는 모델과 Label" lead="먼저 원하는 답을 한 문장으로 정하면 이미지에 어떤 정답 형태를 붙여야 할지 알 수 있습니다." foot="강의의 중심 예시는 사진 한 장의 정상·불량 분류입니다.">
<ConceptCards :items="[[&quot;있나?&quot;,&quot;이미지 전체의 정상·불량&quot;,&quot;Class&quot;],[&quot;어디에 있나?&quot;,&quot;결함 위치를 둘러싼 사각형&quot;,&quot;Box&quot;],[&quot;어디까지인가?&quot;,&quot;결함으로 표시할 픽셀의 영역&quot;,&quot;Mask&quot;]]" />
</LectureSlide>

<!--
Box와 Mask는 대안 과제입니다. 실제 COCO는 일상 물체가 위치하는 맥락과 주석 형식을 설명하는 참고입니다. 여기의 사과 주석은 직접 만든 예시입니다.

참고
- University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위: https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf
- Lin 외, Microsoft COCO, 4절 객체 주석: https://arxiv.org/abs/1405.0312
-->
