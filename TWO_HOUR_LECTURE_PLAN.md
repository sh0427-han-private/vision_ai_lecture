# Vision AI 기초강의 · 승인된 55장 / 120분 운영안

승인 구성은 **Intro 13장 + Course 42장 = 55장**입니다. 순서·개별 시간은 [스토리보드](planning/SLIDE_STORYBOARD.md), 실제 구현 순서·제목은 [Manifest](docs/two_hour_manifest.json)와 [목차](docs/lecture_outline.js)를 기준으로 합니다. 제작·검수 상태는 [진행 기록](automation/PROGRESS.md)을 확인합니다. 과거 59/58장 운영안은 Git 이력에 보존되어 있습니다.

| 구간 | 전역 계획 번호 | Course 번호 | 장수 | 분 | 학습 질문 |
|---|---|---|---:|---:|---|
| A | P01–13 | Intro 1–13 | 13 | 26 | Vision AI란 무엇이며, 사진·영상은 어떤 숫자인가? |
| B | P14–18 | 1–5 | 5 | 10 | Task·Label·규칙·데이터 학습을 어떻게 선택하나? |
| C | P19–27 | 6–14 | 9 | 23 | 왜 CNN인가? 가중합과 비선형성이 왜 필요한가? |
| D | P28–36 | 15–23 | 9 | 22 | Kernel·Map·채널·Stride·Padding·Pooling은 무엇을 계산하나? |
| E | P37–40 | 24–27 | 4 | 9 | 어떤 데이터를 모으고 독립적으로 나누나? |
| F | P41–47 | 28–34 | 7 | Loss를 통해 무엇을 바꾸고, 전이학습은 무엇을 재사용하나? |
| G | P48–52 | 35–39 | 5 | 놓침·오알람·위치 오류를 어떻게 평가하나? |
| H | P53–55 | 40–42 | 3 | 같은 사과 문제에서 전체 원리를 설명할 수 있나? |
| 합계 | P01–55 | Intro13 + Course42 | 55 | 120 | 별도 Q&A 블록 없음 |

120분은 **승인된 시간 배분**이며 실측 수업 시간은 아닙니다. 실제 120분 리허설과 초보 수강생 피드백은 수행 전까지 NOT VERIFIED입니다.

대표 사례는 같은 사과의 작은 갈색 반점입니다. 사진 숫자 → 과제와 Label → CNN 특징 → Weight 학습 → 새 사진의 독립 평가를 연결합니다. 코드를 외우는 대신 AI와 프로젝트를 진행할 때 Task·Label·데이터·평가 기준을 스스로 정하는 기초를 목표로 합니다.

C에서는 필요성·전체 Architecture를 먼저 보고 퍼셉트론 → AND → XOR 한계 → 선형 합성 → ReLU → 비선형 실습으로 내려갑니다. Step 퍼셉트론과 CNN의 ReLU는 구분하며, XOR 실습의 |t|는 ReLU(t)+ReLU(−t)입니다.

P20의 가상 사과 CNN은 64×64×3 → Conv8 → ReLU → Pool → Conv16 → ReLU → GAP16 → Dense2이며 Bias 포함 1,426 Parameters입니다. D/F에서 같은 구조를 재사용합니다. 단일 채널 토이 행렬, 실제 SqueezeNet Feature Map, 단순 회귀, 교육용 100개 Score는 서로 다른 예제임을 밝힙니다.

독립 장으로 중복되던 scene / vision-challenge / vision-evolution / training-log / project-brief / project-run은 승인된 위치로 통합합니다. Batch/Epoch 정의는 P41 발표자 노트, 임계값 UI는 P48, 네 설계 질문은 P53에 둡니다.

학습·구조·Threshold 선택은 Train/Validation에서 수행하고 기준을 고정한 뒤 보관한 Test로 확인합니다. 같은 개체·영상·세션은 그룹으로 묶어 분리합니다. 생성 사진·가상 추세·실측 모델 반응을 구분하고, 실제 사용한 외부 Figure에만 출처를 표시합니다.

전체 구현·최종 검수·PR 준비 후에도 **main 병합과 공개 배포는 별도 사용자 승인 뒤** 진행합니다. 작업 브랜치와 현재 공개 Pages 상태를 혼동하지 않습니다.
