"""Inventory and audit diagram connectors used in the published lecture decks."""
from __future__ import annotations

import argparse
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
        for asset in re.findall(r'(?:src|href)="(assets/[^"?]+\\.svg)', content):
            path = DOCS / asset
            if path.exists():
                seen.add(path)
    return sorted(seen)


def inventory() -> None:
    records = []
    for path in svg_assets():
        root = ET.parse(path).getroot()
        counts = Counter(el.tag.removeprefix(NS) for el in root.iter())
        connectors = []
        for el in root.iter():
            tag = el.tag.removeprefix(NS)
            if tag not in ("path", "line", "polyline", "polygon"):
                continue
            marker = [el.get(x, "") for x in ("marker-end", "marker-start")]
            if any("url(" in value for value in marker):
                connectors.append({"tag": tag, "shape": str(el.get("d") or el.get("points") or "")[:100], "marker": marker})
        records.append({"file":path.name,
          "rect": counts["rect"], "path":counts["path"], "line":counts["line"],
          "polyline":counts["polyline"],"polygon":counts["polygon"],
          "marked":len(connectors),"examples":connectors[:2]})
    targets = [r for r in records if r["marked"] or r["polygon"] or r["polyline"]]
    print("CONNECTOR_INVENTORY",json.dumps({"svg_assets":len(records),"candidate_assets":len(targets)},ensure_ascii=False))
    for r in targets:
        print("CONNECTOR_ASSET",json.dumps(r,ensure_ascii=False))


if __name__ == "__main__":
    inventory()
