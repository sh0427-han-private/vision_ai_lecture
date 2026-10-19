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
assert sum(x['minutes'] for x in m['blocks'])==m['teaching_minutes']==120
assert m['discussion_minutes']==0
assert m['teaching_minutes']+m['discussion_minutes']==120
assert [x['global'] for x in items]==list(range(1,59))
slides={}; concepts={}
for deck,count in [('intro',13),('vision_ai_course',45)]:
 text=(D/(deck+'.html')).read_text()
 ss=re.findall(r'<section\b[^>]*class="slide[^\"]*"[^>]*>.*?</section>',text,re.S)
 assert len(ss)==count,(deck,len(ss))
 assert text.count('class="slide active"')==1
 assert re.findall(r'lecture_outline.js\?v=([^\"]+)',text)==['approved-ab-20261019-1']
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
 # The user's requested ORIGINAL zebra CNN Figure is restored with a local fallback.
 remote_images=re.findall(r'<img[^>]+src="(https?://[^"]+)"',text)
 assert len(remote_images)<=2,(deck,remote_images)
 if remote_images:
  assert deck=='vision_ai_course' and all('developersbreach.com/wp-content/uploads/2020/08/cnn_banner.png' in u for u in remote_images)
  assert 'lf-zebra-fallback' in text and 'lf-no-external' in text
  assert 'Swapna K E' in text
 assert not re.search(r'VGG-16|BatchNorm|γ|β|Grad-CAM|다음 장|기존 숫자',text),'Removed advanced topic or stale transition'
# Prerequisites are executable constraints, not just comments in a teaching plan.
seq=[x['concept'] for x in m['decks']['vision_ai_course']]
for before,after in [('task','rules'),('rules','rules-image'),('rules-image','model-choice'),('model-choice','task-model-data'),('task-model-data','perceptron'),('perceptron','and-rule'),('and-rule','and-gate'),('and-gate','xor-rule'),('xor-rule','xor-gate'),('xor-gate','relu'),('relu','nonlinear'),('nonlinear','cnn-overview'),('cnn-overview','cnn-why'),('cnn-why','kernel'),('kernel','feature-map'),('feature-map','sharing'),('sharing','channels'),('channels','stride'),('stride','padding'),('padding','pool'),('pool','actual-map'),('actual-map','backbone'),('backbone','dataset'),('dataset','split'),('split','leakage'),('leakage','augment'),('augment','learn'),('learn','loss'),('loss','cnn-training'),('cnn-training','infer'),('infer','transfer'),('transfer','cnn-learning-paths'),('cnn-learning-paths','training-log'),('training-log','overfit'),('overfit','threshold'),('threshold','confusion'),('confusion','imbalance'),('imbalance','metrics'),('metrics','iou'),('iou','workflow'),('workflow','project-brief'),('project-brief','project-run'),('project-run','project-iterate'),('project-iterate','project-check')]:
 assert seq.index(before)<seq.index(after),(before,after)
assert not {'affine-net','affine-collapse','xor-net'} & set(seq)
# Every slide must belong to one timed block; no omitted or duplicated material.
for deck,entries in m['decks'].items():
 covered=[n for block in m['blocks'] if block['deck']==deck for n in range(block['start'],block['end']+1)]
 assert covered==list(range(1,len(entries)+1)),(deck,covered)
assert [block['minutes'] for block in m['blocks']]==[14,10,10,18,30,10,14,9,5]
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
assert 'perceptron_one_weight_ko.svg' in concepts['perceptron']
assert all(('data-param="'+name+'"') in concepts['and-gate'] for name in ['w','b'])
assert all(('data-param="'+name+'"') in concepts['xor-gate'] for name in ['w1','b1','w2','b2'])
assert 'data-gate-mode="nonlinear"' in concepts['xor-gate'] and 'data-gate-mode="linear"' in concepts['xor-gate']
assert '역전파(Backpropagation)' in concepts['loss']
assert '지도학습(Supervised Learning)' in concepts['rules-image']
assert '2 Epoch = 6 Step' in concepts['training-log']
assert '80%' in concepts['imbalance'] and '0%' in concepts['imbalance']
assert '실제 불량 확률을 보장하지 않습니다' in concepts['threshold']
assert 'Label도 함께 바꿉니다' in concepts['augment']
assert 'Train에서만' in concepts['augment']
assert 'mAP' in concepts['iou']
assert '실제 모델을 실행한 결과는 아닙니다' in concepts['project-run']
assert 'Validation' in concepts['project-run'] and 'Test' in concepts['project-run']
assert 'Test를 반복 선택에 쓰지 않고' in concepts['project-iterate']
assert 'data-grayscale-lesson' in concepts['gray'] and 'data-rgb-lesson' in concepts['rgb']
assert '960×540' in concepts['resolution'] and '1920' not in concepts['resolution']
assert '갈색 반점 유무' in concepts['relevant-change']
for deck in ['intro','vision_ai_course','ai_basics','vision_ai']:
 text=(D/(deck+'.html')).read_text()
 assert not re.search(r'<a\b[^>]*>\s*(?:<svg|<img)',text),'Image must not open original'
 assert 'cursor:zoom' not in text
