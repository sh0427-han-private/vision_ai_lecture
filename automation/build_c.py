#!/usr/bin/env python3
"""Apply approved P19–P27 only. Root owns ordering/manifest/outline/commits.

Usage: python automation/build_c.py [--root /path/to/repository]
Safe to rerun. Does not alter section count, concept IDs, or existing gate selectors.
"""
from pathlib import Path
import argparse
import re


def section(concept, content, extra=""):
    return f'<section class="slide" data-concept="{concept}" data-level="basic"><div class="slide-inner two-hour c55 {extra}">{content}</div></section>'


def mini(label="ReLU의 이유", focus="relu"):
    return f'<div class="c55-map"><span>{label}</span><div data-cnn-map="{focus}" aria-label="같은 사과 CNN 구조에서 {label} 위치 강조"></div></div>'


def apple_window(x, y, size, uid):
    grid = "".join(f'<path d="M{x+k*size/3:g} {y:g}V{y+size:g}M{x:g} {y+k*size/3:g}H{x+size:g}" stroke="#f2fbfa" stroke-width=".9"/>' for k in (1, 2))
    return f'<svg viewBox="{x} {y} {size} {size}" role="img" aria-label="동일 사과 사진의 관찰 위치 확대" overflow="hidden"><defs><clipPath id="{uid}"><rect x="{x}" y="{y}" width="{size}" height="{size}"/></clipPath></defs><image href="assets/vision_task_apple_reference.jpg" width="960" height="640" clip-path="url(#{uid})"/>{grid}<rect x="{x+1}" y="{y+1}" width="{size-2}" height="{size-2}" fill="none" stroke="#168f79" stroke-width="2"/></svg>'


def gate_graph(kind):
    targets = [0, 0, 0, 1] if kind == "AND" else [0, 1, 1, 0]
    dots = ""
    for (x, y), target in zip([(0, 0), (0, 1), (1, 0), (1, 1)], targets):
        px, py = 70+x*210, 270-y*210
        dots += f'<circle cx="{px}" cy="{py}" r="22" fill="{"#18876d" if target else "#899eaa"}"/><text x="{px}" y="{py+7}" text-anchor="middle" font-size="22" fill="#fff" font-weight="750">{target}</text><text x="{px}" y="{py+43}" text-anchor="middle" font-size="22" fill="#496b7c">({x},{y})</text>'
    boundary = '<path d="M70 186L196 60" stroke="#c08344" stroke-width="3" stroke-dasharray="7 5"/>' if kind == "AND" else ""
    # AND boundary x1+x2=1.4 intersects this [-.2,1.2]^2 diagram at (.2,1.2)/(1.2,.2).
    if kind == "AND":
        boundary = '<path d="M112 18L322 228" stroke="#c08344" stroke-width="3" stroke-dasharray="7 5"/>'
    return f'<figure class="c55-gate-graph"><svg viewBox="0 0 360 330" role="img" aria-label="{kind} 정답 네 점의 좌표와 0 또는 1"><rect x="28" y="18" width="294" height="294" fill="#f5f9fa" stroke="#cbdee4"/><path d="M28 270H338M70 312V8" fill="none" stroke="#789baa" stroke-width="2"/>{boundary}{dots}<text x="340" y="266" font-size="20" fill="#426878">x₁</text><text x="75" y="16" font-size="20" fill="#426878">x₂</text></svg><figcaption>{"점선: x₁+x₂=1.4" if kind == "AND" else "정답 1 두 점은 대각선에 위치"}</figcaption></figure>'


