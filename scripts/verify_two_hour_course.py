"""Final, source-connected checks for the approved 55-slide / 120-minute deck.

Uses only Python's standard library plus Node for the real threshold calculator.
This is a FINAL gate: staged D–H work is expected to fail until implemented.
Browser rendering, keyboard/reset tests and the independent review remain separate.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import ast
import itertools
import json
import math
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class Element:
    def __init__(self, tag="document", attrs=(), parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Element):
                yield from child.walk()

    def text(self):
        return "".join(c.text() if isinstance(c, Element) else c for c in self.children)

    def has_class(self, name):
        return name in self.attrs.get("class", "").split()

    def find(self, tag=None, cls=None, **attrs):
        return [n for n in self.walk() if (tag is None or n.tag == tag)
                and (cls is None or n.has_class(cls))
                and all(k in n.attrs and (v is None or n.attrs[k] == v) for k, v in attrs.items())]


class Document(HTMLParser):
    VOID = {"img", "input", "link", "meta", "br", "hr", "source", "area", "base", "embed", "param", "wbr", "col"}

    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Element()
        self.stack = [self.root]
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Element(tag, attrs, self.stack[-1]))

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def require(value, message):
    assert value, message


def one(nodes, description):
    require(len(nodes) == 1, f"{description}: expected one, found {len(nodes)}")
    return nodes[0]


def math_text(value):
    return re.sub(r"\s+", "", value).translate(str.maketrans("₁₂−×·", "12-**"))


def local_path(url, base=DOCS):
    parts = urlsplit(url)
    if parts.scheme or url.startswith(("#", "url(")):
        return None
    return (base / unquote(parts.path)).resolve() if parts.path else None


def external_svg_elements(path):
    tree = ET.parse(path)
    require(tree.getroot().tag.rsplit("}", 1)[-1] == "svg", f"Not SVG: {path}")
    return list(tree.getroot().iter())


MANIFEST = json.loads((DOCS / "two_hour_manifest.json").read_text())
PLAN = json.loads((ROOT / "planning/approved55.json").read_text())
DOCUMENTS = {deck: Document((DOCS / f"{deck}.html").read_text()).root
             for deck in ("intro", "vision_ai_course")}
SECTIONS = {deck: doc.find("section", cls="slide") for deck, doc in DOCUMENTS.items()}
CONCEPTS = {section.attrs["data-concept"]: section for sections in SECTIONS.values() for section in sections}


def expanded_elements(concept):
    """Rendered markup plus SVGs actually referenced by this concept (no unused assets)."""
    section = CONCEPTS[concept]
    elements = list(section.walk())
    for node in section.find():
        if node.tag in ("img", "image", "use"):
            url = node.attrs.get("src", node.attrs.get("href", ""))
            path = local_path(url)
            if path and path.suffix.lower() == ".svg":
                def convert(source, parent=None):
                    n = Element(source.tag.rsplit("}", 1)[-1], source.attrib.items(), parent)
                    n.children = [source.text or ""]
                    for child in source:
                        n.children.extend([convert(child, n), child.tail or ""])
                    return n
                elements.extend(convert(ET.parse(path).getroot()).walk())
    return elements


def rendered_text(concept):
    return " ".join(n.text() for n in expanded_elements(concept) if n.tag == "text") + " " + CONCEPTS[concept].text()


def matrices(concept):
    """Read visible SVG numeric text with explicit row/column identities."""
    result = {}
    for group in expanded_elements(concept):
        name = group.attrs.get("data-matrix-name")
        if not name:
            continue
        cols = int(group.attrs["data-cols"])
        cells = group.find("text", **{"data-row": None, "data-col": None})
        require(cells, f"{concept}/{name}: no visible numeric text")
        positions = {(int(c.attrs["data-row"]), int(c.attrs["data-col"])): c for c in cells}
        rows = max(r for r, _ in positions)
        require(len(cells) == rows*cols == len(positions), f"{concept}/{name}: incomplete or duplicate cells")
        values = []
        previous_y = -math.inf
        for r in range(1, rows+1):
            row, previous_x = [], -math.inf
            ys = []
            for c in range(1, cols+1):
                node = positions[(r, c)]
                x, y = float(node.attrs["x"]), float(node.attrs["y"])
                require(x > previous_x, f"{concept}/{name}: drawn columns reversed")
                previous_x = x
                ys.append(y)
                row.append(int(node.text().strip().replace("−", "-")))
            require(max(ys)-min(ys) < 1e-6 and ys[0] > previous_y,
                    f"{concept}/{name}: drawn row/column order differs from metadata")
            previous_y = ys[0]
            values.append(row)
        require(name not in result, f"{concept}: duplicate matrix {name}")
        result[name] = values
    return result


def cross_correlation(image, kernel, stride=1, padding=0):
    width = len(image[0]) + 2*padding
    padded = [[0]*width for _ in range(padding)] + [[0]*padding+row+[0]*padding for row in image] + [[0]*width for _ in range(padding)]
    return [[sum(padded[y+i][x+j]*kernel[i][j]
                 for i in range(len(kernel)) for j in range(len(kernel[0])))
             for x in range(0, width-len(kernel[0])+1, stride)]
            for y in range(0, len(padded)-len(kernel)+1, stride)]


def check_contract():
    completed = subprocess.run([sys.executable, str(ROOT / "automation/verify_approved_contract.py"), "--final"],
                               capture_output=True, text=True)
    require(completed.returncode == 0, "Approved final contract failed:\n" + completed.stdout + completed.stderr)


def check_referenced_assets():
    visited = set()

    def validate(url, base, image=False):
        parts = urlsplit(url)
        if image:
            require(not parts.scheme or parts.scheme == "data", f"Core figure depends on external server: {url}")
        path = local_path(url, base)
        if not path:
            return
        require(path.is_file(), f"Missing referenced asset: {path}")
        if path.suffix.lower() != ".svg" or path in visited:
            return
        visited.add(path)
        for element in external_svg_elements(path):
            tag = element.tag.rsplit("}",1)[-1]
            for key in ("href", "{http://www.w3.org/1999/xlink}href"):
                if key in element.attrib:
                    validate(element.attrib[key], path.parent, image=tag in ("image", "use"))

    for deck, document in DOCUMENTS.items():
        versions = []
        for node in document.walk():
            for key in ("src", "href", "data-resolution-source"):
                if key in node.attrs:
                    validate(node.attrs[key], DOCS, image=node.tag in ("img", "image", "use"))
            if node.tag == "script" and "lecture_outline.js" in node.attrs.get("src", ""):
                versions.append(urlsplit(node.attrs["src"]).query)
        require(versions == ["v="+MANIFEST["version"]], f"{deck}: outline cache key mismatch")
        require(not any(a.find("img") or a.find("svg") for a in document.find("a")), "Figure opens another image page")
    # The architecture fetched by JS is a real runtime dependency even though it
    # is not an HTML <img> in every highlighted map.
    arch_js = (DOCS / "cnn_architecture.js").read_text()
    require("assets/lesson/cnn_apple_architecture.svg" in arch_js, "Mini map uses another model")
    validate("assets/lesson/cnn_apple_architecture.svg", DOCS, image=True)


def check_intro_data():
    for concept, attrs in [("gray", ["data-grayscale-lesson", "data-gray-photo", "data-gray-values", "data-gray-tones", "data-gray-reset"]),
                           ("rgb", ["data-rgb-lesson", "data-rgb-selector", "data-rgb-r", "data-rgb-g", "data-rgb-b", "data-rgb-coordinate"])]:
        for attr in attrs:
            require(CONCEPTS[concept].find(**{attr:None}), f"{concept}: missing {attr}")
    source = re.sub(r"\s+", "", (DOCS / "interactive_lessons.js").read_text())
    for expression in ["width=48,height=32", "size=6", "Math.round(.299*data[p]+.587*data[p+1]+.114*data[p+2])", "Math.min(255,Math.round(k*origin))", "ctx.getImageData(0,0,width,height)"]:
        require(expression in source, f"Grayscale source calculation changed: {expression}")
    require("image.naturalWidth" in source and "image.naturalHeight" in source, "RGB must read original image coordinates")
    require("getImageData" in source and "rgbLabels" in source, "RGB labels disconnected from Canvas data")
    hwc = math_text(rendered_text("hwc"))
    require("640*960*3" in hwc and "1,843,200" in hwc, "HWC displayed shape/count changed")
    require(640*960 == 614400 and 640*960*3 == 1843200, "HWC arithmetic")
    frames = CONCEPTS["video-frames"].find("figure")
    require(len(frames) == 4 and len({im.attrs["src"] for f in frames for im in f.find("img")}) == 1,
            "Video must show four representative frames of the same source")
    video = math_text(rendered_text("video-frames"))
    require("T*H*W*3" in video and "30fps" in video and "Frame30" in video, "Video time/array dimensions")
    cards = CONCEPTS["resolution"].find(**{"data-resolution-p":None})
    require([int(c.attrs["data-resolution-p"]) for c in cards] == [90,180,360], "Resolution comparison sizes")
    require([(int(one(c.find("canvas", **{"data-resolution-full":None}), "resolution canvas").attrs["width"]),
              int(one(c.find("canvas", **{"data-resolution-full":None}), "resolution canvas").attrs["height"])) for c in cards] == [(160,90),(320,180),(640,360)], "Resolution actual raster sizes")
    resolution = re.sub(r"\s+", "", (DOCS / "intro_resolution_demo.js").read_text())
    for expression in ["cropRatio=16/9", "cropW=Math.min(naturalW,naturalH*cropRatio)", "cropH=cropW/cropRatio", "zc.imageSmoothingEnabled=false", "zc.drawImage(full,sx,sy,pixelW,pixelH"]:
        require(expression in resolution, f"Shared crop / nearest-neighbor enlargement changed: {expression}")


def check_task_and_learning_diagrams():
    for concept in ("task", "task-model-data"):
        nodes = CONCEPTS[concept].find("image")
        require(nodes and len({n.attrs["href"] for n in nodes}) == 1, f"{concept}: Task inputs differ")
        boxes = CONCEPTS[concept].find("rect")
        require(any([float(n.attrs.get(k, -1)) for k in ("x","y","width","height")] == [565,197,53,57] for n in boxes), f"{concept}: GT defect Box coordinates")
        paths = CONCEPTS[concept].find("path")
        require(any("M581 201" in n.attrs.get("d", "") for n in paths), f"{concept}: missing matching defect Mask")
    arithmetic = one(CONCEPTS["rules"].find("pre"), "Rule function").text().strip()
    function = ast.parse(arithmetic).body[0]
    require(isinstance(function, ast.FunctionDef) and isinstance(function.body[0], ast.Return)
            and isinstance(function.body[0].value, ast.BinOp)
            and isinstance(function.body[0].value.op, ast.Add), "Displayed rule is not an addition function")
    cases = CONCEPTS["rules"].find(cls="rl-math-case")
    outputs = CONCEPTS["rules"].find(cls="rl-math-output")
    require(len(cases) == len(outputs) == 2, "Two arithmetic inputs must share the same function")
    for case, output in zip(cases, outputs):
        a,b = map(int, one(re.findall(r"add\((\d+),\s*(\d+)\)", case.text()), "addition input"))
        actual = int(one(output.find("strong"), "addition result").text())
        require(a+b == actual, "Displayed arithmetic output is wrong")
    strips = CONCEPTS["rules-image"].find(cls="b55-photo-strip")
    require(len(strips) == 2, "Rule/ML comparison must have two photo strips")
    pictures = [[(n.attrs.get("src"), n.attrs.get("class", ""), n.attrs.get("style", "")) for n in s.find("img")] for s in strips]
    require(len(pictures[0]) == 3 and pictures[0] == pictures[1], "Rule and learning must compare the same three image instances")
    for cls in ("b55-model", "b55-training", "b55-new-photo", "b55-inference", "b55-prediction"):
        require(CONCEPTS["rules-image"].find(cls=cls), f"Learning → shared model → new input relationship missing {cls}")
    require(len(CONCEPTS["model-choice"].find(cls="b55-gate")) == 3, "Each choice route needs independent validation")


def check_shared_cnn():
    source = ET.parse(DOCS / "assets/lesson/cnn_apple_architecture.svg").getroot()
    nodes = [n for n in source.iter() if n.get("data-arch-node")]
    require([n.get("data-arch-node") for n in nodes] == ["input","conv-a","relu-a","pool","conv-b","relu-b","gap","head","output"], "Shared model operation order")
    # Shape / Bias-inclusive 1426 counts are checked by the final approved contract.
    require(CONCEPTS["cnn-overview"].find(**{"data-cnn-architecture":None}), "Main CNN figure not connected to local source")
    for concept in [e["concept"] for e in PLAN if "P21" <= e["plan"] <= "P34"]:
        require(CONCEPTS[concept].find(**{"data-cnn-map":None}), f"{concept}: common model map missing")
    require("vision_task_apple_reference.jpg" in str(CONCEPTS["cnn-why"].attrs)+" ".join(n.attrs.get("href", "") for n in CONCEPTS["cnn-why"].find("image")), "CNN reason must use the common apple")


def check_gates():
    for concept, kind, targets in [("and-rule", "and", [0,0,0,1]), ("xor-rule", "xor", [0,1,1,0])]:
        examples = CONCEPTS[concept].find(cls="gb-example")
        require(len(examples) == 4, f"{concept}: four visible truth-table cases required")
        actual_inputs, actual_outputs = [], []
        for example in examples:
            actual_inputs.append(tuple(int(n.text()) for n in example.find(cls="gb-state")))
            actual_outputs.append(int(one(one(example.find(cls="gb-result"), "gate result").find("strong"), "truth output").text()))
        require(actual_inputs == [(0,0),(0,1),(1,0),(1,1)] and actual_outputs == targets, f"{concept}: displayed truth table")
    p = math_text(rendered_text("perceptron"))
    require("W(x1+x2)+b" in p and "w1x1+w2x2+b" in p, "Tied-W special case vs general per-input weights")
    require([int(.5*(x+y)-.7 >= 0) for x,y in itertools.product((0,1), repeat=2)] == [0,0,0,1], "AND Step calculation")
    for concept, expected in [("and-gate", {"w","b"}), ("xor-gate", {"w1","b1","w2","b2"})]:
        controls = CONCEPTS[concept].find("input", **{"data-param":None})
        require(len(controls) == len(expected) and {n.attrs["data-param"] for n in controls} == expected, f"{concept}: calculator controls")
        require(CONCEPTS[concept].find(**{"data-gate-reset":None}), f"{concept}: Reset missing")
    xor = CONCEPTS["xor-gate"]
    require({n.attrs["data-gate-mode"] for n in xor.find("button", **{"data-gate-mode":None})} == {"linear","nonlinear"}, "XOR modes")
    require({n.attrs["data-gate-preset"] for n in xor.find("button", **{"data-gate-preset":None})} == {"linear","nonlinear"}, "Reproducible XOR presets")
    gate_source = re.sub(r"\s+", "", (DOCS / "interactive_gates.js").read_text())
    for expression in ["[values.w,1,values.b]", "[1+values.w1*values.w2,values.w2,values.w2*values.b1+values.b2]", "values.w2*(mode==='nonlinear'?Math.abs(t):t)+x+values.b2", "clippedLine(coeff,clipped)"]:
        require(expression in gate_source, f"Actual gate calculator changed: {expression}")
    expected = []
    for nonlinear in (False,True):
        guesses = [int(-2*(abs(x+y-1) if nonlinear else x+y-1)+x+.5 >= 0) for x,y in itertools.product((0,1), repeat=2)]
        expected.append(sum(a == b for a,b in zip(guesses,[0,1,1,0])))
    require(expected == [3,4], "Presets do not reproduce 3/4 → 4/4")
    require("|t|=ReLU(t)+ReLU(-t)" in math_text(rendered_text("xor-gate")), "Absolute-value/ReLU combination missing")


def check_conv_stride_padding_pool():
    kernel = matrices("kernel")
    image, weights = kernel["kernel-input"], kernel["kernel-weights"]
    require(image == [[1,2,3,0,1],[4,5,6,1,0],[7,8,9,2,1],[0,1,2,3,1],[1,0,1,2,3]], "Drawn kernel input changed")
    require(weights == [[1,0,-1]]*3, "Drawn kernel weights")
    expected = cross_correlation(image, weights)
    require(expected == [[-6,12,16],[-6,8,15],[-4,2,7]], "Convolution arithmetic")
    feature = matrices("feature-map")
    require(feature["feature-input"] == image and feature["feature-weights"] == weights and feature["feature-output"] == expected, "Feature Map not calculated from displayed input/kernel")
    for r,c in itertools.product(range(3),repeat=2):
        require(feature[f"window-{r+1}-{c+1}"] == [row[c:c+3] for row in image[r:r+3]], "Displayed moving window not from the same input")
    stride = matrices("stride")
    for step in (1,2):
        require(stride[f"stride-{step}-input"] == image and stride[f"stride-{step}-output"] == cross_correlation(image,weights,step), f"Stride {step}: displayed input/output")
        markers = [n for n in expanded_elements("stride") if n.attrs.get("data-stride-start") == str(step)]
        require({(int(n.attrs["data-row"]),int(n.attrs["data-col"])) for n in markers} == set(itertools.product(range(1,4,step),repeat=2)), f"Stride {step}: start positions")
    padding = matrices("padding")
    original = padding["padding-input"]
    require(original == [[1,2,3],[4,5,6],[7,8,9]], "Padding uses a separate 3×3 input")
    require(padding["padding-zeros"] == [[0]*5]+[[0]+row+[0] for row in original]+[[0]*5], "Visible added zeros")
    require(padding["padding-0-output"] == cross_correlation(original,[[1]*3]*3) == [[45]], "Padding 0 result")
    require(padding["padding-output"] == cross_correlation(original,[[1]*3]*3,padding=1) == [[12,21,16],[27,45,33],[24,39,28]], "Padding 1 result")
    pool = matrices("pool")
    p = pool["pool-input"]
    expected_pool = [[max(p[2*y+i][2*x+j] for i,j in itertools.product(range(2),repeat=2)) for x in range(2)] for y in range(2)]
    require(len(p) == 4 and all(len(row) == 4 for row in p) and pool["pool-output"] == expected_pool == [[6,4],[7,9]], "Displayed 4×4 → 2×2 Max Pool")
    sharing = rendered_text("sharing")
    require(all(str(v) in sharing for v in ("1,048,576","9,216","9")), "Weight-sharing comparison values missing")
    require(32*32*32*32 == 1048576 and 9*32*32 == 9216, "Weight-sharing arithmetic")


def check_split_and_augmentation():
    split_nodes = [n for n in expanded_elements("split") if "data-split" in n.attrs and "data-count" in n.attrs]
    require(split_nodes, "P38: connect visible split tiles with data-split/data-count")
    counts = Counter()
    for node in split_nodes:
        counts[node.attrs["data-split"].lower()] += int(node.attrs["data-count"])
    require(counts == {"train":700,"validation":150,"test":150}, f"Displayed split counts: {counts}")
    examples = CONCEPTS["leakage"].find(**{"data-split-mode":None})
    # External SVG wrappers are also accepted when the figure is stored locally.
    if not examples:
        examples = [n for n in expanded_elements("leakage") if "data-split-mode" in n.attrs]
    require({n.attrs["data-split-mode"] for n in examples} >= {"random","group"}, "P39: random/group comparison hooks missing")
    for example in examples:
        frames = example.find(**{"data-group":None,"data-frame":None,"data-split":None})
        require(len(frames) == 9, "Group example must contain the same A/B/C × 3 frames")
        partitions = defaultdict(set)
        for frame in frames:
            partitions[frame.attrs["data-group"]].add(frame.attrs["data-split"])
        require(sorted(Counter(f.attrs["data-group"] for f in frames).values()) == [3,3,3], "Group IDs not preserved")
        if example.attrs["data-split-mode"] == "group":
            require(all(len(splits) == 1 for splits in partitions.values()), "A group crosses Train/Validation/Test")
        elif example.attrs["data-split-mode"] == "random":
            require(any(len(splits) > 1 for splits in partitions.values()), "Random example must visibly demonstrate leakage")
    augment = expanded_elements("augment")
    transforms = [n for n in augment if "data-augment-transform" in n.attrs]
    require(transforms, "P40: connect valid photo/Box/Mask transformations with data-augment-transform")
    for transform in transforms:
        require(transform.find("image") and transform.find("rect") and transform.find("path"), "Photo, Box and Mask must share one transform group")
        require("transform" in transform.attrs, "Augmentation transform not applied to shared group")


def check_training_and_transfer():
    learn = CONCEPTS["learn"]
    for attr in ("data-training-lesson","data-weight","data-loss","data-prediction","data-train-step","data-train-run","data-train-reset"):
        require(learn.find(**{attr:None}), f"P41: missing {attr}")
    require(float(one(learn.find(**{"data-weight":None}), "initial weight").text()) == .5, "Initial learning Weight")
    require(float(one(learn.find(**{"data-loss":None}), "initial Loss").text()) == 9, "Initial learning Loss")
    source = re.sub(r"\s+", "", (DOCS / "interactive_lessons.js").read_text())
    for expression in ["constx=2,target=4,rate=.1", "constgradient=2*(weight*x-target)*x", "weight=weight-rate*gradient", "weight=.5;iteration=0;render()"]:
        require(expression in source, f"Actual Gradient Descent source changed: {expression}")
    gradient = 2*(.5*2-4)*2
    updated = .5-.1*gradient
    require(gradient == -12 and math.isclose(updated,1.7) and math.isclose((updated*2-4)**2,.36), "Gradient / Loss arithmetic")
    values = {float(n.replace(",", "").replace("−", "-")) for n in re.findall(r"[−-]?\d+(?:,\d{3})*(?:\.\d+)?", rendered_text("loss"))}
    require({.5,1.7,9,.36,-12,.1} <= values, "P42 drawn numbers no longer match actual training demo")
    updates = [n for n in expanded_elements("cnn-training") if "data-update-target" in n.attrs]
    require({n.attrs["data-update-target"] for n in updates} == {"conv-a","conv-b","head"}, "P43 must send updates to Conv A, Conv B and Head")
    require(all(n.tag == "path" and n.attrs.get("d") and n.attrs.get("marker-end") for n in updates), "CNN update paths must be drawn arrows")
    panels = CONCEPTS["transfer"].find(**{"data-transfer-mode":None})
    require({n.attrs["data-transfer-mode"] for n in panels} == {"head-only","fine-tune"}, "P45 head-only/fine-tune comparison")
    for panel in panels:
        targets = {n.attrs["data-update-target"] for n in panel.find(**{"data-update-target":None})}
        if panel.attrs["data-transfer-mode"] == "head-only":
            require(targets == {"head"}, "Frozen Backbone receives a Weight update")
        else:
            require("head" in targets and targets & {"conv-a","conv-b"}, "Fine-tuning does not update a selected Backbone layer")
    require(CONCEPTS["cnn-learning-paths"].find(cls="su-shared")
            and CONCEPTS["cnn-learning-paths"].find(cls="su-path--sup")
            and CONCEPTS["cnn-learning-paths"].find(cls="su-path--un"), "P46 shared frozen features → supervised/unsupervised branches")


THRESHOLD_PROBE = r'''
const fs=require('fs'),vm=require('vm');
class El {
 constructor(){this.attrs={};this.dataset={};this.style={setProperty(){}};this.children=[];this.listeners={};this.value='';this.textContent='';this.innerHTML='';}
 setAttribute(k,v){this.attrs[k]=String(v);if(k==='value')this.value=String(v);}
 getAttribute(k){return this.attrs[k]??null;}
 addEventListener(k,f){this.listeners[k]=f;}
 appendChild(n){this.children.push(n);return n;}
 append(...ns){this.children.push(...ns);}
 replaceChildren(...ns){this.children=[...ns];}
 removeAttribute(k){delete this.attrs[k];}
 querySelector(q){if(!this.registry)this.registry={};return this.registry[q]??(this.registry[q]=new El());}
 querySelectorAll(q){return [];}
}
const root=new El(),selector=root.querySelector('[data-project-threshold]');selector.value='0.5';
const document={querySelector:q=>q==='[data-project-evaluation]'?root:null,createElementNS:()=>new El(),createElement:()=>new El()};
let source=fs.readFileSync(process.argv[1],'utf8');
if(!/const\s+scores\s*=/.test(source))throw Error('Export hook not found: const scores');
source=source.replace(/const\s+scores\s*=/,'const scores=globalThis.__qaScores=');
const context={document,console,window:{},Math};vm.createContext(context);vm.runInContext(source,context);
const results=[];
for(const threshold of ['0.3','0.5','0.7']){
 selector.value=threshold;selector.listeners.change();
 const counts=Object.fromEntries(['tp','fn','fp','tn'].map(k=>[k,Number(root.querySelector('[data-project-'+k+']').textContent)]));
 results.push({threshold:Number(threshold),counts,bars:{fn:Number(root.querySelector('[data-project-fn-bar]').value),fp:Number(root.querySelector('[data-project-fp-bar]').value)},result:root.querySelector('[data-project-result]').textContent});
}
console.log(JSON.stringify({scores:context.__qaScores,results,ready:root.dataset.ready}));
'''


def check_threshold_and_metrics():
    threshold = CONCEPTS["threshold"]
    for attr in ("data-project-evaluation","data-project-threshold","data-project-reset","data-score-histogram",
                 "data-project-tp","data-project-fn","data-project-fp","data-project-tn","data-project-fn-bar","data-project-fp-bar","data-project-result"):
        require(threshold.find(**{attr:None}), f"P48: calculator not wired to threshold concept: {attr}")
    select = one(threshold.find("select", **{"data-project-threshold":None}), "Threshold selector")
    require([float(n.attrs["value"]) for n in select.find("option")] == [.3,.5,.7], "Threshold options")
    code = subprocess.run(["node", "-e", THRESHOLD_PROBE, str(DOCS / "project_course.js")], capture_output=True,text=True)
    require(code.returncode == 0, "Actual threshold JS execution failed:\n"+code.stderr)
    actual = json.loads(code.stdout)
    scores = actual["scores"]
    require(len(scores) == 100 and sum(r["label"] == 1 for r in scores) == 20, "One educational 100-score array with 20 defects required")
    expected = {.3:{"tp":20,"fn":0,"fp":30,"tn":50}, .5:{"tp":18,"fn":2,"fp":4,"tn":76}, .7:{"tp":11,"fn":9,"fp":2,"tn":78}}
    for result in actual["results"]:
        t = result["threshold"]
        counts = Counter({key:0 for key in ("tp","fn","fp","tn")})
        for row in scores:
            require(row["label"] in (0,1) and 0 <= row["score"] <= 1, "Invalid stored score")
            key = ("tp" if row["score"] >= t else "fn") if row["label"] else ("fp" if row["score"] >= t else "tn")
            counts[key] += 1
        require(result["counts"] == dict(counts) == expected[t], f"Threshold {t}: JS and independent counts differ")
        require(result["bars"] == {"fn":counts["fn"],"fp":counts["fp"]}, "Error bars detached from counts")
        metrics = re.findall(r"([\d.]+)%", result["result"])
        require(len(metrics) == 2 and math.isclose(float(metrics[0]),round(100*counts["tp"]/(counts["tp"]+counts["fp"]),1))
                and math.isclose(float(metrics[1]),round(100*counts["tp"]/(counts["tp"]+counts["fn"]),1)), "Precision/Recall calculation")
    # The static P49/P51 figures must agree with the same t=.50 population.
    for concept in ("confusion","metrics"):
        text = math_text(rendered_text(concept))
        for token in (("18","2","4","76") if concept == "confusion" else ("18/22","81.8%","18/20","90%")):
            require(token in text, f"{concept}: missing actual displayed value {token}")
    imbalance = math_text(rendered_text("imbalance"))
    require("80%" in imbalance and "0%" in imbalance, "All-normal model must display Accuracy80% and Recall0%")


def check_iou_geometry():
    boxes = {n.attrs["data-iou-box"]:n for n in expanded_elements("iou") if "data-iou-box" in n.attrs}
    require(set(boxes) >= {"gt","prediction"}, "P52: visible GT/Prediction integer-coordinate boxes missing")
    bounds, drawn = {}, []
    for role in ("gt","prediction"):
        node = boxes[role]
        require(node.tag == "rect", "IoU coordinate hook must belong to the drawn rectangle")
        x1,y1,x2,y2 = map(float,node.attrs["data-xyxy"].split(","))
        require(x2 > x1 and y2 > y1, "IoU invalid box")
        x,y,w,h = [float(node.attrs[k]) for k in ("x","y","width","height")]
        scale = w/(x2-x1)
        require(math.isclose(scale,h/(y2-y1)), "IoU coordinate metadata changes the aspect ratio")
        drawn.append((scale,x-scale*x1,y-scale*y1,y+scale*y2,x,y,w,h))
        bounds[role] = (x1,y1,x2,y2)
    require(math.isclose(drawn[0][0],drawn[1][0]) and math.isclose(drawn[0][1],drawn[1][1])
            and (math.isclose(drawn[0][2],drawn[1][2]) or math.isclose(drawn[0][3],drawn[1][3])),
            "Drawn IoU boxes use different coordinate transforms (image-down or Cartesian-up permitted)")
    a,b = bounds["gt"],bounds["prediction"]
    area = lambda r:(r[2]-r[0])*(r[3]-r[1])
    intersection = max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
    union = area(a)+area(b)-intersection
    require(area(a) == area(b) == 30 and intersection == 20 and union == 40 and intersection/union == .5, "Displayed IoU must reproduce 20/40=.5")
    require("0.5" in rendered_text("iou"), "Computed IoU absent from slide")


def main():
    checks = [check_contract,check_referenced_assets,check_intro_data,check_task_and_learning_diagrams,
              check_shared_cnn,check_gates,check_conv_stride_padding_pool,check_split_and_augmentation,
              check_training_and_transfer,check_threshold_and_metrics,check_iou_geometry]
    failures = []
    for check in checks:
        try:
            check()
        except (AssertionError,KeyError,ValueError,IndexError,TypeError,FileNotFoundError,ET.ParseError,SyntaxError) as error:
            failures.append((check.__name__,str(error)))
            print(f"FAIL {check.__name__}: {error}")
        else:
            print(f"PASS {check.__name__}")
    if failures:
        raise SystemExit(f"FINAL_55_STATIC_QA_FAILED: {len(failures)} check groups; staged/incomplete work is not a final PASS")
    print("FINAL_55_STATIC_QA_PASSED: Intro13+Course42; 120 minutes; approved order; displayed matrices/shapes/labels; source-connected calculators. Browser visual/interaction review remains separate.")


if __name__ == "__main__":
    main()
