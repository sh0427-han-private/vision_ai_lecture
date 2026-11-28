---
layout: lecture
lectureNumber: P01
concept: start
title: "Vision AI란 무엇인가?"
---

<LectureSlide number="P01" concept="start" title="Vision AI란 무엇인가?" lead="Vision AI는 AI가 사진이나 영상 속 대상을 알아보거나 필요한 위치를 찾는 기술입니다." foot="주황색 원은 작은 반점을 보여 주는 교육용 표시입니다.">
<OpeningExample />
</LectureSlide>

<!--
스마트폰과 로봇청소기에서 AI가 무엇을 본다고 생각하는지 묻습니다. 사과 사례에서는 뒤에서 사진 한 장의 정상·불량 분류를 학습시킵니다.

참고
- MIT 6.S191, Lecture 3 Deep Computer Vision: https://introtodeeplearning.com/#schedule
- University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위: https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf
-->

---
layout: lecture
lectureNumber: P02
concept: ai-ml-dl-cv
title: "AI·ML·DL과 Computer Vision의 관계"
---

<LectureSlide number="P02" concept="ai-ml-dl-cv" title="AI·ML·DL과 Computer Vision의 관계" lead="AI·머신러닝·딥러닝은 기술의 관계입니다. 컴퓨터 비전은 사진과 영상으로 어떤 문제를 푸는지에 관한 분야입니다." foot="CNN은 딥러닝에서 쓰는 여러 구조 중 하나입니다.">
<ConceptCards :items="[[&quot;AI ⊃ 머신러닝 ⊃ 딥러닝&quot;,&quot;데이터로 판단 기준을 배우는 기술이 머신러닝입니다. 딥러닝은 여러 층의 신경망을 사용합니다.&quot;,&quot;기술&quot;],[&quot;컴퓨터 비전&quot;,&quot;사진 속 물체를 찾거나 움직임을 읽는 문제입니다. 전통 영상 처리와 AI 모두 활용합니다.&quot;,&quot;문제&quot;]]" />
</LectureSlide>

<!--
두 카드가 서로 다른 질문에 답한다는 점을 확인합니다. 왼쪽은 어떤 기술인가, 오른쪽은 어떤 입력과 문제인가입니다.

참고
- MIT 6.S191, Lecture 1 Intro to Deep Learning: https://introtodeeplearning.com/#schedule
- MIT 6.S191, Lecture 3 Deep Computer Vision: https://introtodeeplearning.com/#schedule
-->

---
layout: lecture
lectureNumber: P03
concept: vision-value
title: "Vision AI가 필요한 이유"
---

<LectureSlide number="P03" concept="vision-value" title="Vision AI가 필요한 이유" lead="반복해서 사진을 검사할 때 결함이 의심되는 후보를 먼저 제시하면 사람이 볼 곳을 좁힐 수 있습니다." foot="실제 적용에서는 놓친 결함과 잘못 표시한 정상도 확인합니다.">
<AppleComparisons :cases="[[&quot;반복 검사&quot;,&quot;같은 유형의 사과를 여러 장 촬영합니다.&quot;,{}],[&quot;후보 표시&quot;,&quot;사진에 결함으로 의심되는 위치를 표시합니다.&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;zoom&quot;:true}]]" />
<ConceptCards :items="[[&quot;여러 장 촬영&quot;,&quot;입력을 모읍니다.&quot;],[&quot;후보 제시&quot;,&quot;의심스러운 곳을 좁힙니다.&quot;],[&quot;사람 확인&quot;,&quot;결함인지 확인합니다.&quot;]]" flow />
</LectureSlide>

<!--
자동 분석을 사람의 확인을 돕는 흐름으로 설명합니다. 이 화면은 현장 성능이나 처리 시간을 측정한 결과가 아닙니다.

참고
- University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위: https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
-->

---
layout: lecture
lectureNumber: P04
concept: photo-numbers
title: "사람의 의미 인식 vs Pixel 숫자"
---

<LectureSlide number="P04" concept="photo-numbers" title="사람의 의미 인식 vs Pixel 숫자" lead="사람은 사진을 보고 사과라고 말할 수 있지만, 모델의 입력에는 위치마다 숫자가 들어갑니다." foot="강조한 한 칸은 같은 위치를 축소한 사진의 밝기값입니다.">
<ImageEncoding />
</LectureSlide>

<!--
사진에서 반점 근처의 칸을 먼저 가리킨 뒤 오른쪽 대응 칸을 가리킵니다. 축소된 밝기값 배열이 원본의 모든 세부를 보존하지는 않습니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
-->

