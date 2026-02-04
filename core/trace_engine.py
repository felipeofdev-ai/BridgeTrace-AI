"""
BridgeTrace AI
Core Module: Trace Engine

This module performs multi-hop tracing over the Unified Financial Trace Graph,
allowing the discovery of indirect financial flows across banking and crypto layers.
"""

import networkx as nx
from typing import List, Dict


def trace_funds(
    graph: nx.DiGraph,
    source_node: str,
    max_hops: int = 4
) -> List[Dict]:
    """
    Traces possible fund paths starting from a given source node.

    Parameters:
        graph: Unified financial graph
        source_node: Starting node (bank account or crypto wallet)
        max_hops: Maximum traversal depth

    Returns:
        List of traced paths with contextual metadata
    """

    traced_paths = []

    for target_node in graph.nodes:
        if target_node == source_node:
            continue

        try:
            paths = nx.all_simple_paths(
                graph,
                source=source_node,
                target=target_node,
                cutoff=max_hops
            )

            for path in paths:
                edges = []
                total_amount = 0

                for i in range(len(path) - 1):
                    edge_data = graph.get_edge_data(path[i], path[i + 1])
                    edges.append(edge_data)
                    total_amount += edge_data.get("amount", 0)

                traced_paths.append({
                    "source": source_node,
                    "target": target_node,
                    "path": path,
                    "hops": len(path) - 1,
                    "total_amount": total_amount,
                    "channels": [e.get("channel") for e in edges]
                })

        except nx.NetworkXNoPath:
            continue

    return traced_paths
