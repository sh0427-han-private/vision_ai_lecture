/* Educational saved scores, not a live model or measured project performance. */
(() => {
  "use strict";
  const root = document.querySelector("[data-project-evaluation]");
  if (!root) return;
  const scores = [
    ...Array.from({length: 18}, (_, i) => ({label: 1, score: (600 + 15*i)/1000})),
    {label: 1, score: 0.32}, {label: 1, score: 0.41},
    ...[0.56, 0.62, 0.73, 0.88].map(score => ({label: 0, score})),
    ...Array.from({length: 76}, (_, i) => ({label: 0, score: (100 + 4*i)/1000})),
  ];
  const selector = root.querySelector("[data-project-threshold]");
  function update() {
    const threshold = Number(selector.value);
    const counts = {tp: 0, fn: 0, fp: 0, tn: 0};
    for (const row of scores) {
      const predicted = row.score >= threshold;
      counts[row.label ? (predicted ? "tp" : "fn") : (predicted ? "fp" : "tn")]++;
    }
    for (const [name, count] of Object.entries(counts)) {
      root.querySelector(`[data-project-${name}]`).textContent = String(count);
    }
    for (const name of ["fn", "fp"]) {
      root.querySelector(`[data-project-${name}-bar]`).value = counts[name];
      root.querySelector(`[data-project-${name}-label]`).textContent = `${counts[name]}건`;
    }
    const precision = 100 * counts.tp / (counts.tp + counts.fp);
    const recall = 100 * counts.tp / (counts.tp + counts.fn);
    root.querySelector("[data-project-result]").textContent =
      `Precision ${precision.toFixed(1)}% · Recall ${recall.toFixed(1)}%`;
    root.dataset.ready = "true";
  }
  selector.addEventListener("change", update);
  update();
})();
