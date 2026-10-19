# Vision AI Approved 55 — Builder Progress

**Date:** 2026-10-19  
**Branch:** `builder/approved-55-a-intro-20261019`  
**Baseline:** `main@ad3f0a8ce3ca8bce3a52d92c2198654dfcc4c298`, PR #113 already merged.  
**Plan:** `planning/vision-ai-120min-storyboard-draft-20261019/planning/SLIDE_STORYBOARD.md` (Approved).

| Group | Planned slides | Minutes | Status |
|---|---|---:|---|
| A | P01–P13 | 26 | Implemented; Chromium automatic QA passed; Reviewer pending |
| B | P14–P18 | 10 | Implemented; 10-view Chromium B QA and route tests passed; Reviewer pending |
| C | P19–P27 | 23 | Pending |
| D | P28–P36 | 22 | Pending |
| E | P37–P40 | 9 | Pending |
| F | P41–P47 | 15 | Pending |
| G | P48–P52 | 10 | Pending |
| H | P53–P55 | 5 | Pending |

A changes: P01 image→analysis→annotated suspect output; P02 new AI⊃ML⊃DL / Computer Vision dual-axis Figure; P03 repeated checks→AI candidate→human verification; P04 number bridge preserved; P05 H×W and Grayscale 6×6 click preserved; P06 measured RGB click+keyboard preserved; P07 RGB channel stack and pixel count retained; P08 new simulated RGB frame strip and T×H×W×3; P09 original resolution interactive kept; P10 lighting-only controlled three-way comparison; P11 rotation/crop/occlusion/blur distinctions kept; P12 object vs defect labels separated; P13 normal/defect × brightness 2×2 with disclosure of different source images.

**Interim branch slide count:** Intro 13 + Course 45 = 58, legacy time blocks = 120 min (Intro legacy 24 min). Final approval target is 55 slides / 120 minutes with A time allocation 26 min. Reconcile inherited timing with B-H redesign, never mark total 55 complete now.

Changed paths: `docs/intro.html`, `docs/intro_approved_a.css`, `docs/vision_ai_course.html` (only outline cache bust), `docs/two_hour_manifest.json`, `docs/lecture_outline.js`, `scripts/verify_two_hour_course.py`, `scripts/verify_intro_pixel_interactive.py`, `assets/SOURCES.md`, `BUILDER_PROGRESS.md`.

## Automated QA evidence (2026-10-19)

- [Intro pixel interaction CI #39221664937](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39221664937): **SUCCESS**. Playwright Chromium checked pixel 12x8 source measurement, Grayscale 6x6 selection / brightness reset, RGB pixel measured values, HWC shape, resolution Canvas and page exceptions.
- [Figure overlap CI #39221664875](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39221664875): overall **FAIL** (pre-existing out-of-scope Course slides only). Rendered 118 views (59 slides x 2 viewports: 1920x1080, 1366x768). Group A P01-P13 reported **zero** overflow, overlap, broken images or forced shrink issues. Course C11 XOR has 1366x768 fit=0.871 and Course C34 fixed CNN features has fit=0.848; these are known baseline problems scheduled for groups C and F.
- SVG text audit: 78 assets, 1,199 text nodes, zero clipped labels, zero overlaps. Structural verification finished successfully before figure audit failure.
- Due to the two legacy Course layout issues, the figure CI did not reach the full navigation regression test. Independent subjective inspection of the A screenshots, Presenter readability / live rehearsal, Reviewer approval and GitHub Pages deployed verification remain pending.
- Previous PR #113 Reviewer Major RML-01/02/03 and FLOW-01 are tracked for B P16/P17. The Reviewer files were not edited.

**Status:** A source and automated-browser implementation ready for Reviewer; **NOT Reviewer-Verified**. B-H pending and 55-slide final build incomplete.

## Group B implementation (2026-10-19)

- P14: single apple ROI → Classification Class GT / small defect Box GT / Pixel Mask GT.
- P15: retained existing PR #113 Python `add(a,b)` and correct outputs 2/3.
- P16: addressed RML-01 by identical paired D-L/D-D/N-D thumbnails, consistent CSS darkness and normalized normal image size; RML-02 by one shared Model M spanning learning and inference rows with arrows from both flows, explicit prediction not measured and independent evaluation; RML-03 by concise Korean-first main annotations and viewport scoped CSS. Manual Reviewer judgment pending.
- P17: removed duplicate C04 `vision-evolution`, absorbed pretraining and method-selection concepts into revised `model-choice`; one decision flow and an independent validation gate for every exit (FLOW-01).
- P18: three rows comparing image Class, defect Box+Class and Pixel Mask annotation effort, Ground Truth vs Prediction distinction and qualitative-cost caveat.
- The 58-slide staged route has Intro13 + Course45; approved final is 55. Manifest/Outline reindexed downstream Course slide numbers by one. Legacy 120-minute block total retained, approved A=26 min vs interim Intro=24 min still needs regrouping with C–H.
- Files: `docs/vision_ai_course.html`, `docs/b_approved_figure.css`, `docs/intro.html` (outline cache only), `docs/two_hour_manifest.json`, `docs/lecture_outline.js`, `scripts/verify_two_hour_course.py`, `scripts/verify_learning_routes.py`, `assets/SOURCES.md`, `BUILDER_PROGRESS.md`.
- CI evidence and remaining problems: see following final validation notes; do not mark Reviewer-Verified.

## Group B CI validation and unresolved work

- Latest browser CI source [commit c1e01d4](https://github.com/sh0427-han/vision_ai_lecture/commit/c1e01d474b31ee8b3931b19376bed056ab77f5d3). [Intro interaction run 39225261789](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39225261789): **PASS**.
- [Lecture figure + route + targeted B run 39225261764](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39225261764): structural/number/math verification PASS; SVG text layout pass; 116 Chromium captures = 58 slides × 2 viewports (1920×1080, 1366×768). Zero automatically flagged layout issues in P14–P18 and earlier A segment.
- **Targeted approved B Playwright test PASS**: 10 P14–P18 images, six matched D-L/D-D/N-D image instances, sources+brightness equal across panels, aligned photo row coordinates, one shared Model M spanning learning/inference, key node computed font-size ≥16px, three decision/independent validation gates, three GT Label types. Screenshot evidence: [GitHub Actions artifact 12173267197](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39225261764/artifacts/12173267197), `visual_audit_output/approved_b/`.
- **Whole-route Playwright QA PASS**: cross-page deep links, 58-slide TOC continuity, Python add(1,1)=2 and add(2,1)=3, P16 image loading, B content and other interactive slides (run 39225261764).
- **Global layout workflow remains FAIL**, solely due to two inherited out-of-scope screens: course C10 `xor-gate` at 1366×768 fit=0.871 and course C33 `cnn-learning-paths` fit=0.848 (legacy C11/C34 before B). Both are already known and belong to C/F follow-up; no new A/B overlap, broken image or shrink issue reported.
- **Not yet verified:** independent Reviewer evaluation (RML-01/02/03, FLOW-01 closure still subject to reviewer), manual visual inspection of screenshot compositions, actual classroom readability and 120-minute rehearsal, GitHub Pages deployment and final 55-slide consistency. The rule-vs-learn contrast uses distinct source images for healthy/defect apples and a simulated new-input variant, not experimental evidence.
- **Next:** C P19–P27, CNN motivation/architecture/perceptron/nonlinearity and address inherited C10 XOR shrink as part of the approved storyboard. Keep this single work branch / draft PR; do not merge automatically.