for a in ['perceptron_gate_structure_ko','and_xor_gate_geometry_ko','xor_multilayer_gates_ko']:
 ET.parse(D/'assets/lesson'/f'{a}.svg')
assert [x['concept'] for x in m['decks']['intro']] == ["start","ai-ml-dl-cv","vision-value","photo-numbers","gray","rgb","hwc","video-frames","resolution","lighting","transform","diversity","relevant-change"]
assert 'Frame 30' in concepts['video-frames'] and '30fps' in concepts['video-frames']
assert 'T × H × W × 3' in concepts['video-frames']
print('TWO_HOUR_QA_PASSED: staged approved group A, 58 slides, 120 teaching minutes without a Q&A block, principles-first prerequisites, shared numeric examples and local assets')

# Open feedback paths must not render as a solid filled blob.
root=ET.parse(D/'assets/lesson/context_cnn_training.svg').getroot()
feedback=root.find(".//{http://www.w3.org/2000/svg}path[@d='M1060 320C1060 440 375 440 375 320']")
assert feedback is not None and feedback.get('fill')=='none'

# Why/tasks additions and teaching figure must stay attached to their intended slides.
assert set(['vision-value','ai-ml-dl-cv','video-frames']).issubset(concepts)
assert set(['model-choice','task-model-data']).issubset(concepts)
assert seq.index('task-model-data') < seq.index('perceptron')
assert 'vision_motivation.css?v=why-20261019-1' in (D/'intro.html').read_text()
assert 'vision_motivation.css?v=why-20261019-1' in (D/'vision_ai_course.html').read_text()
assert 'lf-training-story' in concepts['cnn-training'] and 'Kernel + Head Weight 갱신' in concepts['cnn-training']
new_diagram=D/'assets/lesson/lecture_cnn_training_feedback_ko.svg'
assert ET.parse(new_diagram).getroot().tag=='{http://www.w3.org/2000/svg}svg'
for required in ['Task Head','Feature Map','Gradient','Optimizer','Loss']:
 assert required in new_diagram.read_text(),required
print('WHY_TASKS_CNN_QA_PASSED: goals, model+label decision, visual training figure')

# Refinement-specific educational assertions.
assert 'Anomaly Detection' not in concepts['task-model-data']
assert 'b55-label-table' in concepts['task-model-data']
assert 'cnn_banner.png' in concepts['cnn-overview'] and 'lf-zebra-fallback' in concepts['cnn-overview']
assert 'lf-kernel-result' in concepts['kernel']
assert 'lf-pad-shared' in concepts['padding'] and '3×3 → 1×1' in concepts['padding'] and '3×3 → 3×3' in concepts['padding']
assert '사용 이유:' in concepts['pool'] and '4×4(16칸) → 2×2(4칸)' in concepts['pool']
assert 'lf-augment-grid' in concepts['augment'] and 'lf-simple-photo-grid' not in concepts['augment']
assert 'lf-transfer-flow' in concepts['transfer'] and 'Freeze' in concepts['transfer'] and 'Classification Head' in concepts['transfer']
print('LECTURE_REFINEMENT_QA_PASSED: original CNN architecture, AND/XOR split, padding and head-only transfer')

# Gate interactive assets must be local, versioned, and wired to their slide controls.
course_page=(D/'vision_ai_course.html').read_text()
assert 'interactive_gates.js?v=20261019-rotate-w-3' in course_page
assert 'interactive_gates.css?v=20261019-rotate-w-3' in course_page
for name in ['interactive_gates.js','interactive_gates.css']:
 assert (D/name).is_file(),name
