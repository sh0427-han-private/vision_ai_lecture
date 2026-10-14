/* Real, deterministic teaching calculations; no neural network inference is claimed. */
(() => {
  "use strict";
  const filterRoot = document.querySelector("[data-filter-lesson]");
  if (filterRoot) initFilter(filterRoot);
  const trainRoot = document.querySelector("[data-training-lesson]");
  if (trainRoot) initTraining(trainRoot);

  function initFilter(root) {
    const width = 300, height = 200;
    const sourceCanvas = root.querySelector('[data-role="source"]');
    const outputCanvas = root.querySelector('[data-role="output"]');
    const sourceCtx = sourceCanvas.getContext("2d", {willReadFrequently:true});
    const outputCtx = outputCanvas.getContext("2d");
    const kernelGrid = root.querySelector("[data-kernel]");
    const sigmaControl = root.querySelector("[data-sigma]");
    const sigmaText = root.querySelector("[data-sigma-text]");
    const sigmaBox = root.querySelector("[data-sigma-box]");
    const noiseControl = root.querySelector("[data-noise]");
    const math = root.querySelector("[data-math]");
    const kernelLabel = root.querySelector("[data-kernel-label]");
    const selectedLabel = root.querySelector("[data-selection]");
    const outputLabel = root.querySelector("[data-output-label]");
    const footnote = root.querySelector("[data-processing-note]");
    const graySource = new Uint8Array(width * height);
    const gray = new Uint8Array(width * height);
    let selectedX = 157, selectedY = 96, mode = "gaussian", loaded = false;
    let weights = [], side = 5;
    const sobelX = [-1,0,1,-2,0,2,-1,0,1];
    const sobelY = [-1,-2,-1,0,0,0,1,2,1];
    const clamp = (n, a, b) => Math.max(a, Math.min(b, n));
    const at = (x,y) => gray[clamp(y,0,height-1)*width+clamp(x,0,width-1)];
    const round3 = n => (Math.abs(n) < .0005 ? 0 : n).toFixed(3);
    function getKernel() {
      if (mode === "original") {side = 3; weights = [0,0,0,0,1,0,0,0,0];}
      if (mode === "mean") {side = 5; weights = Array(25).fill(1/25);}
      if (mode === "gaussian") {
        side = 5;
        const sigma = Number(sigmaControl.value);
        weights = [];
        let total = 0;
        for (let dy = -2; dy <= 2; dy += 1) for (let dx = -2; dx <= 2; dx += 1) {
          const w = Math.exp(-(dx*dx+dy*dy)/(2*sigma*sigma));
          weights.push(w); total += w;
        }
        weights = weights.map(value => value/total);
      }
      if (mode === "sobel") {side = 3; weights = [...sobelX];}
      if (mode === "median") {side = 5; weights = [];}
    }
    function valueAt(x,y) {
      if (mode === "median") {
        const neighbors = [];
        for(let dy=-2;dy<=2;dy+=1)for(let dx=-2;dx<=2;dx+=1)neighbors.push(at(x+dx,y+dy));
        neighbors.sort((a,b)=>a-b);
        return neighbors[12];
      }
      let result=0, second=0;
      for(let k=0;k<side*side;k+=1){
        const dx=k%side-Math.floor(side/2);
        const dy=Math.floor(k/side)-Math.floor(side/2);
        const input=at(x+dx,y+dy);
        result += input * weights[k];
        if(mode==="sobel")second+=input*sobelY[k];
      }
      return mode==="sobel"?Math.hypot(result,second):result;
    }
    function rebuildSource() {
      const useNoise = noiseControl.checked;
      for(let y=0;y<height;y+=1)for(let x=0;x<width;x+=1) {
        const index=y*width+x;
        // Fixed coordinate hash: toggling noise always reproduces the same noisy input.
        const hash=((x*374761393)^(y*668265263)^1376312589)>>>0;
        const chance=hash%1000;
        gray[index]=useNoise&&chance<35 ? (chance<18?0:255):graySource[index];
      }
    }
    function paintSource() {
      const image=sourceCtx.createImageData(width,height);
      for(let i=0;i<gray.length;i+=1){
        const j=i*4, v=gray[i];
        image.data[j]=v;image.data[j+1]=v;image.data[j+2]=v;image.data[j+3]=255;
      }
      sourceCtx.putImageData(image,0,0);
      sourceCtx.strokeStyle="#00b99a";sourceCtx.lineWidth=2.4;
      sourceCtx.beginPath();sourceCtx.arc(selectedX,selectedY,7,0,Math.PI*2);sourceCtx.stroke();
      sourceCtx.beginPath();
      sourceCtx.moveTo(selectedX-12,selectedY);sourceCtx.lineTo(selectedX-8,selectedY);
      sourceCtx.moveTo(selectedX+8,selectedY);sourceCtx.lineTo(selectedX+12,selectedY);
      sourceCtx.stroke();
    }
    function drawKernel(){
      kernelGrid.replaceChildren();
      kernelGrid.style.setProperty("--kernel-size",String(side));
      if(mode==="median"){
        kernelLabel.textContent="중앙값 필터는 가중합이 아닙니다";
        const label=document.createElement("div");
        label.textContent="5×5 주변값을 정렬하고 가운데 값을 선택";
        label.style.cssText="grid-column:1/-1;padding:26px 8px;text-align:center;color:#315e6a;font-weight:700;background:#f3f8f7";
        kernelGrid.append(label);
        return;
      }
      kernelLabel.textContent=mode==="sobel"?"Sobel Gx 커널 (Gy도 함께 계산)":"읽기 전용 Kernel 가중치";
      const max=Math.max(...weights.map(v=>Math.abs(v)),.001);
      weights.forEach((value,index)=>{
        const el=document.createElement("span");
        const shade=.08+Math.abs(value)/max*.28;
        el.style.background=value<0?"rgba(210,146,74,"+shade+")":"rgba(34,152,139,"+shade+")";
        el.textContent=(mode==="sobel"?value: value.toFixed(2));
        el.title=(Math.floor(index/side)+1)+"행 "+(index%side+1)+"열, weight="+value.toFixed(5);
        kernelGrid.append(el);
      });
    }
    function render() {
      if(!loaded)return;
      rebuildSource();getKernel();drawKernel();
      paintSource();
      const img=outputCtx.createImageData(width,height);
      for(let y=0;y<height;y+=1)for(let x=0;x<width;x+=1){
        const v=clamp(Math.round(valueAt(x,y)),0,255);
        const i=(y*width+x)*4;
        img.data[i]=v;img.data[i+1]=v;img.data[i+2]=v;img.data[i+3]=255;
      }
      outputCtx.putImageData(img,0,0);
      const raw=valueAt(selectedX,selectedY);
      const processed=clamp(Math.round(raw),0,255);
      selectedLabel.textContent="선택 ("+selectedX+", "+selectedY+") · 입력 "+at(selectedX,selectedY);
      outputLabel.textContent=String(processed);
      sigmaText.textContent=Number(sigmaControl.value).toFixed(1);
      const sum=weights.reduce((a,b)=>a+b,0);
      if(mode==="median") math.textContent="주변 25개 픽셀의 중앙값 = "+processed;
      else if(mode==="sobel")math.textContent="Gx·Gy 각각 합산 → √(Gx²+Gy²) = "+raw.toFixed(1)+" → "+processed;
      else math.textContent="이웃값×가중치의 합 = "+round3(raw)+" → 8-bit "+processed+
        " (가중치 합 "+sum.toFixed(3)+")";
      footnote.textContent="동일 입력 · Stride 1 · 경계 Pixel 복제 · 8-bit 결과 제한" +
        (mode==="sobel"?" · Sobel 크기":" · Kernel 뒤집지 않는 Cross-correlation");
      root.querySelectorAll("[data-filter-mode]").forEach(button=>{
        button.setAttribute("aria-pressed", String(button.dataset.filterMode===mode));
      });
      sigmaBox.hidden=mode!=="gaussian";
    }
    root.querySelectorAll("[data-filter-mode]").forEach(button=>{
      button.addEventListener("click",()=>{mode=button.dataset.filterMode;render();});
    });
    noiseControl.addEventListener("change",render);
    sigmaControl.addEventListener("input",render);
    function choosePixel(x,y){selectedX=clamp(x,0,width-1);selectedY=clamp(y,0,height-1);render();}
    sourceCanvas.addEventListener("click",event=>{
      const rect=sourceCanvas.getBoundingClientRect();
      choosePixel(Math.floor((event.clientX-rect.left)*width/rect.width),
        Math.floor((event.clientY-rect.top)*height/rect.height));
    });
    sourceCanvas.addEventListener("keydown",event=>{
      const moves={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]};
      if(!moves[event.key])return;
      event.preventDefault();
      choosePixel(selectedX+moves[event.key][0],selectedY+moves[event.key][1]);
    });
    const apple=new Image();
    apple.onload=()=>{
      sourceCtx.drawImage(apple,0,0,width,height);
      const pixels=sourceCtx.getImageData(0,0,width,height).data;
      for(let i=0;i<graySource.length;i+=1){
        const j=i*4;
        graySource[i]=Math.round(.299*pixels[j]+.587*pixels[j+1]+.114*pixels[j+2]);
      }
      loaded=true;render();
    };
    apple.onerror=()=>{
      // Preserve a visibly marked, deterministic fallback; never claim it is the real photograph.
      for(let y=0;y<height;y+=1)for(let x=0;x<width;x+=1){
        const fruit=((x-158)/74)**2+((y-100)/72)**2<1;
        graySource[y*width+x]=fruit?132+Math.round(24*Math.sin(x/11)):228;
      }
      loaded=true;render();
      footnote.textContent="원본 사진을 찾지 못해 합성 도형에 동일한 필터 계산을 적용했습니다.";
    };
    apple.src="assets/vision_task_apple_reference.jpg";
  }

  function initTraining(root) {
    const x=2, target=4, rate=.1;
    let weight=.5, iteration=0, timer=null;
    const predBar=root.querySelector("[data-pred-bar]");
    const predict=root.querySelector("[data-prediction]");
    const weightLabel=root.querySelector("[data-weight]");
    const lossLabel=root.querySelector("[data-loss]");
    const iterLabel=root.querySelector("[data-iteration]");
    const equation=root.querySelector("[data-training-equation]");
    const status=root.querySelector("[data-training-status]");
    const runButton=root.querySelector("[data-train-run]");
    const stepButton=root.querySelector("[data-train-step]");
    const resetButton=root.querySelector("[data-train-reset]");
    const f=n=>n.toFixed(3).replace(/0+$/,"").replace(/\.$/,"");
    const loss=()=> (weight*x-target)**2;
    const active=()=>root.closest(".slide")?.classList.contains("active");
    function render(){
      const predicted=weight*x;
      weightLabel.textContent=f(weight);
      predict.textContent=f(predicted);
      lossLabel.textContent=f(loss());
      iterLabel.textContent=String(iteration);
      equation.textContent="ŷ = "+f(weight)+" × 2 = "+f(predicted);
      predBar.style.setProperty("--bar-height",(predicted/4*100).toFixed(1)+"%");
      status.textContent=iteration===0?
        "처음에는 예측이 정답 4보다 작고 오차가 큽니다.":
        "예측이 정답 4로 가까워집니다. w는 사람이 아닌 학습 알고리즘이 갱신했습니다.";
      stepButton.disabled=iteration>=8;
      if(iteration>=8)stop();
    }
    function step(){
      if(iteration>=8) return;
      const gradient=2*(weight*x-target)*x;
      weight=weight-rate*gradient;
      iteration+=1;render();
    }
    function stop(){
      if(timer!==null)clearInterval(timer);
      timer=null;runButton.textContent="자동 학습";
    }
    stepButton.addEventListener("click",()=>{stop();step();});
    runButton.addEventListener("click",()=>{
      if(timer!==null){stop();return;}
      if(iteration>=8){iteration=0;weight=.5;render();}
      runButton.textContent="일시정지";
      timer=setInterval(()=>{
        if(!active()){stop();return;}
        step();
      },900);
    });
    resetButton.addEventListener("click",()=>{stop();weight=.5;iteration=0;render();});
    document.addEventListener("visibilitychange",()=>{if(document.hidden)stop();});
    render();
  }
})();