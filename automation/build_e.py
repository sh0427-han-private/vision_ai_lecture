#!/usr/bin/env python3
"""Apply approved P37–P40 only. Usage: python automation/build_e.py [--root REPO]."""
import argparse
import re
from pathlib import Path
from html import escape

PHOTO='assets/vision_task_apple_reference.jpg'
NORMAL='assets/generated/apple_studio_preview.png'
MASK='M581 201 C595 200 605 209 609 221 C614 234 606 244 594 246 C580 247 572 236 571 224 C568 213 574 204 581 201Z'
SPLITS=('train','validation','test')
COLORS=('#168975','#397da5','#9b713e')

def t(x,y,s,size=24,color='#31596b',anchor='start',weight=550):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>'

def svg(body,label,w=1200,h=400):
    return f'<svg class="e55-diagram" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg"><g font-family="Noto Sans KR,Malgun Gothic,sans-serif">{body}</g></svg>'

def photo(x,y,w,h,normal=False,dark=False,attrs=''):
    vb='0 0 300 300' if normal else '240 85 475 475'
    im=f'<image href="{NORMAL}" x="18" y="8" width="264" height="284"/>' if normal else f'<image href="{PHOTO}" width="960" height="640"/>'
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{vb}" overflow="hidden" {attrs}'+(' style="filter:brightness(.48)"' if dark else '')+f'><rect x="-1000" y="-1000" width="3000" height="3000" fill="#b9b9b9"/>{im}</svg>'

def dataset():
    b=t(400,28,'정상 · 갈색 반점 없음',26,anchor='middle',weight=750)+t(770,28,'불량 · 갈색 반점 있음',26,anchor='middle',weight=750)
    for row,dark in enumerate((False,True)):
        y=48+row*185
        b+=t(105,y+90,'어두움' if dark else '밝음',27,anchor='middle',weight=750)
        b+=photo(315,y,170,170,True,dark)+photo(685,y,170,170,False,dark)
    b+=t(1000,117,'한 조건만 모으면?',24,anchor='middle',weight=750)
    b+=t(1000,165,'밝음 = 정상',25,anchor='middle')+t(1000,204,'어두움 = 불량',25,anchor='middle')
    b+='<path d="M915 226L1085 226" stroke="#bc6e57" stroke-width="3"/>'
    b+=t(1000,270,'밝기를 외울 위험',25,'#a15440','middle',750)
    b+=t(1000,311,'네 조건을 함께 수집',25,'#168975','middle',750)
    return svg(b,'정상과 불량 각각 같은 원본에 동일한 밝기 변환을 적용한 네 조건',1200,405)

