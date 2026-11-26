---
layout: lecture
lectureNumber: P37
concept: dataset
title: "데이터셋 · 어떤 사진으로 배우나"
---

<LectureSlide number="P37" concept="dataset" title="데이터셋 · 어떤 사진으로 배우나" lead="데이터셋은 사진과 정답의 묶음입니다. 실전에서 마주칠 조건을 생각하며 수집해야 합니다." foot="어두운 사진이나 작은 결함을 빠뜨리면 모델이 그 상황에서 어떻게 판단하는지 알기 어렵습니다.">
<AppleComparisons :cases="[[&quot;정상&quot;,&quot;정상 라벨&quot;,{&quot;normal&quot;:true}],[&quot;작은 결함&quot;,&quot;불량 라벨&quot;,{&quot;mode&quot;:&quot;mark&quot;}],[&quot;다른 조명&quot;,&quot;같은 불량 기준&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;filter&quot;:&quot;brightness(.48)&quot;}]]" />
</LectureSlide>

<!--
세 예시를 모두 독립 촬영처럼 세지 않습니다. 오른쪽은 같은 불량 이미지의 화면 변환입니다. 실제로는 촬영 조건을 로그로 남깁니다.

참고
- Lin 외, Microsoft COCO, 4절 객체 주석: https://arxiv.org/abs/1405.0312
- Geirhos 외, Shortcut learning in deep neural networks: https://www.nature.com/articles/s42256-020-00257-z
-->

---
layout: lecture
lectureNumber: P38
concept: split
title: "Train · Validation · Test"
---

<LectureSlide number="P38" concept="split" title="Train · Validation · Test" lead="학습 데이터로 가중치를 맞추고, 검증 데이터로 모델과 기준을 고릅니다. 테스트는 마지막에 결과를 확인합니다." foot="독립된 사과 그룹을 사용합니다. 700·150·150은 교육용 장수 예시입니다.">
<ConceptCards :items="[[&quot;학습 · Train&quot;,&quot;가중치 갱신에 사용&quot;,&quot;700장&quot;],[&quot;검증 · Validation&quot;,&quot;모델 및 임계값 선택&quot;,&quot;150장&quot;],[&quot;테스트 · Test&quot;,&quot;기준을 고정한 뒤 최종 확인&quot;,&quot;150장&quot;]]" flow />
</LectureSlide>

<!--
개수보다 그룹을 먼저 정합니다. 동일 개체가 여러 촬영에 포함되면 개체 기준을, 적절한 경우 영상 또는 촬영 세션 기준을 사용합니다.

참고
- scikit-learn, Cross-validation iterators for grouped data: https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
- scikit-learn, Tuning the decision threshold: https://scikit-learn.org/stable/modules/classification_threshold.html
-->

---
layout: lecture
lectureNumber: P39
concept: leakage
title: "Video Group Split · 데이터 누출 방지"
---

<LectureSlide number="P39" concept="leakage" title="Video Group Split · 데이터 누출 방지" lead="같은 사과의 연속 프레임은 매우 비슷합니다. 낱장 무작위로 나누면 양쪽에 비슷한 사진이 포함될 수 있습니다." foot="새로운 사과에서도 맞는지 보려면 같은 사과를 모두 한 그룹으로 묶어 분할합니다.">
<ConceptCards :items="[[&quot;낱장 분할&quot;,&quot;학습 A1·B1 / 테스트 A2·B2. A와 B가 두 집합에 모두 있습니다.&quot;,&quot;사과 A, B 중복&quot;],[&quot;그룹 분할&quot;,&quot;사과 A의 모든 프레임은 학습, 사과 B의 모든 프레임은 테스트에 둡니다.&quot;,&quot;사과 A | 사과 B&quot;]]" />
</LectureSlide>

<!--
학생에게 A의 두 영상이 서로 다른 세션이면 어떻게 분할할지 묻습니다. 새 사과 평가의 경우 세션이 달라도 A는 합칩니다.

참고
- scikit-learn, Cross-validation iterators for grouped data: https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
-->

---
layout: lecture
lectureNumber: P40
concept: augment
title: "Data Augmentation · 같은 정답, 다른 조건"
---

<LectureSlide number="P40" concept="augment" title="Data Augmentation · 같은 정답, 다른 조건" lead="훈련 사진의 위치를 옮기거나 크기를 바꾸면, 검출용 박스와 분할용 마스크도 함께 옮겨야 합니다." foot="증강은 학습 집합에서만 만들고, 의미가 바뀌는 변환은 과제에 맞는지 확인합니다.">
<AppleComparisons :cases="[[&quot;기준 이미지&quot;,&quot;사과와 정답 박스&quot;,{&quot;mode&quot;:&quot;box&quot;}],[&quot;같은 내용 확대&quot;,&quot;사과 위치를 확대하면 박스도 함께 확대&quot;,{&quot;mode&quot;:&quot;box&quot;,&quot;zoom&quot;:true}]]" />
</LectureSlide>

<!--
같은 SVG 좌표계에서 원본과 박스를 함께 변환한 예입니다. 원본이 학습 집합에 있으면 변환본도 학습 집합에 둡니다.

참고
- MIT 6.S191, Lecture 3 Deep Computer Vision: https://introtodeeplearning.com/#schedule
- scikit-learn, Cross-validation iterators for grouped data: https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
-->
