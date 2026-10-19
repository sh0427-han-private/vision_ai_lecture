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

  // Intro-friendly parameterization: each layer has just one shared W and one Bias.
  // For two inputs, s=x1+x2. The AND layer reads z=W*s+b.
  // XOR Layer1 computes t=W1*s+b1; Layer2 reads either t (linear) or |t|
  // where |t|=ReLU(t)+ReLU(-t). The latter is a 2-ReLU hidden-layer example.
  function setup(root) {
    const kind = root.dataset.gateLab;
    const isXor = kind === "xor";
    const presets = isXor
      ? {w1:1,b1:-1,w2:-1,b2:.5}
      : {w:.5,b:-.7};
    const sliders = [...root.querySelectorAll('input[type="range"][data-param]')];
    const values = Object.fromEntries(sliders.map(slider => [slider.dataset.param, Number(slider.value)]));
    const svg = root.querySelector('[data-gate-svg]');
    const summary = root.querySelector('[data-gate-summary]');
    const results = root.querySelector('[data-gate-results]');
    const equation = root.querySelector('[data-gate-equation]');
    const stage = root.querySelector('[data-gate-stage]');
    let mode = "linear"; // Explain the impossibility FIRST, then introduce a nonlinearity.
    const target = ([x,y]) => isXor ? x ^ y : x & y;

    function render() {
      sliders.forEach(slider => {
        const label = root.querySelector('[data-value="' + slider.dataset.param + '"]');
        if (label) label.textContent = num(values[slider.dataset.param]);
      });
      const hidden = [values.w1, values.w1, values.b1];
      const finalLine = isXor
        ? [values.w1*values.w2, values.w1*values.w2, values.w2*values.b1+values.b2]
        : [values.w, values.w, values.b];
      const activation = t => isXor && mode === "nonlinear" ? Math.abs(t) : t;
      const score = (x,y) => isXor
        ? values.w2 * activation(values.w1*(x+y)+values.b1) + values.b2
        : values.w*(x+y)+values.b;
      const actual = inputs.map(([x,y]) => step(score(x,y)));
      const expected = inputs.map(target);
      const correct = actual.filter((value,i) => value===expected[i]).length;
      let region = "", lines = "";

      if (!isXor || mode === "linear") {
        region = polygon(halfPlane(rectangle(), finalLine, true), '#40a58d');
        lines = line(finalLine, '#c38144', false, '최종 Wx+b의 직선 경계');
      } else {
        // |t| gives the union of two clipped linear half-planes.
        const posCoeffs = [values.w1*values.w2,values.w1*values.w2,values.w2*values.b1+values.b2];
        const negCoeffs = [-values.w1*values.w2,-values.w1*values.w2,-values.w2*values.b1+values.b2];
        for(const [sign,coefs] of [[true,posCoeffs],[false,negCoeffs]]) {
          const domain = halfPlane(rectangle(), hidden, sign);
          region += polygon(halfPlane(domain,coefs,true),'#40a58d');
          const seg=lineSegment(coefs);
          if(seg){
            const mid=[(seg[0][0]+seg[1][0])/2,(seg[0][1]+seg[1][1])/2];
            if((sign ? 1 : -1)*evalLine(hidden,mid[0],mid[1])>=-1e-8)
              lines += line(coefs,'#c38144',false,'비선형 결정을 구성하는 경계');
          }
        }
      }
      const points=inputs.map(([x,y],i)=>{
        const equal=actual[i]===expected[i],label=expected[i];
        return '<circle cx="'+xPos(x)+'" cy="'+yPos(y)+'" r="19" fill="'+(label?'#16866c':'#8a9daa')+'" stroke="'+(equal?'#fff':'#d34d47')+'" stroke-width="'+(equal?'2.5':'5')+'"/>'+
          '<text x="'+xPos(x)+'" y="'+(yPos(y)+6)+'" fill="#fff" font-size="17" font-weight="700" text-anchor="middle">'+label+'</text>';
      }).join('');
      svg.setAttribute('viewBox','0 0 '+W+' '+H);
      svg.innerHTML='<rect x="'+LEFT+'" y="'+TOP+'" width="'+PW+'" height="'+PH+'" fill="#f4f8f8" stroke="#b2cacd"/>'+
        '<line x1="'+xPos(0)+'" y1="'+TOP+'" x2="'+xPos(0)+'" y2="'+(TOP+PH)+'" stroke="#9fb7c1" stroke-width="1.5"/>'+
        '<line x1="'+LEFT+'" y1="'+yPos(0)+'" x2="'+(LEFT+PW)+'" y2="'+yPos(0)+'" stroke="#9fb7c1" stroke-width="1.5"/>'+
        region+lines+points+
        '<text x="'+(LEFT+PW-5)+'" y="'+(TOP+PH+29)+'" font-size="20" text-anchor="end" fill="#365f70">x₁ →</text>'+
        '<text x="'+(LEFT-8)+'" y="'+(TOP+12)+'" font-size="20" text-anchor="end" fill="#365f70">x₂ ↑</text>';
      results.innerHTML=inputs.map(([x,y],i)=>
        '<span class="gl-outcome '+(actual[i]===expected[i]?'gl-correct':'gl-incorrect')+'">'+
        '<b class="gl-input">('+x+','+y+')</b><small>정답 '+expected[i]+'</small><small>AI 판정 <strong>'+actual[i]+'</strong></small></span>').join('');
      const description=isXor
        ? mode==='linear' ? '비선형이 없으므로 두 층을 지나도 최종 경계는 직선 하나입니다.'
          : '비선형 |t|를 넣으면 두 경계 사이가 선택되어 XOR 네 점을 구분할 수 있습니다.'
        : 'W·Bias를 바꿔도 퍼셉트론의 판정 경계는 직선 하나입니다.';
      summary.textContent='AI 판정 '+correct+' / 4개 일치 · '+description;
      if(isXor){
        const w=values.w1*values.w2, b=values.w2*values.b1+values.b2;
        equation.textContent=mode==='linear'
          ? '최종 z = ('+num(w)+')(x₁+x₂) + ('+num(b)+')  → Wx+b, 직선 하나'
          : 't = '+num(values.w1)+'(x₁+x₂) + ('+num(values.b1)+'); z = '+num(values.w2)+'|t| + ('+num(values.b2)+')';
        if(stage)stage.textContent=mode==='linear'
          ? 'Layer 1의 Wx+b → Layer 2의 Wx+b = 결국 하나의 직선'
          : 'Layer 사이에 |t| = ReLU(t)+ReLU(−t)를 적용 → 두 경계로 XOR 구분';
      }else{
        equation.textContent='z = '+num(values.w)+'(x₁+x₂) + ('+num(values.b)+') · 경계 z=0';
      }
    }

    root.addEventListener('touchend',event=>event.stopPropagation());
    sliders.forEach(slider=>slider.addEventListener('input',()=>{
      values[slider.dataset.param]=Number(slider.value);
      render();
    }));
    root.querySelectorAll('[data-gate-mode]').forEach(button=>button.addEventListener('click',()=>{
      mode=button.dataset.gateMode;
      root.querySelectorAll('[data-gate-mode]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.gateMode===mode)));
      render();
    }));
    const reset=root.querySelector('[data-gate-reset]');
    if(reset)reset.addEventListener('click',()=>{
      Object.assign(values,presets);
      sliders.forEach(s=>{s.value=String(values[s.dataset.param]);});
      mode='linear';
      root.querySelectorAll('[data-gate-mode]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.gateMode===mode)));
      render();
    });
    render();
    root.dataset.ready='true';
  }

  document.querySelectorAll('[data-gate-lab]').forEach(setup);
})();
