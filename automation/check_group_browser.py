"""Capture actual planned-group slides in Chromium at both required resolutions.

This checks observable layout/assets, not semantic Figure quality. An independent
Reviewer must still inspect each capture. No screenshot is a classroom rehearsal.
"""
import argparse,json,os,sys,subprocess
from PIL import Image, ImageChops
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
 browser=p.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
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
   # P54 image.onload is asynchronous: never capture incomplete raster canvases.
   if target['concept']=='project-iterate':
    try:
     page.wait_for_function("""() => {
       const nodes=[...document.querySelectorAll(
         '.slide.active canvas[data-h-review-resolution]')];
       if(nodes.length!==2)return false;
       return nodes.every(c=>{
         const size=Number(c.dataset.hReviewResolution);
         if(c.dataset.ready!=='true'||![24,240].includes(size)||
            c.width!==size||c.height!==size)return false;
         const px=c.getContext('2d').getImageData(0,0,size,size).data;
         let opaque=0,nonuniform=0;
         const first=[px[0],px[1],px[2]];
         for(let i=0;i<px.length;i+=4){
           if(px[i+3]===255)opaque++;
           if(px[i]!==first[0]||px[i+1]!==first[1]||
              px[i+2]!==first[2])nonuniform++;
         }
         return opaque===size*size&&nonuniform>size;
       });
     }""",timeout=20000)
    except Exception as exc:
     report.setdefault('canvas_errors',[]).append({
      'concept':target['concept'],'viewport':f'{w}x{h}',
      'reason':str(exc)[:500]})
     continue  # No misleading screenshot when either canvas is still blank.
   page.wait_for_timeout(160)
   info=inspect_slide(page)
   if target['concept']=='project-iterate':
    # The subject photograph/ROI is fixed; a true background-only pair must
    # share the same clipping geometry and subject pixels, but differ outside.
    svgs=page.locator('.slide.active svg[data-h-background-variant]')
    assert svgs.count()==2,'expected two controlled background composites'
    metas=svgs.evaluate_all("""nodes=>nodes.map(s=>({
      kind:s.dataset.hBackgroundVariant,
      original:s.querySelector('image')?.getAttribute('href'),
      crop:s.querySelector('image')?.getAttribute('width')+'x'+
           s.querySelector('image')?.getAttribute('height'),
      mask:s.querySelector('clipPath path')?.getAttribute('d'),
      roi:s.querySelector('circle')?.outerHTML
    }))""")
    assert [x['kind'] for x in metas]==['matte','grid'],metas
    assert metas[0]['original']==metas[1]['original']==(
     'assets/vision_task_apple_reference.jpg')
    assert metas[0]['crop']==metas[1]['crop']=='960x640'
    assert metas[0]['mask']==metas[1]['mask']
    assert metas[0]['roi']==metas[1]['roi']
    images=[]
    for variant in ['matte','grid']:
     path=args.out/f'{w}-background-{variant}.png'
     svgs.nth(len(images)).screenshot(path=str(path))
     images.append(Image.open(path).convert('RGB'))
    a,b=images
    assert a.size==b.size and min(a.size)>=80,a.size
    fw,fh=a.size
    def area(cx,cy,r=.045):
     x=int(fw*cx);y=int(fh*cy);dx=int(fw*r);dy=int(fh*r)
     return (x-dx,y-dy,x+dx,y+dy)
    # In the subject and annotated defect, both rendered pixel regions match.
    roi_area=area((596-300)/450,(226-85)/450)
    apple_area=area((525-300)/450,(310-85)/450)
    assert ImageChops.difference(
     a.crop(roi_area),b.crop(roi_area)).getbbox() is None,'ROI changed'
    assert ImageChops.difference(
     a.crop(apple_area),b.crop(apple_area)).getbbox() is None,'apple changed'
    # Top-left exterior has actual, not border-only, altered surface pixels.
    diff=ImageChops.difference(a.crop((0,0,int(fw*.2),int(fh*.2))),
                               b.crop((0,0,int(fw*.2),int(fh*.2))))
    diff_pixels=sum(1 for px in diff.getdata() if max(px)>8)
    total=diff.width*diff.height
    assert diff_pixels>total*.015,(diff_pixels,total)
    info['background_checks']={
     'photo':metas[0]['original'],'roi_equal':True,'apple_equal':True,
     'outside_changed_pixels':diff_pixels,'outside_sample_pixels':total,
     'composites':['matte','grid']}
   if target['concept']=='project-iterate':
    info['canvas_checks']=page.locator(
     '.slide.active canvas[data-h-review-resolution]').evaluate_all(
     """nodes=>nodes.map(c=>{
       const p=c.getContext('2d').getImageData(0,0,c.width,c.height).data;
       let opaque=0;
       for(let i=3;i<p.length;i+=4)if(p[i]===255)opaque++;
       return {size:+c.dataset.hReviewResolution,width:c.width,
               height:c.height,ready:c.dataset.ready,opaque_pixels:opaque};
     })""")
   info.update({'concept':target['concept'],'plan':target['plan'],'viewport':f'{w}x{h}'})
   info['file']=f'{w}-{target["concept"]}.png'
   page.screenshot(path=str(args.out/info['file']),animations='disabled')
   report['screens'].append(info)
  page.close()
 browser.close()
issues=[(x['concept'],x['viewport'])for x in report['screens']if x['contentBottomOverflow']>6 or x['contentRightOverflow']>6 or x['browserHorizontalOverflow']>1 or x['fitScale']<.9 or x['overlaps'] or any(not i['loaded']and i['visible']for i in x['images']) or any(not i['loaded']for i in x['svgImages'])]
report['layout_issues']=issues
(args.out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'screens':len(report['screens']),'layout_issues':issues,'page_errors':report['page_errors'],'minimum_fit':min((x['fitScale']for x in report['screens']),default=None),'canvas_errors':report.get('canvas_errors',[])},ensure_ascii=False))
assert len(report['screens'])==len(targets)*2 and not report.get('canvas_errors') and not issues and not report['page_errors'], 'Inspect report and actual images; fix before independent review'