---
layout: lecture
lectureNumber: P05
concept: gray
title: "흑백 사진은 H × W 숫자 배열"
---

<LectureSlide number="P05" concept="gray" title="흑백 사진은 H × W 숫자 배열" lead="사진에서 고른 영역을 밝기 숫자와 명암 격자로 함께 읽어 봅니다." foot="흑백 이미지는 H × W 배열입니다. 픽셀마다 밝기값 하나가 들어 있습니다.">
<PixelLab />
</LectureSlide>

<!--
사진의 6×6 영역을 한 칸 옮기고 두 격자에서 같은 위치를 찾게 합니다. 밝기를 바꿀 때 255에서 잘리는 값도 짚습니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
-->

---
layout: lecture
lectureNumber: P06
concept: rgb
title: "RGB · Pixel당 세 숫자"
---

<LectureSlide number="P06" concept="rgb" title="RGB · Pixel당 세 숫자" lead="사진의 한 점을 고르면 그 자리에 기록된 빨강·초록·파랑 값이 표시됩니다." foot="8비트 RGB 예시에서는 각 채널에 0부터 255까지의 값이 들어갑니다.">
<PixelLab mode="rgb" />
</LectureSlide>

<!--
다른 색의 픽셀 두 곳을 골라 세 채널의 상대값을 비교합니다. RGB 표시는 원본 픽셀 위치와 일치합니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
-->

---
layout: lecture
lectureNumber: P07
concept: hwc
title: "RGB 이미지 전체는 H × W × 3"
---

<LectureSlide number="P07" concept="hwc" title="RGB 이미지 전체는 H × W × 3" lead="사진의 각 위치에 R·G·B가 하나씩 들어갑니다. 한 색 채널만 펼치면 H×W 격자가 됩니다." foot="세 채널을 쌓으면 H×W×3입니다. 라이브러리에 따라 C×H×W 순서로 저장하기도 합니다.">
<ImageEncoding mode="channels" />
</LectureSlide>

<!--
앞 장에서 고른 한 지점의 RGB가 모든 지점에 반복된다고 생각하게 합니다. 각 채널 이미지는 같은 사진을 채널별로 읽은 교육용 컬러 표현입니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
- Stanford CS231n, Conv Layer 및 Pooling Layer: https://cs231n.github.io/convolutional-networks/
-->

---
layout: lecture
lectureNumber: P08
concept: video-frames
title: "동영상은 시간순 RGB 이미지 여러 장"
---

<LectureSlide number="P08" concept="video-frames" title="동영상은 시간순 RGB 이미지 여러 장" lead="영상 파일을 디코딩하면 시간순으로 프레임을 읽을 수 있고, RGB 프레임 한 장은 이미지 하나입니다." foot="사진 한 장으로 만든 프레임 시뮬레이션 · T×H×W×3은 디코딩 후의 표현 예시">
<AppleComparisons :cases="[[&quot;프레임 1&quot;,&quot;t₁&quot;,{}],[&quot;프레임 2&quot;,&quot;t₂&quot;,{}],[&quot;프레임 3&quot;,&quot;t₃&quot;,{}],[&quot;프레임 4&quot;,&quot;t₄&quot;,{}]]" frame />
<p class="featured-stat">한 장 H×W×3  →  T장 T×H×W×3</p>
</LectureSlide>

<!--
입력 원본 한 장을 옮겨 만든 교육용 프레임 시뮬레이션입니다. 압축 파일의 내부 구조를 그린 화면은 아닙니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
-->

---
layout: lecture
lectureNumber: P09
concept: resolution
title: "해상도가 낮으면 작은 결함도 사라질까?"
---

<LectureSlide number="P09" concept="resolution" title="해상도가 낮으면 작은 결함도 사라질까?" lead="같은 원본을 세 해상도로 축소하고 반점이 있는 위치를 같은 표시 크기로 확대합니다." foot="화면에서 크게 표시해도 축소하면서 잃은 세부가 다시 생기지는 않습니다.">
<ResolutionLab />
</LectureSlide>

<!--
해상도를 바꿔 반점이나 경계에 남은 세부가 무엇인지 관찰합니다. 확대 보기에는 최근접 보간을 써서 픽셀 그리드를 드러냅니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
-->

---
layout: lecture
lectureNumber: P10
concept: lighting
title: "조명이 달라지면 Pixel 숫자도 변한다"
---

