#!/usr/bin/env python3
"""Build approved P28–P36 only; root owns ordering, manifest, QA and commits.

Usage: python automation/build_d.py [--root /path/to/repository]
The generated matrices are visible SVG text, with data-matrix-name annotations
for independent extraction and numerical verification. No runtime numeric data.
"""
from pathlib import Path
from html import escape
import argparse
import re

X = [[1,2,3,0,1],[4,5,6,1,0],[7,8,9,2,1],[0,1,2,3,1],[1,0,1,2,3]]
K = [[1,0,-1],[1,0,-1],[1,0,-1]]
PAD_X = [[1,2,3],[4,5,6],[7,8,9]]
POOL_X = [[1,3,2,4],[5,6,1,2],[4,2,9,3],[0,7,8,1]]
COLORS = ['#168975','#326fa8','#925e9c','#b27836','#4e8394','#a45f65','#65833d','#6869a7','#347f81']


def conv(a, k, stride=1, pad=0):
    x = [[0]*(len(a[0])+2*pad) for _ in range(pad)] + [[0]*pad+row+[0]*pad for row in a] + [[0]*(len(a[0])+2*pad) for _ in range(pad)]
    return [[sum(x[r+i][c+j]*k[i][j] for i in range(len(k)) for j in range(len(k[0]))) for c in range(0,len(x[0])-len(k[0])+1,stride)] for r in range(0,len(x)-len(k)+1,stride)]


def text(x, y, value, size=22, color='#294f60', anchor='start', weight=500, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}" {extra}>{escape(str(value))}</text>'


def rect(x, y, w, h, fill='#fff', stroke='#b9cdd5', extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" {extra}/>'


def path(d, color='#6c909e', arrow=False, extra=''):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5" {"marker-end=\"url(#d55-arrow)\"" if arrow else ""} {extra}/>'


def matrix(a, x, y, cell=40, name=None, fill=None, border=None, size=24, labels=None):
    body = ''
    for r, row in enumerate(a):
        for c, value in enumerate(row):
            bg = fill(r,c,value) if fill else '#f3f7f9'
            stroke = border(r,c,value) if border else '#c1d3db'
            body += rect(x+c*cell,y+r*cell,cell,cell,bg,stroke)
            if size > 0: body += text(x+(c+.5)*cell,y+(r+.5)*cell+size*.34,value,size,anchor='middle',weight=650,extra=f'data-row="{r+1}" data-col="{c+1}"')
    attrs = f' data-matrix-name="{name}" data-cols="{len(a[0])}"' if name else ''
    return f'<g{attrs}>{body}</g>'


