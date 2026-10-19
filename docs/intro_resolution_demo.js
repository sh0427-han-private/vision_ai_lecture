/* Same image, three real 16:9 raster output sizes; no external library. */
(() => {
  "use strict";
  const root = document.querySelector("[data-resolution-comparison]");
  if (!root) return;

  const source = new Image();
  source.decoding = "async";
  const status = root.querySelector("[data-resolution-status]");
  const region = { x: 0.58, y: 0.27, width: 0.065 };
  const sizes = [
    {p:90, w:160, h:90},
    {p:180, w:320, h:180},
    {p:360, w:640, h:360}
  ];

  source.onload = () => {
    // All outputs share an identical, centered 16:9 crop of the same source.
    const naturalW = source.naturalWidth, naturalH = source.naturalHeight;
    const cropRatio = 16 / 9;
    const cropW = Math.min(naturalW, naturalH * cropRatio);
    const cropH = cropW / cropRatio;
    const cropX = (naturalW - cropW) / 2;
    const cropY = (naturalH - cropH) / 2;

    for (const size of sizes) {
      const card = root.querySelector('[data-resolution-p="' + size.p + '"]');
      const full = card?.querySelector("[data-resolution-full]");
      const zoom = card?.querySelector("[data-resolution-zoom]");
      if (!full || !zoom) continue;
      full.width = size.w;
      full.height = size.h;
      const context = full.getContext("2d");
      context.imageSmoothingEnabled = true;
      context.imageSmoothingQuality = "high";
      context.drawImage(source, cropX, cropY, cropW, cropH,
        0, 0, size.w, size.h);

      // The same normalized patch is sampled from each raster. Using nearest
      // neighbor only when magnifying makes the actual pixel grid visible.
      const zc = zoom.getContext("2d");
      zc.imageSmoothingEnabled = false;
      const pixelW = region.width * size.w;
      const pixelH = pixelW * (zoom.height / zoom.width);
      const sx = Math.max(0, Math.min(size.w - pixelW, region.x * size.w));
      const sy = Math.max(0, Math.min(size.h - pixelH, region.y * size.h));
      zc.drawImage(full, sx, sy, pixelW, pixelH,
        0, 0, zoom.width, zoom.height);
      const locator = card.querySelector("[data-resolution-locator]");
      if (locator) {
        locator.style.left = (sx / size.w * 100) + "%";
        locator.style.top = (sy / size.h * 100) + "%";
        locator.style.width = (pixelW / size.w * 100) + "%";
        locator.style.height = (pixelH / size.h * 100) + "%";
      }
    }
    root.dataset.resolutionReady = "true";
    root.dataset.sourceWidth = String(naturalW);
    root.dataset.sourceHeight = String(naturalH);
    if (status) status.textContent = "동일한 사진 · 같은 확대 영역 · Pixel 차이 비교";
  };

  source.onerror = () => {
    root.dataset.resolutionReady = "error";
    if (status) status.textContent = "사진을 불러오지 못했습니다.";
  };
  source.src = root.dataset.resolutionSource;
})();
