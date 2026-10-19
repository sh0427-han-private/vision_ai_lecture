# B / P14–P18 independent review — 9deaa71

- Fixed SHA: `9deaa71fb4d4271d37f963a2e5ad4eed2fb5f419`.
- Independent Reviewer archived SHA, rendered system Chromium at1920×1080 and1366×768, and opened **all10/10 screenshots individually**. Evidence: `/tmp/vision-ai-independent/B-9deaa71f/`, `render.json`.
- **Verdict: NEEDS FIX — Critical0 / Major1 / Minor0.** Render/automatic B QA pass; P16 contains internal text overflow that automatic top-level geometry did not detect.

| Plan / concept | Technical and pedagogical assessment | Two-view Figure review |
|---|---|---|
| P14 / task | Same source/same defect ROI; Classification Class, Detection Box+Class, Segmentation Mask are correct and GT versus Prediction explicit. | PASS: matched three images; annotation clearly visible. |
| P15 / rules | Same Python add(a,b) returns2 and3 for(1,1)/(2,1); user-defined rule clearly separated from data learning. | PASS: consistent input/code/output arrows, legible. |
| P16 / rules-image | Rule exception versus supervised labels is accurate; same Model M visually shared between learning and new-input path; no invented model predictions. | **Major B-R1** at1920;1366 PASS. Healthy fruit clipping repaired; source sizes comparable and photos aligned. |
| P17 / model-choice | Manual rule → existing defect model → additional learning, every exit has independent evaluation; apple detection≠defect detection. Existing duplicate vision-evolution removed. | PASS: clear branches and validation gates. |
| P18 / task-model-data | Same input and defect; Class/Box/Mask annotation burden differentiated, qualitative not measured time. Box does not imply exact mask. | PASS: matching rows, visible GT. |

## Major B-R1 — P16 prediction label overflows and overlaps evaluation row — Builder

Independent1920×1080 measurement on the archived SHA:

- `.b55-prediction` y586.20..673.20, fixed height87px, width115.27px.
- Its18px strong `예측 (Prediction?)` wraps to3 lines, y573.42..642 (starts12.78px above box).
- Its16px span `실제 결과 미측정` wraps to2 lines, y646..686 (ends12.80px below box).
- `.b55-check` starts y681.20, so bottom text overlaps the independent-validation region by≈4.8px.
- The adjacent model's Korean title breaks `모델` across lines, making the already dense diagram harder to read.

1366×768 happens to use16px labels and does not overflow; checking only that viewport misses this bug. Fix by shortening primary labels (`예측`, `학습 모델`) and separating optional English/measurement qualifiers into concise secondary lines that fit the minimum node width. Keep meaningful labels≥16px and use row sizing/line spacing appropriately. Do not simply shrink the whole slide. Recheck P16 atboth sizes and allB concepts if shared scoped CSS changes.

## Existing Reviewer issue reconciliation

- RML-01: **CLOSED**. Explicit absolute-positioned contain and normalized healthy-fruit height now display complete fruit of similar scale. Left/right photo trios match and corresponding rows align in actual two-size screenshots.
- RML-02: **CLOSED**. Shared Model M spans rows with training input/learning arrows above and new photo/inference/model/prediction arrows below. An explicit new-input educational variant and independent evaluation remain visible.
- RML-03: Korean-first main labels and≥16px keys implemented, but **B-R1 must close** before visual readability is PASS.
- FLOW-01: **CLOSED in approved scope**. P17 merges prior duplicate approach choices and all three branches end in independent validation.

## Executed checks and limits

- All10 independent archived-SHA renders fit1.000, HTML image loads successful, no page exceptions.
- Independent archived-SHA `scripts/verify_approved_b_browser.py`: **PASS**, ten renders, six paired source/brightness checks and node font assertions. This did not inspect descendant text bounding boxes; B-R1 is real despite automatic PASS.
- Python example independently recalculated2/3; Box/Mask geometry inspected in HTML/SVG and actual screenshots.

**NOT VERIFIED:** real beginners'20-second answers/blind user testing, physical-room projection or actual10-minute teaching rehearsal. Public deployment prohibited until final user approval. Whole55 count/time/navigation regression belongs to final integration, not falsely marked complete here.
