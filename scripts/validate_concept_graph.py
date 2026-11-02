#!/usr/bin/env python3
"""Validate the AI/ML concept graph and learning-path references."""

import json
from collections import defaultdict, deque
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "planning" / "concepts.v1.json"
LEVELS = {"Foundation", "Basic", "Intermediate", "Advanced", "Research"}
STATUSES = {"Implemented", "Experimented", "Reviewed", "Related"}


def validate() -> tuple[int, int]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    records = data["concepts"]
    identifiers = [record["id"] for record in records]
    assert identifiers and len(identifiers) == len(set(identifiers)), "duplicate ID"
    lookup = {record["id"]: record for record in records}
    successors = defaultdict(set)
    indegree = {identifier: 0 for identifier in identifiers}
    edge_count = 0

    for record in records:
        identifier = record["id"]
        assert record["level"] in LEVELS, f"bad level: {identifier}"
        assert record["status"] in STATUSES, f"bad status: {identifier}"
        dependencies = record["prerequisites"]
        assert len(dependencies) == len(set(dependencies)), f"duplicate edge: {identifier}"
        for dependency in dependencies:
            assert dependency in lookup, f"missing dependency {identifier} <- {dependency}"
            assert dependency != identifier, f"self dependency {identifier}"
            successors[dependency].add(identifier)
            indegree[identifier] += 1
            edge_count += 1

    for record in records:
        identifier = record["id"]
        declared = record["next_topics"]
        assert len(declared) == len(set(declared)), f"duplicate next topic: {identifier}"
        assert set(declared) == successors[identifier], f"inverse mismatch: {identifier}"
        for next_id in record["advanced_topics"]:
            assert next_id in lookup, f"unknown advanced topic: {identifier}/{next_id}"

    queue = deque(identifier for identifier in identifiers if indegree[identifier] == 0)
    processed = 0
    while queue:
        identifier = queue.popleft()
        processed += 1
        for successor in successors[identifier]:
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)
    assert processed == len(identifiers), "dependency cycle"

    for name, path in data["learning_paths"].items():
        assert len(path) == len(set(path)), f"repeated learning node: {name}"
        for identifier in path:
            assert identifier in lookup, f"unknown path node: {name}/{identifier}"
    return len(records), edge_count


if __name__ == "__main__":
    nodes, edges = validate()
    print(f"PASS: {nodes} concepts, {edges} edges, DAG and links valid")
