"""Verify published DOM/manifest against approved plan. --final enforces completed55."""
from pathlib import Path
import argparse,json,re,html,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'docs'
p=argparse.ArgumentParser();p.add_argument('--final',action='store_true');args=p.parse_args()
plan=json.loads((ROOT/'planning/approved55.json').read_text());m=json.loads((D/'two_hour_manifest.json').read_text())
outline=json.loads((D/'lecture_outline.js').read_text().split(' = ',1)[1].strip().rstrip(';'))
links=[i for g in outline['groups'] for i in g['items']];concepts={};total=0
for deck,entries in m['decks'].items():
 text=(D/(deck+'.html')).read_text();ss=re.findall(r'<section\b[^>]*class="slide[^\"]*"[^>]*>.*?</section>',text,re.S)
 assert len(ss)==len(entries) and text.count('class="slide active"')==1
 assert 'lecture_outline.js?v=approved55-20261019-1' in text
 for n,s in enumerate(ss,1):
  c=re.search(r'data-concept="([^\"]+)"',s)[1];assert c not in concepts,c;concepts[c]=s
  title=html.unescape(re.sub('<[^>]*>','',re.search(r'<h[12][^>]*class="slide-title[^\"]*"[^>]*>(.*?)</h[12]>',s,re.S)[1])).strip()
  assert entries[n-1]==dict(slide=n,title=title,concept=c)
  total+=1;assert links[total-1]=={'page':deck+'.html','slide':n,'title':title,'global':total}
 for url in re.findall(r'(?:src|href)="([^\"]+)"',text):
  if url.startswith(('https:','http:','#','data:','mailto:','url(')):continue
  path=url.split('?',1)[0].split('#',1)[0]
  if path: assert (D/path).is_file(),(deck,path)
 covered=[n for b in m['blocks'] if b['deck']==deck for n in range(b['start'],b['end']+1)]
 assert covered==list(range(1,len(entries)+1))
assert [i['global'] for i in links]==list(range(1,total+1))
actual=[e['concept'] for entries in m['decks'].values() for e in entries];expected=[x['concept'] for x in plan]
assert [c for c in actual if c in expected]==expected
assert [b['minutes'] for b in m['blocks']]==[26,10,23,22,9,15,10,5]
assert m['teaching_minutes']==m['duration_minutes']==120 and m['discussion_minutes']==0
if args.final:
 assert actual==expected and total==55
 assert [len(m['decks'][k]) for k in ['intro','vision_ai_course']]==[13,42]
 assert not re.search(r'<img[^>]*src="https?://',(D/'vision_ai_course.html').read_text())
# Independent arithmetic, including bias terms and output shapes.
shape=lambda n,k,p,s:(n+2*p-k)//s+1
assert shape(64,3,1,1)==64 and shape(64,2,0,2)==32 and shape(32,3,1,1)==32
assert (3*3*3+1)*8==224 and (3*3*8+1)*16==1168 and (16+1)*2==34
assert 224+1168+34==1426
# Inspect the values actually drawn in the shared local model, not a hidden fixture.
arch=ET.parse(D/'assets/lesson/cnn_apple_architecture.svg').getroot()
def has_class(node,name):return name in node.get('class','').split()
shown_shapes=[''.join(n.itertext()).strip() for n in arch.iter() if has_class(n,'arch-shape')]
assert shown_shapes==['64×64×3','64×64×8','64×64×8','32×32×8','32×32×16','32×32×16','16','2'],shown_shapes
shown_weights=[int(re.sub(r'[^0-9]','',''.join(n.itertext()))) for n in arch.iter() if has_class(n,'arch-weight')]
assert shown_weights==[224,1168,34],shown_weights
assert {n.get('data-arch-node') for n in arch.iter() if n.get('data-arch-node')}=={'input','conv-a','relu-a','pool','conv-b','relu-b','gap','head','output'}

