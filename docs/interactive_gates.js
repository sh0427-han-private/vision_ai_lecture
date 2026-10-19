/* Interactive AND/XOR decision boundaries. Deterministic numeric educational demo. */
(() => {
  "use strict";
  const NS = "http://www.w3.org/2000/svg";
  const MIN = -0.28, MAX = 1.28, W = 430, H = 330;
  const LEFT = 52, TOP = 22, PW = 335, PH = 268;
  const inputs = [[0, 0], [0, 1], [1, 0], [1, 1]];
  const xPos = x => LEFT + (x - MIN) / (MAX - MIN) * PW;
  const yPos = y => TOP + (MAX - y) / (MAX - MIN) * PH;
  const num = v => (Math.abs(v) < 1e-8 ? 0 : v).toFixed(1);
  const evalLine = (p, x, y) => p[0] * x + p[1] * y + p[2];
  const rectangle = () => [[MIN, MIN], [MAX, MIN], [MAX, MAX], [MIN, MAX]];

  function halfPlane(vertices, coeff, keepPositive) {
    const sign = keepPositive ? 1 : -1;
    const inside = p => sign * evalLine(coeff, p[0], p[1]);
    const out = [];
    if (!vertices.length) return out;
    for (let i = 0; i < vertices.length; i++) {
      const a = vertices[i], b = vertices[(i + 1) % vertices.length];
      const fa = inside(a), fb = inside(b);
      const ia = fa >= -1e-9, ib = fb >= -1e-9;
      if (ia) out.push(a);
      if (ia !== ib && Math.abs(fa - fb) > 1e-12) {
        const t = fa / (fa - fb);
        out.push([a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])]);
      }
    }
    return out;
  }

  function lineSegment(coeff) {
    const [a, b, c] = coeff;
    if (Math.abs(a) + Math.abs(b) < 1e-9) return null;
    const options = [];
    if (Math.abs(b) > 1e-9) {
      for (const x of [MIN, MAX]) {
        const y = (-c - a * x) / b;
        if (y >= MIN - 1e-7 && y <= MAX + 1e-7) options.push([x, y]);
      }
    }
    if (Math.abs(a) > 1e-9) {
      for (const y of [MIN, MAX]) {
        const x = (-c - b * y) / a;
        if (x >= MIN - 1e-7 && x <= MAX + 1e-7) options.push([x, y]);
      }
    }
    const unique = options.filter((p, i) => options.findIndex(q => Math.hypot(p[0] - q[0], p[1] - q[1]) < 1e-7) === i);
    if (unique.length < 2) return null;
    let pair = [unique[0], unique[1]], best = 0;
    for (let i = 0; i < unique.length; i++) for (let j = i + 1; j < unique.length; j++) {
      const distance = Math.hypot(unique[i][0] - unique[j][0], unique[i][1] - unique[j][1]);
      if (distance > best) { best = distance; pair = [unique[i], unique[j]]; }
    }
    return pair;
  }

  function polygon(vertices, color) {
    if (vertices.length < 3) return "";
    return '<polygon points="' + vertices.map(p => xPos(p[0]).toFixed(2) + ',' + yPos(p[1]).toFixed(2)).join(' ') + '" fill="' + color + '" fill-opacity=".18"/>';
  }
  function line(coeff, color, dashed, label) {
    const segment = lineSegment(coeff);
    if (!segment) return "";
    const [a, b] = segment;
    return '<line x1="' + xPos(a[0]) + '" y1="' + yPos(a[1]) + '" x2="' + xPos(b[0]) + '" y2="' + yPos(b[1]) + '" stroke="' + color + '" stroke-width="3.5" ' +
      (dashed ? 'stroke-dasharray="8 5" ' : '') + 'aria-label="' + label + '"/>';
  }
  function step(v) { return v >= -1e-9 ? 1 : 0; }

  function setup(root) {
    const kind = root.dataset.gateLab, isXor = kind === "xor";
    const sliders = [...root.querySelectorAll('input[type="range"][data-param]')];
    const values = Object.fromEntries(sliders.map(s => [s.dataset.param, Number(s.value)]));
    const svg = root.querySelector('[data-gate-svg]');
    const summary = root.querySelector('[data-gate-summary]');
    const results = root.querySelector('[data-gate-results]');
    const equation = root.querySelector('[data-gate-equation]');
    let activation = isXor ? 'step' : 'step';

    const configs = isXor
      ? {a1:1,b1:-1,c1:-.5,a2:-1,b2:1,c2:-.5,u1:1,u2:1,d:-.5}
      : {w1:.5,w2:.5,b:-.7};

    function render() {
      sliders.forEach(slider => {
        const target = root.querySelector('[data-value="' + slider.dataset.param + '"]');
        if (target) target.textContent = num(values[slider.dataset.param]);
      });
      const normal = [values.w1, values.w2, values.b];
      const h1 = [values.a1, values.b1, values.c1];
      const h2 = [values.a2, values.b2, values.c2];
      const outputAffine = isXor
        ? [values.u1*h1[0] + values.u2*h2[0], values.u1*h1[1] + values.u2*h2[1], values.u1*h1[2] + values.u2*h2[2] + values.d]
        : normal;
      const score = (x, y) => {
        if (!isXor) return evalLine(normal, x, y);
        const v1 = evalLine(h1, x, y), v2 = evalLine(h2, x, y);
        const z1 = activation === 'step' ? step(v1) : v1;
        const z2 = activation === 'step' ? step(v2) : v2;
        return values.u1*z1 + values.u2*z2 + values.d;
      };
      const predictions = inputs.map(([x, y]) => step(score(x, y)));
      const targets = inputs.map(([x,y]) => isXor ? x ^ y : x & y);
      const correct = predictions.filter((p, i) => p === targets[i]).length;
      const points = inputs.map(([x, y], i) => {
        const predicted = predictions[i], pass = predicted === targets[i];
        return '<circle cx="' + xPos(x) + '" cy="' + yPos(y) + '" r="18" fill="' + (predicted ? '#16866c' : '#8a9daa') + '" stroke="' + (pass ? '#fff' : '#d34d47') +
          '" stroke-width="' + (pass ? '2.5' : '5') + '"/>' +
          '<text x="' + xPos(x) + '" y="' + (yPos(y)+6) + '" fill="#fff" font-size="17" font-weight="700" text-anchor="middle">' + predicted + '</text>';
      }).join('');

      let region = '';
      if (isXor && activation === 'step') {
        for (const a of [0,1]) for (const b of [0,1]) {
          if (step(values.u1 * a + values.u2 * b + values.d) === 1) {
            const first = halfPlane(rectangle(), h1, Boolean(a));
            const both = halfPlane(first, h2, Boolean(b));
            region += polygon(both, '#40a58d');
          }
        }
      } else {
        region = polygon(halfPlane(rectangle(), outputAffine, true), '#40a58d');
      }
      const boundaries = isXor && activation === 'step'
        ? line(h1, '#2276a1', true, '은닉 뉴런 1의 경계') + line(h2, '#c38144', true, '은닉 뉴런 2의 경계')
        : line(outputAffine, '#c38144', false, '단일 직선 경계');

      svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
      svg.innerHTML = '<rect x="' + LEFT + '" y="' + TOP + '" width="' + PW + '" height="' + PH + '" fill="#f4f8f8" stroke="#b2cacd"/>' +
        '<line x1="' + xPos(0) + '" y1="' + TOP + '" x2="' + xPos(0) + '" y2="' + (TOP+PH) + '" stroke="#9fb7c1" stroke-width="1.5"/>' +
        '<line x1="' + LEFT + '" y1="' + yPos(0) + '" x2="' + (LEFT+PW) + '" y2="' + yPos(0) + '" stroke="#9fb7c1" stroke-width="1.5"/>' +
        region + boundaries + points +
        '<text x="' + (LEFT+PW-5) + '" y="' + (TOP+PH+29) + '" font-size="20" text-anchor="end" fill="#365f70">x₁ →</text>' +
        '<text x="' + (LEFT-8) + '" y="' + (TOP+12) + '" font-size="20" text-anchor="end" fill="#365f70">x₂ ↑</text>';
      results.innerHTML = inputs.map(([x,y],i) => '<span class="gl-outcome ' + (predictions[i] === targets[i] ? 'gl-correct' : 'gl-incorrect') + '">' +
        '('+x+','+y+') <b>'+predictions[i]+'</b><small>정답 '+targets[i]+'</small></span>').join('');
      summary.textContent = '정답 ' + correct + ' / 4 · ' +
        (isXor ? (activation === 'linear' ? '비선형성이 없으면 두 층도 직선 하나와 같습니다.' : 'Step 은닉 뉴런 2개가 서로 다른 경계를 만듭니다.') :
          'Weight·Bias 변화에 따라 하나의 결정 경계가 이동합니다.');
      if (isXor) {
        equation.textContent = activation === 'linear'
          ? '활성화 없음: z = (' + num(outputAffine[0]) + ')x₁ + (' + num(outputAffine[1]) + ')x₂ + (' + num(outputAffine[2]) + ') → 직선 하나'
          : 'h₁=Step(w₁₁x₁+w₁₂x₂+b₁), h₂=Step(w₂₁x₁+w₂₂x₂+b₂), y=Step(v₁h₁+v₂h₂+b₃)';
      } else {
        equation.textContent = 'z = ' + num(values.w1) + 'x₁ + ' + num(values.w2) + 'x₂ + (' + num(values.b) + ')  ·  경계 z=0';
      }
    }

    // Drag gestures belong to the lab, not the deck's global swipe-to-next handler.
    root.addEventListener('touchend', event => event.stopPropagation());
    sliders.forEach(s => s.addEventListener('input', () => {
      values[s.dataset.param] = Number(s.value);
      render();
    }));
    root.querySelectorAll('[data-gate-mode]').forEach(button => button.addEventListener('click', () => {
      activation = button.dataset.gateMode;
      root.querySelectorAll('[data-gate-mode]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.gateMode === activation)));
      render();
    }));
    const reset = root.querySelector('[data-gate-reset]');
    if (reset) reset.addEventListener('click', () => {
      Object.assign(values, configs);
      sliders.forEach(s => { s.value = String(values[s.dataset.param]); });
      activation = 'step';
      root.querySelectorAll('[data-gate-mode]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.gateMode === activation)));
      render();
    });
    render();
    root.dataset.ready = 'true';
  }
  document.querySelectorAll('[data-gate-lab]').forEach(setup);
})();
