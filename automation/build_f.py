#!/usr/bin/env python3
"""Apply approved F/P41–P47; python automation/build_f.py [--root REPO]."""
import argparse
import re
from pathlib import Path
from html import escape
from zlib import crc32

PHOTO='assets/vision_task_apple_reference.jpg'
GREEN='#18856c'; BLUE='#397c9b'; RED='#b2684b'

def t(x,y,s,size=25,color='#31596b',anchor='middle',weight=650):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>'

def path(d,color=BLUE,marker='forward',attrs=''):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#{marker})" {attrs}/>'

def box(x,y,w,h,label,sub='',color=BLUE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#f3f7f8" stroke="{color}" stroke-width="2"/>'+t(x+w/2,y+34,label,25,color)+ (t(x+w/2,y+67,sub,22,color) if sub else '')

def svg(body,label,h=440,w=1280):
    defs=''.join(f'<marker id="{name}" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6Z" fill="{color}"/></marker>' for name,color in [('forward',BLUE),('update',GREEN),('backward',RED)])
    uid='f'+str(crc32(label.encode()))+'-'
    defs=re.sub(r'id="([^"]+)"',lambda m:'id="'+uid+m[1]+'"',defs)
    body=re.sub(r'url\(#([^)]*)\)',lambda m:'url(#'+uid+m[1]+')',body)
    return f'<svg class="f55-diagram" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg"><defs>{defs}</defs><g font-family="Noto Sans KR,Malgun Gothic,sans-serif">{body}</g></svg>'

def photo(x,y,w=130,h=130,dark=False):
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="440 100 300 300" overflow="hidden"><g'+(' style="filter:brightness(.45)"' if dark else '')+f'><image href="{PHOTO}" width="960" height="640"/><rect x="565" y="197" width="53" height="57" fill="none" stroke="#187c9a" stroke-width="4"/></g></svg>'

def model(root,prefix):
    """Adapt only the P20 nodes/forward paths/shapes; preserve exact model identity."""
    source=(root/'docs/assets/lesson/cnn_apple_architecture.svg').read_text()
    nodes=''.join(re.findall(r'<g class="arch-node".*?</g>',source,re.S))
    conn=re.search(r'<g class="arch-connectors">.*?</g>',source,re.S).group()
    conn=conn.replace('class="arch-path"',f'fill="none" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#forward)"')
    shapes=''.join(re.findall(r'<text [^>]*class="arch-shape".*?</text>',source))
    nodes=nodes.replace('<rect ', '<rect fill="#eef5f8" stroke="#7196a5" stroke-width="2" ').replace('<text ','<text text-anchor="middle" fill="#294f60" font-size="23" font-weight="750" ')
    shapes=shapes.replace('class="arch-shape"','text-anchor="middle" fill="#31596b" font-size="22"')
    return f'<g data-model-id="apple-cnn-1426" data-ready="true" data-architecture-source="cnn_apple_architecture.svg" id="{prefix}">{nodes}{conn}{shapes}</g>'

def loss():
    b=''
    items=[('입력','x = 2'),('예측','ŷ = 0.5×2 = 1'),('정답','y = 4'),('Loss','(1−4)² = 9'),('Gradient','dL/dw = −12'),('Optimizer','η = 0.1')]
    for i,(name,sub) in enumerate(items):
        x=10+i*213;b+=box(x,70,195,92,name,sub,GREEN if i==5 else BLUE)
        if i<5:b+=path(f'M{x+195} 116H{x+213}')
    b+=box(12,240,290,91,'모델 Weight','w = 0.5 → 1.7',GREEN)
    b+=path('M1172 162V286H302',GREEN,'update')
    b+=t(766,266,'w′ = 0.5 − 0.1 × (−12) = 1.7',30,GREEN)
    b+=t(650,360,'Gradient: 2(wx−y)x = 2(1−4)×2 = −12',27,RED)
    b+=t(650,409,'다음 예측 3.4 → Loss (3.4−4)² = 0.36',29,GREEN)
    return svg(b,'입력 예측 정답 Loss Gradient Optimizer 여섯 단계와 모델 Weight로 돌아오는 갱신 화살표',440)

def training(root):
    # Feedback above the model keeps the exact P20 tensor/parameter labels clear.
    b=box(1100,10,178,84,'Loss','예측 + Label',RED)
    b+=box(730,10,275,84,'② Backpropagation','각 Weight의 Gradient',RED)+path('M1100 52H1005',RED,'backward')
    b+=box(385,10,250,84,'③ Optimizer','Gradient로 W,b 갱신',GREEN)+path('M730 52H635',RED,'backward')
    b+=t(130,43,'정답 Label',25,BLUE)+t(130,76,'고정된 비교 기준',22,BLUE)
    b+=path('M230 45V2H1189V10')
    b+='<g transform="translate(0 200)">'+model(root,'f-training-model')+'</g>'
    b+=path('M1278 245V160H1189V94')
    for target,x,lane,start in [('conv-a',206,165,420),('conv-b',628,140,510),('head',1039,115,600)]:
        b+=path(f'M{start} 94V{lane}H{x}V216',GREEN,'update',f'data-update-target="{target}"')
    for x,label in [(206,'W,b 224개'),(628,'W,b 1,168개'),(1039,'W,b 34개')]:b+=t(x,352,label,23,GREEN)
    b+=photo(2,330,108,108)
    b+=t(640,401,'ReLU · Pool · GAP: 학습 Weight 0개 · Gradient는 연산을 통과',25,RED)
    b+=t(640,450,'① Forward: 왼쪽 → 오른쪽 · Parameter 합계 1,426개 · 실측 학습 결과 아님',24,BLUE)
    return svg(b,'P20 동일 CNN Forward와 Loss 역전파 Optimizer, ConvA ConvB DenseHead에만 닿는 갱신 화살표',470)

def infer():
    b=t(310,30,'Training · 배울 때',30,GREEN)+t(970,30,'Inference · 사용할 때',30,BLUE)
    b+='<path d="M640 20V410" stroke="#c7d8df" stroke-width="2"/>'
    b+=photo(20,72,120,120)+t(80,223,'사진 / Frame',22)+box(205,85,205,90,'Model','Weight 갱신',GREEN)+path('M140 130H205')
    b+=box(460,85,155,90,'Prediction','Class Score')+path('M410 130H460')
    b+=box(360,280,255,90,'Label + Loss','Backward → Optimizer',GREEN)+path('M540 175V280')
    b+=path('M360 325H307V175',GREEN,'update')+t(177,357,'정답으로 비교하며 반복',23,GREEN)
    b+=photo(665,72,120,120)+t(725,223,'새 사진 / Frame',22)+box(850,85,205,90,'Model','Weight 고정',BLUE)+path('M785 130H850')
    b+=box(1100,85,175,90,'Prediction','Class Score')+path('M1055 130H1100')
    b+=t(965,310,'정답 Label 없이 Forward',29,BLUE)+t(965,351,'학습된 Weight를 그대로 사용',25,BLUE)
    return svg(b,'학습은 Label Loss Optimizer 반복, 추론은 새 입력 고정 Weight Class Score 단방향',405)

def transfer(root):
    b=''
    for i,mode in enumerate(['head-only','fine-tune']):
        y=i*255
        title='① Head-only · Conv A/B 고정 🔒 · 새 Dense Head 학습' if i==0 else '② Fine-tuning · Conv A 고정 🔒 · Conv B + Head 추가 학습'
        b+=f'<g data-transfer-mode="{mode}" transform="translate(0 {y})">'+t(8,25,title,27,GREEN,'start')
        b+='<g transform="translate(0 48)">'+model(root,'f-transfer-'+mode)+'</g>'
        b+=t(480,202,'Frozen Backbone · Weight 고정' if i==0 else 'Conv B 잠금 해제 · 일부 Backbone 학습',24,BLUE)
        b+=box(970,177,155,57,'Optimizer','',GREEN)
        targets=[('head',1039)] if i==0 else [('conv-b',628),('head',1039)]
        for n,(target,x) in enumerate(targets):
            # Arrows originate at visible optimizer; only trainable node bottom y122.
            d=f'M{1000+n*70} 177V{135+n*2}H{x}V122'
            b+=path(d,GREEN,'update',f'data-update-target="{target}"')
        b+='</g>'
    return svg(b,'P20 동일 로컬 CNN 두 패널; Head-only는 Head만 갱신, Fine-tuning은 ConvB와 Head 갱신',490)

def paths():
    b='<g class="su-shared">'+photo(80,20,100,100)+photo(130,30,100,100)+photo(180,40,100,100)+t(180,169,'여러 사과 사진',23)+path('M280 80H365')+box(365,35,400,90,'하나의 Frozen CNN Backbone','두 경로 모두 Weight 고정 🔒')+path('M765 80H850')+box(850,35,275,90,'같은 Feature Vector','16개 수치')+'</g>'
    b+=path('M990 125V160H310V210')+path('M990 160H975V210')
    b+='<g class="su-path--sup">'+t(310,247,'지도 · 정답 Label 있음',29,GREEN)+box(55,275,510,91,'Classifier Head + Label 기반 Loss','Head Weight 학습 → 정상 / 불량',GREEN)+'</g>'
    b+='<g class="su-path--un">'+t(975,247,'비지도 · Label 사용 안 함',29,BLUE)+box(720,275,510,91,'K-means · 특징의 유사성으로 군집화','군집 중심 계산 → 이름 없는 Group A / B',BLUE)+'</g>'
    # Neutral arbitrary cluster colors avoid mapping to normal/defect class colors.
    for x,y in [(760,391),(783,406),(798,389),(1020,396),(1040,412),(1060,394)]:b+=f'<circle cx="{x}" cy="{y}" r="6" fill="'+('#8773a1' if x<900 else '#a48762')+'"/>'
    b+=t(860,405,'A',23,'#8773a1')+t(1130,405,'B',23,'#a48762')
    b+=t(310,412,'목표: 알려진 Class를 예측',24,GREEN)
    return svg(b,'하나의 고정 Backbone과 동일 Feature16에서 Label 기반 분류 Head 학습과 Label 없는 Kmeans 군집화로 분기',435)

def overfit():
    b=t(60,25,'Loss',26,BLUE,'start')+path('M90 345V47')+path('M90 345H775')+t(755,390,'Epoch',26,BLUE)
    b+='<path d="M100 74 C180 180 255 227 350 250 S590 294 750 310" fill="none" stroke="'+GREEN+'" stroke-width="5"/>'
    b+='<path d="M100 98 C180 178 260 219 350 226 S530 184 750 87" fill="none" stroke="'+RED+'" stroke-width="5"/>'
    b+='<path d="M360 68V345" stroke="#82949a" stroke-width="2" stroke-dasharray="7 7"/>'
    b+=t(480,49,'Validation 반등 · 일반화 점검',25,RED)+t(690,73,'Validation',24,RED)+t(700,338,'Train',24,GREEN)
    b+=photo(850,75,170,170)+photo(1060,75,170,170,True)
    b+=t(935,282,'같은 원본 · 밝음',23)+t(1145,282,'밝기 ×0.45',23)
    b+=t(1040,335,'가설: 다른 조명에 취약할까?',25,BLUE)+t(1040,377,'새 조명 조건별 성능으로 확인',23,BLUE)
    b+=t(410,432,'교육용 가상 추세 · 동일한 고정 Train / Validation 분할',23,'#647b86')
    return svg(b,'Epoch Loss 교육용 곡선 Train 감소 Validation 반등; 동일 사과 밝기 변환은 원인 가설 보조 예시',450)

def section(concept,title,subtitle,body,takeaway,caption):
    return f'<section class="slide" data-concept="{concept}" data-level="basic"><div class="slide-inner two-hour f55"><h2 class="slide-title">{title}</h2><p class="slide-subtitle">{subtitle}</p>{body}<p class="lesson-takeaway">{takeaway}</p><p class="f55-caption">{caption}</p></div></section>'

def build(root):
    file=root/'docs/vision_ai_course.html';doc=file.read_text();n=len(re.findall(r'<section\b',doc))
    old=re.search(r'<section\b[^>]*data-concept="learn".*?</section>',doc,re.S).group()
    ui=re.search(r'<figure\b[^>]*data-training-lesson.*?</figure>',old,re.S).group()
    notes='<aside class="f55-presenter-notes" hidden aria-hidden="true">발표자 노트: Batch는 한 번에 보는 사진 묶음. 6 images / Batch 2 = 3 Steps per Epoch. 2 Epochs = 6 Steps. 1 Batch → 1 Step(Weight 갱신). 사과 분류에는 실제 이미지와 정답 Label이 필요하며 이 회귀 수치는 CNN 실측 결과가 아니다.</aside>'
    parts={
    'learn':section('learn','모델 학습 · 오차를 줄이는 반복','사진 + 정답 Label로 배우는 원리를, <strong>x=2 · y=4인 회귀 문제</strong>로 작게 확인합니다.','<div class="f55-learn-bridge">'+'<svg viewBox="0 0 80 80" role="img" aria-label="정답 불량 Label의 생성 사과 입력 예시">'+photo(0,0,80,80)+'</svg>'+'<strong>사과 사진 / Frame + 정답 Label: 불량</strong><span>→ Weight 계산은 아래 작은 회귀 문제로 단순화</span></div>'+ui+notes,'입력과 정답은 고정하고 <strong>Weight를 바꿔 Loss를 줄입니다.</strong> 사과 분류는 Task에 맞는 별도 Loss를 사용합니다.','실제 경사하강 계산 · 사과 CNN 실험 아님 · ŷ=wx · Loss=(ŷ−y)² · η=0.1 · Bias=0 · 1 Batch → 1 Step'),
    'loss':section('loss','Loss · 틀린 정도를 줄이는 방향','Gradient는 <strong>어느 방향으로 얼마나 바꿀지</strong>, Optimizer는 <strong>실제 Weight 갱신</strong>을 담당합니다.',loss(),'한 단계: <strong>w 0.5 → 1.7 · Loss 9 → 0.36</strong>. 입력과 정답은 바뀌지 않습니다.','교육용 단일 변수 회귀 계산 · CNN 결함 분류의 실측 Loss 아님'),
    'cnn-training':section('cnn-training','CNN 학습 · 예측에서 Weight 갱신까지','앞서 본 같은 CNN에서 <strong>Conv Kernel과 Dense Head의 W,b</strong>를 학습합니다.',training(root),'Forward → Loss → Backward → Optimizer를 반복합니다. <strong>초록 화살표가 닿는 세 블록만 Weight를 갱신</strong>합니다.','파랑: Forward · 갈색: Backprop Gradient · 초록: Optimizer Update · Label은 고정 정답 · 교육용 모델 개념도'),
    'infer':section('infer','Training과 Inference의 차이','배울 때는 정답으로 Weight를 바꾸고, <strong>사용할 때는 고정된 Weight로 새 입력을 예측</strong>합니다.',infer(),'Inference는 정답 Label 없이 수행합니다. <strong>출력 raw Score는 보정된 확률을 보장하지 않습니다.</strong>','사진 / 디코딩된 동영상 Frame 입력 예시 · 학습·추론 흐름을 설명하는 자체 개념도'),
    'transfer':section('transfer','전이학습 · 특징은 고정하고 분류기만 학습','<a href="vision_ai_course.html#slide-7" data-ref-concept="cnn-overview">P20 같은 사과 CNN</a> 구조로, <strong>고정할 부분과 학습할 부분</strong>을 비교합니다.',transfer(root),'먼저 Head를 학습하고 필요하면 일부 Conv를 미세조정합니다. <strong>특징 재사용의 적합성은 Validation으로 확인</strong>합니다.','사전학습 모델을 재사용한다고 가정한 교육용 구조 · 사과 결함을 이미 학습했다는 뜻 아님 · 파라미터: Conv A 224 + Conv B 1,168 + Head 34'),
    'cnn-learning-paths':section('cnn-learning-paths','같은 CNN 특징 · 지도와 비지도 활용','두 경로 모두 <strong>하나의 고정 Backbone이 만든 같은 특징</strong>을 사용합니다.', '<div class="su-figure f55-paths">'+paths()+'</div>','지도: <strong>Label로 Head 학습</strong>. 비지도 후단: <strong>Label 없이 특징 군집화</strong>. Group A/B는 정상/불량을 뜻하지 않습니다.','고정된 사전학습 Backbone의 후단 활용 비교 · Backbone의 과거 사전학습에는 Label이 사용되었을 수도 있음 · CNN 전체의 두 학습법 비교 아님'),
    'overfit':section('overfit','Overfitting · 새 데이터 일반화','Train Loss가 계속 내려가도 <strong>Validation Loss가 다시 오르면</strong> 새 데이터 성능을 점검합니다.',overfit(),'학습 사진을 잘 맞히는 것만으로 충분하지 않습니다. <strong>독립된 Validation 조건과 실패 사례</strong>를 함께 봅니다.','곡선은 교육용 가상 추세이며 실제 훈련 로그 아님 · 생성 사과의 화면 밝기 변환은 조명 취약성 가설용이며 실제 재촬영·측정 결과 아님')}
    for key,html in parts.items():
        doc,count=re.subn(rf'<section\b[^>]*data-concept="{key}"[^>]*>.*?</section>',lambda m:html,doc,flags=re.S);assert count==1,(key,count)
    doc,removed=re.subn(r'<section\b[^>]*data-concept="training-log"[^>]*>.*?</section>\s*','',doc,flags=re.S)
    assert removed<=1
    assert len(re.findall(r'<section\b',doc))==n-removed
    if 'approved_f.css' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="approved_f.css?v=approved-f-20261019-1">\n</head>')
    file.write_text(doc)
    print(f'Applied F 7 concepts; absorbed training-log={removed}; sections {n}→{n-removed}')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);build(p.parse_args().root)