assert 'data-gate-lab="and"' in concepts['and-gate'] and 'data-gate-reset' in concepts['and-gate']
assert 'data-gate-lab="xor"' in concepts['xor-gate'] and 'data-gate-reset' in concepts['xor-gate']
assert 'x₂=−Wx₁−b' in concepts['and-gate']
assert '비선형' in concepts['xor-gate']
print('GATE_INTERACTIVE_QA_PASSED: 2 AND sliders, 4 XOR sliders, linear-to-nonlinear toggle, 120m all-teaching schedule')

# One shared weight + bias per layer, no neuron-specific w11/w12 UI.
assert concepts['and-gate'].count('data-param=')==2
assert concepts['xor-gate'].count('data-param=')==4
assert '뉴런 A' not in concepts['xor-gate'] and 'w₁₁' not in concepts['xor-gate']
assert '|t|' in concepts['xor-gate'] and 'ReLU' in concepts['xor-gate']
assert 'data-gate-stage' in concepts['xor-gate']
assert 'AI 판정' in concepts['xor-gate'] and '정답' in concepts['xor-gate']
print('GATE_SIMPLIFICATION_QA_PASSED: W/B per layer, linear boundary then ReLU-based nonlinearity')

# Regression for slope/offset geometry, not only moving a fixed-slope line.
assert 'z=Wx₁+1·x₂+b' in concepts['and-gate']
assert (('기울기 −W' in concepts['and-gate'] and 'y절편 −b' in concepts['and-gate']) or ('기울기(−W)' in concepts['and-gate'] and 'y절편(−b)' in concepts['and-gate']))
assert 'z=W₂t+1·x₁+b₂' in concepts['xor-gate']
assert 'x₁ Weight=1 고정' in concepts['xor-gate']
js_source=(D/'interactive_gates.js').read_text()
assert '[values.w,1,values.b]' in js_source
assert '[1+values.w1*values.w2, values.w2, values.w2*values.b1+values.b2]' in js_source
assert 'clippedLine' in js_source
print('GATE_ROTATION_QA_PASSED: W rotates effective linear boundary, b translates, XOR nonlinear contours clipped')

assert 'cnn_banner.png' in concepts['transfer']
assert '완전 연결' in concepts['cnn-why'] and 'Kernel을 여러 위치에서 공유' in concepts['cnn-why']
assert 'zebra_feature_photo.png' in concepts['cnn-why']
assert seq.index('cnn-why') == seq.index('cnn-overview') + 1

# Logic rules must precede their Perceptron and interactive boundary demonstrations.
assert seq.index('perceptron') < seq.index('and-rule') < seq.index('and-gate')
assert seq.index('and-gate') < seq.index('xor-rule') < seq.index('xor-gate') < seq.index('relu')
for concept, outputs in [('and-rule',[0,0,0,1]),('xor-rule',[0,1,1,0])]:
 slide=concepts[concept]
 assert slide.count('<article class="gb-example') == 4,(concept,'four visual truth table cases')
 assert [int(x) for x in re.findall(r'<strong>([01])</strong><small>(?:켜짐|꺼짐)</small>',slide)] == outputs,concept
 assert 'gb-examples' in slide and 'gb-rule' in slide
assert '단일 퍼셉트론' in concepts['and-rule']
assert '직선 하나로 분리할 수 없습니다' in concepts['xor-rule']
assert (D/'gate_basics.css').is_file()
assert 'gate_basics.css?v=gate-rule-20261019-1' in (D/'vision_ai_course.html').read_text()
print('GATE_RULES_QA_PASSED: AND/XOR operation explained before demonstrations')

# One neuron can have two input-connection weights; tied weights are a special AND case.
p=concepts['perceptron'];a=concepts['and-gate'];x=concepts['xor-gate']
assert 'z = W(x₁ + x₂) + b' in p
assert p.count('<div class="pw-equation pw-equation--') == 1 and '두 입력에 공통 Weight W 적용' in p
assert '쉬운 예시' in p and '입력별 여러 가중치를 묶어' in p
assert 'w₂=1로 고정' in a and 'z=Wx₁+1·x₂+b' in a
assert 'Weight는 1로 고정' in x and '각 층에서 Weight 하나만 조절' in x
assert (D/'perceptron_weights_clarity.css').is_file()
assert 'perceptron_weights_clarity.css?v=one-w-20261019-2' in (D/'vision_ai_course.html').read_text()
print('PERCEPTRON_INPUT_WEIGHTS_QA_PASSED: two input weights/one neuron, tied-weight AND, fixed-coefficient rotating lab')

