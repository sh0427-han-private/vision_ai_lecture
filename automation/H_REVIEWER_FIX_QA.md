# H구간 P53–P55 Reviewer 이슈 수정 및 재검수 인계

- **Builder source tested:** `c35f1f7175788921f2a924f3ef1f4e0e552bb5e2` ([Commit](https://github.com/sh0427-han/vision_ai_lecture/commit/c35f1f7175788921f2a924f3ef1f4e0e552bb5e2)).
- **Work branch:** `automation/approved-55-20261019`. This QA handoff documentation is added after the tested source SHA, with no subsequent HTML/CSS/JS/QA-script change.
- **Original independent review pinned to:** `4469656244e55476b2c0e8ca2a1344a9710a29db`, `review/h-4469656-20261019`; its three Reviewer reports, judgement and SHA are unchanged. **Reviewer must independently re-review this new source SHA; do not auto-close H-01/02/03.**
- **Reviewer references:** `reviews/automation/H-4469656.md`, `reviews/automation/H-4469656-VIEWPORT-EVIDENCE.md`, `reviews/automation/H-4469656-CHROMIUM.md`.

## Implementation changes

| Issue | File | Change | Builder check |
|---|---|---|---|
| H-01 Major | `docs/vision_ai_course.html`, `docs/approved_h.css` | Replace outline-only background condition with two side-by-side **educational synthetic composites**: neutral matte surface and a grid-patterned surface. Both independently render the **same original generated JPEG** with identical source dimensions (960×640), user-space subject clip path, image placement, circle ROI at (596,226), radius 39 and stroke. No lighting change applied to the apple. Actual exterior background pixels change. Captions and adjacent text state controlled synthetic comparison; not actual model predictions/errors. | Browser at both viewports: SVG source/path/circle equal, subject and green-ROI rendered pixel crops exactly equal, external matte/grid sample differs by **120/1600** pixels (difference >8 RGB levels). No simulated model scores. |
| H-02 Minor | `docs/vision_ai_course.html`, `docs/approved_h.css` | P53 generated photo given a nearby visible caption: educational generated photo, green ROI explanatory mark, not model detection. | Readable in 1920 and 1366 screenshots; source semantics and underlying workflow nodes unchanged. |
| H-03 Minor | `automation/check_group_browser.py` | Before P54 capture wait up to 20 seconds for exactly two `data-ready=true` Canvas elements with exact dimensions **240² and 24²**, all pixels opaque and nonuniform; on timeout record `canvas_errors`, skip incomplete screenshot and fail the final check. Snapshot additionally compares two synthetic backgrounds at matched image dimensions without modifying the full-slide screenshot. | Both viewports: 240 Canvas 57,600 opaque pixels and 24 Canvas 576 opaque pixels; no canvas errors. |

**Scope:** 42 Course slide sections retained; only P53/P54 content and H-scoped CSS changed; P55 HTML unchanged. No A–G slide sections, G correction data, Manifest, Outline, title/Concept IDs, approved Storyboard or Reviewer reports modified. Synthetic mask is a hand-defined foreground contour, **not a model-produced mask nor real measured background replacement**. The side-by-side images are controlled illustrations; live photographic validation remains recommended if this is converted into an empirical result.

## Observed browser, static and regression evidence

- **H job:** [Approved H browser correction CI — SUCCESS](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424771) at the tested `c35f1f7175788921f2a924f3ef1f4e0e552bb5e2`.
- **H PNG and JSON artifact:** [approved-h-browser-qa](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424771/artifacts/12183008736). Full-screen six captures: `1920-workflow.png`, `1920-project-iterate.png`, `1920-project-check.png`, `1366-workflow.png`, `1366-project-iterate.png`, `1366-project-check.png`; four 200px pixel-comparison image crops; `report.json`.
- **Actual viewport fitScale (1920 / 1366):** P53 **1.000 / 0.984**, P54 **1.000 / 0.943**, P55 **1.000 / 0.968**. No `contentBottomOverflow`, `contentRightOverflow`, horizontal scroll overflow, bounding-box overlap, broken SVG image, console `pageerror`, or blank resolution Canvas. All six PNGs also inspected visually by Builder; no observed crops, label collision, unreadable core labels or clipped content.
- **Core consistency:** `python automation/verify_approved_contract.py --final` **PASS**; `python scripts/verify_two_hour_course.py` **PASS**. Exactly **Intro13 + Course42 = 55 slides** and 8 blocks **26+10+23+22+9+15+10+5 = 120 minutes**. Manifest, Outline and complete approved sequence checked.
- **Interactive/route regression:** `python scripts/verify_learning_routes.py` **PASS** in the H CI; this exercises deck navigation, ToC/deep links, P53 workflow links, P54 canvas raster, P55 details/Mask Label expansion and the established threshold/keyboard/Reset operations.
- **G unchanged-implementation regression:** [Approved G browser re-review — SUCCESS](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424868); [G 10 PNG + report](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39246424868/artifacts/12182733802). H changes did not regress the 10 G viewport captures or interaction assertions.
- This is technical and visual Builder QA, **not independent Reviewer PASS**, not 120-minute in-class rehearsal or observed GitHub Pages deployment. A–F were preserved but were not re-reviewed exhaustively here. The G independent final re-review remains separate.

## Reviewer-specific acceptance gates

Confirm H-01 at the new SHA by direct 1920/1366 image examination (same subject/defect/location/lighting, actually different background pixels, text clearly describing *synthetic not inference*). Confirm H-02 caption legibility beside the P53 apple. Confirm H-03 by `canvas_checks` in `report.json` and optional induced delayed loading / error path. Confirm P55 previous/next controls and details; ensure G CI evidence remains valid. **Do not rewrite or retroactively change the pinned review reports.** No `main` merge or Pages deployment was performed.