def split():
    b=t(0,27,'1,000장 = 100타일 × 10장',25,weight=750)
    positions=[(0,14,70),(720,3,15),(930,3,15)]
    for i,(start,cols,count) in enumerate(positions):
        for n in range(count):
            x=start+(n%cols)*44;y=66+(n//cols)*39
            b+=f'<rect x="{x}" y="{y}" width="35" height="30" fill="{COLORS[i]}" opacity=".8" data-split="{SPLITS[i]}" data-count="10"/>'
    for x,label,n,color in [(300,'Train',700,COLORS[0]),(780,'Validation',150,COLORS[1]),(990,'Test',150,COLORS[2])]:
        b+=t(x,295,f'{label} · {n}장',25,color,'middle',750)
    b+='<path d="M300 310V338M780 310V338M990 310V338" stroke="#6e8e9c" stroke-width="3"/>'
    b+=t(300,376,'Weight 업데이트',27,COLORS[0],'middle',750)
    b+=t(780,376,'모델·임계값 선택',24,COLORS[1],'middle',750)
    b+='<path d="M1047 353V342a9 9 0 0 1 18 0v11M1043 353h26v24h-26Z" fill="none" stroke="#9b713e" stroke-width="3"/>'
    b+=t(990,413,'최종 1회 평가 · 잠금',24,COLORS[2],'middle',750)
    return svg(b,'100타일 각각10장, Train700 Validation150 Test150; 학습 선택 최종평가 역할 분리',1200,435)

def frames(mode):
    b=t(295,30,'프레임 무작위 분할 · 누출 예' if mode=='random' else '그룹 분할 · 독립성 유지',26,'#a15440' if mode=='random' else '#168975','middle',750)
    for row,split_name in enumerate(SPLITS):
        y=58+row*111
        b+=t(0,y+47,['Train','Validation','Test'][row],22,COLORS[row],weight=750)
        ids=[(g,row+1) for g in 'ABC'] if mode=='random' else [('ABC'[row],f) for f in (1,2,3)]
        for col,(g,f) in enumerate(ids):
            x=153+col*133
            b+=f'<g data-group="{g}" data-frame="{f}" data-split="{split_name}">'
            # Each ID denotes a hypothetical observation; identical assets across the two arrangements.
            b+=photo(x,y,83,78,normal=g=='B',dark=g=='C')
            b+=t(x+41,y+101,f'{g}{f}',23,anchor='middle',weight=750)+'</g>'
    b+=t(295,415,'A → 세 Split에 등장' if mode=='random' else 'A / B / C → 각각 한 Split',24,'#a15440' if mode=='random' else '#168975','middle',750)
    return f'<g data-split-mode="{mode}">{b}</g>'

def leakage():
    return svg(frames('random')+'<path d="M591 0V430" stroke="#c8d8df" stroke-width="2"/>'+f'<g transform="translate(622 0)">{frames("group")}</g>','같은 가상9개 A1 A2 A3 B1 B2 B3 C1 C2 C3를 무작위 분할과 그룹 분할에 재배치',1220,435)

def augment():
    b=''
    for i,(label,transform,dark,valid) in enumerate([('원본 · 불량','translate(0 0)',False,True),('밝기 ×0.65','translate(0 0)',True,True),('회전 +12°','rotate(12 590 250)',False,True),('결함 완전 가림','translate(0 0)',False,False)]):
        x=i*300
        b+=t(x+135,30,label,25,anchor='middle',weight=750)
        b+=f'<svg x="{x+10}" y="55" width="250" height="250" viewBox="440 100 300 300" overflow="hidden"><g data-augment-transform="{i}" data-augment-valid="{str(valid).lower()}" transform="{transform}">'
        b+=f'<image href="{PHOTO}" width="960" height="640"'+(' style="filter:brightness(.65)"' if dark else '')+'/>'
        b+=f'<path d="{MASK}" fill="#338db7" fill-opacity=".32" stroke="#176b95" stroke-width="2"/><rect x="565" y="197" width="53" height="57" fill="none" stroke="#176b95" stroke-width="3"/>'
        if not valid:
            b+='<rect x="554" y="184" width="78" height="84" fill="#e5e8e8" stroke="#899ca3" stroke-width="2"/>'
        b+='</g></svg>'
        b+=t(x+135,340,'Label 유지 ✓' if valid else '기존 Label 사용 ✕',25,'#168975' if valid else '#a15440','middle',750)
    b+='<path d="M334 375H848M334 369V381M848 369V381" stroke="#338db7" stroke-width="3"/>'
    b+=t(590,413,'사진 + Box + Mask를 함께 변환',27,'#176b95','middle',750)
    return svg(b,'동일한 결함 사과 원본과 밝기 회전 유효 변환, 결함 전체를 가리는 무효 변환. 사진과 정답을 같은 좌표변환 그룹에 포함',1200,435)

def section(concept,title,subtitle,body,takeaway,caption):
    return f'<section class="slide" data-concept="{concept}" data-level="basic"><div class="slide-inner two-hour e55"><h2 class="slide-title">{title}</h2><p class="slide-subtitle">{subtitle}</p>{body}<p class="lesson-takeaway">{takeaway}</p><p class="e55-caption">{caption}</p></div></section>'

def build(root):
    file=root/'docs/vision_ai_course.html';doc=file.read_text();n=len(re.findall(r'<section\b',doc))
    parts={
      'dataset':section('dataset','데이터셋 · 어떤 사진으로 배우나','정상·불량과 밝기 조건을 <strong>교차해서 모아야</strong> 엉뚱한 단서를 외울 위험을 줄일 수 있습니다.',dataset(),'모델이 배워야 할 것은 <strong>밝기가 아니라 결함의 특징</strong>입니다. 애매한 반점의 Label 기준도 합의합니다.','독립된 생성 사과 두 원본을 유사한 크기로 정렬한 교육용 비교 · 원본별 같은 Crop·밝기 ×1 / ×0.48 · 실제 재촬영 아님.'),
      'split':section('split','Train · Validation · Test','데이터를 <strong>학습 · 선택 · 최종 평가</strong>의 서로 다른 역할로 나눕니다.',split(),'Train으로 배우고, Validation으로 선택하고, <strong>잠가 둔 Test에서 최종 확인</strong>합니다.','교육용 70/15/15 사진 수 예시이며 무작위 사진 분할 지시가 아닙니다. 먼저 원본 사과·영상·세션 그룹의 독립성을 확인합니다.'),
      'leakage':section('leakage','Video Group Split · 데이터 누출 방지','사진이 달라도 <strong>같은 사과·영상의 인접 Frame</strong>이면 거의 같은 정보를 공유할 수 있습니다.',leakage(),'원본 사과·영상·연속 촬영 세션을 묶어 분할한 뒤, <strong>Train 안에서만 증강</strong>합니다.','가상 Group A/B/C × 3 Frame: 기존 사진을 재사용한 도식이며 실제 9회 관측이 아닙니다.<br>그룹 키는 평가 목표에 맞춰 설정: 사과·영상·세션, 필요하면 날짜·설비 조건까지 확장합니다.'),
      'augment':section('augment','Data Augmentation · 같은 정답, 다른 조건','분할을 끝낸 <strong>Train에서만</strong>, 정답 의미를 유지하는 밝기·회전 변형을 만듭니다.',augment(),'변형 후에도 <strong>정답이 유효한지</strong> 확인합니다. 결함을 가렸다면 기존 결함 Label을 그대로 쓰지 않습니다.','동일 생성 사과의 화면 처리 시뮬레이션 · 파란 Box/Mask는 사람이 지정한 GT 예시 · Validation/Test는 정해 둔 평가 전처리를 유지합니다.')}
    for key,html in parts.items():
        pat=rf'<section\b[^>]*data-concept="{key}"[^>]*>.*?</section>'
        doc,count=re.subn(pat,lambda m:html,doc,flags=re.S);assert count==1,(key,count)
    assert len(re.findall(r'<section\b',doc))==n
    if 'approved_e.css' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="approved_e.css?v=approved-e-20261019-1">\n</head>')
    file.write_text(doc)
    print('Applied E: '+', '.join(parts)+f'; section count preserved at {n}')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);build(p.parse_args().root)
