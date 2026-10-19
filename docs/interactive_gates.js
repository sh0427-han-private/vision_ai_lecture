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

  // Geometric interpretation: z = W*x1 + x2 + b => x2 = -W*x1 - b.
  // W changes the slope, while b changes the offset (the y-intercept is -b).
  // XOR has two simplified affine stages with one adjustable W/b per stage:
  //   t = W1*x1 + x2 + b1
  //   z = W2*g(t) + x1 + b2
  // Here the +x1 term in layer 2 is a fixed, non-trainable skip input.
  // Without nonlinearity: z = (W1*W2+1)*x1 + W2*x2 + W2*b1+b2,
  // a SINGLE line whose slope responds to either weight when W2!=0.
  // With |t| = ReLU(t)+ReLU(-t), a piecewise-linear two-edge XOR region forms.
  function setup(root) {
    const kind = root.dataset.gateLab, isXor = kind === "xor";
    const presets = isXor
      ? {w1:1,b1:-1,w2:-2,b2:.5}
      : {w:1,b:-1.2};
    const sliders = [...root.querySelectorAll('input[type="range"][data-param]')];
    const values = Object.fromEntries(sliders.map(slider => [slider.dataset.param, Number(slider.value)]));
    const svg = root.querySelector('[data-gate-svg]');
    const summary = root.querySelector('[data-gate-summary]');
    const results = root.querySelector('[data-gate-results]');
    const equation = root.querySelector('[data-gate-equation]');
    const stage = root.querySelector('[data-gate-stage]');
    let mode = 'linear';

    // Clip the zero-level line to a convex polygon, so the nonlinear branches
    // show the FINAL output decision boundary, not misleading whole lines.
    function clippedLine(coeff, convexPoly) {
      if (!convexPoly || convexPoly.length < 2) return '';
      const f = p => evalLine(coeff,p[0],p[1]);
      let points = [];
      for(let j=0;j<convexPoly.length;j++){
        const a=convexPoly[j], b=convexPoly[(j+1)%convexPoly.length];
        const fa=f(a),fb=f(b);
        if(Math.abs(fa)<1e-9) points.push(a);
        if(fa*fb< -1e-12) {
          const t=fa/(fa-fb);
          points.push([a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])]);
        }
      }
      points=points.filter((p,i)=>points.findIndex(q=>Math.hypot(p[0]-q[0],p[1]-q[1])<1e-7)===i);
      if(points.length<2) return '';
      let best=[points[0],points[1]],d=-1;
      for(let i=0;i<points.length;i++)for(let j=i+1;j<points.length;j++){
        const length=Math.hypot(points[i][0]-points[j][0],points[i][1]-points[j][1]);
        if(length>d){d=length;best=[points[i],points[j]];}
      }
      return '<line x1="'+xPos(best[0][0])+'" y1="'+yPos(best[0][1])+
        '" x2="'+xPos(best[1][0])+'" y2="'+yPos(best[1][1])+
        '" stroke="#c38144" stroke-width="3.5" aria-label="최종 비선형 판정 경계"/>';
    }

    function render() {
      sliders.forEach(slider => {
        const label=root.querySelector('[data-value="'+slider.dataset.param+'"]');
        if(label) label.textContent=num(values[slider.dataset.param]);
      });
      // The x2 coefficient is fixed at 1 in the single AND layer.
      const andLine=[values.w,1,values.b];
      const h1=[values.w1,1,values.b1];
      const linearLine=isXor
        ? [1+values.w1*values.w2, values.w2, values.w2*values.b1+values.b2]
        : andLine;
      const score=(x,y)=>{
        if(!isXor) return values.w*x+y+values.b;
        const t=values.w1*x+y+values.b1;
        return values.w2*(mode==='nonlinear'?Math.abs(t):t)+x+values.b2;
      };
      const targets=inputs.map(([x,y])=>isXor ? x^y : x&y);
      const guesses=inputs.map(([x,y])=>step(score(x,y)));
      const hits=guesses.filter((v,i)=>v===targets[i]).length;

      let region='', boundaries='';
      if(!isXor || mode==='linear'){
        region=polygon(halfPlane(rectangle(),linearLine,true),'#40a58d');
        boundaries=line(linearLine,'#c38144',false,'최종 Wx+b 직선 판정 경계');
      }else{
        const positive=[1+values.w1*values.w2,values.w2,values.w2*values.b1+values.b2];
        const negative=[1-values.w1*values.w2,-values.w2,-values.w2*values.b1+values.b2];
        for(const [keepPositive, coeff] of [[true,positive],[false,negative]]){
          const clipped=halfPlane(rectangle(),h1,keepPositive);
          region+=polygon(halfPlane(clipped,coeff,true),'#40a58d');
          boundaries+=clippedLine(coeff,clipped);
        }
      }
      const dots=inputs.map(([x,y],i)=>{
        const matches=targets[i]===guesses[i];
        return '<circle cx="'+xPos(x)+'" cy="'+yPos(y)+'" r="19" fill="'+(targets[i]?'#16866c':'#8a9daa')+
          '" stroke="'+(matches?'#fff':'#d34d47')+'" stroke-width="'+(matches?'2.5':'5')+'"/>'+
          '<text x="'+xPos(x)+'" y="'+(yPos(y)+6)+'" fill="#fff" font-size="17" font-weight="700" text-anchor="middle">'+targets[i]+'</text>';
      }).join('');
      svg.setAttribute('viewBox','0 0 '+W+' '+H);
      svg.innerHTML='<rect x="'+LEFT+'" y="'+TOP+'" width="'+PW+'" height="'+PH+'" fill="#f4f8f8" stroke="#b2cacd"/>'+
        '<line x1="'+xPos(0)+'" y1="'+TOP+'" x2="'+xPos(0)+'" y2="'+(TOP+PH)+'" stroke="#9fb7c1" stroke-width="1.5"/>'+
        '<line x1="'+LEFT+'" y1="'+yPos(0)+'" x2="'+(LEFT+PW)+'" y2="'+yPos(0)+'" stroke="#9fb7c1" stroke-width="1.5"/>'+
        region+boundaries+dots+
        '<text x="'+(LEFT+PW-5)+'" y="'+(TOP+PH+29)+'" font-size="20" text-anchor="end" fill="#365f70">x₁ →</text>'+
        '<text x="'+(LEFT-8)+'" y="'+(TOP+12)+'" font-size="20" text-anchor="end" fill="#365f70">x₂ ↑</text>';
      results.innerHTML=inputs.map(([x,y],i)=>
        '<span class="gl-outcome '+(targets[i]===guesses[i]?'gl-correct':'gl-incorrect')+'">'+
        '<b class="gl-input">('+x+','+y+')</b><small>정답 '+targets[i]+'</small>'+
        '<small>AI 판정 <strong>'+guesses[i]+'</strong></small></span>').join('');
      const explanation=isXor
        ? mode==='linear'
          ? '가중합만 연결하면 한 직선입니다.'
          : '|t|는 꺾인 경계를 표현합니다.'
        : 'W는 직선의 기울기(-W)를, b는 위치(-b)를 바꿉니다.';
      summary.textContent='AI 판정 '+hits+' / 4개 일치 · '+explanation;
      if(isXor){
        const w=1+values.w1*values.w2, v=values.w2, bias=values.w2*values.b1+values.b2;
        equation.textContent=mode==='linear'
          ? '최종 z = ('+num(w)+')x₁ + ('+num(v)+')x₂ + ('+num(bias)+') → 직선 하나'
          : 't='+num(values.w1)+'x₁+x₂+('+num(values.b1)+'),  z='+num(values.w2)+'|t|+x₁+('+num(values.b2)+')';
        if(stage) stage.textContent=mode==='linear'
          ? '선형 g(t)=t · 최종 경계는 직선 하나'
          : 'Layer 사이에 |t|=ReLU(t)+ReLU(−t) · 꺾인 경계 표현';
      }else{
        equation.textContent='z = '+num(values.w)+'x₁ + x₂ + ('+num(values.b)+') · 경계 x₂=−Wx₁−b';
      }
    }

    root.addEventListener('touchend',event=>event.stopPropagation());
    sliders.forEach(slider=>slider.addEventListener('input',()=>{
      values[slider.dataset.param]=Number(slider.value);render();
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
    render();root.dataset.ready='true';
  }

  document.querySelectorAll('[data-gate-lab]').forEach(setup);
})();