<LectureSlide number="P10" concept="lighting" title="조명이 달라지면 Pixel 숫자도 변한다" lead="사진이 더 어두워지면 같은 사과의 같은 위치도 다른 밝기값을 갖습니다." foot="동일한 교육용 생성 사진의 표시 밝기를 바꾼 예입니다.">
<AppleComparisons :cases="[[&quot;원본&quot;,&quot;밝기 1.0×&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;zoom&quot;:true}],[&quot;어두운 예&quot;,&quot;밝기 0.48×&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;zoom&quot;:true,&quot;filter&quot;:&quot;brightness(.48)&quot;}]]" />
</LectureSlide>

<!--
같은 과일과 같은 결함 표시를 유지합니다. 발광과 카메라 응답 전체를 측정한 실험이 아니라 화면상의 변환입니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
- Geirhos 외, Shortcut learning in deep neural networks: https://www.nature.com/articles/s42256-020-00257-z
-->

---
layout: lecture
lectureNumber: P11
concept: transform
title: "회전·크롭·가림·흐림은 무엇을 바꿀까?"
---

<LectureSlide number="P11" concept="transform" title="회전·크롭·가림·흐림은 무엇을 바꿀까?" lead="사진을 회전하거나 일부를 가리면 같은 사과라도 경계와 질감의 배치가 달라집니다." foot="같은 교육용 생성 사진에 화면 변환을 적용했습니다.">
<AppleComparisons :cases="[[&quot;원본&quot;,&quot;기준 사진&quot;,{}],[&quot;회전&quot;,&quot;경계가 이동&quot;,{&quot;effect&quot;:&quot;rotate&quot;}],[&quot;크롭&quot;,&quot;보이는 영역 축소&quot;,{&quot;zoom&quot;:true}],[&quot;가림&quot;,&quot;일부 정보 소실&quot;,{&quot;effect&quot;:&quot;occlude&quot;}],[&quot;흐림&quot;,&quot;세부가 약해짐&quot;,{&quot;filter&quot;:&quot;blur(9px)&quot;}]]" />
</LectureSlide>

<!--
어떤 변화에서 정보가 약해지고 어떤 변화에서 화면 밖으로 잘리는지 물어봅니다. 가려진 정보까지 항상 복원할 수 있는 것은 아닙니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
-->

---
layout: lecture
lectureNumber: P12
concept: diversity
title: "다르게 생겨도 같은 종류"
---

<LectureSlide number="P12" concept="diversity" title="다르게 생겨도 같은 종류" lead="색, 크기, 반점은 달라도 두 사진 모두 ‘사과’라는 종류로 묶일 수 있습니다." foot="물체의 종류와 검사 과제의 정상·불량 라벨은 따로 정합니다.">
<AppleComparisons :cases="[[&quot;사진 A&quot;,&quot;종류 · 사과&quot;,{&quot;normal&quot;:true}],[&quot;사진 B&quot;,&quot;종류 · 사과&quot;,{&quot;mode&quot;:&quot;mark&quot;}]]" />
</LectureSlide>

<!--
학생에게 제품 종류만 묻는다면 두 답이 같은지 먼저 물은 뒤 검사 라벨과 구분합니다.

참고
- Szeliski, Computer Vision: Algorithms and Applications, 2판, 영상 형성과 처리: https://link.springer.com/book/10.1007/978-3-030-34372-9
- University of Michigan EECS 498/598, Lecture 1 비전 문제의 범위: https://web.eecs.umich.edu/~justincj/slides/eecs498/WI2022/598_WI2022_lecture01.pdf
-->

---
layout: lecture
lectureNumber: P13
concept: relevant-change
title: "큰 변화보다 중요한 차이"
---

<LectureSlide number="P13" concept="relevant-change" title="큰 변화보다 중요한 차이" lead="밝기 차이는 사진을 크게 바꾸어도 정상·불량 기준을 바꾸지 않을 수 있습니다. 작은 지정 반점은 판단을 바꿀 수 있습니다." foot="이 강의의 교육용 검사에서 불량은 지정한 표면 반점이 있는 경우입니다.">
<AppleComparisons :cases="[[&quot;정상&quot;,&quot;지정 반점 없음&quot;,{&quot;normal&quot;:true}],[&quot;불량&quot;,&quot;지정 반점 있음&quot;,{&quot;mode&quot;:&quot;mark&quot;}],[&quot;불량&quot;,&quot;같은 반점, 더 어두운 화면&quot;,{&quot;mode&quot;:&quot;mark&quot;,&quot;filter&quot;:&quot;brightness(.48)&quot;}]]" />
</LectureSlide>

<!--
정상과 불량 사진은 서로 다른 생성 원본입니다. 오른쪽 사진에만 밝기 변환을 적용했습니다. 현장에서는 결함 정의와 합의가 필요합니다.

참고
- Geirhos 외, Shortcut learning in deep neural networks: https://www.nature.com/articles/s42256-020-00257-z
-->
