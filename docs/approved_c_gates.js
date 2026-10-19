/* Additional reproducible presets; the existing gate calculator remains authoritative. */
(() => {
  "use strict";
  const root = document.querySelector('[data-gate-lab="xor"]');
  if (!root) return;
  const nonlinear = root.querySelector('[data-gate-mode="nonlinear"]');
  const label = root.querySelector('[data-gate-composition]');
  const refresh = () => {
    if (label) label.textContent = nonlinear.getAttribute("aria-pressed") === "true" ? "g(t)=|t|" : "g(t)=t";
  };
  root.querySelectorAll("[data-gate-preset]").forEach(button => {
    button.addEventListener("click", () => {
      root.querySelector("[data-gate-reset]").click();
      if (button.dataset.gatePreset === "nonlinear") nonlinear.click();
      refresh();
    });
  });
  root.querySelectorAll("[data-gate-mode],[data-gate-reset]").forEach(button => button.addEventListener("click", refresh));
  refresh();
})();