def gate_tiles(kind):
    targets = [0, 0, 0, 1] if kind == "AND" else [0, 1, 1, 0]
    tiles = []
    for (x, y), target in zip([(0, 0), (0, 1), (1, 0), (1, 1)], targets):
        tiles.append(f'<article class="gb-example {"gb-example--one" if target else ""}" aria-label="{kind} 입력 {x},{y} 정답 {target}"><div class="gb-pair"><div class="gb-input"><small>x₁</small><span class="gb-state {"gb-state--on" if x else ""}">{x}</span></div><div class="gb-input"><small>x₂</small><span class="gb-state {"gb-state--on" if y else ""}">{y}</span></div></div><span class="gb-arrow" aria-hidden="true">→</span><div class="gb-gate">{kind}</div><span class="gb-arrow" aria-hidden="true">→</span><div class="gb-result"><small>正답</small><strong>{target}</strong></div></article>'.replace("正답", "정답"))
    return '<div class="gb-examples" role="group" aria-label="입력 두 값과 정답의 네 가지 진리표">'+"".join(tiles)+"</div>"


def relu_graph(linear):
    name = "활성화 없음" if linear else "ReLU 활성화"
    formula = "y=z" if linear else "y=max(0,z)"
    curve = 'M70 270L270 70' if linear else 'M70 170H170L270 70'
    color = "#6a8796" if linear else "#168d74"
    graph = '<path d="M40 170H300M170 300V40" stroke="#8ba4af" stroke-width="2" fill="none"/>'
    for n in (-2, -1, 0, 1, 2):
        p = 170+50*n
        graph += f'<path d="M{p} 166V174M166 {p}H174" stroke="#8ba4af" stroke-width="1.5"/>'
        if n:
            graph += f'<text x="{p}" y="194" text-anchor="middle" font-size="18" fill="#587482">{n}</text><text x="151" y="{170-50*n+6}" text-anchor="end" font-size="18" fill="#587482">{n}</text>'
    graph += f'<path d="{curve}" stroke="{color}" stroke-width="5" fill="none" stroke-linejoin="round"/><circle cx="70" cy="{270 if linear else 170}" r="6" fill="{color}"/><circle cx="270" cy="70" r="6" fill="{color}"/><text x="306" y="176" font-size="20" fill="#426878">z</text><text x="170" y="30" text-anchor="middle" font-size="20" fill="#426878">y</text><text x="189" y="193" font-size="18" fill="#587482">0</text>'
    graph = graph.replace('font-size="18"', 'font-size="24"').replace('font-size="20"', 'font-size="24"')
    return f'<figure><figcaption><strong>{name}</strong><span>{formula}</span></figcaption><svg viewBox="0 0 340 330" role="img" aria-label="동일한 축 눈금의 {formula} 그래프. −2 입력은 {"−2" if linear else "0"}, 2 입력은 2 출력">{graph}</svg><p class="c55-foot" style="text-align:center">−2 → {"−2" if linear else "0"}　·　2 → 2</p></figure>'


