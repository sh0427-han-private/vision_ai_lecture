/* One local architecture source, reused as the full figure and highlighted maps. */
(() => {
  "use strict";
  const script = document.currentScript;
  const asset = new URL("assets/lesson/cnn_apple_architecture.svg?v=approved-c-20261019-1", script.src);
  const highlights = {
    relu: ["relu-a", "relu-b"], conv: ["conv-a", "conv-b"],
    pool: ["pool"], head: ["head"], all: ["conv-a", "relu-a", "pool", "conv-b", "relu-b", "gap", "head"]
  };
  const roots = [...document.querySelectorAll("[data-cnn-map],[data-cnn-architecture]")];
  if (!roots.length) return;
  fetch(asset).then(response => {
    if (!response.ok) throw new Error("Local CNN architecture failed: " + response.status);
    return response.text();
  }).then(source => {
    const original = new DOMParser().parseFromString(source, "image/svg+xml").documentElement;
    roots.forEach((root, index) => {
      const svg = original.cloneNode(true), mini = root.hasAttribute("data-cnn-map");
      // Resolve the image relative to its SVG file before inserting it in HTML.
      svg.querySelectorAll("image[href]").forEach(image => image.setAttribute("href", new URL(image.getAttribute("href"), asset).href));
      // Inline copies must not share marker/title IDs.
      const prefix = "cnn-map-" + index + "-";
      svg.querySelectorAll("[id]").forEach(node => {
        const before = node.id, after = prefix + before;
        svg.innerHTML = svg.innerHTML.replaceAll("url(#" + before + ")", "url(#" + after + ")");
      });
      svg.querySelectorAll("[id]").forEach(node => { node.id = prefix + node.id; });
      svg.id = prefix + "svg";
      const style = svg.querySelector("style");
      style.textContent = style.textContent.replace(/([^{}]+)\{/g, (_, selectors) => selectors.split(",").map(selector => "#" + svg.id + " " + selector.trim().replace(/^\.c55-model-svg\s*/, "")).join(",") + "{");
      svg.setAttribute("aria-labelledby", prefix + "arch-title " + prefix + "arch-desc");
      svg.removeAttribute("width"); svg.removeAttribute("height");
      if (mini) {
        svg.setAttribute("viewBox", "0 0 1280 90");
        svg.querySelector(".arch-detail").remove();
        svg.querySelector('[data-arch-node="input"] text').textContent = "RGB";
        svg.querySelector('[data-arch-node="pool"] text').textContent = "Pool";
        (highlights[root.dataset.cnnMap] || []).forEach(key => svg.querySelector('[data-arch-node="' + key + '"]').classList.add("arch-hi"));
        svg.querySelector("desc").textContent = "사과 CNN의 같은 구조. 강조 위치: " + root.dataset.cnnMap;
      }
      svg.classList.add(mini ? "c55-mini-svg" : "c55-architecture-svg");
      root.replaceChildren(svg); root.dataset.modelId = "apple-cnn-1426"; root.dataset.ready = "true";
    });
    // The normal slide fit pass also observes this custom layout completion.
    window.dispatchEvent(new Event("resize"));
  }).catch(error => {
    roots.forEach(root => { root.textContent = "CNN 구조 그림을 불러오지 못했습니다. 페이지를 다시 열어주세요."; root.dataset.ready = "error"; });
    console.error(error);
  });
})();
