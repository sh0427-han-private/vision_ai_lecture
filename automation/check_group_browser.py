"""Capture actual planned-group slides in Chromium at both required resolutions.

This checks observable layout/assets, not semantic Figure quality. An independent
Reviewer must still inspect each capture. No screenshot is a classroom rehearsal.
"""
import argparse,json,os,sys,subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_visual_slides import inspect_slide

parser=argparse.ArgumentParser()
parser.add_argument('--group',required=True,choices=list('ABCDEFGH'))
parser.add_argument('--out',type=Path,required=True)
parser.add_argument('--base',default=os.getenv('AUDIT_BASE_URL','http://127.0.0.1:8766'))
args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
plan=json.loads((ROOT/'planning/approved55.json').read_text())
manifest=json.loads((ROOT/'docs/two_hour_manifest.json').read_text())
locations={entry['concept']:(deck,entry['slide']) for deck,entries in manifest['decks'].items() for entry in entries}
targets=[p for p in plan if p['group']==args.group]
report={'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'group':args.group,'screens':[],'page_errors':[]}
with sync_playwright()as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for w,h in[(1920,1080),(1366,768)]:
  page=browser.new_page(viewport={'width':w,'height':h})
  page.on('pageerror',lambda e:report['page_errors'].append(str(e)))
  deck0=locations[targets[0]['concept']][0]
  page.goto(f'{args.base}/{deck0}.html',wait_until='load')
  page.evaluate('document.fonts.ready')
  for target in targets:
   deck,number=locations[target['concept']]
   if not page.url.split('#')[0].endswith(deck+'.html'):page.goto(f'{args.base}/{deck}.html')
   page.evaluate('(n)=>location.hash="slide-"+n',number)
   page.wait_for_function('(c)=>document.querySelector(".slide.active")?.dataset.concept===c',arg=target['concept'])
   page.wait_for_timeout(160)
   info=inspect_slide(page)
   info.update({'concept':target['concept'],'plan':target['plan'],'viewport':f'{w}x{h}'})
   info['file']=f'{w}-{target["concept"]}.png'
   page.screenshot(path=str(args.out/info['file']),animations='disabled')
   report['screens'].append(info)
  page.close()
 browser.close()
issues=[(x['concept'],x['viewport'])for x in report['screens']if x['contentBottomOverflow']>6 or x['contentRightOverflow']>6 or x['browserHorizontalOverflow']>1 or x['fitScale']<.9 or x['overlaps'] or any(not i['loaded']and i['visible']for i in x['images'])]
report['layout_issues']=issues
(args.out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'screens':len(report['screens']),'layout_issues':issues,'page_errors':report['page_errors'],'minimum_fit':min(x['fitScale']for x in report['screens'])},ensure_ascii=False))
assert not issues and not report['page_errors'], 'Inspect report and actual images; fix before independent review'
