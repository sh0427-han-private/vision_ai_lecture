"""Browser QA of the complete two-hour route, TOC, interactions and legacy URLs."""
from pathlib import Path
import os,json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
M=json.loads((ROOT/'docs/two_hour_manifest.json').read_text())
BASE=os.getenv('AUDIT_BASE_URL','http://127.0.0.1:8765')
OUT=ROOT/'visual_audit_output'
DECKS=[(k,len(v)) for k,v in M['decks'].items()]
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
  page.goto(BASE+'/index.html');position(page,'intro',1,11)
  assert page.locator('[data-slide-prev]').is_disabled()
  assert page.locator('#lecture-toc-drawer').get_attribute('aria-hidden')=='true'
  page.click('.lecture-toc-toggle')
  assert page.locator('.lecture-toc-link').count()==46
  toc=page.locator('.lecture-toc-sections');toc.hover(position={'x':100,'y':170})
  page.mouse.wheel(0,540)
  page.wait_for_function("()=>document.querySelector('.lecture-toc-sections').scrollTop>0")
  position(page,'intro',1,11)
  page.keyboard.press('PageDown');position(page,'intro',1,11)
  page.keyboard.press('Escape')
  assert page.locator('#lecture-toc-drawer').get_attribute('aria-hidden')=='true'
  # Open the containing chapter and use a real TOC link across pages.
  page.click('.lecture-toc-toggle')
  target=page.locator('.lecture-toc-link[href="vision_ai_course.html#slide-13"]')
  unit=target.locator('xpath=ancestor::details[1]')
  if unit.get_attribute('open') is None:unit.locator('summary').click()
  target.click();position(page,'vision_ai_course',13,35)
  assert page.locator('.slide.active').get_attribute('data-concept')=='kernel'
  assert page.locator('#lecture-toc-drawer').get_attribute('aria-hidden')=='true'
  # Training demonstration really follows the same step as the adjacent slide.
  page.goto(BASE+'/vision_ai_course.html#slide-3');position(page,'vision_ai_course',3,35)
  page.click('[data-train-step]')
  assert abs(float(page.locator('[data-weight]').inner_text())-1.7)<1e-6
  assert abs(float(page.locator('[data-loss]').inner_text())-.36)<1e-6
  page.click('[data-train-reset]')
  assert float(page.locator('[data-weight]').inner_text())==.5
  # Every current slide remains reachable in order through the normal controls.
  for deck,total in DECKS:
   page.goto(f'{BASE}/{deck}.html#slide-1');position(page,deck,1,total)
   for n in range(2,total+1):
    page.click('[data-slide-next]');position(page,deck,n,total)
   assert not page.locator('.slide.active a:has(img)').count()
  assert page.locator('[data-slide-next]').is_disabled()
  page.goto(BASE+'/intro.html#slide-11');page.click('[data-slide-next]')
  position(page,'vision_ai_course',1,35)
  page.click('[data-slide-prev]');position(page,'intro',11,11)
  page.goto(BASE+'/vision_ai_course.html?mode=core#slide-21');position(page,'vision_ai_course',21,35)
  assert 'mode=core' not in page.url
  page.click('header a.brand');position(page,'intro',1,11)
  assert not errors,errors
  page.screenshot(path=str(OUT/'two_hour_navigation.jpg'),type='jpeg',quality=85)
  browser.close()
 print('TWO_HOUR_NAV_QA_PASSED: 46 slides, TOC, legacy redirects, chapter boundary, real training update, no JS errors')
if __name__=='__main__':main()