A=[[1,2,3,0,1],[4,5,6,1,0],[7,8,9,2,1],[0,1,2,3,1],[1,0,1,2,3]];K=[[1,0,-1]]*3
M=[[sum(A[y+i][x+j]*K[i][j] for i in range(3) for j in range(3)) for x in range(3)] for y in range(3)]
assert M==[[-6,12,16],[-6,8,15],[-4,2,7]]
assert [[M[y][x] for x in (0,2)] for y in (0,2)]==[[-6,16],[-4,7]]
P=[[1,3,2,4],[5,6,1,2],[4,2,9,3],[0,7,8,1]]
assert [[max(P[2*y+i][2*x+j] for i in range(2) for j in range(2)) for x in range(2)] for y in range(2)]==[[6,4],[7,9]]
assert abs(.5-.1*(2*(.5*2-4)*2)-1.7)<1e-12 and abs((1.7*2-4)**2-.36)<1e-12
assert 700+150+150==1000 and 18+2+4+76==100
assert 18/22*100>81.8 and 18/20==.9 and (18+76)/100==.94
assert 32*32*32*32==1048576 and 9*32*32==9216
# Once D is applied, read the numbers drawn in its SVGs (not Builder fixtures).
if 'data-matrix-name="kernel-input"' in concepts['kernel']:
 drawn={}
 for c in ['kernel','feature-map','stride','padding','pool']:
  for source in re.findall(r'<svg\b.*?</svg>',concepts[c],re.S):
   for node in ET.fromstring(source).iter():
    key=node.get('data-matrix-name')
    if not key:continue
    cols=int(node.get('data-cols'));cells=[n for n in node.iter() if n.get('data-row')]
    assert len(cells)%cols==0
    values=[int(''.join(n.itertext()).replace('−','-')) for n in cells]
    drawn[key]=[values[i:i+cols] for i in range(0,len(values),cols)]
 assert drawn['kernel-input']==drawn['feature-input']==drawn['stride-1-input']==drawn['stride-2-input']==A
 assert drawn['kernel-weights']==drawn['feature-weights']==K
 assert drawn['feature-output']==drawn['stride-1-output']==M
 for y in range(3):
  for x in range(3):assert drawn[f'window-{y+1}-{x+1}']==[row[x:x+3] for row in A[y:y+3]]
 assert drawn['stride-2-output']==[[M[y][x] for x in (0,2)] for y in (0,2)]
 orig=drawn['padding-input'];pad=drawn['padding-zeros']
 assert orig==[[1,2,3],[4,5,6],[7,8,9]]
 assert pad==[[0]*5]+[[0]+row+[0] for row in orig]+[[0]*5]
 assert drawn['padding-output']==[[sum(pad[y+i][x+j] for i in range(3) for j in range(3)) for x in range(3)] for y in range(3)]
 assert drawn['pool-input']==P and drawn['pool-output']==[[6,4],[7,9]]
# Every local SVG actually referenced by the two decks parses successfully.
for name in re.findall(r'(?:src|href)="([^\"]+\.svg)(?:\?[^\"]*)?"',(D/'intro.html').read_text()+(D/'vision_ai_course.html').read_text()):
 if not name.startswith(('http:','https:','data:')):ET.parse(D/name)
# H final recaps: inspect actual slide DOM and the shared-photo controls.
if args.final:
 assert 'project-brief' not in concepts and len(concepts)==55
 h53=concepts['workflow']
 assert len(re.findall(r'data-review-node="[^"]+"',h53))==5
 assert len(re.findall(r'data-question-node="[^"]+"',h53))==4
 assert h53.count('marker-end="url(#h55-arrow)"')==4
 assert 'Test 점수로 모델과 기준을 반복 선택하지 않습니다' in h53
 h54=concepts['project-iterate']
 assert len(re.findall(r'class="h55-compare"',h54))==3
 assert set(re.findall(r'data-h-review-resolution="(\d+)"',h54))=={'240','24'}
 assert '실제 모델의 실패 결과가 아닙니다' in h54
 h55=concepts['project-check']
 assert set(re.findall(r'data-review-answer="([^"]+)"',h55))=={'pixel','feature','learn','evaluate'}
 assert 'Recall = 18 / 20 = 90%' in h55 and 'Loss 9 → 0.36' in h55
 for k in ['workflow','project-iterate','project-check']:
  assert 'vision_task_apple_reference.jpg' in concepts[k]
 source_js=(D/'approved_h.js').read_text()
 assert 'source.src=\'assets/vision_task_apple_reference.jpg\'' in source_js
 assert 'ctx.drawImage(source,300,85,450,450,0,0,size,size)' in source_js
 css=(D/'approved_h.css').read_text()
 assert '.h55-hypotheses' in css and '.h55-answers' in css
 assert 'approved_h.js' in (D/'vision_ai_course.html').read_text()
print(('APPROVED55_FINAL_CONTRACT_PASS' if args.final else 'APPROVED55_STAGED_CONTRACT_PASS'),total,'slides; 120 minutes; source/DOM/outline and independent numeric checks')