def replace_section(doc, concept, replacement):
    pattern = rf'<section\b[^>]*data-concept="{re.escape(concept)}"[^>]*>.*?</section>'
    updated, count = re.subn(pattern, lambda _: replacement, doc, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Expected exactly one section {concept}; found {count}")
    return updated


def build(root):
    path = root / "docs/vision_ai_course.html"
    doc = path.read_text()
    old_sections = {m.group(1):m.group(0) for m in re.finditer(r'<section\b[^>]*data-concept="([^"]+)"[^>]*>.*?</section>', doc, re.S)}
    why = '''<h2 class="slide-title">왜 CNN인가? · 사과의 작은 특징 반복 탐색</h2><p class="slide-subtitle">사람이 반점과 윤곽 같은 시각적 단서를 모아 판단하듯, CNN은 <strong>작은 지역의 패턴을 여러 위치에서 반복 탐색</strong>합니다.</p>
<div class="c55-why-grid"><article><h3>① 사진의 작은 영역</h3><svg class="c55-apple-photo" viewBox="300 65 450 450" role="img" aria-label="같은 사과의 정상표면, 갈색반점, 윤곽 세 위치"><image href="assets/vision_task_apple_reference.jpg" width="960" height="640"/><rect x="440" y="240" width="60" height="60" fill="none" stroke="#168f79" stroke-width="4"/><rect x="565" y="197" width="60" height="60" fill="none" stroke="#168f79" stroke-width="4"/><rect x="675" y="280" width="60" height="60" fill="none" stroke="#168f79" stroke-width="4"/><g font-size="26" font-weight="750" fill="#0e6e5a"><text x="440" y="230">A</text><text x="565" y="187">B</text><text x="675" y="270">C</text></g></svg></article><article><h3>② 같은 작은 관찰창 반복</h3><div class="c55-observations">'''
    why = why.replace('x="675" y="280"', 'x="650" y="280"').replace('x="675" y="270"', 'x="650" y="270"')
    for x, y, label, uid in [(440,240,"A · 정상 표면","c55-normal"),(565,197,"B · 갈색 반점","c55-defect"),(650,280,"C · 윤곽","c55-edge")]:
        why += f'<figure>{apple_window(x,y,60,uid)}<figcaption>{label}</figcaption></figure>'
    why += '''</div><p>3×3 칸은 <strong>관찰창의 모양</strong>입니다.<br>같은 Weight를 위치마다 재사용합니다.</p></article><article><h3>③ 반응을 모아 판정</h3><svg class="c55-response-svg" viewBox="0 0 220 185" role="img" aria-label="세 위치에서 얻은 중간 반응을 지도에 놓는 설명용 도식"><rect x="25" y="15" width="155" height="135" fill="#eaf2f5" stroke="#9bb8c1"/><path d="M76 15V150M128 15V150M25 60H180M25 105H180" stroke="#b9ccd2"/><rect x="26" y="61" width="50" height="43" fill="#b9ddd0"/><rect x="77" y="16" width="50" height="43" fill="#80bca6"/><rect x="129" y="61" width="50" height="43" fill="#d3e7df"/><g fill="#285c68" font-size="22" text-anchor="middle"><text x="51" y="90">A</text><text x="102" y="45">B</text><text x="154" y="90">C</text></g><text x="110" y="180" text-anchor="middle" font-size="19" fill="#527685">위치별 중간 반응</text></svg><p>여러 반응의 조합으로<br><strong>정상 / 불량?</strong></p></article></div>
<div class="c55-summary-flow">사과 사진　→　작은 특징 반복 탐색　→　특징 조합　→　판정</div><p class="lesson-takeaway">모든 Pixel을 각 뉴런에 완전 연결하면 연결 수가 커집니다. <strong>지역 연결은 계산 범위를 줄이고, 같은 Kernel 공유는 Weight 수를 줄입니다.</strong></p><p class="c55-foot">생성 사과 사진의 동일 위치를 확대한 화면입니다. 3×3 격자와 오른쪽 반응 지도는 원리 도식이며 실제 Pixel 값·학습된 활성화가 아닙니다.</p>'''
    doc = replace_section(doc, "cnn-why", section("cnn-why", why))

    overview = '''<h2 class="slide-title">CNN Architecture 전체 그림 · 사과 판정까지</h2><p class="slide-subtitle">사진에서 특징을 찾는 <strong>Feature Extractor</strong>와, 그 특징을 결과로 바꾸는 <strong>Classification Head</strong>를 한 구조로 봅니다.</p><figure class="c55-arch-figure" data-cnn-architecture aria-label="64×64 RGB 사과에서 Conv·ReLU·Pool·GAP·Dense 2로 이어지는 로컬 모델"><img src="assets/lesson/cnn_apple_architecture.svg?v=approved-c-20261019-1" alt="사과 CNN의 전체 연산과 Tensor Shape, 학습 파라미터 1426개"></figure><div class="c55-params"><span>Conv A <strong>(3×3×3+1)×8 = 224</strong></span><span>Conv B <strong>(3×3×8+1)×16 = 1,168</strong></span><span>Dense Head <strong>(16+1)×2 = 34</strong></span></div><p class="lesson-takeaway"><strong>Conv·Dense의 Weight는 학습 대상</strong>, ReLU·Pool·GAP는 고정 연산입니다. 이제 하나의 뉴런부터 <strong>가중합과 비선형성</strong>을 확대해 봅니다.</p><p class="c55-foot">학습하지 않은 교육용 2-class 모델 · Bias 포함 총 1,426개 · 모든 CNN이 이 구조를 쓰는 것은 아닙니다. 원시 Score는 미측정이며 확률·정확도를 뜻하지 않습니다.</p>'''
    doc = replace_section(doc, "cnn-overview", section("cnn-overview", overview))

    perceptron = '''<h2 class="slide-title">퍼셉트론 · 하나의 W와 b로 판정</h2><p class="slide-subtitle">퍼셉트론은 <strong>입력의 가중합</strong>을 계산하고, Step 함수로 <strong>0 또는 1</strong>을 결정하는 뉴런 하나입니다.</p>'''+mini("가중합 → 비선형성")+'''<figure class="lesson-figure gate-reference-figure"><div class="figure-display"><img src="assets/lesson/perceptron_one_weight_ko.svg?v=one-w-20261019-1" alt="두 입력에 공통 W를 곱해 더하고 Bias b를 더한 후 Step으로 0 또는 1 출력"></div></figure><div class="c55-neuron-note"><span><strong>이 예시: w₁=w₂=W</strong><br>z=W(x₁+x₂)+b</span><span>일반 뉴런은 입력마다 다른 Weight 가능<br>z=w₁x₁+w₂x₂+b</span></div><p class="lesson-takeaway">뉴런이 하나여도 연결별 Weight는 여러 개입니다. 여기서는 <strong>두 Weight를 같은 값으로 묶었고</strong>, Step은 z≥0이면 1, 아니면 0을 냅니다.</p><p class="c55-foot">Step은 0/1 판정용 예시입니다. 같은 Architecture의 ReLU는 뒤에서 별도로 확대합니다.</p>'''
    perceptron = perceptron.replace('perceptron_one_weight_ko.svg?v=one-w-20261019-1', 'perceptron_approved_c.svg?v=approved-c-20261019-1')
    doc = replace_section(doc, "perceptron", section("perceptron", perceptron, "neuron-story"))

    for kind, concept in [("AND", "and-rule"), ("XOR", "xor-rule")]:
        title = "두 입력이 모두 1일 때" if kind == "AND" else "입력이 다를 때만 1"
        message = "두 스위치가 모두 ON이면 1" if kind == "AND" else "둘 중 정확히 하나만 ON이면 1"
        subtitle = "두 조건이 모두 참(1)일 때만 정답이 1입니다." if kind == "AND" else "두 입력이 서로 다를 때만 정답이 1입니다. 같은 네 좌표에서 AND와 비교합니다."
        end = "W=0.5, b=−0.7이면 <strong>z=0.5(x₁+x₂)−0.7</strong>. Step(z≥0)은 네 경우 모두 AND 정답과 같습니다." if kind == "AND" else "정답 1 두 점이 대각선에 있으므로 <strong>직선 하나로 0과 1을 모두 분리할 수 없습니다.</strong> 층을 더 쌓으면 달라질까요?"
        body = f'<h2 class="slide-title">{kind} Gate · {title}</h2><p class="slide-subtitle">{subtitle}</p>'+mini()+f'<div class="gb-lead"><div class="gb-rule">{message}</div></div><div class="c55-gate-layout">'+gate_tiles(kind)+gate_graph(kind)+f'</div><p class="gb-caption">스위치와 점 안 숫자는 <strong>논리 규칙의 정답</strong>입니다. 초록은 정답 1, 회색은 정답 0입니다.</p><p class="lesson-takeaway">{end}</p>'
        doc = replace_section(doc, concept, section(concept, body, "gb-lesson"))

    and_lab = re.sub(r'<div class="c55-map">.*?</div></div>', '', old_sections["and-gate"], flags=re.S)
    and_lab = and_lab.replace('class="slide-inner two-hour c55 gl-lesson"', 'class="slide-inner two-hour gl-lesson"')
    and_lab = and_lab.replace('class="slide-inner two-hour gl-lesson"', 'class="slide-inner two-hour c55 gl-lesson"')
    and_lab = and_lab.replace('<div class="gl-layout lesson-inline-lab"', mini()+ '<div class="gl-layout lesson-inline-lab"', 1)
    and_lab = and_lab.replace('여기서는 <strong>w₂=1로 고정</strong>하고 w₁=W만 조절합니다. 따라서 W는 기울기(−W)를, b는 y절편(−b)을 바꿉니다.', '앞의 공통 W 예시와 다른 설정입니다. <strong>w₂=1 고정, w₁=W 조절</strong>로 W는 기울기를, b는 y절편을 바꿉니다.')
    doc = replace_section(doc, "and-gate", and_lab)

    affine = '''<h2 class="slide-title">비선형성 · 깊어져도 직선이면?</h2><p class="slide-subtitle">가중합(Affine) 계산만 반복하면 <strong>하나의 가중합</strong>으로 다시 합칠 수 있습니다. 층을 늘리는 것만으로 XOR의 한계를 넘지는 못합니다.</p>'''+mini()+'''<div class="c55-affine"><article><h3>① 가중합 두 층을 연결</h3><p>h = W₁x + b₁<br>z = W₂h + b₂</p><p class="c55-equation">z = W₂(W₁x+b₁)+b₂</p><p>최종 경계는 여전히 한 직선</p><svg class="c55-bend" viewBox="0 0 450 125" role="img" aria-label="하나의 직선 결정 경계"><path d="M20 110H430M70 120V10" stroke="#b3c7cf" stroke-width="2"/><path d="M100 110L350 15" stroke="#658f9f" stroke-width="4"/></svg></article><article><h3>② 전개하면 하나의 계산</h3><p class="c55-equation">z = (W₂W₁)x<br>　 + (W₂b₁+b₂)</p><p>새 Weight = W₂W₁<br>새 Bias = W₂b₁+b₂</p><p><strong>중간에 비선형 변환</strong>을 넣으면<br>하나의 Affine으로 합칠 수 없습니다.</p></article></div><p class="lesson-takeaway">두 층의 Weight와 Bias를 바꾸면 경계의 <strong>기울기와 위치</strong>가 달라집니다. 그래도 한 직선입니다. 다음은 반응을 꺾는 <strong>ReLU</strong>입니다.</p>'''
    doc = replace_section(doc, "nonlinear", section("nonlinear", affine))

    relu = '''<h2 class="slide-title">ReLU · 비선형성의 시작</h2><p class="slide-subtitle">ReLU는 <strong>음수는 0으로, 0 이상은 그대로</strong> 통과시킵니다. 같은 축과 같은 눈금에서 0의 꺾임을 비교합니다.</p>'''+mini("ReLU 확대")+'<div class="nb-activation-charts">'+relu_graph(True)+relu_graph(False)+'''</div><p class="lesson-takeaway"><strong>ReLU(z)=max(0,z)</strong>는 0에서 꺾이는 비선형 함수입니다. 여러 반응을 조합하면 한 직선보다 복잡한 패턴을 표현할 수 있습니다.</p><p class="c55-foot">단일 ReLU 하나만으로 XOR이 바로 해결되는 것은 아닙니다. 다음 실습은 두 ReLU를 조합한 |t|의 효과를 비교합니다.</p>'''
    doc = replace_section(doc, "relu", section("relu", relu, "neuron-story"))

    xor = re.sub(r'<div class="c55-map">.*?</div></div>', '', old_sections["xor-gate"], flags=re.S)
    xor = xor.replace('class="slide-inner two-hour c55 gl-lesson"', 'class="slide-inner two-hour gl-lesson"')
    xor = re.sub(r'<svg class="gl-stage-flow".*?</svg>', '', xor, flags=re.S)
    xor = re.sub(r'<p class="gl-description c55-combined">.*?</p>', '', xor, flags=re.S)
    xor = re.sub(r'<p class="c55-foot">.*?</p>', '', xor, flags=re.S)
    xor = xor.replace('<div class="c55-layer-pair">', '')
    xor = xor.replace('</div><p class="gl-equation"', '<p class="gl-equation"', 1) if 'c55-layer-pair' in old_sections["xor-gate"] else xor
    xor = re.sub(r'<div class="gl-presets">.*?</div>', '<button class="gl-reset" type="button" data-gate-reset>XOR 기본값 복원</button>', xor, flags=re.S)
    # Normalize only C-added wrappers so subsequent fixes remain idempotent.
    if '<h3>① Layer별 W · Bias</h3>' not in xor:
        xor = xor.replace('<article class="gl-controls">', '<article class="gl-controls"><h3>① Layer별 W · Bias</h3>', 1)
    xor = xor.replace('class="slide-inner two-hour gl-lesson"', 'class="slide-inner two-hour c55 gl-lesson"')
    xor = xor.replace('XOR 정답은 (0,1), (1,0)만 1입니다. 두 선형층의 W를 바꿔도 <strong>최종 경계는 하나의 직선으로 기울기만 달라질 뿐</strong>입니다.', '가중합만 연결하면 경계의 <strong>기울기·위치는 바뀌어도 한 직선</strong>입니다. |t|를 사이에 넣어 꺾이는 경계와 비교합니다.')
    xor = xor.replace('<div class="gl-layout gl-layout--xor', mini("ReLU 효과")+'<div class="gl-layout gl-layout--xor', 1)
    xor = xor.replace('<h3>① Layer별 W · Bias</h3>', '<h3>① 두 층과 고정 연결</h3><svg class="gl-stage-flow" viewBox="0 0 640 92" role="img" aria-label="x1과 x2에서 첫 층 t, 변환 g, 두 번째 층 z로 연결. x1은 두 번째 층에 고정 계수 1로 직접 연결"><defs><marker id="c55-skip-arrow" markerWidth="5" markerHeight="5" refX="4.5" refY="2.5" orient="auto"><path d="M0 0L5 2.5L0 5Z" fill="#5a8c97"/></marker></defs><g fill="none" stroke="#5a8c97" stroke-width="2" marker-end="url(#c55-skip-arrow)"><path d="M40 30L92 51M40 76L92 60M248 55H283M398 55H435M561 55H605M40 22V6H501V27"/></g><g fill="#eef5f6" stroke="#8db1b9"><rect x="100" y="34" width="140" height="43"/><rect x="291" y="34" width="99" height="43"/><rect x="443" y="34" width="110" height="43"/></g><g fill="#365e70" font-size="23" text-anchor="middle"><text x="20" y="34">x₁</text><text x="20" y="81">x₂</text><text x="170" y="61">첫 층 t</text><text x="341" y="61" data-gate-composition>g(t)=t</text><text x="498" y="61">둘째 층 z</text><text x="620" y="61">z</text><text x="330" y="26">+x₁ · 계수 1 고정</text></g></svg>')
    xor = xor.replace('<p class="gl-equation" data-gate-equation></p>', '<p class="gl-equation" data-gate-equation></p><p class="gl-description c55-combined">g(t)=t일 때: z=(W₂W₁+1)x₁+W₂x₂+(W₂b₁+b₂)</p>')
    xor = xor.replace('<button class="gl-reset" type="button" data-gate-reset>XOR 기본값 복원</button>', '<div class="gl-presets"><button type="button" data-gate-preset="linear">선형 프리셋 3/4</button><button type="button" data-gate-preset="nonlinear">비선형 프리셋 4/4</button><button class="gl-reset" type="button" data-gate-reset>Reset</button></div>')
    xor = xor.replace('<h3>① 두 층과 고정 연결</h3>', '')
    xor = xor.replace('<path d="M40 30L92 51M40 76L92 60M248 55H283M398 55H435M561 55H605M40 22V6H501V27"/>', '<path d="M40 30L92 51"/><path d="M40 76L92 60"/><path d="M248 55H283"/><path d="M398 55H435"/><path d="M561 55H605"/><path d="M40 22V6H501V27"/>')
    xor = re.sub(r'<p class="gl-description">t=W₁.*?</p>', '', xor)
    xor = re.sub(r'<p class="gl-description">z=W₂.*?</p>', '', xor)
    xor = xor.replace('<h4>Layer 1</h4>', '<h4>Layer 1 · W₁x₁ + 1·x₂ + b₁</h4>')
    xor = xor.replace('<h4>Layer 2</h4>', '<h4>Layer 2 · W₂t + 1·x₁ + b₂</h4>')
    xor = xor.replace('<h4>Layer 1 · W₁x₁ + 1·x₂ + b₁</h4>', '<h4>Layer 1</h4><p class="gl-description">t=W₁x₁+x₂+b₁</p>')
    xor = xor.replace('<h4>Layer 2 · W₂t + 1·x₁ + b₂</h4>', '<h4>Layer 2</h4><p class="gl-description">z=W₂g(t)+x₁+b₂</p>')
    xor = xor.replace('<div class="gl-layer-card">', '<div class="c55-layer-pair"><div class="gl-layer-card">', 1)
    xor = xor.replace('<p class="gl-equation"', '</div><p class="gl-equation"', 1)
    for before, after in [('Weight W₁ <output', 'W₁ <output'), ('Bias b₁ <output', 'b₁ <output'), ('Weight W₂ <output', 'W₂ <output'), ('Bias b₂ <output', 'b₂ <output')]:
        xor = xor.replace(before, after)
    xor = xor.replace('<h3>② 최종 결정 경계</h3>', '')
    xor = xor.replace('비선형 없음</button>', '선형 g(t)=t</button>').replace('비선형 추가</button>', '비선형 g(t)=|t|</button>')
    xor = re.sub(r'<p class="lesson-takeaway">.*?</p>', '<p class="lesson-takeaway"><strong>|t|=ReLU(t)+ReLU(−t)</strong>는 두 ReLU 반응의 조합입니다. CNN도 Conv 사이의 비선형성으로 복잡한 패턴을 표현합니다.</p><p class="c55-foot">3/4·4/4는 제공한 프리셋 결과 · 단일 ReLU와 구별 · 다음은 같은 CNN의 Conv를 확대해 작은 영역의 계산을 봅니다.</p>', xor, flags=re.S)
    doc = replace_section(doc, "xor-gate", xor)

    # Add only local dependencies. Root synchronizes global cache keys later.
    refs = '<link rel="stylesheet" href="approved_c.css?v=approved-c-20261019-1">\n<script src="cnn_architecture.js?v=approved-c-20261019-1" defer></script>\n<script src="approved_c_gates.js?v=approved-c-20261019-1" defer></script>\n'
    if 'href="approved_c.css' not in doc:
        doc = doc.replace('</head>', refs+'</head>', 1)
    doc = doc.replace("interactive_gates.js?v=20261019-rotate-w-3", "interactive_gates.js?v=approved-c-20261019-2")
    path.write_text(doc)

    # Correct overgeneralized prose while preserving the existing calculator.
    js_path = root / "docs/interactive_gates.js"
    js = js_path.read_text()
    js = js.replace('중간에 |t|를 추가하면 두 경계가 생기고 XOR 네 정답을 분리할 수 있습니다.', '중간의 |t|는 꺾인 경계를 만듭니다. 제공한 비선형 프리셋에서는 네 정답을 모두 맞춥니다.')
    js = js.replace('Layer 사이에 |t|=ReLU(t)+ReLU(−t) 추가 → 최종 두 경계로 XOR 분리', 'Layer 사이에 |t|=ReLU(t)+ReLU(−t) · 꺾인 경계 표현')
    js = js.replace('Layer 1: t=W₁x₁+x₂+b₁ → Layer 2: z=W₂t+x₁+b₂ = 최종 Wx+b, 직선 하나', '선형 g(t)=t · 최종 경계는 직선 하나')
    js = js.replace('선형층을 두 개 연결해도 최종 결과는 한 직선입니다. XOR의 네 정답을 모두 나눌 수 없습니다.', '가중합만 연결하면 한 직선입니다.')
    js = js.replace('중간의 |t|는 꺾인 경계를 만듭니다. 제공한 비선형 프리셋에서는 네 정답을 모두 맞춥니다.', '|t|는 꺾인 경계를 표현합니다.')
    js_path.write_text(js)
    print('Applied C section content, local dependencies, and gate explanation corrections. Ordering and manifest unchanged.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    build(parser.parse_args().root)
