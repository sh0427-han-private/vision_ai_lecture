"""Browser QA of the complete two-hour route, TOC, interactions and legacy URLs."""
from pathlib import Path
import os,json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
M=json.loads((ROOT/'docs/two_hour_manifest.json').read_text())
BASE=os.getenv('AUDIT_BASE_URL','http://127.0.0.1:8765')
OUT=ROOT/'visual_audit_output'
DECKS=[(k,len(v)) for k,v in M['decks'].items()]
COURSE_TOTAL=len(M['decks']['vision_ai_course'])
TOTAL=sum(n for _,n in DECKS)
def number(concept):
 return next(e['slide'] for e in M['decks']['vision_ai_course'] if e['concept']==concept)
def position(page,deck,n,total):
 page.wait_for_url(f'**/{deck}.html*#slide-{n}')
 page.wait_for_function("n=>document.querySelector('[data-slide-current]')?.textContent.trim()===String(n)",arg=n)
 assert page.locator('.slide.active').count()==1
 assert page.locator('[data-slide-total]').inner_text()==str(total)
def main():
 OUT.mkdir(exist_ok=True)
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  page=browser.new_page(viewport={'width':1366,'height':768});errors=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  for deck,total in DECKS:
   page.goto(f'{BASE}/docs/{deck}.html?from=legacy#slide-3');position(page,deck,3,total)
   assert '/docs/' not in page.url and 'from=legacy' in page.url
  page.goto(BASE+'/index.html');position(page,'intro',1,DECKS[0][1])
  assert page.locator('[data-slide-prev]').is_disabled()
  assert page.locator('#lecture-toc-drawer').get_attribute('aria-hidden')=='true'
  page.click('.lecture-toc-toggle')
  assert page.locator('.lecture-toc-link').count()==TOTAL
  toc=page.locator('.lecture-toc-sections');toc.hover(position={'x':100,'y':170})
  page.mouse.wheel(0,540)
  page.wait_for_function("()=>document.querySelector('.lecture-toc-sections').scrollTop>0")
  position(page,'intro',1,DECKS[0][1])
  page.keyboard.press('PageDown');position(page,'intro',1,DECKS[0][1])
  page.keyboard.press('Escape')
  assert page.locator('#lecture-toc-drawer').get_attribute('aria-hidden')=='true'
  # Open the containing chapter and use a real TOC link across pages.
  page.click('.lecture-toc-toggle')
  kernel=number('kernel')
  target=page.locator(f'.lecture-toc-link[href="vision_ai_course.html#slide-{kernel}"]')
  unit=target.locator('xpath=ancestor::details[1]')
  if unit.get_attribute('open') is None:unit.locator('summary').click()
  target.click();position(page,'vision_ai_course',kernel,COURSE_TOTAL)
  assert page.locator('.slide.active').get_attribute('data-concept')=='kernel'
  assert page.locator('#lecture-toc-drawer').get_attribute('aria-hidden')=='true'
  for deck, total in DECKS:
   for n in range(1,total+1):
    page.click('.lecture-toc-toggle')
    link=page.locator(f'.lecture-toc-link[href="{deck}.html#slide-{n}"]')
    chapter=link.locator('xpath=ancestor::details[1]')
    if chapter.get_attribute('open') is None:chapter.locator('summary').click()
    link.click();position(page,deck,n,total)
  # The AND/XOR explanations are separate and the new diagrams are present.
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('and-gate')}")
  assert page.locator('.lf-gate-table').count()==1
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('xor-gate')}")
  assert page.locator('.lf-gate-table').count()==1
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('padding')}")
  assert page.locator('.lf-pad-shared .concept-matrix').count()==1
  assert page.locator('.lf-pad-result .concept-matrix').count()==2
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('transfer')}")
  assert page.locator('.lf-transfer-block').count()==4
  assert 'Freeze' in page.locator('.slide.active').inner_text()
  # Training demonstration really follows the same step as the adjacent slide.
  learn=number('learn')
  page.goto(f'{BASE}/vision_ai_course.html#slide-{learn}');position(page,'vision_ai_course',learn,COURSE_TOTAL)
  page.click('[data-train-step]')
  assert abs(float(page.locator('[data-weight]').inner_text())-1.7)<1e-6
  assert abs(float(page.locator('[data-loss]').inner_text())-.36)<1e-6
  page.click('[data-train-reset]')
  assert float(page.locator('[data-weight]').inner_text())==.5
  # Recompute the educational validation results when the learner changes threshold.
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('project-run')}")
  page.wait_for_selector('[data-project-evaluation][data-ready="true"]')
  for threshold,expected in [('0.5',[18,2,4,76]),('0.3',[20,0,30,50]),('0.7',[11,9,2,78])]:
   page.select_option('[data-project-threshold]',threshold)
   actual=[int(page.locator(f'[data-project-{key}]').inner_text()) for key in ['tp','fn','fp','tn']]
   assert actual==expected,(threshold,actual)
   for key, count in [("fn", expected[1]), ("fp", expected[2])]:
    assert page.locator(f"[data-project-{key}-bar]").evaluate("el => el.value") == count
    assert page.locator(f"[data-project-{key}-label]").inner_text() == f"{count}건"
   assert sum(actual)==100
   precision=100*expected[0]/(expected[0]+expected[2]);recall=100*expected[0]/20
   assert page.locator('[data-project-result]').inner_text()==f'Precision {precision:.1f}% · Recall {recall:.1f}%'
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('project-check')}")
  page.click('.project-answer summary')
  assert page.locator('.project-answer p').is_visible()
  assert 'Mask Label' in page.locator('.project-answer p').inner_text()
  # Every current slide remains reachable in order through the normal controls.
  for deck,total in DECKS:
   page.goto(f'{BASE}/{deck}.html#slide-1');position(page,deck,1,total)
   for n in range(2,total+1):
    page.click('[data-slide-next]');position(page,deck,n,total)
   assert not page.locator('.slide.active a:has(img)').count()
   for n in range(total-1,0,-1):
    page.click('[data-slide-prev]');position(page,deck,n,total)
   page.goto(f'{BASE}/{deck}.html#slide-{total}');position(page,deck,total,total)
  assert page.locator('[data-slide-next]').is_disabled()
  page.goto(f"{BASE}/intro.html#slide-{DECKS[0][1]}");page.click('[data-slide-next]')
  position(page,'vision_ai_course',1,COURSE_TOTAL)
  page.click('[data-slide-prev]');position(page,'intro',DECKS[0][1],DECKS[0][1])
  page.goto(BASE+'/vision_ai_course.html?mode=core#slide-21');position(page,'vision_ai_course',21,COURSE_TOTAL)
  assert 'mode=core' not in page.url
  page.click('header a.brand');position(page,'intro',1,DECKS[0][1])
  page.set_viewport_size({'width':390,'height':844})
  page.click('.lecture-toc-toggle')
  assert page.locator('#lecture-toc-drawer').get_attribute('aria-hidden')=='false'
  page.keyboard.press('Escape')
  assert page.locator('#lecture-toc-drawer').get_attribute('aria-hidden')=='true'
  page.locator('.slide.active .slide-title').click()
  page.keyboard.press('ArrowRight');position(page,'intro',2,DECKS[0][1])
  assert not errors,errors
  page.screenshot(path=str(OUT/'two_hour_navigation.jpg'),type='jpeg',quality=85)
  browser.close()
 print(f'TWO_HOUR_NAV_QA_PASSED: {TOTAL} slides, TOC, legacy redirects, chapter boundary, real training update, threshold recalculation, review answer, no JS errors')
if __name__=='__main__':main()
