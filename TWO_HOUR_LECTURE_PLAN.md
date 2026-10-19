# Vision AI 초급 강의 · 55장 / 120분 Approved 운영 계획

> **기획 승인:** 2026-10-19 사용자 확정 · **Intro 13장 + Course 42장 = 총 55장, 발표 목표 120분, 별도 Q&A 전용 시간 없음.**
> **Builder 단일 상세 명세:** 동일 브랜치 `planning/SLIDE_STORYBOARD.md`의 **§3 P01~P55**. 본 문서는 전체 교수 흐름·운영 시간·승인/구현 경계의 기준이다.
> **현재 사이트 상태와 구분:** `main`의 `docs/two_hour_manifest.json`은 아직 Intro13+Course46=59장, version `20261019-arithmetic-rule-vision-learning`. **이 55장안은 승인된 기획이지 구현·배포 완료안이 아니다.**
> **현재 파일의 적용 위치:** `planning/vision-ai-120min-storyboard-draft-20261019` 기획 브랜치. `main`, HTML, CSS, JS, 이미지, Manifest는 변경하지 않음.

## 1. 강의 목표 및 수강생 출발점

**대상:** AI·ML·Computer Vision을 처음 배우는 비전공자. 모델 구현이나 코드 실습보다는 컴퓨터의 이미지·동영상 입력 및 학습·검증 원리를 이해하는 데 집중한다.

**중심 질문:** "사과 사진·카메라 영상에서 작은 갈색 반점을 안정적으로 찾아 정상/불량을 판단하려면, 컴퓨터는 어떤 숫자를 보고 무엇을 학습해야 할까?"

**강의 종료 시 기대 결과:**
- **Vision AI 의미:** 카메라 사진/영상에서 필요한 정보를 찾도록 AI를 활용하는 것이라고 설명한다. `AI ⊃ ML ⊃ DL`은 기술의 포함 관계이며 **Computer Vision**은 해결하려는 시각 *문제 분야*라고 구분한다. CNN은 DL의 이미지 처리에 자주 쓰이는 **신경망 아키텍처 중 하나**다.
- **G1 입력·어려움:** 흑백 `H×W`(2축 숫자 표) → RGB 한 Pixel `[R,G,B]` → RGB 이미지 전체 `H×W×3`(3축) → **RGB 사과 이미지 여러 장의 시간순 배열** `T×H×W×3`(4축)을 그림으로 읽고 조명·해상도·원근·가림·시간 변화가 결함 검사에 미치는 영향을 말한다. 이 축은 공간 차원과 별개이며 압축 MP4 자체의 형식이 아니다.
- **G2 학습 원리:** 사람이 명시 규칙을 작성하는 Rule-based와 Label+Loss를 바탕으로 Weight를 조절하는 ML을 비교한다. CNN 전체 Architecture를 먼저 보고 Kernel·Feature Map·Weight Sharing·ReLU·Stride·Padding·Max Pooling·Head를 확대해 원리를 이해한다.
- **평가·일반화:** Label/Prediction 구분, Train/Validation/Test·Video Group Split, Forward/Loss/Backward/Optimizer/Weight 갱신과 Inference 차이, Score Threshold·FP/FN·Precision/Recall·IoU의 의미를 설명한다.

**제외:** 별도 Preprocessing 강의 복구, 고급 Transformer Architecture 상세, 동영상 Tracking, 수학적 증명, 직접 모델 학습·코딩. 기존 UI 시연은 120분 발표 시간에 포함한다.

## 2. 승인된 55장·120분 구성

| 단원 | 전역 계획 번호 | 장수 | 배정 시간 | 교수 질문 |
|---|---|---:|---:|---|
| A. Intro — Vision AI 개관·AI/ML/DL·CV 관계·Pixel·영상·난점 | P01–P13 | 13 | **26분** | Vision AI는 무엇인가? 숫자로 된 이미지·영상은 왜 어려운가? |
| B. Task와 Rule-based vs ML·모델 선택 | P14–P18 | 5 | **10분** | 규칙을 언제 사람이 쓰고, 언제 데이터로 배우며, 어떤 Label이 필요한가? |
| C. CNN 필요성·전체 Architecture·비선형성 | P19–P27 | 9 | **23분** | 이미지를 다루는 CNN이 필요한 이유, ReLU의 필요성은 무엇인가? |
| D. CNN 구성요소·숫자 계산 | P28–P36 | 9 | **22분** | Kernel/Feature Map/Channel/Stride/Padding/Pooling/Head는 각자 무슨 일을 하는가? |
| E. 데이터와 독립 분할 | P37–P40 | 4 | **9분** | 정상/불량·촬영 조건을 어떻게 수집·분할해야 하는가? |
| F. Weight 학습·Transfer·일반화 | P41–P47 | 7 | **15분** | Loss·Gradient는 어떤 Weight를 언제 바꾸는가? |
| G. Threshold와 평가 지표 | P48–P52 | 5 | **10분** | 어떤 결함을 놓쳤고 무엇을 잘못 경고했는가? |
| H. 사과 사례로 원리 회수 | P53–P55 | 3 | **5분** | Task·Label·CNN·학습·평가를 내 말로 설명할 수 있나? |
| **합계** | **P01–P55** | **55장** | **120분** | 별도 Q&A 시간 없음 |

