"""Trace service business logic."""

from __future__ import annotations

from typing import Any, Dict

from app.backends import GraphBackend, InMemoryGraphBackend
from app.core.exceptions import GraphTraversalError, NotFoundError
from app.core.logging import get_logger
from app.metrics import record_trace_result, track_latency, update_graph_size

logger = get_logger(__name__)


class TraceService:
    """Service that resolves financial traces and graph views."""

    def __init__(self, backend: GraphBackend | None = None):
        self.backend = backend or InMemoryGraphBackend()
        self._initialize_sample_graph()

    def _initialize_sample_graph(self) -> None:
        """Initialize with sample data."""

        nodes = [
            ("bank_001", {"type": "bank_account", "name": "Banco X"}),
            ("pix_001", {"type": "pix_key", "name": "PIX ***123"}),
            ("crypto_001", {"type": "crypto_wallet", "name": "BTC Wallet"}),
        ]
        for node_id, attrs in nodes:
            self.backend.add_node(node_id, **attrs)

        edges = [
            ("bank_001", "pix_001", {"amount": 5000, "channel": "pix", "risk": 0.2, "risk_transfer": 0.9}),
            ("pix_001", "crypto_001", {"amount": 4800, "channel": "bridge", "risk": 0.5, "risk_transfer": 0.8}),
        ]
        for src, dst, attrs in edges:
            self.backend.add_edge(src, dst, **attrs)

        size = self.backend.size()
        update_graph_size(size["nodes"], size["edges"])

    async def trace_flow(
        self,
        source_id: str,
        max_hops: int = 5,
        min_amount: float = 0.0,
    ) -> Dict[str, Any]:
        """Trace financial flow from source."""

        logger.info("trace_flow_started", source_id=source_id, max_hops=max_hops)

        if not self.backend.has_node(source_id):
            record_trace_result(hops=0, success=False)
            raise NotFoundError(f"Node {source_id} not found")

        paths = []
        try:
            with track_latency("trace"):
                for target in self.backend.successors(source_id):
                    edge_data = self.backend.get_edge(source_id, target)
                    if edge_data.get("amount", 0) >= min_amount:
                        paths.append({"from": source_id, "to": target, "data": edge_data})
        except Exception as exc:
            record_trace_result(hops=0, success=False)
            raise GraphTraversalError(f"Failed to traverse graph: {str(exc)}") from exc

        record_trace_result(hops=len(paths), success=True)

        return {"source_id": source_id, "paths": paths, "total_paths": len(paths), "max_hops": max_hops}

    async def graph_snapshot(self, entity_id: str) -> Dict[str, Any]:
        """Return graph neighborhood and graph size for an entity."""

        if not self.backend.has_node(entity_id):
            raise NotFoundError(f"Node {entity_id} not found")

        neighborhood = self.backend.neighbors_with_edges(entity_id)
        size = self.backend.size()
        return {"graph": neighborhood, "graph_size": size}
