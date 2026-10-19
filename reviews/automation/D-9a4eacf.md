# D / P28–P36 independent review — 9a4eacf

Fixed SHA: `9a4eacf4510becad2d0346f2bdf348fdd5b41667`.
**Verdict: PASS — Critical0 / Major0 / Minor1 (nonblocking photo-caption precision).**

Independent Reviewer archived this SHA and individually opened all18 screenshots (1920×1080/1366×768): `/tmp/vision-ai-independent/D-9a4eacf4/`. No page exceptions, broken HTML images, visible label clipping or overlap. Minimum fit.920 on P29 retains readable calculation labels; no whole-slide tiny-font workaround.

| Plan / concept | Independent assessment |
|---|---|
| P28 kernel | PASS. Real85×85 photo ROI separated by dashed boundary from artificial5×5/3×3 values. Nine displayed products sum−6; trainable weights/cross-correlation/bias0 correctly disclosed. |
| P29 feature-map | PASS. Nine marked input starts correspond to nine displayed3×3 windows and outputs[[-6,12,16],[-6,8,15],[-4,2,7]]. First/right shift−6→12 correct; not resizedRGB or defectmask. |
| P30 sharing | PASS. Same32×32 single-channel/S1/P1 comparison:1048576/9216/9weights, bias excluded. Shared9weights distinguished from9216multiplications including padded zeros. |
| P31 channels | PASS. Two3×3×3filters read the sameRGB input in parallel, producing2maps; separate from P20 filters8/16. |
| P32 stride | PASS. Same original input/kernel;9 versus4starts and3×3 versus2×2outputs. S2 selects 1-based (1,1),(1,3),(3,1),(3,3), values[[-6,16],[-4,7]]. |
| P33 padding | PASS. New3×3 input and oneskernel distinguished from P28. Padding0→45; explicitaddedzeros→[[12,21,16],[27,45,33],[24,39,28]], no learned padding layer. |
| P34 pool | PASS. Four colored2×2windows max6/4/7/9 correctly point tooutputcells. Per-channel spatialhalving, channelsunchanged, no trainable weight, location information loss explained. |
| P35 actual-map | PASS with Minor. OriginalPNG and threeSqueezeNet stages visible. IDs/shapes/features[1]/[7]/[12] and channelwise 2–99 percentile normalization match reproducible source code/provenance. Differentfromtoy apple CNN. |
| P36 backbone | PASS. Spatial32×32×16backbone ends beforeclassificationGAP/Dense; alternativeBox/Maskheads use spatialfeatures, hypotheticaloutputs clearly disclosed. |

## Executed independent numerical/failure checks

Temporary independent parser read **24 named matrices actually drawn in inline SVG**, ordering row/column hooks; recomputed all 9 cross-correlations, each displayed window, stride 2 subsample, padded windows and max pool. **PASS**. No hidden fixture substituted for visible numbers.

Actual PNG deliberately aborted in system Chromium at both viewports. `data-load-state=error` shows truthful failure message and hides empty heatmap stage; no fabricated activation fallback. **PASS**.

P35 metadata checked against `scripts/render_cnn_feature_maps.py` and `assets/SOURCES.md`: same CS231n Lecture 5 slide 37 dog crop,224×224BilinearResize/ImageNetnormalization,SqueezeNet 1.1 ImageNet weights; shapes111×111×64/27×27×256/13×13×512; selected channels35,30,44,32 /2,62,24,153 /471,302,409,415. Channelwise percentile display is not cross-channel absolute comparison. The PNG is unchanged.

**Minor D-R1:** portrait display crop is separately resized by renderer(226×266), whereasactual model tensor is 224×224. Caption`전처리 후 모델 입력` ismoreprecisely`모델에 넣은 강아지 원본`/`입력 사진 표시`; actual 224 resize condition is already disclosed. This does not invalidate measured features.

**NOT VERIFIED:** fresh Torch/SqueezeNet inference (Torch/torchvision not installed), model weights re-download, real student responses, live 22/120 min rehearsal, auditorium projection andpublic deployment. Code/provenance verification is not claimed as fresh inference. Previous A/B/C not rerun; D scoped changes only.
