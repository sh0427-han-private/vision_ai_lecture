"""Apply approved P53–55 after G PASS; absorb project-brief, keep 55 concepts."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]

def section(concept,body):return f'<section class="slide" data-concept="{concept}" data-level="basic"><div class="slide-inner two-hour h55">{body}</div></section>'
def photo(label='강의 시작의 같은 결함 사과'):
    return f'<svg viewBox="300 85 450 450" role="img" aria-label="{label}"><image href="assets/vision_task_apple_reference.jpg" width="960" height="640"/><circle cx="596" cy="226" r="39" fill="none" stroke="#16876f" stroke-width="4"/></svg>'

def workflow():
    b='<defs><marker id="h55-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#7195a3"/></marker></defs>'
    nodes=[('Pixel','H×W×3','RGB 숫자 배열'),('Task + Label','정상 / 불량','질문과 정답 정의'),('CNN','Kernel → Map','특징 → 분류 Head'),('Training','Loss ↓ · Weight 갱신','Train / Val 분리'),('Independent Eval','FN · FP 확인','고정 기준 · 독립 Test')]
    for i,(name,line,detail)in enumerate(nodes):
        x=10+i*242
        b+=f'<g data-review-node="{i+1}"><rect x="{x}" y="12" width="220" height="132" rx="4" fill="#f3f8f9" stroke="#9cbfc7"/><g text-anchor="middle" fill="#335e70"><text x="{x+110}" y="46" font-size="24" font-weight="750">{name}</text><text x="{x+110}" y="88" font-size="22">{line}</text><text x="{x+110}" y="121" font-size="20">{detail}</text></g></g>'
        if i<4:b+=f'<path d="M{x+220} 77H{x+239}" stroke="#7195a3" stroke-width="2.5" marker-end="url(#h55-arrow)"/>'
    # Questions connect to their relevant node; they are annotation lines, not feedback from Test.
    questions=[('무엇을 찾나?','사과 결함 유무',1),('정답은 무엇인가?','일관된 정상·불량 Label',1),('무슨 사진이 필요한가?','다양한 조건 · Group Split',3),('어떻게 성공을 판단하나?','놓침 FN · 오알람 FP',4)]
    for i,(q,a,dest)in enumerate(questions):
        x=10+i*303;cx=x+139;to=120+dest*242
        b+=f'<path data-question-node="{dest+1}" d="M{cx} 219V184H{to}V145" fill="none" stroke="#93b6bc" stroke-width="1.8" stroke-dasharray="5 4"/><g text-anchor="middle" fill="#335e70"><text x="{cx}" y="248" font-size="22" font-weight="750">{q}</text><text x="{cx}" y="282" font-size="20">{a}</text></g>'
    return '<svg class="h55-workflow" viewBox="0 0 1210 305" role="img" aria-label="사과의 Pixel에서 Task Label CNN Training 독립 평가로 연결되는 다섯 단계와 네 가지 질문">'+b+'</svg>'

def build():
    p=ROOT/'docs/vision_ai_course.html';doc=p.read_text()
    bodies={}
    bodies['workflow']='''<h2 class="slide-title">Vision AI 원리 · 한 장으로 연결</h2><p class="slide-subtitle">같은 사과의 결함을 찾는 문제로 돌아와, 사진의 숫자부터 새 사진의 평가까지 연결합니다.</p><div class="h55-recall-photo">'''+photo()+'''<p><strong>이 사과에 결함이 있는가?</strong><br>AI와 프로젝트를 진행할 때도 아래 네 질문의 답을 먼저 정합니다.</p></div>'''+workflow()+'''<p class="lesson-takeaway">학습은 Train, 선택은 Validation, 최종 확인은 독립 Test입니다. <strong>Test 점수로 모델과 기준을 반복 선택하지 않습니다.</strong></p>'''
    bodies['project-iterate']='''<h2 class="slide-title">실패 사진이 알려 주는 것</h2><p class="slide-subtitle">실패를 발견했다면 먼저 원인 가설을 세우고, 한 조건만 바꾼 비교로 확인합니다.</p><div class="h55-hypotheses"><article><h3>① 조명 가설</h3><div class="h55-pair"><figure>'''+photo('기준 밝기의 같은 사과')+'''<figcaption>기준 밝기</figcaption></figure><figure class="h55-dark">'''+photo('CSS 밝기0.35의 같은 사과')+'''<figcaption>밝기 ×0.35</figcaption></figure></div><p><strong>관찰:</strong> 반점과 표면이 함께 어두워짐<br><strong>가설:</strong> 조명 조건에 민감한가?</p><div class="h55-compare">추가 촬영 → 같은 개체·배경에서<br>조명만 바꾸어 Recall 비교</div></article><article><h3>② 배경 가설</h3><div class="h55-pair"><figure>'''+photo()+'''<figcaption>기준 표시</figcaption></figure><figure class="h55-background">'''+photo('같은 사진 외곽의 배경 조건 표식')+'''<figcaption>배경 조건 표식</figcaption></figure></div><p><strong>관찰:</strong> 특정 배경에서만 오류가 난다면?<br><strong>가설:</strong> 배경 단서에 의존하는가?</p><div class="h55-compare">추가 촬영 → 같은 개체·조명에서<br>실제 배경만 교체해 FP·FN 비교</div></article><article><h3>③ 해상도 가설</h3><div class="h55-pair"><figure><canvas width="240" height="240" data-h-review-resolution="240" aria-label="같은 사과240×240래스터">사진 로딩 중</canvas><figcaption>240×240</figcaption></figure><figure><canvas width="24" height="24" data-h-review-resolution="24" aria-label="같은 사과24×24래스터">사진 로딩 중</canvas><figcaption>24×24 확대</figcaption></figure></div><p><strong>관찰:</strong> 작은 반점의 정보가 줄어듦<br><strong>가설:</strong> 축소 시 결함을 잃는가?</p><div class="h55-compare">추가 촬영 → 같은 위치를 고해상도로<br>확보하고 축소·Crop 조건 비교</div></article></div><p class="h55-note">동일 생성 사진의 교육용 화면 변형입니다. 테두리는 배경 조건 표식이며 실제 배경 교체가 아닙니다. 실제 모델의 실패 결과가 아닙니다.</p><p class="lesson-takeaway">원인은 아직 가설입니다. <strong>Validation으로 조건별 비교 후 설계를 고정</strong>하고, 새 독립 Test에서 확인합니다.</p>'''
    bodies['project-check']='''<h2 class="slide-title">Vision AI 원리 · 무엇을 설명할 수 있나?</h2><p class="slide-subtitle">같은 사과 한 장을 네 가지 관점으로 설명할 수 있다면, AI와 프로젝트를 시작할 기초가 연결된 것입니다.</p><div class="h55-answers"><article data-review-answer="pixel"><h3>① 입력은 어떤 숫자인가?</h3><strong>H×W×3</strong><p>높이·너비·RGB 세 채널.<br>축소하면 작은 결함 정보를 잃을 수 있습니다.</p></article><div class="h55-answer-photo">'''+photo()+'''<p>처음 본 같은 사과<br>결함 유무 → Class Label<br>정확한 모양 → Mask Label</p></div><article data-review-answer="feature"><h3>② Kernel은 무엇을 만드나?</h3><strong>작은 영역의 가중합 → Map</strong><p>같은 Weight를 여러 위치에서 공유.<br>5×5 입력의 첫 반응 −6 → 다음 12.</p></article><article data-review-answer="learn"><h3>③ 무엇을 바꾸어 배우나?</h3><strong>Loss → Gradient → Weight</strong><p>단순 회귀 예: w 0.5 → 1.7<br>Loss 9 → 0.36<br>CNN에서는 Conv·Head가 학습 대상입니다.</p></article><article data-review-answer="evaluate"><h3>④ 놓친 결함을 어떻게 보나?</h3><strong>Recall = 18 / 20 = 90%</strong><p>기준 0.50 참조: 찾음 TP18 · 놓침 FN2.<br>새 개체·영상은 Group으로 분리합니다.</p></article></div><p class="lesson-takeaway"><strong>Task·Label·데이터·평가 기준</strong>을 정하고, Pixel → CNN → 학습 → 독립 평가를 설명할 수 있어야 합니다.</p><details class="project-answer"><summary>복습 · 결함의 정확한 모양이 필요하다면?</summary><p>분할 Task와 Mask Label, 영역 평가가 필요합니다.</p></details><p class="h55-note">사진은 동일 생성 예시입니다. 회귀 수치·Kernel 계산·평가 100건은 앞서 배운 각각의 교육용 예제이며 하나의 실제 모델 측정값이 아닙니다.</p>'''
    for concept,body in bodies.items():
        doc,n=re.subn(rf'<section\b[^>]*data-concept="{concept}"[^>]*>.*?</section>',lambda _:section(concept,body),doc,count=1,flags=re.S);assert n==1
    doc=re.sub(r'<section\b[^>]*data-concept="project-brief"[^>]*>.*?</section>','',doc,flags=re.S)
    doc=doc.replace('\nundefined\n','\n')
    if 'approved_h.css' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="approved_h.css?v=approved-h-20261019-1">\n<script src="approved_h.js?v=approved-h-20261019-1" defer></script>\n</head>')
    doc=re.sub(r'<title>.*?</title>','<title>Vision AI 기초 · 원리 중심 · Course 42장</title>',doc,count=1)
    p.write_text(doc)

if __name__=='__main__':build()