# A separate beginner diagram uses one shared W and one Bias, not two visible w1/w2 terms.
assert 'w₁x₁ + w₂x₂' not in concepts['perceptron']
assert 'perceptron_one_weight_ko.svg?v=one-w-20261019-1' in concepts['perceptron']
import xml.etree.ElementTree as _Xml
pict=_Xml.parse(D/'assets/lesson/perceptron_one_weight_ko.svg').getroot()
pict_text=''.join(pict.itertext())
assert 'z = W(x₁ + x₂) + b' in pict_text
assert 'w₁' not in pict_text and 'w₂' not in pict_text
# Common frozen CNN features -> labeled classifier OR unlabeled clusters is downstream-stage comparison.
su=concepts['cnn-learning-paths']
for keyword in ['Feature Extractor','Freeze','지도학습','비지도학습','Label','Classification Head','Clustering','K-means','그룹 A / B','학습 목표','CNN 특징 추출기 자체도 다른 방식으로 학습']:
 assert keyword in su,keyword
assert su.count('class="su-path su-path--') == 2
assert (D/'supervised_unsupervised_cnn.css').is_file()
assert 'supervised_unsupervised_cnn.css?v=cnn-paths-20261019-1' in course_page
assert seq.index('transfer')+1==seq.index('cnn-learning-paths')
print('CNN_SUPERVISION_QA_PASSED: 58-slide course with same frozen features, labeled classification vs unlabeled clustering')

# Intro13 + Course45, no dedicated image preprocessing slide.
assert 'preprocess' not in seq and 'preprocess' not in concepts
assert seq.index('leakage') + 1 == seq.index('augment')
assert seq.index('augment') + 1 == seq.index('learn')
assert '데이터 · 독립 분할과 증강' in [block['name'] for block in m['blocks']]
print('PREPROCESSING_REMOVAL_QA_PASSED: 58 slides, dataset→split→leakage→augmentation→training')

# Rule-based arithmetic and image-based learning must occupy two DISTINCT slides.
ar=concepts['rules'];vision=concepts['rules-image']
# PR #113 merged Python add(a,b) and labeled-image figures in main.
assert '규칙 기반' in ar and 'rl-python-figure' in ar
assert ar.count('class="rl-math-case"')==2
assert 'add(1, 1)' in ar and 'add(2, 1)' in ar
assert 'return</span> a + b' in ar
assert '데이터 학습은 필요하지 않습니다' in ar
assert vision.count('class="rl-pane rl-pane--')==2
assert vision.count('<figure class="rl-photo-card')==6
assert vision.count('vision_task_apple_reference.jpg')==4
assert vision.count('apple_studio_preview.png')==2
assert all(vision.count('<b>'+k+'</b>')==2 for k in ['D-L','D-D','N-D'])
assert '갈색 Pixel 수 ≥ k ?' in vision and '지도학습(Supervised Learning)' in vision
assert all(x in vision for x in ['Model M','b55-training','b55-inference','b55-bottom-three','b55-prediction','실제 결과 미측정','Validation / Test'])
assert (D/'b_approved_figure.css').is_file()
assert 'b_approved_figure.css?v=approved-b-20261019-1' in (D/'vision_ai_course.html').read_text()
assert 'rules_vs_learning.css?v=python-rule-label-training-20261019-1' in (D/'vision_ai_course.html').read_text()
assert seq.index('rules')+1==seq.index('rules-image')
assert seq.index('rules-image')+1==seq.index('model-choice')
assert 'vision-evolution' not in concepts
assert concepts['model-choice'].count('class="b55-gate"')==3
assert '사과 객체 인식 ≠ 결함 판정' in concepts['model-choice']
assert all(x in concepts['task-model-data'] for x in ['Class: 불량','Box + Class: 불량','Pixel Mask','Box만 표시한 Label'])
assert 'b55-tasks' in concepts['task'] and '정답(GT)' in concepts['task']
print('RULE_VS_LEARNING_QA_PASSED: Python arithmetic, GT, Model M, independent validation and label costs')
