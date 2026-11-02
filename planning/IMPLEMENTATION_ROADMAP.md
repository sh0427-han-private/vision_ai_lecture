# Knowledge Platform — 구현 로드맵

> 현재 진행 단계 **Phase 1–3 설계 작성**, Independent Reviewer **PENDING**, HTML 구현 **NOT STARTED**. Base `23d48aeeb9124edcbffa3662c63cd7cf34f80315`. 이번 브랜치에서 기존 Manifest/강의/Pages 배포 원본은 미수정.

| Phase | 작업 및 산출물 | Acceptance Criteria | 현재 상태 |
|---|---|---|---|
| 1 Repo Audit | 기존 55장/Manifest/Deep Link/디자인 8종 조사 | main HEAD·경로·이전 URL 추적 | 조사 수행, Pages 실서비스 미확인 |
| 2 Curriculum | FULL_CURRICULUM, CONCEPT_CATALOG, CONCEPT_DEPENDENCIES, concepts.v1.json | 모든 노드 ID 유일, missing ref=0, DAG cycle=0, 분기별 선수 관계 검토 | 문서 작성, 독립 검토 대기 |
| 3 Content/Design | CONTENT_STYLE_GUIDE, TEMPLATE_MAPPING, LEARNING_PATHS, KNOWLEDGE_PLATFORM_PLAN | 기존 Slide 보존·Scroll 정보 설계·8패턴 매핑 | 문서 작성, 독립 검토 대기 |
| 4 Vertical Slice | Pixel→RGB→Matrix/Tensor→Kernel→Convolution→Feature Map→CNN | Input·식·Python·JS·Figure·Shape 일치, 실제 브라우저 테스트 | NOT STARTED |
| 5 Expand | PART 00–14를 작은 독립 PR로 확장 | 선행 개념·출처·실습·한계·독립 리뷰 | NOT STARTED |
| 6 QA/Release | 정적/브라우저/원문/접근성/배포 검증 | 55장 회귀·Deep Link·4 viewport·계산·Reviewer PASS | NOT STARTED |

## Planner → Builder 구현 지시: Phase 4

**유지:** `docs/intro.html`, `docs/vision_ai_course.html`, `docs/two_hour_manifest.json`, `docs/lecture_outline.js`, `docs/index.html`, `index.html`, 기존 CSS/JS 전체. 공개 Pages 주소 변경 금지. 디자인 Reference 저장소 읽기 전용.

**허용 추가:** `docs/knowledge/` 신규 Scroll/index/선택된 7개 기본 Concept 및 독립 CSS/JS/실습/테스트. 메타데이터는 `planning/concepts.v1.json`을 정본으로 읽는다. 신규 미구현 Concept URL은 클릭 가능한 깨진 링크 대신 'planned' 로 표시한다.

**교육 설계:** (1) 원본 픽셀 선택과 RGB 수치 대응, (2) H/W/C와 Matrix/Tensor, (3) 5×5 입력·3×3 커널의 1회 합성곱 숫자 계산, (4) Filter 이동과 Feature Map, (5) S/P 변화와 출력 Shape, (6) CNN 내 H/W 축소·채널 수 관계, (7) 기존 55장 관련 Slide로 연결. Fixed filter와 학습 Kernel, 학습과 고정 Weight 설명용 계산을 구분한다.

## 필수 QA

1. `python scripts/validate_concept_graph.py`: ID/참조/순환/후속 역인덱스 검사.
2. `python scripts/verify_curriculum_overhaul.py`: 기존 55장 구조 검사(현 main의 테스트 환경 규정 준수).
3. Python NumPy와 브라우저 JS가 5×5·3×3/S1/P0/D1→3×3을 동일 계산, 최소 2개 셀의 곱/합을 손으로 검산.
4. Pixel/RGB/Shape/좌표를 동일 실제 입력에서 갱신. HTML/JS 미실행을 시각 PASS로 대체하지 않음.
5. 1600×950,1440×810,1366×768,1280×720 Chromium screenshots와 Overflow·동작·폰트 확인.
6. 기존 55장 제목·수·Manifest 버전·Slide ID와 Deep Link 불변.
7. 실제 산업 프로젝트 측정 수치와 Toy/Synthetic 구분.
8. Independent Reviewer는 변경된 최신 commit, 산출물, 테스트 결과를 **수정 없이 직접** 검토하여 PASS/REVISE/BLOCKED 기록.

## Reviewer 인계

이번 구현 주체의 자체 검증만 가능. 현재 도구에서 Builder와 다른 독립 Agent/격리 세션 실행 기능을 확인하지 못했기 때문에 **Reviewer PENDING**이며 PASS가 아니다. 독립 세션이 실제 GitHub의 새 문서·JSON·diff·회귀 기준을 재검토해야 한다. 특히 483개 노드의 정확한 최소 선수 관계, 중복 이름, Part Anchor의 과잉 의존, 55장 링크 대응을 점검한다.

REVISE인 경우 지적별 근거/영향/대상 파일/기대동작을 명시하고 Planner가 범위를 정해 Builder가 수정한 뒤 **새 SHA**를 독립 재검토한다. 자동 수정/재검토는 최대 3회.

## Release Gate

Main Merge/실제 Pages 공개 배포는 별도 사용자 승인 후 시행. 현재 `README.md`/`PROJECT_GUIDE.md`의 과거 GitHub Pages URL은 배포 환경에서 확인 전 일괄 치환 금지. 신규 사이트 경로, 모바일 브라우저 수준, 현장 사례 실험 증거는 각각 별도 검증 필요.
