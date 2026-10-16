/* Real grayscale matrix derived from the very same local apple image on
   Intro 3. The 12×8 raster is a legible illustration, NOT model inference. */
(() => {
  "use strict";
  const root = document.querySelector("[data-apple-matrix-bridge]");
  if (!root) return;
  const img = root.querySelector("[data-apple-matrix-source]");
  const grid = root.querySelector("[data-apple-matrix-grid]");
  const status = root.querySelector("[data-apple-matrix-status]");
  const width = 12, height = 8;

  const render = () => {
    if (!img.naturalWidth || !img.naturalHeight) return;
    try {
      const canvas = document.createElement("canvas");
      canvas.width = width;
      canvas.height = height;
      const ctx = canvas.getContext("2d", {willReadFrequently:true});
      ctx.imageSmoothingEnabled = true;
      ctx.imageSmoothingQuality = "high";
      ctx.drawImage(img, 0, 0, width, height);
      const data = ctx.getImageData(0, 0, width, height).data;
      const cells = document.createDocumentFragment();
      const values = [];
      for (let i = 0; i < width * height; i++) {
        const k = i * 4;
        // Explicit ITU-R BT.601 luma-style demonstration:
        // grayscale = round(0.299 R + 0.587 G + 0.114 B).
        const value = Math.round(
          0.299 * data[k] + 0.587 * data[k+1] + 0.114 * data[k+2]
        );
        const cell = document.createElement("span");
        cell.textContent = String(value);
        cells.appendChild(cell);
        values.push(value);
      }
      grid.replaceChildren(cells);
      root.dataset.appleMatrixReady = "true";
      root.dataset.appleMatrixSize = width + "x" + height;
      root.dataset.appleSourceSize = img.naturalWidth + "x" + img.naturalHeight;
      if (status) status.textContent =
        "같은 사진을 12 × 8 크기로 축소한 실제 Grayscale 값(0~255)입니다.";
    } catch (error) {
      root.dataset.appleMatrixReady = "error";
      if (status) status.textContent = "숫자 데이터를 표시할 수 없습니다.";
    }
  };

  if (img.complete && img.naturalWidth) render();
  else {
    img.addEventListener("load", render, {once:true});
    img.addEventListener("error", () => {
      root.dataset.appleMatrixReady = "error";
      if (status) status.textContent = "원본 이미지를 불러올 수 없습니다.";
    }, {once:true});
  }
})();
