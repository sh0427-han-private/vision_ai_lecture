# 2026-10-19 · 초보자 강의 슬라이드 수정 및 검토 기록

> 기준: 변경 직전 `main` `3431148b85d967bf4167359a80d47ac4309175bc` / Intro 13장 + Course 41장 = 54장.  
> 변경 목표: 사용자 요청대로 퍼셉트론과 AND·XOR를 단계별로 설명하고, 이전 얼룩말 CNN Architecture부터 Kernel/Matrix·Padding·Pooling·CNN 학습·전이학습까지 큰 그림으로 연결.  
> 변경 뒤 목표: **Intro 13 + Course 42 = 총 55장**, 본강의 110분 + 복습/질의 10분.  
> **검증 상태 구분**: 정적 구조/수치/링크 검증 vs 실제 브라우저 전체 110뷰/배포 확인은 별개이다. 이 기록은 후자를 완료했다고 주장하지 않는다.

## 1. 사용자의 지적과 실제 번호 대조

| 사용자가 언급한 부분 | 2026-10-18 당시 정확한 위치 | 이번 수정 뒤 위치 | 판단과 조치 |
|---|---|---|---|
| Intro 13 사진이 틀림 | **Intro 13** · Vision의 어려움 | Intro 13 | 원인은 기존 사진 변환 CSS가 `.iv-revision` 영역에 한정되어 있으나 새 장표의 적용 구조가 달랐기 때문. 기존 동일 생성 사과에 **어두움·평면 회전·부분 가림**을 각각 확실히 적용. 사진은 실제 카메라 시점 재촬영이 아님. |
| Course 5 Anomaly Detection 제외 | C5 Task/Model/Data | C5 | 4종→**Classification/Detection/Segmentation 3종**. 출력·Model/Label 구조 비교. |
| 퍼셉트론→AND→XOR 천천히 | C6 퍼셉트론, C7 AND/XOR 동시 | **C6 퍼셉트론, C7 AND, C8 XOR** | 두 Gate 각각 **진리표/입력 좌표/출력/직선 분리 여부** 별도 시각화. C9 ReLU→C10 Affine층 한계로 연결. |
| Course 9 사진이 적절한가? | 구 C9 **비선형성** | **C10 비선형성** | 사진이 아니라 **선형층과 ReLU 비선형층의 개념 SVG**가 적합하다. 실사 사진을 넣으면 수학적 분리 가능성에 대응하기 어려우므로 비교 도식을 유지. 현재 C9는 ReLU 그래프. |
| “Intro 11 Kernel 이후 Matrix” | Intro 11은 ‘사과 종류 다양성’, 실제 **Course 11 Kernel / Course 12 Feature Map** | **C12 Kernel / C13 Feature Map** | 기존 입력 5×5·Kernel 3×3 수치를 유지하고 **출력 Feature Map 3×3 전체**를 같은 장에서 직접 표시, 다음 장의 위치별 이동과 대응. |
| C13~14 설명이 잘 안 됨 | **C13 Weight Sharing / C14 Feature Channel** | **C14 / C15** | “왜 같은 Weight 9개를 사진 전체에서 공유하는가?”, “왜 RGB 3채널을 보는 필터 2개가 Map 2장을 만드는가?”를 부제에 직접 명시. |
| Padding 왼쪽/오른쪽 Matrix 비교 | 구 C16 Padding | **C17 Padding** | **같은 원본 입력 3×3, Kernel 3×3=1, Stride 1**을 위에 공통 배치. 왼쪽 Padding0→1×1 출력45 / 오른쪽 Padding1→바깥 0의 5×5 입력→3×3 출력 `[[12,21,16],[27,45,33],[24,39,28]]`. |
| Max Pooling 사용 이유 | 구 C17 | **C18** | 4×4의 16칸→2×2의 4칸으로 줄여 **다음 연산량·메모리 감소**, 강한 반응을 보존하지만 위치 정보가 손실되는 장단점 명시. |
| Course 23~24 슬라이드 속 슬라이드 | 구 C23–24 | **C24–25** | 실사 처리결과를 ‘완성된 PPT 한 장’ 형태 이미지로 넣는 구조를 없애고 **같은 사과 사진을 각 패널에 직접 배치**. 비율 왜곡/Letterbox와 밝기/회전/가림은 브라우저 표시 변환 시뮬레이션(실제 새 이미지 파일 생성/학습은 아님). |
| 기존 얼룩말 CNN Architecture | 구 C10 자체 개념도 | **C11** | 이전에 쓰던 Developers Breach **cnn_banner.png 원본 링크**를 다시 표시. 브라우저가 원본 이미지에 접근 못할 때 자체 로컬 ‘이미지→Conv/Feature Map→분류 Head’ 구조로 대체. 슬라이드 안에 원본 이미지 출처 표시. |
| Course 27 도형 정렬 | 구 C27 학습 Forward/Backward 교차 SVG | **C28** | **두 개의 수평 레인**: Forward 사진→Extractor→Head→Prediction, Backward 정답+예측→Loss→Gradient→Optimizer. 선/박스 교차를 제거하고 어떤 Weight가 업데이트되는지 명시. |
| Course 29 전이학습 | 구 C29 | **C30** | 앞 CNN Architecture와 같은 ‘입력→Feature Extractor→Classification Head→Class’ 구조로 표시. **Backbone 파란색 Freeze, Head 초록색 Train**, 필요 시 Fine-tuning을 설명. |

## 2. 핵심 계산과 교육 정확성 검토

