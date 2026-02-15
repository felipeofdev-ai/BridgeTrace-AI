"""Benchmark risk propagation engine against simple baselines (deterministic)."""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from pathlib import Path
from statistics import mean

import networkx as nx

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.analytics.risk_propagation import RiskPropagationEngine


def build_synthetic_graph(nodes: int = 300, edges: int = 1200, seed: int = 42) -> nx.DiGraph:
    rng = random.Random(seed)
    graph = nx.DiGraph()
    for idx in range(nodes):
        graph.add_node(f"N{idx}")
    for _ in range(edges):
        a = f"N{rng.randint(0, nodes - 1)}"
        b = f"N{rng.randint(0, nodes - 1)}"
        if a != b:
            graph.add_edge(a, b, risk_transfer=round(rng.uniform(0.2, 1.0), 3))
    return graph


def propagation_scores(graph: nx.DiGraph, seeds: dict[str, float]) -> dict[str, float]:
    engine = RiskPropagationEngine(decay=0.75, min_signal=0.01)
    result = engine.run(graph, seeds, max_hops=4)
    return result.scores


def bfs_baseline(graph: nx.DiGraph, seed: str, max_hops: int = 4) -> dict[str, float]:
    scores = {node: 0.0 for node in graph.nodes}
    visited = {seed}
    frontier = [(seed, 0)]
    scores[seed] = 1.0

    while frontier:
        node, depth = frontier.pop(0)
        if depth >= max_hops:
            continue
        for nxt in graph.successors(node):
            if nxt not in visited:
                visited.add(nxt)
                scores[nxt] = 1.0 / (depth + 2)
                frontier.append((nxt, depth + 1))
    return scores


def local_baseline(graph: nx.DiGraph, seed: str) -> dict[str, float]:
    scores = {node: 0.0 for node in graph.nodes}
    scores[seed] = 1.0
    for nxt in graph.successors(seed):
        scores[nxt] = 0.5
    return scores


def pseudo_quality(scores: dict[str, float]) -> tuple[float, float]:
    predicted = {node for node, val in scores.items() if val >= 0.2}
    relevant = {node for node in scores if node.endswith("7") or node.endswith("9")}
    tp = len(predicted & relevant)
    fp = len(predicted - relevant)
    fn = len(relevant - predicted)

    precision = tp / max((tp + fp), 1)
    recall = tp / max((tp + fn), 1)
    return precision, recall


def run_benchmark(seed: int = 42, runs_count: int = 10) -> dict:
    graph = build_synthetic_graph(seed=seed)
    seeds = {"N0": 0.95, "N3": 0.55}

    runs = []
    for _ in range(runs_count):
        t0 = time.perf_counter()
        p_scores = propagation_scores(graph, seeds)
        p_lat = time.perf_counter() - t0

        t1 = time.perf_counter()
        b_scores = bfs_baseline(graph, "N0")
        b_lat = time.perf_counter() - t1

        t2 = time.perf_counter()
        l_scores = local_baseline(graph, "N0")
        l_lat = time.perf_counter() - t2

        p_pr, p_rc = pseudo_quality(p_scores)
        b_pr, b_rc = pseudo_quality(b_scores)
        l_pr, l_rc = pseudo_quality(l_scores)

        runs.append(
            {
                "propagation": (p_pr, p_rc, p_lat),
                "bfs": (b_pr, b_rc, b_lat),
                "local": (l_pr, l_rc, l_lat),
            }
        )

    def avg(metric: str, idx: int) -> float:
        return mean(run[metric][idx] for run in runs)

    return {
        "seed": seed,
        "rows": {
            "propagation": {
                "precision": round(avg("propagation", 0), 4),
                "recall": round(avg("propagation", 1), 4),
                "latency_ms": round(avg("propagation", 2) * 1000, 2),
            },
            "bfs": {
                "precision": round(avg("bfs", 0), 4),
                "recall": round(avg("bfs", 1), 4),
                "latency_ms": round(avg("bfs", 2) * 1000, 2),
            },
            "local": {
                "precision": round(avg("local", 0), 4),
                "recall": round(avg("local", 1), 4),
                "latency_ms": round(avg("local", 2) * 1000, 2),
            },
        },
        "scalability": {"nodes": graph.number_of_nodes(), "edges": graph.number_of_edges()},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--runs", type=int, default=10)
    parser.add_argument("--json-output", type=Path, default=None)
    args = parser.parse_args()

    result = run_benchmark(seed=args.seed, runs_count=args.runs)

    print("=== Risk Engine Benchmark ===")
    print("metric,precision,recall,latency_ms")
    for name in ["propagation", "bfs", "local"]:
        row = result["rows"][name]
        print(f"{name},{row['precision']:.4f},{row['recall']:.4f},{row['latency_ms']:.2f}")
    print(f"scalability,nodes={result['scalability']['nodes']},edges={result['scalability']['edges']}")

    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, indent=2))
        print(f"json_output={args.json_output}")


if __name__ == "__main__":
    main()
