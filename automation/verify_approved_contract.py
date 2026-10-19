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
# Every local SVG actually referenced by the two decks parses successfully.
for name in re.findall(r'(?:src|href)="([^\"]+\.svg)(?:\?[^\"]*)?"',(D/'intro.html').read_text()+(D/'vision_ai_course.html').read_text()):
 if not name.startswith(('http:','https:','data:')):ET.parse(D/name)
print(('APPROVED55_FINAL_CONTRACT_PASS' if args.final else 'APPROVED55_STAGED_CONTRACT_PASS'),total,'slides; 120 minutes; source/DOM/outline and independent numeric checks')