- **AND**: `z=0.5x₁+0.5x₂−0.7`, Step `z≥0`이면 1. `(1,1)`에서만 `z=0.3`으로 1; 나머지 `z<0`, 직선 `x₁+x₂=1.4`로 구분 가능.
- **XOR**: `(0,1)`과 `(1,0)`만 1. 좌표 평면에서 두 양성이 대각선에 있어 직선 하나로 분리 불가. 별도 ReLU 이후 여러 뉴런·비선형 조합과 연결.
- **Kernel→Feature Map**: 같은 5×5 입력·3×3 Kernel · Stride1/Padding0/Bias0. `[[-6,12,16],[-6,8,15],[-4,2,7]]` 출력. Kernel 장에는 전체 결과를 시각적으로 표시하지만 verifier가 읽는 *기존 5×5/3×3 Matrix는 그대로 유지*.
- **Padding**: 공통 원본 `[[1,2,3],[4,5,6],[7,8,9]]`, 모두 1인 3×3 Kernel, Stride1. Padding0→45 한 칸, Padding1→3×3 결과. 양쪽 입력·Kernel이 동일하다는 사실을 제목과 Layout로 확인.
- **Pooling**: 기존 검증용 4×4→2×2 Max 결과 `[[6,4],[7,9]]`; Channel마다 별도 적용, 위치 세부를 잃음.
- **전이학습**: ‘Backbone Freeze + 새 Head 학습’은 대표적인 **Head-only** 방식이고 모든 Transfer Learning이 항상 그렇게 동작하는 것은 아님. 미세 조정 때는 Backbone 일부도 갱신할 수 있음.
- **시각자료 구분**: 브라우저 CSS 사진 변형 = 표시 시뮬레이션 / 교육용 합성 원본 = 실측 생산라인 사진 아님 / 원본 얼룩말 Architecture = 외부 재사용 Figure(출처 표시). 같은 이미지를 썼더라도 실제 모델의 Pixel 출력이라고 주장하지 않음.

## 3. 수정 파일과 기술 영향

- `docs/intro.html`, `docs/vision_motivation.css`: I13 사진 변형과 표현 수정.
- `docs/vision_ai_course.html`: C5/C7–8/C11–18/C24–25/C28/C30 재구성. 기타 55장 순서와 인접 슬라이드 논리는 보존.
- `docs/cnn_lecture_refinement.css`(신규): 모든 Gate, 행렬, Padding, CNN 구조·학습·Freeze, Preprocessing/Augmentation Figure에만 적용되는 스코프 CSS.
- `docs/two_hour_manifest.json` / `docs/lecture_outline.js`: 55장 전체 새 물리적 번호와 9개 시간 블록(합계 110분) 동기화.
- `README.md`, `TWO_HOUR_LECTURE_PLAN.md`, `PROJECT_GUIDE.md`, `TODO_VISION_AI_LECTURE.md`: 현행 개수/번호/시간표, 이번 수정을 반영.
- `scripts/verify_two_hour_course.py`, `scripts/verify_learning_routes.py`, `scripts/audit_visual_slides.py`: 55장, 별도 AND/XOR, Padding/전이학습 Layout, 외부 원본 Zebra + Fallback 조건 점검.

## 4. 검사 결과 및 남은 QA

**GitHub Connector 기반 정적 HTML 내용·구조 검사(수정 브랜치):**
- [x] Intro 13 + Course 42, 총 55장 · 55개 Outline 항목.
- [x] 각 슬라이드 Title/Concept/Manifest 동일 / 9구간 110분+질의 10분 / 55개 슬라이드 범위 커버.
- [x] 슬라이드 HTML 열림·닫힘 태그 균형 및 CSS 스코프 규칙 중괄호 균형.
- [x] Kernel 입력/출력 계산, Padding 원본/0/1, Max Pooling 출력 숫자 일치.
- [x] 새 Gate·Kernel·Pool·Transfer 도식과 CSS Cache 버전 정적 연결 확인.

**별도 검증 필요:**
- [ ] Python 자체 정적 검증 스크립트 `python scripts/verify_curriculum_overhaul.py`와 `python scripts/verify_two_hour_course.py` 실제 실행 결과.
- [ ] Chromium `scripts/verify_learning_routes.py`의 55개 TOC, Intro I13→Course1, Pixel/RGB, 학습 C26, 교육용 Threshold C40 확인.
- [ ] 발표 해상도 1920×1080 / 1366×768 각각 **55장 × 2 = 110개 View**: 글자 잘림·과밀·그림 겹침·이미지 로딩 확인. 특히 C5/7/8/11/12/17/18/24/25/28/30.
- [ ] 원본 얼룩말 외부 CDN 이미지의 실제 로딩과 회사 네트워크 차단 시 로컬 Fallback 표시. 외부 URL이 실패해도 **구조 자체가 보이도록** 설계했지만 실제 브라우저 확인이 필요하다.
- [ ] 변경 후 PR Merge→최신 main SHA 확인→GitHub Pages Workflow 성공→공개 URL 렌더 확인.
- [ ] 마지막 발표 실제 120분 리허설. Gate 1장을 늘렸어도 전체 배정은 110+10으로 고정.

## 5. 직접 재사용 외부 그림 출처

Swapna K E, **Convolutional Neural Network | Deep Learning**, Developers Breach, Aug 21, 2020.  
원문: https://developersbreach.com/convolution-neural-network-deep-learning/  
원본 그림: https://i0.wp.com/developersbreach.com/wp-content/uploads/2020/08/cnn_banner.png?fit=1200%2C564&ssl=1

기존 `assets/SOURCES.md`에도 같은 원본 출처가 보존되어 있다. 이 Figure는 CNN 입력·Convolution/Pooling·분류 결과를 설명하는 대표 교육용 그림으로 사용하며 **특정 사용자의 사과 검사 모델 실제 구조/결과는 아니다**.