**시간 조정 근거:** 기존 54장/120분 Draft에서 AI·ML·DL/Computer Vision 관계도 P02 1장(2분)을 추가했다. 이를 위해 P17 `model-choice`, P18 `task-model-data`, P19 `cnn-why`, P35 `actual-map`에서 각 30초씩 회수했다. CNN Kernel 4분, XOR 비교 실습 5분, Max Pooling 2분, CNN Weight 학습 3분은 보호한다. 장별 총합은 상세 스토리보드에 명시한다. **발표 시간 실측 완료를 뜻하지 않는다.**

## 3. 교수 진행 — Intro 13장 (26분)

| 전역 계획 | 기존 물리/새 concept | 역할과 전달할 연결 |
|---|---|---|
| **P01** | I01 `start` | 처음부터 'Vision AI란 사과 사진·영상에서 결함을 찾아주는 분석'을 입력→AI→교육용 출력 그림으로 보여 준다 |
| **P02** | 신규 `ai-ml-dl-cv` | 기술의 포함 관계 `AI⊃ML⊃DL`과 별도 CV 문제 영역. CNN은 DL Architecture 예. CV를 DL 상자에 넣지 않는다 |
| **P03** | I03 `vision-value` | 반복 사과 품질검사에서 AI가 후보 판단을 보조하지만 검증·사람의 확인이 필요함을 보여 준다 |
| P04 | I04 `photo-numbers` | 사람에게는 '사과', 컴퓨터 입력은 Pixel 숫자라는 대비 |
| **P05** | I05 `gray` | 사과 클릭→한 Pixel 밝기 수 1개, 전체 `H×W` 2축 배열. 밝기 변환식/Slider는 보조 |
| **P06** | I06 `rgb` | **현재 상호작용 유지**: RGB 사과 사진 클릭→실제 같은 Pixel 좌표의 `[R,G,B]` 세 값과 Swatch |
| **P07** | I07 `hwc` | RGB 숫자 세 개를 전체 H행/W열로 확장→`H×W×3` 3축, 640×960 Pixel 614400/값 1843200 |
| **P08** | 신규 `video-frames` | **RGB 사과 이미지 한 장→같은 사과가 조금 움직이는 시간순 대표 Frame 4장→Video 묶음**. **수식은 마지막에만** `T×H×W×3`; `30fps×1초=30 Frame`은 30장 중 4장 대표 표기 |
| P09–P13 | I08–I12 | 해상도·조명·회전·가림·흐림·다양성·결함 신호의 중요성; 후속 Task로 연결 |

**발표자 원칙:** '2차원/3차원/4차원'은 물리 공간이 아니라 **배열 축 개수**라고 안내. 동영상은 MP4 파일 구조 자체가 아니라 **디코딩한 RGB 프레임의 교육용 시퀀스**다. P08은 Decoder나 4D 수식부터 설명하지 말고 같은 사과 Frame 4장과 시간 화살표를 먼저 가리킨다.

## 4. Course 42장 — 기술 선택→CNN→학습→평가

### P14–P18 · Task / Rule-based vs ML · Label

- **P14 `task`:** 사과 결함에 필요한 결과가 전체 정상/불량(Classification)인지, 작은 반점의 Box(Detection)인지, 세밀한 Mask(Segmentation)인지 정의. 설명용 GT와 실제 모델 Output을 혼동하지 않는다.
- **P15 `rules` → P16 `rules-image`:** 명확한 `1+1=2`, `2+1=3`는 사람이 만든 한 규칙으로 처리. 조명·정상/불량 사과 사진의 결함 판정은 수동 규칙의 예외가 늘 수 있어 이미지·정답 Label로 학습하는 방법과 비교. Rule-based가 언제나 불가능하다는 이분법 금지.
- **P17 `model-choice`:** Intro의 AI/ML/DL Nested Figure를 **반복하지 않는다**. `규칙이 충분? → 기존 모델이 반점을 검출? → 부족하면 Label 수집 후 추가 학습`의 선택 흐름과 전 경로 독립 검증을 보여 준다.
- **P18 `task-model-data`:** Class/Box+Class/Mask Label 형식·제작 비용·Task 대응 확인.

