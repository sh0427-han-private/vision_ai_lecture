# Vision AI 기초강의 — 원리 중심 개편 실행 기록

**작업일:** 2026-10-18 (KST)  
**사용자 결정:** 검토서의 A안 — Vision AI 내부 원리 이해 중심  
**선행 검토:** [내용·흐름](2026-10-18_VISION_AI_CONTENT_FLOW_REVIEW.md) / [UI·그림](2026-10-18_VISION_AI_UI_FIGURE_REVIEW.md)

## 구현 범위

1. 강의는 Intro 11장 + Course 39장 **50장 유지**. 110분 본강의 + 10분 질의.
2. 전체 순서: Input/Pixel → 환경 변화 → Task → 퍼셉트론/AND·XOR/ReLU → **CNN 전체·세부** → Dataset·독립분할·전처리·증강 → Weight 학습/Loss·Inference/Transfer → 평가 → 개념 회수.
3. 실제 구조를 알기 전에 `ŷ=wx`와 Gradient가 나오던 **Course 4–6을 새 23–25로 이동**. CNN 전체 구조는 새 **Course 8**.
4. 새로운 정확한 HTML/SVG/CSS 중심 도식: 모델 선택, 비선형 층 대비, CNN 전체 Feature Map 구조, 지역 연결/가중치 공유, RGB→Feature Channel의 **병렬 계산**, 데이터 촬영 조건, Loss 갱신, Batch/Epoch, Accuracy 함정, 전체 프로젝트 과정·질문·실패 상황.
5. Intro의 첫 화면을 **동일 사과 결함 질문**으로 연결하고, 의자 다양성·균열 예시가 왜 등장하는지 문장에 명확히 적음. 사람 vs 숫자 대비에서는 유아적인 얼굴 SVG 아이콘 제거. 7–9번에는 정리 한 줄 추가.
6. 실제 Pixel 클릭·RGB 값·해상도 비교, 학습 가중치 갱신, 임계값별 교육용 100건 재집계 등 기존 실습 유지. 교육용 수치와 실제 SqueezeNet Feature Map을 혼동하지 않게 구분.
7. 각 항목의 제목/짧은 부제/중앙 Figure/하단 정리 형식 유지. 외부 **직접 사용한** 회랑·Stanford 강아지 원본 사진의 출처 유지, 자체 수치 도식에는 출처 추가하지 않음.

## 주요 신구 번호 대응

| 주제 | 이전 Course | 개편 Course |
|---|---:|---:|
| 퍼셉트론 | 7 | 4 |
| AND / XOR | 8 | 5 |
| ReLU | 9 | 6 |
| CNN 전체 구조 | 11 | 8 |
| Kernel → Feature Map | 12–13 | 9–10 |
| 지역 연결 / Channel | 14–15 | 11–12 |
| Stride / Padding / Pooling | 16–18 | 13–15 |
| 실제 SqueezeNet Feature Map | 19 | 16 |
| Backbone / Head | 21 | 17 |
| Dataset / Split | 22–24 | 18–20 |
| 전처리 / 증강 | 28–29 | 21–22 |
| 가중치 학습 데모 / Loss / 추론 | 4–6 | 23–25 |
| Kernel 학습 / 전이학습 / 로그 / 과적합 | 20,25–27 | 26–29 |
| Threshold / 지표 / IoU | 30–34 | 30–34 |
| 개념 회수와 검증 | 35–39 | 35–39 |

## 검증한 것 — GitHub Connector 기반 정적 검사

- 두 HTML의 50장과 50개 목차·`manifest.json`의 **슬라이드 개념·제목·번호 일치**.
- 9개 연속 시간 블록이 110분을 차지하고, 질문 10분을 별도 유지.
- 의도한 선행개념 순서(CNN 구조가 Loss 학습보다 먼저 등장) 확인.
- 전체 22개 고유 로컬 이미지 경로를 GitHub에서 **실제 존재 확인**.
- 새 강의 CSS 블록 중괄호 **137개 여닫힘 개수 일치**.
- 새 HTML의 열고 닫는 주요 Tag 구조, Subtitle, 간결한 Title, 목차 Cache Key 일치.
- 기존 숫자 예제 재검산: Feature Map `[[-6,12,16],[-6,8,15],[-4,2,7]]`, Padding 출력 `[[12,21,16],[27,45,33],[24,39,28]]`, Max Pooling `[[6,4],[7,9]]`.
- Threshold 실습의 TP/FN/FP/TN 단일 DOM 바인딩과 코드 계산 수치 보존.
- 외부 원본 사진 출처가 남아 있는 4개 공개 슬라이드(I-02, C-16, C-21, C-22) 확인.

## 아직 완료로 간주하지 않은 항목

- **실제 GitHub Pages 렌더링 스크린샷**(1920×1080, 1366×768 포함), 실측 글자 잘림·도형 겹침·과도한 자동축소.
- Playwright로 모든 슬라이드를 실제 클릭 이동, 학습 버튼, Threshold 선택, 모바일 목차와 접힘을 실행한 브라우저 테스트.
- 실제 `main` merge 이후 GitHub Pages Workflow와 웹사이트의 최신 Commit 반영.

위 항목은 Connector의 정적 파일 검사만으로 성공을 보증할 수 없다. 실제 CI/브라우저 결과를 확인할 수 있을 때 따로 기록하고, **정적 검증 결과를 UI 실측 결과로 표현하지 않는다.**

## 후속 변경 시 주의

- 옛 `#slide-N` 고정 링크가 다른 내용으로 이동할 수 있으므로 `docs/lecture_outline.js`, `docs/two_hour_manifest.json`, `TWO_HOUR_LECTURE_PLAN.md`, `README.md`를 함께 갱신.
- `docs/ai_basics.html` 및 `docs/vision_ai.html`은 이전 참고 슬라이드로 보존.
- 실습의 계산 JS·데이터 파라미터는 건드리지 않고, 검증된 결과만 시각적으로 교체.
- 사진/논문 Figure를 직접 사용했다면 이미지 가까이 출처를 표기. HTML/SVG 자체 제작 도식은 정확한 입력·출력·수치 관계를 재검증.
