"""Risk propagation logic for graph-based financial risk scoring."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable

import networkx as nx


@dataclass(frozen=True)
class PropagationResult:
    """Result object with propagated scores and dominant paths."""

    scores: Dict[str, float]
    dominant_source: Dict[str, str]


class RiskPropagationEngine:
    """Propagate initial risk across a directed graph using edge weights and decay."""

    def __init__(self, decay: float = 0.7, min_signal: float = 0.01):
        self.decay = decay
        self.min_signal = min_signal

    def run(
        self,
        graph: nx.DiGraph,
        seed_scores: Dict[str, float],
        max_hops: int = 4,
    ) -> PropagationResult:
        """Propagate risk from seed nodes up to max_hops.

        Edge attribute `risk_transfer` is used as weight when present.
        """

        scores: Dict[str, float] = {node: 0.0 for node in graph.nodes}
        dominant_source: Dict[str, str] = {}

        frontier: Iterable[tuple[str, float, str, int]] = [
            (seed, score, seed, 0) for seed, score in seed_scores.items() if seed in graph
        ]

        for seed, score in seed_scores.items():
            if seed in scores:
                scores[seed] = max(scores[seed], score)
                dominant_source[seed] = seed

        pending = list(frontier)
        while pending:
            node, incoming_risk, source, depth = pending.pop(0)
            if depth >= max_hops:
                continue

            for nxt in graph.successors(node):
                edge = graph[node][nxt]
                transfer = float(edge.get("risk_transfer", 0.8))
                propagated = incoming_risk * transfer * self.decay
                if propagated < self.min_signal:
                    continue

                if propagated > scores.get(nxt, 0.0):
                    scores[nxt] = round(propagated, 4)
                    dominant_source[nxt] = source
                    pending.append((nxt, propagated, source, depth + 1))

        return PropagationResult(scores=scores, dominant_source=dominant_source)
