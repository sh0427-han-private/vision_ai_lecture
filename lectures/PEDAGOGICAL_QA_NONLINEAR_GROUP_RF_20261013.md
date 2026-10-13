# 2026-10-13 추가 교육적 검토 — 비선형성, 데이터 분리, CNN 특징 계층

## 적용한 99장 중 5개 슬라이드

1. AI Basics 13 (Manifest 12) **Activation**: 기존의 ReLU 그래프와 별도 XOR 사례 대신, `−2,−1,0,1,2` 입력이 `0,0,0,1,2`로 바뀌는 **동일한 계산의 그래프·값 비교**를 제시한다.
2. AI Basics 14 (Manifest 13) **선형 Layer의 한계**: `h=2x+1`, `y=3h−2`는 `y=6x+1`로 합성된다는 실제 수치 예시. `y=3ReLU(2x+1)−2`는 `x=-0.5`에서 기울기가 달라진다는 차이를 설명한다. 선형 Layer의 Bias가 포함되므로 정확한 용어는 Affine이다.
3. AI Basics 31 (Manifest 30) **Group Split**: Video A/B/C 각각 3프레임, 총 9개. Random Split(Train A1/B1/C1, Val A2/B2/C2, Test A3/B3/C3)과 Video Group Split(Train A1/A2/A3, Val B1/B2/B3, Test C1/C2/C3)로 원본 중복 여부를 시각적 비교한다. 같은 원본의 프레임 분할이 과대평가를 유발할 수 있다는 설명이며, 점수 수치를 생성하지 않았다.
4. Vision AI 29 (Manifest 28) **특징의 조합**: 같은 사과 원본 이미지를 사용해 초기 국소 경계 반응 → 패턴 조합 → 더 넓은 Task 관련 형태로 이어지는 개념 그림을 만든다. 이 예시는 **측정된 실제 Feature Map이 아니다**. 모든 CNN이 동일한 의미론적 순서로 특징을 학습한다고 주장하지 않는다.
5. Vision AI 30 (Manifest 29) **Receptive Field**: 7×7 동일한 원본 격자에서 3×3 / 5×5 / 7×7 입력 범위를 단계별 강조. 3×3 Conv, Stride=1, Dilation=1을 연속 3개 Layer 사용했을 때의 **이론적 수용영역**이며 실효적 기여 범위/어텐션과 동일하지 않다.

## 인접 콘텐츠와 연결

- AI Basics 12 AND/XOR에서 하나의 직선의 한계 → Activation으로 비선형 계산 → Affine Layer의 합성과 Activation의 차이로 진행한다.
- AI Basics 30 데이터 분리(Train/Validation/Test) → 31 Group Split (9개 프레임·3원본) → 32 Data Leakage (동일 원본 섞임, 전처리 통계, 반복 Test 사용)로 원인을 누적한다.
- Vision AI 28 출력 크기 등의 계산 → 29 특징 조합 → 30 이론적 수용영역 → CNN 전체 흐름으로 연결한다.
- 소스 및 학습 결과의 구분: 사과 사진은 기존 저장소 교육용 이미지이며, Feature Hierarchy는 실제 관찰한 모델 중간 출력을 재현한 것이 아니다.

## 신규 파일

- `docs/assets/lesson/lesson_relu_value_graph.svg`
- `docs/assets/lesson/lesson_affine_relu_comparison.svg`
- `docs/assets/lesson/lesson_video_group_split_comparison.svg`
- `docs/assets/lesson/lesson_cnn_feature_hierarchy.svg`
- `docs/assets/lesson/lesson_receptive_field_growth.svg`

각 이미지는 독립 편집 가능한 SVG다. 웹 HTML, `docs/assets/lesson/manifest.json`, `scripts/build_lesson_revision.py`, `scripts/verify_curriculum_overhaul.py`를 함께 갱신했다.

## 수치적 확인 및 QA 한계

- ReLU 벡터: `[-2,-1,0,1,2]→[0,0,0,1,2]`.
- Affine composition: `3(2x+1)−2=6x+1`.
- Video Group: Train 원본 A, Val B, Test C가 서로 겹치지 않는다. 9개 원본 Frame의 합계가 각 방식에서 같다.
- RF 성장: 3×3 Conv k=3/stride1/dilation1 기준 레이어별 `3,5,7`.
- 이 수치들은 `scripts/verify_curriculum_overhaul.py`를 통해 검증한다.
- Chromium 브라우저 1920×1080 및 1366×768 레이아웃 검사 기록은 GitHub Actions `Visual QA - full lecture`의 run으로 확인한다.
- 브라우저 자동 검사 결과만으로 개별 SVG 내부의 모든 라벨 겹침이나 특정 실제 프로젝터 환경의 가독성을 보장하지 않는다.

## Chromium 198화면 최종 검사 결과

- GitHub Pages 배포: https://github.com/sh0427-han/vision_ai_lecture/actions/runs/38345874602 — 성공
- 브라우저 시각 검사: https://github.com/sh0427-han/vision_ai_lecture/actions/runs/38345874619 — 성공
- Intro 15장 · AI Basics 44장 · Vision AI 40장 × 2개 뷰포트(1920×1080, 1366×768), 총 **198화면 렌더링**.
- 자동 레이아웃 문제 레코드 **0건**, 최저 fitScale **0.95**. 자동 검사에서는 주요 블록 클리핑/이미지 로딩 오류가 발견되지 않음.
- 1366×768 실제 스크린샷으로 AI Basics 웹 13, 14, 31장과 Vision AI 웹 29, 30장을 눈으로 확인: 새 ReLU값·Affine 수치·Video Group Split·사과 특징 조합·3/5/7 수용영역의 정렬 및 라벨 확인.
- 이 검사는 HTML 컨테이너의 겹침/잘림과 5개 Figure의 화면을 확인한 것이며, 99개 모든 도식의 SVG 내부 요소에 대한 완전한 형식적 검증이나 모든 모바일 화면에서의 가독성을 보장하지는 않음.

