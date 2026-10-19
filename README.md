# Vision AI 기초강의

사진의 Pixel부터 CNN·학습·독립 평가까지 연결하는 초급 강의입니다. 승인 구성은 **Intro13 + Course42 = 55장 / 120분**입니다. 학생이 AI와 프로젝트를 진행할 때 Task·Label·데이터·평가 기준을 설명할 수 있는 기초를 목표로 합니다.

[공개 강의](https://sh0427-han.github.io/vision_ai_lecture/) · [승인 스토리보드](planning/SLIDE_STORYBOARD.md) · [운영안](TWO_HOUR_LECTURE_PLAN.md) · [제작·검수 현황](automation/PROGRESS.md)

이 개편은 별도 작업 브랜치에서 진행합니다. **작업 브랜치의 구현과 현재 공개 Pages 버전은 다를 수 있습니다.** 최종 검수 후에도 main 병합과 공개 배포에는 사용자 승인이 필요합니다.

| 구간 | 슬라이드 | 분 | 내용 |
|---|---|---:|---|
| A | P01–13 | 26 | Vision AI 개관, Pixel·RGB·영상, 시각적 변화 |
| B | P14–18 | 10 | Task·Label, Rule-based와 데이터 학습 |
| C | P19–27 | 23 | CNN 필요성·전체 구조, 퍼셉트론·AND/XOR·비선형성 |
| D | P28–36 | 22 | Kernel·Feature Map·채널·Stride·Padding·Pooling |
| E | P37–40 | 9 | Dataset·Train/Validation/Test·Group Split·증강 |
| F | P41–47 | 15 | Loss·Gradient·CNN Training·전이학습 |
| G | P48–52 | 10 | Threshold·혼동행렬·Precision/Recall·IoU |
| H | P53–55 | 5 | 같은 사과 사례로 전체 원리 복습 |

`docs/intro.html`에서 시작합니다. 목차 버튼으로 원하는 슬라이드에 이동하고, 이전/다음·키보드로 순서대로 볼 수 있습니다. 정확한 제목·번호는 [Manifest](docs/two_hour_manifest.json)와 [Outline](docs/lecture_outline.js)을 기준으로 합니다.

관련 개념 안에 흑백·RGB Pixel, 해상도, AND/XOR 경계, Gradient Descent, 임계값 실습을 배치합니다. 별도 Lab·외부 CDN을 요구하지 않습니다. 같은 사과 사진·로컬 CNN 구조를 재사용하며, 실제 Feature Map과 교육용 수치 예제를 구분합니다.

참고 노트: [Vision AI 입문](lectures/01_intro/README.md), [AI 기초](lectures/02_ai_basics/README.md), [Vision AI](lectures/03_vision_ai/README.md). 노트의 과거 번호보다 현재 Manifest와 승인 스토리보드를 우선합니다.

이미지·Figure의 실제 사용 출처와 생성 이력은 [assets/SOURCES.md](assets/SOURCES.md)에 기록합니다. 정밀 수식·Tensor·Kernel은 자체 SVG/HTML로 검산하고, 외부 Figure를 사용한 슬라이드에는 원문 출처를 표시합니다.

개발 전 [AGENTS.md](AGENTS.md), [PROJECT_GUIDE.md](PROJECT_GUIDE.md), [HTML_DESIGN_RULES.md](HTML_DESIGN_RULES.md)를 확인합니다. 최종 정적 검증은 `python scripts/verify_curriculum_overhaul.py`, 브라우저 검증은 `scripts/verify_learning_routes.py`, `scripts/verify_intro_pixel_interactive.py`, `scripts/audit_visual_slides.py`를 사용합니다. 서버의 docs 루트를 `AUDIT_BASE_URL`로 지정하며 Playwright와 Chromium이 필요합니다.

120분은 계획된 배분입니다. 실제 강의 리허설·초보 수강생 피드백·공개 배포 검증은 실제 수행한 경우에만 완료로 기록합니다.
