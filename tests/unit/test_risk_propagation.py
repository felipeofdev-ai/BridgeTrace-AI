"""Unit tests for graph risk propagation."""

import networkx as nx

from app.analytics.risk_propagation import RiskPropagationEngine


def test_risk_propagation_spreads_risk_to_downstream_nodes() -> None:
    graph = nx.DiGraph()
    graph.add_edge("A", "B", risk_transfer=1.0)
    graph.add_edge("B", "C", risk_transfer=0.5)

    engine = RiskPropagationEngine(decay=1.0, min_signal=0.0)
    result = engine.run(graph, seed_scores={"A": 1.0}, max_hops=3)

    assert result.scores["A"] == 1.0
    assert result.scores["B"] == 1.0
    assert result.scores["C"] == 0.5
    assert result.dominant_source["C"] == "A"
