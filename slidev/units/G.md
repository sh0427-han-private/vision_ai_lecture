---
layout: lecture
lectureNumber: P48
concept: threshold
title: "Score Threshold · 판정 기준"
---

<LectureSlide number="P48" concept="threshold" title="Score Threshold · 판정 기준" lead="같은 사진 점수라도 기준을 어디에 놓느냐에 따라 불량 알림이 달라집니다." foot="임계값을 고르는 100건의 교육용 검증 예시입니다. 정한 기준은 별도 테스트에 고정 적용합니다.">
<ScoreExercise />
</LectureSlide>

<!--
먼저 한 사과 점수 0.60을 비교하고, 실제 정상·불량 100건의 오분류를 확인합니다. 기준을 높여 놓치는 불량이 늘어나는지 묻습니다. 점수는 보정된 확률이 아닙니다.

참고
- scikit-learn, Tuning the decision threshold: https://scikit-learn.org/stable/modules/classification_threshold.html
-->

---
layout: lecture
lectureNumber: P49
concept: confusion
title: "Confusion Matrix · 100건 평가"
---

<LectureSlide number="P49" concept="confusion" title="Confusion Matrix · 100건 평가" lead="가로는 예측, 세로는 실제 정답으로 두면 네 칸에서 어떤 판단이 틀렸는지 읽을 수 있습니다." foot="P48의 같은 검증용 100건을 기준 0.50에서 읽은 표입니다.">
<ScoreMatrix />
</LectureSlide>

<!--
가로와 세로를 먼저 손으로 가리킵니다. 내 강의 기준에서 양성은 불량입니다. 이 표는 최종 테스트 성능이 아닙니다.

참고
- scikit-learn, Tuning the decision threshold: https://scikit-learn.org/stable/modules/classification_threshold.html
-->

---
layout: lecture
lectureNumber: P50
concept: imbalance
title: "Accuracy의 함정 · 모두 정상이라면?"
---

<LectureSlide number="P50" concept="imbalance" title="Accuracy의 함정 · 모두 정상이라면?" lead="모든 사과를 정상으로 통과시켜도 정상 비율이 80%이면 정확도는 80%입니다." foot="불량을 하나도 찾지 못한 상황이므로 정확도 하나만으로는 판단하기 어렵습니다.">
<ScoreExercise mode="accuracy" />
</LectureSlide>

<!--
정상 비율이 높은 검사에서 분모가 무엇인지 짚습니다. 놓쳤을 때의 비용을 문제 정의 단계에서 합의해야 한다고 연결합니다.

참고
- scikit-learn, Tuning the decision threshold: https://scikit-learn.org/stable/modules/classification_threshold.html
-->

---
layout: lecture
lectureNumber: P51
concept: metrics
title: "Precision과 Recall"
---

<LectureSlide number="P51" concept="metrics" title="Precision과 Recall" lead="정밀도는 알림이 얼마나 믿을 만한지, 재현율은 실제 불량을 얼마나 놓치지 않았는지를 보여줍니다." foot="같은 검증용 100건, 기준 0.50의 참조값입니다.">
<ScoreExercise mode="metrics" />
</LectureSlide>

<!--
정밀도는 불량이라고 알린 22건, 재현율은 실제 불량 20건이 분모입니다. 검증에서 고른 기준은 별도 테스트에서 바꾸지 않습니다.

참고
- scikit-learn, Tuning the decision threshold: https://scikit-learn.org/stable/modules/classification_threshold.html
-->

---
layout: lecture
lectureNumber: P52
concept: iou
title: "IoU · 박스 겹침 비율"
---

<LectureSlide number="P52" concept="iou" title="IoU · 박스 겹침 비율" lead="이제 사진 전체의 라벨 대신, 검출에서 정답 박스와 예측 박스 위치가 얼마나 겹치는지 봅니다." foot="사과 위의 두 박스와 표시한 면적은 같은 좌표에서 계산했습니다.">
<IouExample />
</LectureSlide>

<!--
사과 사진 위의 예측 박스는 교육용입니다. 교집합 45×52와 합집합 5290을 확인합니다. 위치가 완전히 같으면 1, 안 겹치면 0입니다.

참고
- Lin 외, Microsoft COCO, 4절 객체 주석: https://arxiv.org/abs/1405.0312
- COCO API, computeIoU: https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py
-->
