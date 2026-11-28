---
layout: lecture
lectureNumber: P53
concept: workflow
title: "Vision AI 원리 · 한 장으로 연결"
---

<LectureSlide number="P53" concept="workflow" title="Vision AI 원리 · 한 장으로 연결" lead="입력, 특징 계산, 학습, 평가가 한 문제에서 어떻게 이어졌는지 돌아봅니다." foot="출발점은 작은 표면 반점을 찾고 싶은 사과 검사 질문입니다.">
<ConceptCards :items="[[&quot;입력&quot;,&quot;카메라의 픽셀 배열&quot;],[&quot;정답&quot;,&quot;사진마다 정상·불량&quot;],[&quot;특징&quot;,&quot;CNN 커널의 반응&quot;],[&quot;학습&quot;,&quot;예측 오차로 가중치 갱신&quot;],[&quot;평가&quot;,&quot;새 사과에서 놓침과 오알람 확인&quot;]]" flow />
<p class="featured-stat">어떤 답이 필요한가 → 어떤 사진과 정답을 더 모을까</p>
</LectureSlide>

<!--
같은 질문에서 단계별로 사람이 결정해야 하는 요구사항을 묻습니다. 새 사진에서 성능이 낮으면 필요한 촬영 조건과 라벨을 다시 정합니다.

참고
- MIT 6.S191, Lecture 3 Deep Computer Vision: https://introtodeeplearning.com/#schedule
-->

---
layout: lecture
lectureNumber: P54
concept: project-iterate
title: "실패 사진이 알려 주는 것"
---

<LectureSlide number="P54" concept="project-iterate" title="실패 사진이 알려 주는 것" lead="새 사과에서 놓친 사진을 찾으면, 어떤 조건에서 모델이 어려워하는지 확인할 수 있습니다." foot="검증으로 기준을 정한 뒤 다른 사과 그룹에서 같은 기준으로 평가합니다.">
<AppleComparisons :cases="[[&quot;새 조건&quot;,&quot;낮은 해상도와 조명에서는 작은 결함이 흐려질 수 있습니다.&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;zoom&quot;:true,&quot;filter&quot;:&quot;brightness(.48) blur(5px)&quot;}],[&quot;다음 데이터&quot;,&quot;같은 문제를 확인할 다른 사과를 모읍니다.&quot;,{&quot;normal&quot;:true}]]" />
<p class="featured-stat">예: 검증에서 기준 0.50을 정하고, 잠가 둔 다른 사과 그룹에서 한 번 평가</p>
</LectureSlide>

<!--
이 화면에는 별도 테스트를 실행한 성능 숫자가 없습니다. 새 조명에서 놓친 불량을 찾고, 그 조건을 더 수집하되 기존 평가용 그룹과는 섞지 않는 판단을 설명하게 합니다.

참고
- Geirhos 외, Shortcut learning in deep neural networks: https://www.nature.com/articles/s42256-020-00257-z
- scikit-learn, Cross-validation iterators for grouped data: https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
- scikit-learn, Tuning the decision threshold: https://scikit-learn.org/stable/modules/classification_threshold.html
-->

---
layout: lecture
lectureNumber: P55
concept: project-check
title: "Vision AI 원리 · 무엇을 설명할 수 있나?"
---

<LectureSlide number="P55" concept="project-check" title="Vision AI 원리 · 무엇을 설명할 수 있나?" lead="처음 보는 사과 사진에서도 어떤 과정을 거쳐 판단을 내리는지 설명해 봅니다." foot="말로 먼저 답하고 각 질문을 눌러 확인합니다.">
<RecapQuestions />
</LectureSlide>

<!--
수강생에게 네 질문을 자신의 말로 설명하게 합니다. 마무리로 새 조명에서 불량을 놓치면 어떤 사진, 정답, 평가 기준을 바꿀지 묻습니다.
-->