### P19–P36 · CNN 전체 Figure와 각 내부 개념

- **P19 `cnn-why`:** 같은 3×3 관찰창으로 사과의 작은 국소 결함 특징을 위치마다 반복 탐색하는 필요성을 먼저 보여 준다.
- **P20 `cnn-overview`:** 교육용 가상 Architecture **`64×64×3→Conv8(3×3,S1,P1)→64×64×8→ReLU→MaxPool(2×2,S2)→32×32×8→Conv16(3×3,S1,P1)→32×32×16→ReLU→GAP16→Dense2`**를 왼쪽→오른쪽 한 줄로 보여 준다. 파란 Extractor와 초록 Head를 분리하고, **학습하는 Weight=Conv+Dense Head**, **고정 연산=ReLU+Max Pool**, **연산 설정=Stride+Padding**이라고 표시. 모든 CNN이 Pool/GAP를 쓰는 것은 아님.
- **P21–P27:** Perceptron → AND 진리표·경계 실습 → XOR 진리표 → Affine 층의 한계 → ReLU → XOR 비선형 전환 실습. AND는 단일 선형 경계로 되지만 XOR는 안 됨. `z=W(x₁+x₂)+b`는 **두 입력에 같은 W를 적용한 특수 예시**; XOR 실습의 `|t|=ReLU(t)+ReLU(-t)`는 단일 ReLU와 다름.
- **P28–P36:** Conv Kernel 5×5 입력/3×3 Kernel → Feature Map 3×3 교육용 값 `[[-6,12,16],[-6,8,15],[-4,2,7]]` → Weight Sharing → RGB/Feature Channel → Stride → Padding → Max Pooling 4×4→2×2 값 `[[6,4],[7,9]]` → 실제 SqueezeNet Feature Map **실측 예시** → Backbone과 Class/Box/Mask Task Head. P20의 축소 Architecture 미니맵을 각 장에서 현재 블록에 강조 표시.

### P37–P47 · 데이터와 Weight 학습

- **P37–P40:** 정상/불량×밝음/어두움 데이터를 교차 수집, Train/Validation/Test 분리, 동일 사과 개체·같은 영상 인접 Frame은 그룹 단위 분할, Train 세트에만 Augmentation. 압축 파일이나 Video Frame 간 유사성은 P08과 연결한다.
- **P41–P44:** 간단한 수치 `ŷ=wx` 예시로 Loss 감소와 Weight 갱신을 이해한 뒤 CNN에서 `사과 RGB→Conv→Feature Map→Head→Prediction→Loss(+Label)→Gradient/Optimizer→Conv/Head Weight Update`를 도식화. Training과 Inference의 Weight 갱신 여부를 명확히 구분한다.
- **P45–P47:** 고정 사전학습 Feature Extractor와 Head 학습(전이학습), 같은 고정 Feature의 지도 Classifier vs Label 없는 Clustering 활용, 새 촬영 조건에서 Overfitting 여부 확인. 지도/비지도는 **Label 사용과 학습 목적**으로 구분한다.

### P48–P55 · 평가와 통합 회수

- **P48–P49:** 동일한 교육용 100건 Score 집합에서 Threshold 0.30/0.50/0.70에 따라 TP/FP/FN/TN 집계를 변경해 Confusion Matrix로 표시. 평가 숫자는 실제 모델 Test 성능이 아니다.
- **P50–P52:** Accuracy 불균형 함정, Precision/Recall, 결함 GT Box와 Prediction Box의 IoU. FN(놓친 결함)의 업무 위험을 사과 검사로 회수한다.
- **P53–P55:** 처음 사과 사진을 다시 보고 Pixel→Task/Label→CNN→학습→독립 검증을 한 그림에 연결. 실패 사진의 조명·해상도 원인은 단정 아닌 조사할 **가설**이며 마지막에 네 질문으로 수강생 이해 확인.

## 5. Builder 인계 조건 및 변경 제어

