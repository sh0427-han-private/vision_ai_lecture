# 55-slide automation progress

Integration branch: `automation/approved-55-20261019`. Main baseline ad3f0a8; approved storyboard 28fc97d. Existing Builder A/B 9ce8be57 reused. Main merge and Pages deployment are **PROHIBITED until final user approval**.

| Group | Slides | Minutes | Build SHA | Independent review | Status |
|---|---|---:|---|---|---|
| A | P01–13 |26|2280772|PASS final2280772|Verified technical A; 26+8 independent views, Critical0/Major0/Minor1 (P04 selected-cell linkage)|
| B | P14–18 |10|b803380|PASS independent re-review|RML01/02/03 and FLOW01 closed; 10+2 views, Critical0/Major0|
| C | P19–27 |23|fc8d463 (cache/test follow-up014c4c3)|PASS independent|9 slides/18+2 independent views, 2 viewport interaction/geometry runs, Critical0/Major0/Minor0|
| D | P28–36 |22|—|pending|Builder D implementing nine numerical CNN/actual-map/Head lessons|
| E | P37–40 |9|—|pending|Pending|
| F | P41–47 |15|—|pending|Pending|
| G | P48–52 |10|—|pending|Pending|
| H | P53–55 |5|—|pending|Pending|

Actual checks: Python3.12, Playwright/Pillow/lxml/system Chromium154 imports/version pass. Intro Pixel browser QA started. Existing main exact-text static assertion fails; no assertion bypass counted as pass. GitHub API and official web host access blocked (403), native Git fetch successful. See ENVIRONMENT.md. Existing screenshots/CI and old independent A review are historical evidence, not approval of current HEAD.

Next: D build and fixed-SHA independent review. Classroom rehearsal/learner feedback and public Pages rendering: NOT VERIFIED. These require actual external observations; technical Build PASS will be explicitly distinguished.

Historical Builder progress is available at commit9ce8be57:BUILDER_PROGRESS.md; this file is the consolidated active status record.

## Prior audit issues (technical closure; classroom evidence separate)

| Issue | Required groups | Status / evidence |
|---|---|---|
| AUD-01 | A/B/F/G/H | Open until independent55 merge/removal audit |
| AUD-02 | C | Open: Affine→ReLU→XOR presets |
| AUD-03 | C/D | Open: motivation→architecture→numeric Conv |
| AUD-04 | A/E | A relationship/video PASS; GroupSplit E pending |
| AUD-08 | B | Technical CLOSED at b803380, B-b803380.md; blind actual students NOT VERIFIED |
| AUD-09 | F | Open: Frozen backbone / supervised head / no-label clusters |
| AUD-10 | D/F | Open: actual SqueezeNet metadata and offline shared architecture |
| AUD-11 | A/C/F/G | A Pixel/RGB/resolution PASS; remaining interactions pending |
| AUD-13 | F | Open: stable P20 reference |
| AUD-14 | C/F | Open: remove remote architecture dependency |
| AUD-15 | F | Open: Optimizer arrows reach ConvA/B/Head |
| AUD-16 | C/D | Open: architecture→neuron→Conv bridge |
| AUD-17 | D | Open: real photo ROI vs educational numeric array |
| RML-01/02/03 | B | Technical CLOSED at b803380, independent10+2 views |
| FLOW-01 | B | CLOSED: prior vision-evolution merged into model-choice |
| AUD-05/06 | C | Minor pending Weight constraints / boundary equations |
| AUD-07 | B | Minor rule threshold is educational; B technical PASS |
| AUD-12 | E/G | Minor pending split and threshold/static reference labels |
| A-R1 | A | Open Minor: optional selected-cell/photo ROI correspondence; whole-image downsample already correct |

C parent integration: approved staged contract PASS at58 slides/120min (not final55), full58-slide route/TOC/gate/learning/threshold regression PASS after exact prose assertions were updated to the new visible content. Global historical static checker still awaits final55 migration; not reported as passed. Architecture full figure and maps share modelId apple-cnn-1426.

## Resumption after usage limit

2026-10-19: work resumed on automation/approved-55-20261019 at014c4c3. C independent PASS report had been written but not committed before the interruption; report is now preserved. D Builder has implementation GO. No main merge/deploy performed.
