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
  # Approved P15/P16: one executable Python function for both arithmetic inputs.
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('rules')}")
  assert page.locator('.slide.active .rl-math-case').count() == 2
  assert page.locator('.slide.active .rl-python-rule').count() == 1
  assert page.locator('.slide.active .rl-math-output').count() == 2
  assert page.locator('.slide.active .rl-join-paths').count() == 1
  assert page.locator('.slide.active .rl-split-paths').count() == 1
  python_code = page.locator('.slide.active .rl-python-code').inner_text()
  assert 'def add(a, b):' in python_code
  assert 'return a + b' in python_code
  scope = {}
  exec(python_code, scope)
  assert scope['add'](1, 1) == 2
  assert scope['add'](2, 1) == 3
  assert 'add(1, 1)' in page.locator('.slide.active').inner_text()
  assert 'add(2, 1)' in page.locator('.slide.active').inner_text()
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('rules-image')}")
  assert page.locator('.slide.active .rl-pane').count() == 2
  assert page.locator('.slide.active .rl-photo-card').count() == 6
  assert page.locator('.slide.active .b55-dark-photo').count() == 4
  assert page.locator('.slide.active .b55-rule-card').count() == 1
  assert '갈색 Pixel 수 ≥ k ?' in page.locator('.slide.active .b55-rule-card').inner_text()
  assert '그림자?' in page.locator('.slide.active .b55-rule-card').inner_text()
  assert page.locator('.slide.active .b55-ml-path .b55-step').count() == 6
  assert '정답 사진 + Label' in page.locator('.slide.active').inner_text()
  assert '지도학습(Supervised Learning)' in page.locator('.slide.active').inner_text()
  assert '독립' in page.locator('.slide.active').inner_text()
  assert '미측정' in page.locator('.slide.active .b55-prediction').inner_text()
  page.wait_for_function("""() => {
   const images = [...document.querySelectorAll('.slide.active .rl-photo-card img')];
   return images.length === 6 &&
     images.every(img => img.complete && img.naturalWidth > 0);
  }""", timeout=15000)
  assert page.locator('.slide.active .rl-photo-card img').count() == 6
  # P14-P18: GT annotations, shared model and label preparation cost.
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('task')}")
  assert page.locator('.slide.active .b55-tasks article').count()==3
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('rules-image')}")
  assert page.locator('.slide.active .b55-model').count()==1
  assert page.locator('.slide.active .b55-training').count()==1
  assert page.locator('.slide.active .b55-inference').count()==1
  assert page.locator('.slide.active .b55-prediction').count()==1
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('model-choice')}")
  assert page.locator('.slide.active .b55-gate').count()==3
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('task-model-data')}")
  assert page.locator('.slide.active .b55-label-row').count()==3
  # Same frozen pretrained CNN output can feed a supervised head or an
  # unlabeled feature clustering stage; these are not equivalent class labels.
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('cnn-learning-paths')}")
  page.wait_for_selector('.slide.active .su-figure')
  assert page.locator('.slide.active .su-stage--backbone').count()==1
  assert page.locator('.slide.active .su-path').count()==2
  assert '정상 / 불량' in page.locator('.slide.active .su-path--sup').inner_text()
  assert '그룹 A / B' in page.locator('.slide.active .su-path--un').inner_text()
  assert '학습 데이터의 Label과 학습 목표' in page.locator('.slide.active').inner_text()
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('perceptron')}")
  assert page.locator('.slide.active img[src*="perceptron_approved_c.svg"]').count()==1
  # General one-neuron perceptron first; AND logic rule is its application.
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('perceptron')}")
  assert '하나의 W와 b로 판정' in page.locator('.slide.active').inner_text()
  assert 'z=W(x₁+x₂)+b' in page.locator('.slide.active .c55-neuron-note').inner_text()
  assert '일반 뉴런은 입력마다 다른 Weight 가능' in page.locator('.slide.active .c55-neuron-note').inner_text()
  # Concept explanation before slider labs (the four cases are a visual truth table).
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('and-rule')}")
  assert page.locator('.slide.active .gb-example').count()==4
  assert '모두 1' in page.locator('.slide.active').inner_text()
  assert 'z=0.5(x₁+x₂)−0.7' in page.locator('.slide.active').inner_text()
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('xor-rule')}")
  assert page.locator('.slide.active .gb-example').count()==4
  assert '서로 다를 때' in page.locator('.slide.active').inner_text()
  assert '직선 하나로 0과 1을 모두 분리할 수 없습니다' in page.locator('.slide.active').inner_text()
  # Course 7: W actually ROTATES the line, while b translates it.
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('and-gate')}")
  page.wait_for_selector('[data-gate-lab="and"][data-ready="true"]')
  assert page.locator('[data-gate-lab="and"] input[type="range"]').count()==2
  assert 'AI 판정 4 / 4개 일치' in page.locator('[data-gate-lab="and"] [data-gate-summary]').inner_text()
  line_sel='[data-gate-lab="and"] [data-gate-svg] line[aria-label="최종 Wx+b 직선 판정 경계"]'
  def line_gradient():
   x1,y1,x2,y2=page.locator(line_sel).evaluate("(e)=>['x1','y1','x2','y2'].map(k=>Number(e.getAttribute(k)))")
   return (y2-y1)/(x2-x1)
  slope_start=line_gradient()
  page.locator('[data-gate-lab="and"] [data-param="w"]').evaluate("(el)=>{el.value='0.4';el.dispatchEvent(new Event('input',{bubbles:true}));}")
  slope_rotated=line_gradient()
  assert abs(slope_start-slope_rotated)>0.1,(slope_start,slope_rotated)
  page.click('[data-gate-lab="and"] [data-gate-reset]')
  assert 'AI 판정 4 / 4개 일치' in page.locator('[data-gate-lab="and"] [data-gate-summary]').inner_text()
  slope_reset=line_gradient()
  page.locator('[data-gate-lab="and"] [data-param="b"]').evaluate("(el)=>{el.value='-0.5';el.dispatchEvent(new Event('input',{bubbles:true}));}")
  assert 'AI 판정 2 / 4개 일치' in page.locator('[data-gate-lab="and"] [data-gate-summary]').inner_text()
  assert abs(slope_reset-line_gradient())<1e-7,'b changed the slope instead of translating'
  page.click('[data-gate-lab="and"] [data-gate-reset]')
  assert 'AI 판정 4 / 4개 일치' in page.locator('[data-gate-lab="and"] [data-gate-summary]').inner_text()
  # Course 8: both W1 and W2 alter the final line's angle, nonlinear gives two edges.
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('xor-gate')}")
  page.wait_for_selector('[data-gate-lab="xor"][data-ready="true"]')
  assert page.locator('[data-gate-lab="xor"] input[type="range"]').count()==4
  assert 'AI 판정 3 / 4개 일치' in page.locator('[data-gate-lab="xor"] [data-gate-summary]').inner_text()
  assert page.locator('[data-gate-lab="xor"] [data-gate-mode="linear"]').get_attribute('aria-pressed')=='true'
  assert '직선 하나' in page.locator('[data-gate-lab="xor"] [data-gate-equation]').inner_text()
  assert page.locator('[data-gate-lab="xor"] .gl-outcome').count()==4
  assert '정답 0' in page.locator('[data-gate-lab="xor"] .gl-outcome').first.inner_text()
  assert 'AI 판정 1' in page.locator('[data-gate-lab="xor"] .gl-outcome').first.inner_text()
  xor_line='[data-gate-lab="xor"] [data-gate-svg] line[aria-label="최종 Wx+b 직선 판정 경계"]'
  def xor_gradient():
   x1,y1,x2,y2=page.locator(xor_line).evaluate("(e)=>['x1','y1','x2','y2'].map(k=>Number(e.getAttribute(k)))")
   return (y2-y1)/(x2-x1)
  initial_gradient=xor_gradient()
  page.locator('[data-gate-lab="xor"] [data-param="w1"]').evaluate("(el)=>{el.value='0.5';el.dispatchEvent(new Event('input',{bubbles:true}));}")
  assert abs(xor_gradient()-initial_gradient)>0.1,'XOR W1 did not rotate final line'
  page.click('[data-gate-lab="xor"] [data-gate-reset]')
  page.locator('[data-gate-lab="xor"] [data-param="w2"]').evaluate("(el)=>{el.value='-1.5';el.dispatchEvent(new Event('input',{bubbles:true}));}")
  assert abs(xor_gradient()-initial_gradient)>0.1,'XOR W2 did not rotate final line'
  page.click('[data-gate-lab="xor"] [data-gate-reset]')
  page.click('[data-gate-lab="xor"] [data-gate-mode="nonlinear"]')
  assert page.locator('[data-gate-lab="xor"] [data-gate-mode="nonlinear"]').get_attribute('aria-pressed')=='true'
  assert 'AI 판정 4 / 4개 일치' in page.locator('[data-gate-lab="xor"] [data-gate-summary]').inner_text()
  assert 'ReLU' in page.locator('[data-gate-lab="xor"] [data-gate-stage]').inner_text()
  assert page.locator('[data-gate-lab="xor"] [data-gate-svg] line[aria-label="최종 비선형 판정 경계"]').count()==2
  page.locator('[data-gate-lab="xor"] [data-param="w1"]').evaluate("(el)=>{el.value='0';el.dispatchEvent(new Event('input',{bubbles:true}));}")
  assert 'AI 판정 2 / 4개 일치' in page.locator('[data-gate-lab="xor"] [data-gate-summary]').inner_text()
  page.click('[data-gate-lab="xor"] [data-gate-reset]')
  assert page.locator('[data-gate-lab="xor"] [data-gate-mode="linear"]').get_attribute('aria-pressed')=='true'
  assert 'AI 판정 3 / 4개 일치' in page.locator('[data-gate-lab="xor"] [data-gate-summary]').inner_text()
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('padding')}")
  def shown_matrix(name):
   return page.locator(f'.slide.active [data-matrix-name="{name}"]').evaluate("g=>{const c=+g.dataset.cols,a=[...g.querySelectorAll('text[data-row]')].map(t=>+t.textContent);return Array.from({length:a.length/c},(_,i)=>a.slice(i*c,(i+1)*c));}")
  assert shown_matrix('padding-input')==[[1,2,3],[4,5,6],[7,8,9]]
  assert shown_matrix('padding-output')==[[12,21,16],[27,45,33],[24,39,28]]
  page.goto(f"{BASE}/vision_ai_course.html#slide-{number('transfer')}")
  assert page.locator('.zebra-transfer-legend article').count()==2
  # Staged build: P20 is local now; P45 will be replaced in F, which is not yet Verified.
  page.wait_for_selector('[data-concept="cnn-overview"] [data-cnn-architecture][data-ready="true"]',state='attached')
  assert page.locator('[data-concept="cnn-overview"] [data-cnn-architecture]').get_attribute('data-model-id')=='apple-cnn-1426'
  assert 'Head 교체' in page.locator('.slide.active').inner_text()
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