**기획 상태는 Approved이며 실제 제작 완료 상태가 아니다.** Builder는 `planning/SLIDE_STORYBOARD.md`의 **P01~P55, 각 `data-concept`, 학습 목표, 상세 Figure, 예상 시간, Reviewer 완료 기준**을 바탕으로 별도 구현 브랜치에서 HTML/SVG/CSS/JS·이미지·Manifest를 개발한다. `TWO_HOUR_LECTURE_PLAN.md`의 120분 합계와 목차 순서를 동일하게 맞춘다.

**Builder에게 전달할 문구:**

> "55장·120분 Approved 강의 구성은 `planning/SLIDE_STORYBOARD.md`의 §3 P01~P55 및 `TWO_HOUR_LECTURE_PLAN.md`의 동일 Git Commit을 기준으로 구현하십시오. 현재 main은 59장으로 다르므로 계획 P번호를 현재 물리 HTML 번호와 혼동하지 말고 `concept` ID 매핑으로 대응하십시오. Intro의 Grayscale/RGB 클릭·AND/XOR Slider·학습·Threshold 인터랙션을 보존하면서 신규 AI/ML/DL-CV 관계도와 RGB Frame 시간축 Figure를 구현하십시오. 설명용 결함 ROI·가상 CNN 구조·교육용 계산·실측 SqueezeNet Figure의 사실성 Caption을 유지하십시오. Manifest/목차/네비게이션을 55장에 일치시키고 QA 결과를 제출하십시오. `main` 병합·공개 배포는 별도 최종 승인 전 하지 마십시오."

**범위 관리:** 새로운 모델, 고급 수학, 3D/Tracking, 별도 Preprocessing 슬라이드는 임의 추가 금지. 교육적인 결함 발견 시 Reviewer가 학습 목표·전후 연결을 지적하면 Planner가 기획을 수정한다. CSS 위치·Figure 배치 같은 구현 문제는 Builder/Reviewer가 처리한다.

## 6. QA 기준과 미실행 상태

1. **구조 정합성:** 실제 구현 후 Intro 13·Course42·총55, Concept ID 55개 고유, Manifest·목차·이전/다음 이동, 페이지 수 일치.
2. **교육·기술 검수:** Intro AI/ML/DL과 CV 관계, Pixel H/W/C/T 축, CNN 숫자 Shape, AND/XOR/비선형성, Kernel/Pooling, GT/Prediction, 학습 Weight 갱신, 영상 Group Leakage, 100건 Threshold 값의 논리 확인.
3. **브라우저 실제 QA:** 55장×(1920×1080,1366×768)=**110개 화면**, 사과 사진/실측 Feature Map 로드, 텍스트 오버플로·화살표 정합성·Console, Grayscale/RGB Click·Gate Slider·학습·Threshold 인터랙션 동작 검증.
4. **120분 리허설:** 핵심 계산/시연 시간을 보호하며 시간 초과·축약된 부분 기록. 계획 시간 120분 확인 ≠ 발표 리허설 성공.
5. **배포:** Reviewer 완료와 별도 병합 승인 후 `main` 및 GitHub Pages의 실제 55장 배포 상태를 다시 확인한다.

**지금까지 실시한 것:** GitHub 최신 main 문서 및 기존 HTML/Manifest 기준 정적 조사, 승인 기획의 슬라이드 수·계획 분 합계와 concept 매핑 정리. **미실시:** 55장 구현, 110뷰 브라우저 실렌더, 상호작용 QA, 발표 리허설, 공개 Pages 검수.

## 7. main(59장)과 승인 계획(55장)의 차이

- `main`은 Intro13+Course46=59장이고, 현재 공개 사이트의 원본 동작 기준이다.
- 승인 계획은 Intro13+Course42=55장. Intro의 기존 `scene`과 `vision-challenge`는 주변 내용에 흡수했고 `ai-ml-dl-cv`, `video-frames`를 신규 추가해 Intro 장수 13을 유지했다.
- Course에서는 `vision-evolution`, `training-log`, `project-brief`, `project-run`이 각각 `model-choice`, `learn`, `workflow`, `threshold`로 통합되어 42장이다.
- 54장 구안은 Git 커밋 이력에서 확인 가능하며 **Builder의 55장 실행 번호 기준에 포함하지 않는다.**
- 실물 슬라이드의 구현 완료 후 Reviewer 결과와 발표 시간을 기반으로 구현 버전을 기록하되, **사용자 승인 없이 강의 범위·핵심 개념·제외 주제 변경 금지**.
