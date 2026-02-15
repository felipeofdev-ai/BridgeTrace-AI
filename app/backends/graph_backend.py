"""Pluggable graph backend abstractions."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

import networkx as nx


class GraphBackend(ABC):
    """Generic interface for graph backend implementations."""

    @abstractmethod
    def add_node(self, node_id: str, **attrs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_edge(self, source_id: str, target_id: str, **attrs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def successors(self, node_id: str) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def get_edge(self, source_id: str, target_id: str) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def has_node(self, node_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def size(self) -> Dict[str, int]:
        raise NotImplementedError

    @abstractmethod
    def neighbors_with_edges(self, node_id: str) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def to_networkx(self) -> nx.DiGraph:
        raise NotImplementedError


class InMemoryGraphBackend(GraphBackend):
    """NetworkX-backed in-memory implementation."""

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id: str, **attrs: Any) -> None:
        self.graph.add_node(node_id, **attrs)

    def add_edge(self, source_id: str, target_id: str, **attrs: Any) -> None:
        self.graph.add_edge(source_id, target_id, **attrs)

    def successors(self, node_id: str) -> List[str]:
        return list(self.graph.successors(node_id))

    def get_edge(self, source_id: str, target_id: str) -> Dict[str, Any]:
        return dict(self.graph[source_id][target_id])

    def has_node(self, node_id: str) -> bool:
        return node_id in self.graph

    def size(self) -> Dict[str, int]:
        return {"nodes": self.graph.number_of_nodes(), "edges": self.graph.number_of_edges()}

    def neighbors_with_edges(self, node_id: str) -> Dict[str, Any]:
        outgoing = []
        for target in self.graph.successors(node_id):
            outgoing.append({"target": target, "edge": dict(self.graph[node_id][target])})
        return {"entity": node_id, "outgoing": outgoing}

    def to_networkx(self) -> nx.DiGraph:
        return self.graph


class MockGraphBackend(InMemoryGraphBackend):
    """Mock backend for tests; currently aliases in-memory behavior."""


class Neo4jGraphBackend(GraphBackend):
    """Placeholder for Neo4j implementation.

    This class defines the contract for production graph DB integration.
    """

    def __init__(self, uri: Optional[str] = None):
        self.uri = uri

    def _not_implemented(self) -> None:
        raise NotImplementedError("Neo4j backend integration is planned for production deployments")

    def add_node(self, node_id: str, **attrs: Any) -> None:
        self._not_implemented()

    def add_edge(self, source_id: str, target_id: str, **attrs: Any) -> None:
        self._not_implemented()

    def successors(self, node_id: str) -> List[str]:
        self._not_implemented()

    def get_edge(self, source_id: str, target_id: str) -> Dict[str, Any]:
        self._not_implemented()

    def has_node(self, node_id: str) -> bool:
        self._not_implemented()

    def size(self) -> Dict[str, int]:
        self._not_implemented()

    def neighbors_with_edges(self, node_id: str) -> Dict[str, Any]:
        self._not_implemented()

    def to_networkx(self) -> nx.DiGraph:
        self._not_implemented()
