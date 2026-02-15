"""Graph statistics metrics."""

from __future__ import annotations

from prometheus_client import Gauge

GRAPH_NODES_TOTAL = Gauge("graph_nodes_total", "Current number of graph nodes")
GRAPH_EDGES_TOTAL = Gauge("graph_edges_total", "Current number of graph edges")


def update_graph_size(nodes: int, edges: int) -> None:
    GRAPH_NODES_TOTAL.set(nodes)
    GRAPH_EDGES_TOTAL.set(edges)
