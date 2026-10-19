"""Apply approved P48–52 after F PASS. Root-owned, no automatic git operations."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
JS_SOURCE=r'''/* One fixed educational score array feeds every displayed count and distribution. */
(() => {
  "use strict";
  const root=document.querySelector("[data-project-evaluation]");
  if(!root)return;
  const scores=[
    // Approved 100-case cohort: 20 defects, 80 normal.
    ...[[.8,11],[.6,7],[.4,2]].flatMap(([score,count])=>
      Array.from({length:count},()=>({label:1,score}))),
    ...[[.8,2],[.6,2],[.4,26],[.2,50]].flatMap(([score,count])=>
      Array.from({length:count},()=>({label:0,score}))),
  ];
  const selector=root.querySelector("[data-project-threshold]");
  const histogram=root.querySelector("[data-score-histogram]");
  const bins=Array.from({length:10},()=>({positive:0,negative:0}));
  for(const row of scores)bins[Math.min(9,Math.floor(row.score*10))][row.label?"positive":"negative"]++;
  const svg=(tag,attributes,text)=>{
    const n=document.createElementNS("http://www.w3.org/2000/svg",tag);
    for(const [k,v]of Object.entries(attributes))n.setAttribute(k,v);
    if(text!==undefined)n.textContent=text;
    return n;
  };
  function renderHistogram(threshold){
    if(!histogram)return;
    histogram.replaceChildren();
    const base=192,x0=58,dx=49;
    const peak=Math.max(...bins.map(b=>b.positive+b.negative));
    const axisMax=Math.max(50,Math.ceil(peak/10)*10);
    const unit=160/axisMax; // 50-case peak fits above baseline at y=32.
    for(let y=0;y<=axisMax;y+=10){
      const py=base-y*unit;
      histogram.append(svg("path",{d:`M${x0} ${py}H548`,stroke:"#d7e3e8",fill:"none"}));
      histogram.append(svg("text",{x:45,y:py+6,"text-anchor":"end","font-size":19,fill:"#527282"},String(y)));
    }
    bins.forEach((bin,i)=>{
      const x=x0+i*dx+5,nh=bin.negative*unit,ph=bin.positive*unit;
      const group=svg("g",{"data-score-bin":i,"data-positive":bin.positive,"data-negative":bin.negative});
      group.append(svg("rect",{x,y:base-nh,width:39,height:nh,fill:"#9aaebc"}));
      group.append(svg("rect",{x,y:base-nh-ph,width:39,height:ph,fill:"#218c74"}));
      if(bin.positive+bin.negative)group.append(svg("text",{x:x+19.5,y:base-nh-ph-7,"text-anchor":"middle","font-size":19,fill:"#345c70"},String(bin.positive+bin.negative)));
      histogram.append(group);
    });
    for(let i=0;i<=10;i++)histogram.append(svg("text",{x:x0+i*dx,y:218,"text-anchor":"middle","font-size":19,fill:"#527282"},(i/10).toFixed(1)));
    const tx=x0+threshold*490;
    histogram.append(svg("path",{d:`M${tx} 18V192`,stroke:"#b97629","stroke-width":3,"stroke-dasharray":"7 4","data-threshold-line":threshold}));
    histogram.append(svg("text",{x:tx+8,y:25,"font-size":20,fill:"#a36722"},`기준 ${threshold.toFixed(2)}`));
    histogram.append(svg("text",{x:12,y:20,"font-size":19,fill:"#527282"},"건"));
    histogram.append(svg("text",{x:555,y:242,"text-anchor":"end","font-size":19,fill:"#527282"},"불량 Score →"));
  }
  function update(){
    const threshold=Number(selector.value),counts={tp:0,fn:0,fp:0,tn:0};
    for(const row of scores){const pred=row.score>=threshold;counts[row.label?(pred?"tp":"fn"):(pred?"fp":"tn")]++;}
    for(const [name,value]of Object.entries(counts))root.querySelector(`[data-project-${name}]`).textContent=String(value);
    for(const name of["fn","fp"]){root.querySelector(`[data-project-${name}-bar]`).value=counts[name];root.querySelector(`[data-project-${name}-label]`).textContent=`${counts[name]}건`;}
    const precision=100*counts.tp/(counts.tp+counts.fp),recall=100*counts.tp/(counts.tp+counts.fn);
    root.querySelector("[data-project-result]").textContent=`Precision ${precision.toFixed(1)}% · Recall ${recall.toFixed(1)}%`;
    root.dataset.threshold=String(threshold);root.dataset.ready="true";renderHistogram(threshold);
  }
  selector.addEventListener("change",update);
  root.querySelector("[data-project-reset]").addEventListener("click",()=>{selector.value="0.5";update();});
  update();
})();
'''

def replace(doc,concept,body):
    section=f'<section class="slide" data-concept="{concept}" data-level="basic"><div class="slide-inner two-hour g55">{body}</div></section>'
    doc,n=re.subn(rf'<section\b[^>]*data-concept="{concept}"[^>]*>.*?</section>',lambda _:section,doc,count=1,flags=re.S)
    assert n==1,concept
    return doc

def build():
    path=ROOT/'docs/vision_ai_course.html'; doc=path.read_text()
    old={m[1]:m[0] for m in re.finditer(r'<section\b[^>]*data-concept="([^"]+)"[^>]*>.*?</section>',doc,re.S)}
    control='''<div class="project-evaluation-control"><label for="project-threshold">判定 기준 · Threshold</label><select id="project-threshold" data-project-threshold><option value="0.3">0.30</option><option value="0.5" selected>0.50</option><option value="0.7">0.70</option></select><button type="button" data-project-reset>초기화 · 0.50</button><span>Score ≥ 기준 → 불량 알림</span></div>'''.replace('判定','판정')
    matrix=re.search(r'<table class="pf-confusion">.*?</table>',old.get('project-run',old['threshold']),re.S)[0]
    bars='''<div class="g55-bars"><label>놓친 불량 FN <output data-project-fn-label>2건</output><progress data-project-fn-bar max="100" value="2" aria-label="놓친 불량 FN"></progress></label><label>오알람 FP <output data-project-fp-label>4건</output><progress data-project-fp-bar max="100" value="4" aria-label="오알람 FP"></progress></label></div>'''
    body='''<h2 class="slide-title">Score Threshold · 판정 기준</h2><p class="slide-subtitle">같은 교육용 저장 점수 100건 · 실제 불량 20 / 정상 80. 기준만 바꾸어 놓침과 오알람을 비교합니다.</p><div class="project-evaluation" data-project-evaluation>'''+control+'''<div class="g55-eval"><figure class="g55-distribution"><h3>동일한 100개 Score의 분포</h3><svg data-score-histogram viewBox="0 0 600 250" role="img" aria-label="정상과 불량 점수 분포 및 현재 임계값"></svg><figcaption><span class="g55-pos">■ 실제 불량 20건</span>　<span class="g55-neg">■ 실제 정상 80건</span><br>각 구간: 왼쪽 값 이상, 오른쪽 값 미만</figcaption></figure><div class="g55-counts">'''+matrix+bars+'''</div></div><p class="project-result" aria-live="polite" data-project-result>Precision 81.8% · Recall 90.0%</p></div><p class="lesson-takeaway">기준을 낮추면 FN은 줄고 FP는 늘 수 있습니다. <strong>Validation에서 기준을 선택·고정한 뒤 독립 Test로 최종 평가</strong>합니다.</p><p class="g55-note">교육용 가상 Score이며 실제 모델을 실행한 결과는 아닙니다. Score는 실제 불량 확률을 보장하지 않습니다. 분포·표·오류 막대·지표는 같은 100건에서 계산합니다.</p>'''
    doc=replace(doc,'threshold',body)
    doc=re.sub(r'<section\b[^>]*data-concept="project-run"[^>]*>.*?</section>','',doc,flags=re.S)
    # Existing accurate matrix, 100 tiles and 22/20 metric dots are retained.
    doc=doc.replace('총 100건의 같은 평가 데이터를 다음 지표 계산까지 이어갑니다. 실제 불량 20건 중 18건을 찾고, 정상 80건 중 4건을 잘못 알렸습니다.','앞 실습의 기준을 0.50으로 고정한 참조 표입니다. 실제 불량 20건 중 18건을 찾고, 정상 80건 중 4건을 잘못 알렸습니다.')
    doc=doc.replace('직전 혼동행렬의 TP=18·FP=4·FN=2를 그대로 사용합니다.','Threshold 0.50 고정 참조 · P49의 TP=18·FP=4·FN=2를 그대로 사용합니다.')
    body='''<h2 class="slide-title">IoU · 박스 겹침 비율</h2><p class="slide-subtitle">위치도 맞아야 하는 검출에서는 정답(GT)과 예측 박스의 <strong>교집합 ÷ 합집합</strong>을 계산합니다.</p><div class="g55-iou"><figure><h3>사과의 같은 결함을 둘러싼 두 박스</h3><svg viewBox="450 130 260 240" role="img" aria-label="사과 반점의 정답 박스와 교육용 예측 박스"><image href="assets/vision_task_apple_reference.jpg" width="960" height="640"/><rect x="565" y="197" width="60" height="60" fill="#187c9a30" stroke="#187c9a" stroke-width="3"/><rect x="580" y="205" width="62" height="65" fill="#d58c3230" stroke="#c17b27" stroke-width="3" stroke-dasharray="7 4"/><rect x="580" y="205" width="45" height="52" fill="#487c9760"/></svg><figcaption><span class="g55-pos">실선: 정답 GT</span>　<span class="g55-pred">점선: 예측 예시</span><br>동일 생성 사진 위의 위치 도식 · 실측 예측 아님</figcaption></figure><figure><h3>별도의 정수 좌표 예제 · 면적 검산</h3><svg viewBox="0 0 420 340" role="img" aria-label="GT x1 y1 너비5 높이6, 예측 x1 y3 너비5 높이6, 겹침5×4, 합집합40"><rect x="85" y="25" width="150" height="240" fill="#e9f0f4"/><rect x="85" y="85" width="150" height="180" fill="#187c9a20" stroke="#187c9a" stroke-width="3" data-iou-box="gt" data-xyxy="1,1,6,7"/><rect x="85" y="25" width="150" height="180" fill="#d58c3220" stroke="#c17b27" stroke-width="3" stroke-dasharray="7 4" data-iou-box="prediction" data-xyxy="1,3,6,9"/><rect x="85" y="85" width="150" height="120" fill="#759fa777"/><g font-size="22" fill="#365d70"><text x="95" y="137">겹침 5×4</text><text x="125" y="168">=20</text><text x="49" y="272">1</text><text x="49" y="212">3</text><text x="49" y="92">7</text><text x="49" y="32">9</text><text x="80" y="296">1</text><text x="230" y="296">6</text><text x="270" y="296">x</text><text x="47" y="16">y</text><text x="255" y="102">GT (1,1)</text><text x="255" y="130">w=5, h=6</text><text x="255" y="185">예측 (1,3)</text><text x="255" y="213">w=5, h=6</text><text x="80" y="331">각 박스 면적 5×6=30</text></g></svg><figcaption><strong>IoU = 20 / (30+30−20) = 0.5</strong><br>왼쪽 사진의 픽셀 좌표와는 별도의 예제입니다.</figcaption></figure></div><p class="lesson-takeaway">완전 일치 1 · 겹치지 않음 0. IoU는 위치의 일치도입니다. 검출 전체 성능은 클래스·놓침·중복까지 함께 평가하는 mAP 등으로 봅니다.</p>'''
    doc=replace(doc,'iou',body)
    if 'approved_g.css' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="approved_g.css?v=approved-g-20261019-1">\n</head>')
    doc=re.sub(r'project_course.js\?v=[^" ]+', 'project_course.js?v=approved-g-20261019-1',doc)
    path.write_text(doc)
    (ROOT/'docs/project_course.js').write_text(JS_SOURCE)

if __name__=='__main__':build()
