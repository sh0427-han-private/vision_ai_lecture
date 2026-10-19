"""Synchronize real slides with the approved sequence; retain staged legacy extras until merged.
Run after each Builder patch. Final mode rejects all extra/absent concepts.
"""
import argparse,json,re,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs'
parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');args=parser.parse_args()
plan=json.loads((ROOT/'planning/approved55.json').read_text());rank={p['concept']:i for i,p in enumerate(plan)}
parts={};pages={};extras={}
for deck in ['intro','vision_ai_course']:
 path=D/(deck+'.html');text=path.read_text();matches=list(re.finditer(r'<section\b[^>]*class="slide[^\"]*"[^>]*>.*?</section>',text,re.S))
 items=[];last=None
 for match in matches:
  c=re.search(r'data-concept="([^\"]+)"',match[0])[1]
  if c in rank:items.append((c,match[0]));last=c
  else:extras.setdefault(last,[]).append((c,match[0]))
 items.sort(key=lambda item:rank[item[0]])
 ordered=[]
 for c,body in items:
  ordered.append((c,body));ordered+=extras.pop(c,[])
 assert not extras,(deck,extras)
 if args.final:assert len(ordered)==(13 if deck=='intro' else 42)
 new=[];entries=[]
 for i,(c,body) in enumerate(ordered,1):
  body=body.replace('class="slide active"','class="slide"')
  if i==1:body=body.replace('class="slide"','class="slide active"',1)
  new.append(body)
  title=html.unescape(re.sub('<[^>]+>','',re.search(r'<h[12][^>]*class="slide-title[^\"]*"[^>]*>(.*?)</h[12]>',body,re.S)[1])).strip()
  entries.append({'slide':i,'title':title,'concept':c})
 text=text[:matches[0].start()].rstrip()+'\n'+'\n'.join(new)+'\n'+text[matches[-1].end():].lstrip()
 text=re.sub(r'lecture_outline.js\?v=[^\"]+','lecture_outline.js?v=approved55-20261019-1',text)
 path.write_text(text);pages[deck]=entries
m={'version':'approved55-20261019-1','duration_minutes':120,'teaching_minutes':120,'discussion_minutes':0,'decks':pages,'blocks':[]}
mins={'A':26,'B':10,'C':23,'D':22,'E':9,'F':15,'G':10,'H':5};names={'A':'Vision AI·이미지·영상 입력','B':'Task·규칙과 데이터 학습','C':'CNN 구조·뉴런·비선형성','D':'CNN 내부 연산','E':'데이터와 독립 분할','F':'Loss·CNN 학습·전이학습','G':'평가와 오류','H':'원리 회수'}
group_for={x['concept']:x['group'] for x in plan};group_for.update({'training-log':'F','project-brief':'H','project-run':'H'})
outline={'version':m['version'],'groups':[]};global_n=0
for deck,items in pages.items():
 for group in mins:
  entries=[x for x in items if group_for[x['concept']]==group]
  if not entries:continue
  numbers=[x['slide'] for x in entries];assert numbers==list(range(numbers[0],numbers[-1]+1)),(group,numbers)
  m['blocks'].append({'name':names[group],'deck':deck,'start':numbers[0],'end':numbers[-1],'minutes':mins[group]})
  links=[]
  for x in entries:global_n+=1;links.append({'page':deck+'.html','slide':x['slide'],'title':x['title'],'global':global_n})
  outline['groups'].append({'name':names[group],'items':links})
(D/'two_hour_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
(D/'lecture_outline.js').write_text('/* Approved 55-slide plan; '+('final' if args.final else 'actual staged')+' count '+str(global_n)+'. */\nwindow.LECTURE_OUTLINE = '+json.dumps(outline,ensure_ascii=False,indent=2)+';\n')
if args.final:assert global_n==55 and len({x['concept'] for items in pages.values() for x in items})==55
for legacy in D.glob('*.html'):
 text=legacy.read_text();updated=re.sub(r'lecture_outline.js\?v=[^\"]+','lecture_outline.js?v=approved55-20261019-1',text)
 if updated!=text:legacy.write_text(updated)
print('SYNC',global_n,'slides; 120 planned minutes; final=',args.final)
