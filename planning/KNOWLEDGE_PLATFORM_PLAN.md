# Vision AI → AI/ML Knowledge Platform 설계

> **작업 상태:** Phase 1–3 설계 초안 · 2026-11-02 · Base `23d48aeeb9124edcbffa3662c63cd7cf34f80315`. 독립 Reviewer **PENDING**. 기존 55장 강의와 사이트 구현은 이번 PR에서 변경하지 않는다.

## Repository 조사 결과

| 대상 | 현행 확인 사항 | 보존·통합 결정 |
|---|---|---|
| 작업 Repository | [sh0427-han-private/vision_ai_lecture](https://github.com/sh0427-han-private/vision_ai_lecture), main | 이 저장소만 쓰기 |
| 디자인 Repository | [sh0427-han/design-template-library](https://github.com/sh0427-han/design-template-library), main | 읽기 전용. HTML 8종·컴포넌트 명세 참조 |
| Intro 강의 | `docs/intro.html`, 13장 | 수정하지 않고 개념 페이지에서 슬라이드 링크 |
| 본 강의 | `docs/vision_ai_course.html`, 42장 | 수정하지 않고 연결 |
| Manifest | `docs/two_hour_manifest.json`, `approved55-20261019-1` | Slide ID, Deep Link, 강의 순서 보존 |
| Routing | `index.html`, `docs/index.html`은 Intro 1번으로 Redirect | 현행 공개 경로 보존 |
| UI·실습 | `docs/slide.css`, `docs/slide.js`, `docs/interactive_lessons.css/js` | 기존 스타일/실습 유지; 신규 Knowledge 전용 namespace 계획 |
| 검증 | `scripts/verify_curriculum_overhaul.py`, 브라우저 감사 스크립트 | 기존 정적/브라우저 회귀 유지 |
| Pages workflow | `.github/workflows/deploy-pages.yml`, `main` push → `./docs` 업로드 | 신규 정적 페이지도 `docs` 아래만 배포 가능 |

**이전 주소 감사:** 현재 README와 PROJECT_GUIDE에는 `sh0427-han.github.io/vision_ai_lecture/` 등 이전 주소가 남아 있다. 실제 Pages 배포 URL과 현재 상태를 API/사이트에서 확인하지 못했으므로 이번 PR에서 URL을 임의 교체하지 않는다. 실제 이전 검증 후 별도 수정한다.

**문서 이력 주의:** `planning/SLIDE_STORYBOARD.md`에는 59장 당시 현재 상태를 기술한 역사적 문장이 있다. 현행 구조는 `docs/two_hour_manifest.json`과 `docs/lecture_outline.js`가 우선이며 55장이다.

## 핵심 설계

1. 483개 고유 Concept ID를 15개 PART에 분류했다. 등록 노드의 `status`는 전부 `Related`: 현장 구현/실험 기록이 확인됐다는 주장 아님.
2. 필수 선행은 Directed Acyclic Graph(DAG), 추천 경로는 별도 `learning_paths`로 분리한다. 동일 개념은 여러 경로에서 링크로 재사용한다.
3. 순차적 입문은 **Pixel → RGB → Matrix/Tensor → Kernel → Convolution → Feature Map → CNN**이라는 설명 흐름으로 제공하되, 각 수학 노드의 내부 선수 관계는 정확히 유지한다.
4. 이후 CV, Anomaly Detection, Video AI, Geometry, Time-series, MLOps로 분기한다. Evaluation·Dataset·Engineering은 각 경로에서 사용한다.
5. 한 개념에 Why/Intuition/Mechanism/Math/Code/Application/Limitations/Related를 갖되, 기초 개념의 화면에는 핵심만 먼저 보여준다.
6. 기초 난이도와 실제 구현 검증 상태는 분리. `legacy_slide`는 현재 강의 설명 연결이지 현장 적용 상태의 증거는 아니다.

## 웹 정보 구조 제안 (이번 작업에서 미구현)

```text
docs/intro.html                        # existing: preserve
docs/vision_ai_course.html             # existing: preserve
docs/knowledge/index.html              # proposed: PART 00–14
docs/knowledge/concepts/<id>.html       # proposed: Scroll concept detail
docs/knowledge/paths/index.html        # proposed: learning paths
docs/knowledge/projects/index.html     # proposed: verified cases
docs/knowledge/assets/                 # proposed: isolated CSS/JS
planning/concepts.v1.json              # created: concept graph canonical source
scripts/validate_concept_graph.py      # created: graph validator
```

새 Concept URL 인코딩과 메뉴 통합은 Vertical Slice에서 결정한다. 메인 리다이렉트/기존 강의용 Slide JS·CSS는 이번 단계에서 변경하지 않는다. 로그인·DB·서버 API·외부 CDN은 범위 밖.

## 개념 상태와 사례 관계

`level`은 학습 수준(Foundation/Basic/Intermediate/Advanced/Research). `status`는 증거(Implemented/Experimented/Reviewed/Related). 실제 연구 프로젝트 Case A–G는 `applications`를 통해 **후보 관계**만 부여했다. 프로젝트 코드·실험 로그/데이터셋 없는 상태에서 성능 수치나 구현 완료를 주장하지 않는다.

## 참고 원본

- Vision AI: AGENTS, README, PROJECT_GUIDE, HTML_DESIGN_RULES, SLIDE_STORYBOARD, TWO_HOUR_LECTURE_PLAN, two_hour_manifest, automation/PROGRESS, 현재 HTML/CSS/JS.
- Template library: AGENTS, README, DESIGN_SYSTEM, TEMPLATE_CATALOG, REFERENCE_REUSE_WORKFLOW, FIGURE_PRODUCTION_STANDARD, DESIGN_COMPONENT_RECIPES, REFERENCE_PAGE_SPECS와 `templates/html/` 원본.
- 브라우저 실제 렌더링은 이번 문서 설계 단계에서 실행하지 않음. Reference 저장소 과거 테스트를 신규 Vision AI 브라우저 검수 결과로 사용하지 않는다.

## 요구사항과 산출물 연결

[전체 교육과정](FULL_CURRICULUM.md) · [고유 개념 표](CONCEPT_CATALOG.md) · [선수 그래프](CONCEPT_DEPENDENCIES.md) · [추천 학습 경로](LEARNING_PATHS.md) · [콘텐츠 규약](CONTENT_STYLE_GUIDE.md) · [8패턴 매핑](TEMPLATE_MAPPING.md) · [단계별 로드맵](IMPLEMENTATION_ROADMAP.md). 기계 판독용 정본은 [concepts.v1.json](concepts.v1.json).
