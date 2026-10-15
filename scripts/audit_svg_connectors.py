"""Inventory and audit diagram connectors used in the published lecture decks."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NS = "{http://www.w3.org/2000/svg}"


def svg_assets() -> list[Path]:
    seen: set[Path] = set()
    for name in ("intro", "ai_basics", "vision_ai"):
        content = (DOCS / (name + ".html")).read_text("utf-8")
        for asset in re.findall(r'(?:src|href)="(assets/[^"?]+[.]svg)', content):
            path = DOCS / asset
            if path.exists():
                seen.add(path)
    return sorted(seen)



def parse_segment(el: ET.Element) -> tuple[float,float,float,float] | None:
    if el.tag == NS+"line":
        try:
            return tuple(float(el.get(k, "0")) for k in ("x1","y1","x2","y2"))
        except ValueError:
            return None
    if el.tag != NS+"path":
        return None
    d=el.get("d", "")
    num=r"(-?(?:\d+(?:\.\d*)?|\.\d+))"
    p=re.fullmatch(rf"\s*M\s*{num}[,\s]+{num}\s*L\s*{num}[,\s]+{num}\s*",d,re.I)
    if p: return tuple(map(float,p.groups()))
    p=re.fullmatch(rf"\s*M\s*{num}[,\s]+{num}\s*([HVhv])\s*{num}\s*",d)
    if p:
        x,y=float(p[1]),float(p[2]);v=float(p[4])
        op=p[3]
        return (x,y, v if op=="H" else x+v if op=="h" else x,
                      v if op=="V" else y+v if op=="v" else y)
    return None


def inspect_svg(path:Path) -> dict:
    root=ET.parse(path).getroot()
    rects=[]
    for el in root.iter(NS+"rect"):
        try:
            x,y,w,h=(float(el.get(q,"0")) for q in ("x","y","width","height"))
        except ValueError: continue
        if w<35 or h<30 or w>440 or h>350: continue
        rects.append((x,y,x+w,y+h))
    arrows=[]
    for el in root.iter():
        if el.tag not in (NS+"line",NS+"path"): continue
        if "url(" not in el.get("marker-end",""): continue
        v=parse_segment(el)
        if not v: continue
        x1,y1,x2,y2=v
        horizontal=(abs(y1-y2)<2 and abs(x1-x2)>5)
        vertical=(abs(x1-x2)<2 and abs(y1-y2)>5)
        if not(horizontal or vertical): continue
        if horizontal:
            d=1 if x2>x1 else -1
            source=[abs(x1-(r[2] if d==1 else r[0])) for r in rects
                    if r[1]-5<=y1<=r[3]+5 and abs(x1-(r[2] if d==1 else r[0]))<55]
            dest=[(r[0]-x2 if d==1 else x2-r[2]) for r in rects
                  if r[1]-5<=y2<=r[3]+5 and -30<= (r[0]-x2 if d==1 else x2-r[2])<=50]
        else:
            d=1 if y2>y1 else -1
            source=[abs(y1-(r[3] if d==1 else r[1])) for r in rects
                    if r[0]-5<=x1<=r[2]+5 and abs(y1-(r[3] if d==1 else r[1]))<55]
            dest=[(r[1]-y2 if d==1 else y2-r[3]) for r in rects
                  if r[0]-5<=x2<=r[2]+5 and -30<= (r[1]-y2 if d==1 else y2-r[3])<=50]
        if source or dest:
            arrows.append({"d":el.get("d") or f"M{x1},{y1} L{x2},{y2}",
             "start_gap":round(min(source),1) if source else None,
             "end_gap":round(min(dest,key=abs),1) if dest else None})
    return {"file":path.name,"arrows":arrows}


def inventory() -> None:
    assets=svg_assets()
    records=[]
    for path in assets:
        root=ET.parse(path).getroot()
        counts=Counter(el.tag.removeprefix(NS) for el in root.iter())
        connectors=[el for el in root.iter()
                    if el.get("marker-end","").startswith("url(")]
        records.append({"file":path.name,"rect":counts["rect"],
                        "path":counts["path"],"polygon":counts["polygon"],
                        "marked":len(connectors)})
    candidates=[r for r in records if r["marked"] or r["polygon"]]
    print("CONNECTOR_INVENTORY",json.dumps(
      {"svg_assets":len(records),"candidate_assets":len(candidates)},ensure_ascii=False))
    for record in candidates: print("CONNECTOR_ASSET",json.dumps(record,ensure_ascii=False))
    geometries=[inspect_svg(p) for p in assets]
    for geo in geometries:
        if geo["arrows"]:
            print("CONNECTOR_GEOMETRY",json.dumps(geo,ensure_ascii=False))


    reviewed = {
        "lesson_affine_relu_comparison.svg",
        "lesson_cnn_feature_hierarchy.svg",
        "lesson_backbone_tensor_head_options.svg",
        "lesson_featuremap_numeric_continuation.svg",
        "lesson_multichannel_filter_to_maps.svg",
        "lesson_perceptron_numeric_flow.svg",
        "lesson_sgd_update_flow.svg",
        "lesson_chain_rule_graph.svg",
        "workflow_basic.svg",
        "lesson_transfer_freeze_vs_finetune.svg",
        "lesson_transfer_pretraining_to_task.svg",
        "lesson_relu_value_graph.svg",
        "preprocess_basic.svg",
        "hierarchy_professional.svg",
        "lesson_backbone_head_roles.svg",
        "lesson_receptive_field_growth.svg",
        "lecture_mean_calculation.svg",
    }
    failures = []
    for geo in geometries:
        if geo["file"] not in reviewed:
            continue
        if not geo["arrows"]:
            failures.append({"file": geo["file"], "error": "no connectors checked"})
        for arrow in geo["arrows"]:
            for side in ("start_gap", "end_gap"):
                gap = arrow.get(side)
                if gap is not None and gap < 7:
                    failures.append({"file": geo["file"], "arrow": arrow, "side": side})
    print("CONNECTOR_SPACING_AUDIT", json.dumps({
        "reviewed_assets": len(reviewed), "flagged_connectors": len(failures),
    }, ensure_ascii=False))
    for item in failures:
        print("CONNECTOR_SPACING_ISSUE", json.dumps(item, ensure_ascii=False))
    if failures:
        raise SystemExit("Connector-to-box spacing regression detected")


if __name__ == "__main__":
    inventory()