def svg(body, label, w=1200, h=370, extra=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" class="d55-diagram" {extra}><defs><marker id="d55-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#638895"/></marker></defs><g font-family="Noto Sans KR,Malgun Gothic,sans-serif">{body}</g></svg>'


def kernel_svg():
    fill = lambda r,c,v: ['#dceee6','#f2f5f6','#f6e4de'][c] if r<3 and c<3 else '#fff'
    b = text(105,30,'가상 입력 · 5×5',24,anchor='middle',weight=750)
    b += matrix(X,0,54,42,'kernel-input',fill=fill)
    b += rect(0,54,126,126,'none','#168975','stroke-width="3"')
    b += text(315,30,'Kernel · 3×3×1',24,anchor='middle',weight=750)
    b += matrix(K,252,54,42,'kernel-weights',fill=lambda r,c,v:['#dceee6','#f2f5f6','#f6e4de'][c])
    b += path('M225 117H239',arrow=True)
    for r in range(3):
        y = 84+r*65
        b += text(438,y,f'{X[r][0]}×(+1)',24,'#168975',weight=750)
        b += text(541,y,f'+ {X[r][1]}×0',24,'#7b8b93')
        b += text(640,y,f'+ {X[r][2]}×(−1)',24,'#a45f48',weight=750)
        b += text(783,y,'= −2',25,'#294f60',weight=750)
    b += path('M433 238H864')
    b += text(650,286,'−2 + (−2) + (−2) = −6',30,'#147963','middle',750)
    b += text(105,297,'左上 3×3 윈도우',20,anchor='middle')
    b = b.replace('左上','왼쪽 위')
    b += text(315,297,'학습으로 바뀌는 9 Weight',20,anchor='middle')
    return svg(b,'교육용 단일채널 5×5 입력에서 첫 3×3 영역과 Kernel의 아홉 곱을 더해 −6',900,325)


def map_svg():
    out = conv(X,K)
    outputs = []
    b = text(120,26,'같은 입력 · 5×5',24,anchor='middle',weight=750)
    b += matrix(X,10,50,43,'feature-input')
    for r in range(3):
        for c in range(3):
            i=r*3+c
            b += f'<circle cx="{16+c*43}" cy="{56+r*43}" r="5" fill="{COLORS[i]}"/>'
    b += text(120,295,'같은 Kernel · 3×3',22,anchor='middle',weight=700)
    b += matrix(K,70,307,32,'feature-weights',size=20)
    for r in range(3):
        for c in range(3):
            i=r*3+c; xx=270+c*310; yy=12+r*133; col=COLORS[i]
            win=[row[c:c+3] for row in X[r:r+3]]
            b += rect(xx,yy,292,121,'#fff',col,'stroke-width="2"')
            b += text(xx+13,yy+25,f'시작 ({r+1},{c+1})',21,col,weight=750)
            b += matrix(win,xx+13,yy+35,25,f'window-{r+1}-{c+1}',size=22)
            b += path(f'M{xx+102} {yy+73}H{xx+136}',col,True)
            b += rect(xx+152,yy+40,120,63,'#f5faf8',col)
            outputs.append(text(xx+212,yy+83,out[r][c],36,col,'middle',750,extra=f'data-row="{r+1}" data-col="{c+1}" data-feature-output="true"'))
            b += text(xx+212,yy+25,f'출력 ({r+1},{c+1})',19,col,'middle')
    b += '<g data-matrix-name="feature-output" data-cols="3">'+''.join(outputs)+'</g>'
    b += text(120,435,'행·열은 1부터',20,anchor='middle')
    b += text(735,435,'첫 −6 → 한 칸 오른쪽 12 → 아홉 위치의 3×3 Feature Map',22,anchor='middle',weight=700)
    return svg(b,'같은 Kernel로 입력의 아홉 3×3 윈도우를 계산하며 시작 좌표와 Feature Map 출력 좌표를 일대일 대응',1200,450)


def sharing_svg():
    b=''
    labels=['전체 연결','지역 연결 · 위치별 다른 Weight','지역 연결 · 같은 Weight 공유']
    for k,label in enumerate(labels):
        x=k*400
        b += text(x+195,30,label,24,anchor='middle',weight=750)
        if k==0:
            for i in range(5):
                for j in range(5): b += path(f'M{x+75} {68+i*30}L{x+315} {68+j*30}','#c5d8df')
            for i in range(5):
                b += f'<circle cx="{x+75}" cy="{68+i*30}" r="7" fill="#769bab"/><circle cx="{x+315}" cy="{68+i*30}" r="7" fill="#429780"/>'
        else:
            for p in range(2):
                xx=x+25+p*180
                col=('#3a8b77' if k==2 or p==0 else '#85559b')
                b += matrix([[1,1,1]]*3,xx,62,20,size=0,fill=lambda r,c,v:'#e4f0f3')
                # Text-zero labels are omitted: these 3×3 cells represent connections, not numeric weights.
                b += path(f'M{xx+70} 92H{xx+132}',col,True)
                b += f'<circle cx="{xx+151}" cy="92" r="17" fill="{col}"/>'
                b += text(xx+80,157,f'위치 {p+1}',21,col,'middle',700)
                b += text(xx+80,189,'같은 9개' if k==2 else f'별도 9개 ({p+1})',20,col,'middle')
        nums=['1,048,576','9,216','9']; formulas=['1024 × 1024','1024 × 9','3 × 3 = 9']
        b += text(x+195,252,nums[k],40,'#197a65','middle',750)
        b += text(x+195,289,formulas[k]+' Weight',22,anchor='middle',weight=650)
    b += text(600,338,'공유하는 Weight는 9개여도, 1024개 위치에서 9개씩 = 9,216번 곱합니다.',25,'#294f60','middle',700)
    return svg(b,'전체 연결, 위치별 독립 3×3, 공유 3×3 Kernel의 가중치 수 비교. 공유 가중치 9개와 곱셈 9216회를 구별',1200,360)


def volume(x,y,col,kind):
    b=''
    fills=['#efceca','#d3e7d2','#d2e1f0'] if kind=='rgb' else [col]*3
    for p in range(3):
        xx=x+p*13; yy=y+p*11
        b += rect(xx,yy,92,80,fills[p],'#6f91a1')
        for a in (1,2): b += path(f'M{xx+a*92/3} {yy}V{yy+80}M{xx} {yy+a*80/3}H{xx+92}','#a6c3ce')
        if kind=='rgb': b += text(xx+10,yy+21,'RGB'[p],18,weight=750)
    return b


def channel_svg():
    b=text(125,29,'같은 RGB 입력',24,anchor='middle',weight=750)
    b += volume(50,119,'#d9e8ed','rgb')
    b += text(125,260,'H × W × 3',24,anchor='middle',weight=700)
    b += path('M206 171H268V93H387',arrow=True)+path('M268 171V265H387',arrow=True)
    for p,col in enumerate(['#168975','#326fa8']):
        y=24+p*172; name='AB'[p]
        b += volume(410,y+30,'#d5e9e7' if not p else '#d6e2ef','weight')
        b += text(571,y+68,f'Filter {name}',25,col,weight=750)
        b += text(571,y+102,'3 × 3 × 3',24,col,weight=700)
        b += path(f'M728 {y+85}H807',col,True)
        for r in range(3):
            for c in range(4):
                b += rect(828+c*34,y+35+r*29,34,29,['#e6f1ed','#b4d8cb','#70aa96'][(r+c+p)%3],col)
        b += text(989,y+70,f'Map {name}',25,col,weight=750)
        b += text(989,y+104,'H′ × W′ × 1',22,col,weight=700)
    b += path('M1150 67H1170V327H1150')
    b += text(600,380,'필터 2개는 같은 3채널 전체를 각각 읽습니다. → 출력 2채널: H′ × W′ × 2',25,anchor='middle',weight=700)
    return svg(b,'같은 RGB 세 채널에서 두 개 3×3×3 필터로 병렬 분기하여 출력 특징 지도 두 장을 만드는 구조',1200,405)


def stride_svg():
    b=''
    for k,s in enumerate((1,2)):
        x=k*610; out=conv(X,K,stride=s)
        b += text(x+285,28,f'Stride {s} · 시작 {9 if s==1 else 4}곳',26,anchor='middle',weight=750)
        b += matrix(X,x+20,57,43,f'stride-{s}-input',size=23)
        for r in range(0,3,s):
            for c in range(0,3,s):
                b += f'<circle cx="{x+26+c*43}" cy="{63+r*43}" r="5" fill="#168975" data-stride-start="{s}" data-row="{r+1}" data-col="{c+1}"/>'
        b += path(f'M{x+250} 164H{x+319}',arrow=True)
        b += matrix(out,x+342,85,58,f'stride-{s}-output',size=29)
        b += text(x+123,309,'시작 행·열: '+('1, 2, 3' if s==1 else '1, 3'),22,anchor='middle')
        b += text(x+428,309,f'출력 {len(out)}×{len(out)}',25,anchor='middle',weight=750)
    b += text(600,358,'Stride 2 결과 = Stride 1 Map의 (1,1), (1,3), (3,1), (3,3)',25,'#197a65','middle',700)
    return svg(b,'같은 5×5 입력과 3×3 Kernel의 시작 위치 9곳 대 4곳과 일치하는 출력 값. 좌표는 행 열 1부터',1200,380)


def padding_svg():
    z=[[0]*5]+[[0]+row+[0] for row in PAD_X]+[[0]*5]
    b=text(115,25,'별도 입력 · 3×3',24,anchor='middle',weight=750)
    b += matrix(PAD_X,50,60,42,'padding-input')
    b += text(115,235,'Kernel 3×3 · 모두 1',22,anchor='middle',weight=700)
    b += text(115,269,'Stride 1 · Bias 0',21,anchor='middle')
    b += path('M197 123H252V62H319',arrow=True)+path('M252 123V239H444',arrow=True)
    b += text(390,30,'Padding 0',25,anchor='middle',weight=750)
    b += matrix([[45]],339,50,100,'padding-0-output',size=38)
    b += text(390,186,'3×3 → 1×1',24,anchor='middle',weight=750)
    b += text(800,30,'Padding 1 · 바깥 0 추가',25,anchor='middle',weight=750)
    b += matrix(z,465,77,43,'padding-zeros',size=23,fill=lambda r,c,v:'#e9edf0' if r in (0,4) or c in (0,4) else '#fff',border=lambda r,c,v:'#8e9faa' if r in (0,4) or c in (0,4) else '#b9cdd5')
    b += path('M703 184H793',arrow=True)
    b += matrix(conv(PAD_X,[[1]*3]*3,pad=1),817,94,57,'padding-output',size=29)
    b += text(902,315,'3×3 → 3×3',25,anchor='middle',weight=750)
    b += text(590,354,'회색 0은 촬영 Pixel이 아니라 연산 전에 경계 바깥에 더한 값입니다.',24,'#526f7c','middle')
    return svg(b,'동일한 3×3 입력에 Padding 0은 출력45 한 칸, Padding1은 바깥0을 넣어 3×3 출력 생성',1200,380)


def pool_svg():
    colors=['#def0e7','#dce9f4','#f0e6d8','#e9e1f0']
    maxima={(1,1),(0,3),(3,1),(2,2)}
    edgecolors=['#168975','#326fa8','#b27836','#925e9c']
    b=text(219,29,'입력 Feature Map · 4×4',26,anchor='middle',weight=750)
    b += matrix(POOL_X,95,55,61,'pool-input',size=29,fill=lambda r,c,v:colors[(r//2)*2+c//2],border=lambda r,c,v:edgecolors[(r//2)*2+c//2] if (r,c) in maxima else '#bacdd5')
    for r,c in maxima: b += rect(95+c*61+3,55+r*61+3,55,55,'none',edgecolors[(r//2)*2+c//2],'stroke-width="3"')
    for i,(value,label) in enumerate([(6,'왼쪽 위'),(4,'오른쪽 위'),(7,'왼쪽 아래'),(9,'오른쪽 아래')]):
        y=80+i*61
        b += rect(416,y-28,265,47,colors[i],'#bdcfd5')+text(548,y+4,f'{label} Max = {value}',22,anchor='middle',weight=650)
        out_y=116 if i<2 else 207
        # Region identity is both named and color matched; no ambiguous line crossings across the input.
        if i%2==0:
            b += path(f'M696 {y-5}H743V{out_y}H780',edgecolors[i],True)
        else:
            route_y=43 if i==1 else 281
            b += path(f'M696 {y-5}H723V{route_y}H1005V{out_y}H988',edgecolors[i],True)
    b += text(928,29,'Max Pool 2×2 · Stride 2',26,anchor='middle',weight=750)
    b += matrix([[6,4],[7,9]],793,70,91,'pool-output',size=37,fill=lambda r,c,v:colors[r*2+c])
    b += text(600,346,'4×4×8 → 2×2×8 · 공간은 절반씩, 채널 수는 그대로 · 학습 Weight 없음',26,'#197a65','middle',700)
    return svg(b,'4×4 지도 네 영역의 최대값6,4,7,9를 같은 색2×2출력으로 보존하며 채널 수 유지',1200,370)


def photo(x,y,w,h,uid,annotation=''):
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 960 640" preserveAspectRatio="xMidYMid meet"><image href="assets/vision_task_apple_reference.jpg" width="960" height="640"/>{annotation}</svg>'


def head_svg():
    b=text(285,27,'P20과 같은 Backbone',26,'#326c81','middle',750)
    b+=photo(12,90,185,160,'head-input')+text(104,280,'64×64×3 입력',21,anchor='middle')
    b+=path('M206 170H236',arrow=True)
    b+=rect(246,69,426,212,'#f4f8fa','#9cb9c7')
    b+='<svg x="260" y="97" width="397" height="81" viewBox="138 0 672 90" overflow="hidden"><defs><clipPath id="d55-backbone-clip"><rect x="138" y="0" width="672" height="90"/></clipPath></defs><image href="assets/lesson/cnn_apple_architecture.svg?v=approved-c-20261019-1" width="1280" height="430" clip-path="url(#d55-backbone-clip)"/></svg>'
    b+=text(459,208,'Conv A → ReLU → Pool',24,anchor='middle',weight=700)+text(459,243,'→ Conv B → ReLU',24,anchor='middle',weight=700)
    b+=text(459,317,'공간 특징 32×32×16',24,'#326c81','middle',750)
    b+=path('M685 172H720V66H758',arrow=True)+path('M720 172V186H758',arrow=True)+path('M720 172V306H758',arrow=True)
    for i,(title,desc) in enumerate([('Class Head','GAP 16 → Dense 2'),('Box Head','Class + Box 좌표'),('Mask Head','Pixel별 Class')]):
        y=22+i*120
        b+=rect(772,y,220,87,'#edf6f0','#7bb49f')
        b+=text(882,y+34,title,25,'#197a65','middle',750)+text(882,y+67,desc,21,'#366f61','middle')
        b+=path(f'M1005 {y+44}H1042',arrow=True)
        if i==0:
            b+=text(1130,y+40,'정상 / 불량',24,'#294f60','middle',750)+text(1130,y+72,'Score · 미측정',20,'#526f7c','middle')
        else:
            ann=('<rect x="565" y="197" width="53" height="57" fill="none" stroke="#0d8d74" stroke-width="17"/>' if i==1 else '<path d="M570 204L587 197L611 207L618 226L608 247L586 254L565 239L565 220Z" fill="#168975" fill-opacity=".82"/>')
            b+=photo(1058,y-6,145,98,f'head-out-{i}',ann)
    b+=text(600,402,'분류는 P20의 GAP+Dense2 경로 · 검출/분할은 공간 특징을 쓰는 다른 Head 설계',23,'#526f7c','middle')
    return svg(b,'같은 사과 CNN의 Conv A ReLU Pool Conv B ReLU 공간 특징에서 Class,Box,Mask의 대체 가능한 Head경로와 출력',1220,425)


def mini(label='Conv 계산 확대', focus='conv'):
    return f'<div class="c55-map d55-map"><span>{label}</span><div data-cnn-map="{focus}" aria-label="같은 P20 사과 CNN에서 {label} 강조"></div></div>'


def section(concept,title,subtitle,body,takeaway,caption='',focus='conv',label='Conv 계산 확대',extra=''):
    return f'<section class="slide" data-concept="{concept}" data-level="basic"><div class="slide-inner two-hour d55 {extra}"><h2 class="slide-title">{title}</h2><p class="slide-subtitle">{subtitle}</p>{mini(label,focus)}{body}<p class="lesson-takeaway">{takeaway}</p>{f"<p class=\"d55-caption\">{caption}</p>" if caption else ""}</div></section>'


def real_map_body():
    specs=[('입력 사진','RGB · 224×224×3','59 263 226 266',None,'모델에 넣은 강아지 원본'),('얕은 층','111×111×64','362 272 331 240',1,'4 / 64채널 · 35, 30, 44, 32'),('중간 층','27×27×256','766 272 331 240',7,'4 / 256채널 · 2, 62, 24, 153'),('깊은 층','13×13×512','1170 272 331 240',12,'4 / 512채널 · 471, 302, 409, 415')]
    b='<div class="d55-real" data-d55-real-maps data-load-state="loading"><div class="cnn-feature-flow">'
    for i,(name,shape,box,layer,ids) in enumerate(specs):
        xx,yy,ww,hh=box.split()
        cls=['input','shallow','middle','deep'][i]
        b+=f'<figure class="cnn-feature-stage cnn-feature-stage--{cls}"><h3>{name}</h3><p class="cnn-feature-shape">{shape}</p><svg class="cnn-feature-visual" viewBox="{box}" role="img" aria-label="{name} · {ids}" overflow="hidden"><defs><clipPath id="d55-real-{i}"><rect x="{xx}" y="{yy}" width="{ww}" height="{hh}"/></clipPath></defs><image href="assets/lesson/cnn_squeezenet_actual_feature_maps.png" width="1600" height="690" clip-path="url(#d55-real-{i})"/></svg><figcaption>{f"features[{layer}]<br>" if layer is not None else ""}{ids}</figcaption></figure>'
    b+='</div><div class="d55-map-fallback" role="status"><strong>시각화 불러오기 실패</strong><p>같은 강아지 입력 → SqueezeNet 1.1 → 얕은·중간·깊은 층의 반응</p><p>원본 실측 이미지를 불러올 수 없습니다. 이 설명은 모델의 계산 흐름만 표시합니다.</p></div></div>'
    return b


def replace_section(doc,concept,replacement):
    pattern=rf'<section\b[^>]*data-concept="{re.escape(concept)}"[^>]*>.*?</section>'
    updated,count=re.subn(pattern,lambda _:replacement,doc,count=1,flags=re.S)
    if count!=1: raise RuntimeError(f'Expected exactly one {concept}; got {count}')
    return updated


def build(root):
    assert conv(X,K)==[[-6,12,16],[-6,8,15],[-4,2,7]]
    assert conv(X,K,stride=2)==[[-6,16],[-4,7]]
    assert conv(PAD_X,[[1]*3]*3,pad=1)==[[12,21,16],[27,45,33],[24,39,28]]
    assert [[max(POOL_X[2*r+i][2*c+j] for i in range(2) for j in range(2)) for c in range(2)] for r in range(2)]==[[6,4],[7,9]]
    course=root/'docs/vision_ai_course.html'; doc=course.read_text()
    start_count=len(re.findall(r'<section\b',doc))
    photo_roi='<div class="d55-kernel-photo"><h3>사과 사진 · 실제 ROI</h3><svg viewBox="0 0 960 640" role="img" aria-label="사과 사진의 실제85×85 관심영역"><image href="assets/vision_task_apple_reference.jpg" width="960" height="640"/><rect x="550" y="185" width="85" height="85" fill="none" stroke="#168975" stroke-width="9"/></svg><svg viewBox="550 185 85 85" role="img" aria-label="동일 사과85×85 JPEG 영역확대" overflow="hidden"><defs><clipPath id="d55-roi"><rect x="550" y="185" width="85" height="85"/></clipPath></defs><image href="assets/vision_task_apple_reference.jpg" width="960" height="640" clip-path="url(#d55-roi)"/></svg><p>같은 85×85 Pixel 확대</p></div>'
    toys='P20 전체 RGB 모델에서 Conv 원리만 확대한 별도 교육용 단일채널 예시 · 실제 사과 Pixel 값 아님 · Kernel을 뒤집지 않는 cross-correlation · Bias 0'
    parts={}
    parts['kernel']=section('kernel','Kernel · 작은 영역의 가중합','작은 영역의 값과 Kernel Weight를 같은 위치끼리 곱하고 더하면, <strong>반응값 하나</strong>가 됩니다.',f'<div class="d55-kernel">{photo_roi}<div class="d55-toy-boundary"><h3>교육용 가상 숫자 · 실제 JPEG에서 추출한 값 아님</h3>{kernel_svg()}</div></div>','3×3 영역의 <strong>9쌍 곱을 합하면 −6</strong>입니다. CNN의 Kernel Weight는 학습으로 바뀝니다.',toys,extra='d55-kernel-slide')
    parts['feature-map']=section('feature-map','Feature Map · 같은 계산을 위치마다','P28과 <strong>같은 입력·같은 Kernel</strong>입니다. 입력 창의 시작 (행, 열)이 출력의 (행, 열)과 대응합니다.',map_svg(),'첫 위치는 <strong>−6</strong>, 오른쪽 한 칸은 <strong>(2−0)+(5−1)+(8−2)=12</strong>. 아홉 반응이 3×3 Map을 채웁니다.','행·열 좌표는 1부터 · Stride 1, Padding 0 · ReLU 전 중간 반응이며 사진 축소판·결함 Mask가 아닙니다. '+toys)
    parts['sharing']=section('sharing','CNN · 지역 연결과 가중치 공유','비교 조건: <strong>32×32 단일 입력·출력 채널</strong> · Kernel 3×3 · Stride 1 · Padding 1 · Bias 제외.',sharing_svg(),'지역 연결은 보는 범위를 제한하고, <strong>Weight Sharing은 같은 9개 Weight를 모든 위치에서 재사용</strong>합니다.','9개 Weight ≠ 곱셈 9회 · 32×32×9 = 9,216회(0 테두리 계산 포함). 세 구조의 표현력은 같지 않습니다. P20 전체 모델과 별도 비교입니다.')
    parts['channels']=section('channels','RGB에서 Feature Channel까지','<strong>필터 한 개는 R·G·B 세 채널 전체의 3×3 값</strong>을 합쳐 출력 Map 한 장을 만듭니다.',channel_svg(),'입력의 3은 <strong>색 채널</strong>, 출력의 2는 <strong>서로 다른 필터의 반응 지도 수</strong>입니다.','두 필터·반응 색상은 원리 도식(실측 아님). P20 Conv A는 필터 8개→64×64×8, Conv B는 입력8채널에 필터16개→32×32×16입니다.')
    parts['stride']=section('stride','Stride · 계산 위치의 간격','P28·P29의 <strong>같은 5×5 입력과 3×3 Kernel</strong>을 사용합니다. 점은 Kernel 왼쪽 위의 시작 위치입니다.',stride_svg(),'간격 1은 <strong>3×3</strong>, 간격 2는 <strong>2×2</strong>. 간격을 늘리면 계산 위치와 출력 공간 크기가 줄어듭니다.','출력 한 변 = ⌊(5−3)/Stride⌋+1 · Padding 0 · 좌표 1부터 · '+toys)
    parts['padding']=section('padding','Padding · 같은 입력, 다른 출력 크기','입력 바깥에 0을 더하면 <strong>가장자리 위치도 중심으로 계산</strong>할 수 있습니다.',padding_svg(),'두 경우는 <strong>같은 입력·같은 Kernel</strong>입니다. 바깥 0의 유무가 출력 1×1과 3×3을 가릅니다.','P28과 다른 교육용 3×3 입력·ones Kernel 예시. Padding은 Conv의 설정이며 별도 학습 Layer가 아닙니다.')
    parts['pool']=section('pool','Max Pooling · 영역별 최댓값','각 채널의 작은 영역에서 <strong>가장 큰 반응 하나</strong>만 남겨 가로·세로를 줄입니다.',pool_svg(),'네 영역의 <strong>6, 4, 7, 9</strong>만 남습니다. 영역 안의 정확한 위치와 나머지 반응값은 사라집니다.','별도 교육용 4×4 Feature Map 한 채널 확대 · 같은 Max 연산을 8채널에 각각 적용하면 4×4×8→2×2×8 · 학습 Kernel 아님.',focus='pool',label='Max Pool 확대')
    parts['actual-map']=section('actual-map','실제 Feature Map · CNN 내부 반응','이번에는 <strong>실제 ImageNet 사전학습 SqueezeNet 1.1</strong>입니다. 같은 강아지 한 장에서 세 단계의 반응을 계산했습니다.',real_map_body(),'밝은색은 해당 채널 안에서 상대적으로 큰 반응입니다. <strong>채널별 2–99% 정규화</strong>로 채널·층 사이 절대 밝기를 비교할 수 없습니다.','Shape는 H×W×C · 입력224×224 Bilinear Resize + ImageNet 정규화 · P20 가상 사과 CNN과 다른 모델입니다. <br><span class="d55-real-source">입력 사진: <a href="https://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture5.pdf" target="_blank" rel="noopener">Stanford CS231n 2017 Lecture 5, Slide 37</a>의 강아지 Crop. 실제 계산: scripts/render_cnn_feature_maps.py · <a href="https://pytorch.org/vision/stable/models/generated/torchvision.models.squeezenet1_1.html" target="_blank" rel="noopener">SqueezeNet1_1_Weights.IMAGENET1K_V1</a></span>',label='특징 지도 위치',extra='d55-actual-map')
    parts['backbone']=section('backbone','Backbone과 Task Head','지금까지 배운 Conv·ReLU·Pool은 <strong>공간 특징을 만드는 Backbone</strong>입니다. 필요한 출력에 맞춰 Head를 연결합니다.',head_svg(),'같은 특징 추출 원리에서 <strong>Class·Box·Mask에 맞는 서로 다른 Head</strong>를 선택합니다.','분류의 P20 구조를 회수한 설계 비교입니다. 사진 위 Box·Mask는 출력 형식을 보이는 표시이며 실제 모델 예측이 아닙니다. 세 Head가 자동으로 모두 제공되는 것은 아닙니다.',focus='all',label='Backbone / Head')
    for concept,html in parts.items(): doc=replace_section(doc,concept,html)
    assert len(re.findall(r'<section\b',doc))==start_count
    for element,needle in [('<link rel="stylesheet" href="approved_d.css?v=approved-d-20261019-1">','approved_d.css'),('<script src="approved_d.js?v=approved-d-20261019-1" defer></script>','approved_d.js')]:
        if needle not in doc: doc=doc.replace('</head>',element+'\n</head>')
    # Each SVG lives in its own section: namespace its marker IDs for DOM validity.
    for concept in parts:
        pattern=rf'<section\b[^>]*data-concept="{re.escape(concept)}"[^>]*>.*?</section>'
        doc=re.sub(pattern,lambda m:m.group(0).replace('id="d55-arrow"',f'id="d55-arrow-{concept}"').replace('url(#d55-arrow)',f'url(#d55-arrow-{concept})'),doc,flags=re.S)
    course.write_text(doc)
    print('Applied D: '+', '.join(parts)+'; section count preserved at '+str(start_count))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);build(p.parse_args().root)
