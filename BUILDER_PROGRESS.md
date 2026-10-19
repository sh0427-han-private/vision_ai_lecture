# Vision AI Approved 55 — Builder Progress

**Date:** 2026-10-19  
**Branch:** `builder/approved-55-a-intro-20261019`  
**Baseline:** `main@ad3f0a8ce3ca8bce3a52d92c2198654dfcc4c298`, PR #113 already merged.  
**Plan:** `planning/vision-ai-120min-storyboard-draft-20261019/planning/SLIDE_STORYBOARD.md` (Approved).

| Group | Planned slides | Minutes | Status |
|---|---|---:|---|
| A | P01–P13 | 26 | Implemented; Chromium automatic QA passed; Reviewer pending |
| B | P14–P18 | 10 | Pending |
| C | P19–P27 | 23 | Pending |
| D | P28–P36 | 22 | Pending |
| E | P37–P40 | 9 | Pending |
| F | P41–P47 | 15 | Pending |
| G | P48–P52 | 10 | Pending |
| H | P53–P55 | 5 | Pending |

A changes: P01 image→analysis→annotated suspect output; P02 new AI⊃ML⊃DL / Computer Vision dual-axis Figure; P03 repeated checks→AI candidate→human verification; P04 number bridge preserved; P05 H×W and Grayscale 6×6 click preserved; P06 measured RGB click+keyboard preserved; P07 RGB channel stack and pixel count retained; P08 new simulated RGB frame strip and T×H×W×3; P09 original resolution interactive kept; P10 lighting-only controlled three-way comparison; P11 rotation/crop/occlusion/blur distinctions kept; P12 object vs defect labels separated; P13 normal/defect × brightness 2×2 with disclosure of different source images.

**Interim branch slide count:** Intro 13 + unchanged Course 46 = 59, legacy time blocks = 120 min (Intro legacy 24 min). Final approval target is 55 slides / 120 minutes with A time allocation 26 min. Reconcile inherited timing with B-H redesign, never mark total 55 complete now.

Changed paths: `docs/intro.html`, `docs/intro_approved_a.css`, `docs/vision_ai_course.html` (only outline cache bust), `docs/two_hour_manifest.json`, `docs/lecture_outline.js`, `scripts/verify_two_hour_course.py`, `scripts/verify_intro_pixel_interactive.py`, `assets/SOURCES.md`, `BUILDER_PROGRESS.md`.

## Automated QA evidence (2026-10-19)

- [Intro pixel interaction CI #39221664937](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39221664937): **SUCCESS**. Playwright Chromium checked pixel 12x8 source measurement, Grayscale 6x6 selection / brightness reset, RGB pixel measured values, HWC shape, resolution Canvas and page exceptions.
- [Figure overlap CI #39221664875](https://github.com/sh0427-han/vision_ai_lecture/actions/runs/39221664875): overall **FAIL** (pre-existing out-of-scope Course slides only). Rendered 118 views (59 slides x 2 viewports: 1920x1080, 1366x768). Group A P01-P13 reported **zero** overflow, overlap, broken images or forced shrink issues. Course C11 XOR has 1366x768 fit=0.871 and Course C34 fixed CNN features has fit=0.848; these are known baseline problems scheduled for groups C and F.
- SVG text audit: 78 assets, 1,199 text nodes, zero clipped labels, zero overlaps. Structural verification finished successfully before figure audit failure.
- Due to the two legacy Course layout issues, the figure CI did not reach the full navigation regression test. Independent subjective inspection of the A screenshots, Presenter readability / live rehearsal, Reviewer approval and GitHub Pages deployed verification remain pending.
- Previous PR #113 Reviewer Major RML-01/02/03 and FLOW-01 are tracked for B P16/P17. The Reviewer files were not edited.

**Status:** A source and automated-browser implementation ready for Reviewer; **NOT Reviewer-Verified**. B-H pending and 55-slide final build incomplete.
