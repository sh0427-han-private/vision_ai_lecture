"""Verify the published 120-minute curriculum, real HTML arrays and prerequisites.
The historical individual decks retain their separate figure/math checks.
"""
from pathlib import Path
import re,json,html,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs'
m=json.loads((D/'two_hour_manifest.json').read_text())
outline=json.loads((D/'lecture_outline.js').read_text().split(' = ',1)[1].strip().rstrip(';'))
items=[x for g in outline['groups'] for x in g['items']]
assert m['duration_minutes']==120
assert sum(x['minutes'] for x in m['blocks'])==m['teaching_minutes']==110
assert m['teaching_minutes']+m['discussion_minutes']==120
assert [x['global'] for x in items]==list(range(1,47))
slides={}; concepts={}
for deck,count in [('intro',11),('vision_ai_course',35)]:
 text=(D/(deck+'.html')).read_text()
 ss=re.findall(r'<section\b[^>]*class="slide[^\"]*"[^>]*>.*?</section>',text,re.S)
 assert len(ss)==count,(deck,len(ss))
 assert text.count('class="slide active"')==1
 assert re.findall(r'lecture_outline.js\?v=([^\"]+)',text)==['two-hour-20261018']
 slides[deck]=ss
 for n,s in enumerate(ss,1):
  c=re.search(r'data-concept="([^\"]+)"',s)[1];concepts[c]=s
  t=html.unescape(re.sub('<[^>]+>','',re.search(r'<h[12] class="slide-title[^\"]*">(.*?)</h[12]>',s,re.S)[1])).strip()
  assert m['decks'][deck][n-1]=={'slide':n,'title':t,'concept':c}
  assert any(x['page']==deck+'.html' and x['slide']==n and x['title']==t for x in items)
 for url in re.findall(r'(?:src|href)="([^\"]+)"',text):
  if url.startswith(('http:','https:','#','data:','mailto:')):continue
  path=url.split('?',1)[0].split('#',1)[0]
  if path:assert (D/path).is_file(),(deck,path)
 assert not re.search(r'<img[^>]+src="https?://',text),'Lecture figures must load locally'
 assert not re.search(r'VGG-16|BatchNorm|γ|β|Grad-CAM|다음 장|기존 숫자',text),'Removed advanced topic or stale transition'
# Prerequisites are executable constraints, not just comments in a teaching plan.
seq=[x['concept'] for x in m['decks']['vision_ai_course']]
for before,after in [('task','learn'),('learn','perceptron'),('perceptron','affine-net'),('affine-net','affine-collapse'),('and-xor','xor-net'),('xor-net','relu'),('relu','kernel'),('kernel','feature-map'),('feature-map','sharing'),('channels','actual-map'),('stride','cnn-overview'),('learn','cnn-training'),('backbone','transfer'),('split','overfit'),('threshold','confusion'),('confusion','metrics'),('metrics','iou')]:
 assert seq.index(before)<seq.index(after),(before,after)
def matrices(concept):
 s=concepts[concept]; result=[]
 for cols,body in re.findall(r'<div class="concept-matrix[^\"]*" style="--cols:(\d+)"[^>]*>(.*?)</div>',s,re.S):
  vals=[int(v) for v in re.findall(r'<span class="concept-cell[^\"]*">(−?-?\d+)</span>',body)]
  cols=int(cols);result.append([vals[y:y+cols] for y in range(0,len(vals),cols)])
 return result
A,K=matrices('kernel'); assert len(A)==5 and len(K)==3
M=[[sum(A[y+i][x+j]*K[i][j] for i in range(3) for j in range(3)) for x in range(3)] for y in range(3)]
assert M==[[-6,12,16],[-6,8,15],[-4,2,7]]
assert matrices('feature-map')==[A,K,M]
assert matrices('stride')==[M,[[M[y][x] for x in (0,2)] for y in (0,2)]]
orig,pad,result=matrices('padding')
assert pad==[[0]*5]+[[0]+row+[0] for row in orig]+[[0]*5]
assert result==[[sum(pad[y+i][x+j] for i in range(3) for j in range(3)) for x in range(3)] for y in range(3)]
pool,out=matrices('pool')
assert out==[[max(pool[2*y+i][2*x+j] for i in range(2) for j in range(2)) for x in range(2)] for y in range(2)]
assert round((.5*2-4)**2,2)==9 and round((1.7*2-4)**2,2)==.36
assert abs(.5-.1*(2*(.5*2-4)*2)-1.7)<1e-12
assert 'w=0.5' in concepts['loss'] and 'w=1.7' in concepts['loss']
assert '9,216' in concepts['sharing'] and 9*1024==9216
assert 'x₁ + 7x₂ + 3' in concepts['affine-collapse']
assert '입력층' in concepts['affine-net'] and '은닉층 2' in concepts['affine-net'] and 'y = z₁ + z₂' in concepts['affine-net']
assert 'perceptron_gate_structure_ko.svg' in concepts['perceptron']
assert 'x₁+x₂ = 1.4' in concepts['and-xor']
assert 'xor_multilayer_gates_ko.svg' in concepts['xor-net']
assert 'data-grayscale-lesson' in concepts['gray'] and 'data-rgb-lesson' in concepts['rgb']
assert '960×540' in concepts['resolution'] and '1920' not in concepts['resolution']
assert '균열 유무' in concepts['relevant-change']
for deck in ['intro','vision_ai_course','ai_basics','vision_ai']:
 text=(D/(deck+'.html')).read_text()
 assert not re.search(r'<a\b[^>]*>\s*(?:<svg|<img)',text),'Image must not open original'
 assert 'cursor:zoom' not in text
for a in ['perceptron_gate_structure_ko','and_xor_gate_geometry_ko','xor_multilayer_gates_ko']:
 ET.parse(D/'assets/lesson'/f'{a}.svg')
print('TWO_HOUR_QA_PASSED: 46 slides, 110+10 minutes, prerequisites, shared numeric examples, local assets and static figures')
