"""Trace service business logic."""
from typing import List, Dict, Any
import networkx as nx
from app.core.logging import get_logger
from app.core.exceptions import GraphTraversalError, NotFoundError

logger = get_logger(__name__)

class TraceService:
    def __init__(self):
        self.graph = nx.DiGraph()
        self._initialize_sample_graph()
    
    def _initialize_sample_graph(self):
        """Initialize with sample data."""
        nodes = [
            ("bank_001", {"type": "bank_account", "name": "Banco X"}),
            ("pix_001", {"type": "pix_key", "name": "PIX ***123"}),
            ("crypto_001", {"type": "crypto_wallet", "name": "BTC Wallet"}),
        ]
        for node_id, attrs in nodes:
            self.graph.add_node(node_id, **attrs)
        
        edges = [
            ("bank_001", "pix_001", {"amount": 5000, "channel": "pix", "risk": 0.2}),
            ("pix_001", "crypto_001", {"amount": 4800, "channel": "bridge", "risk": 0.5}),
        ]
        for src, dst, attrs in edges:
            self.graph.add_edge(src, dst, **attrs)
    
    async def trace_flow(
        self,
        source_id: str,
        max_hops: int = 5,
        min_amount: float = 0.0
    ) -> Dict[str, Any]:
        """Trace financial flow from source."""
        logger.info("trace_flow_started", source_id=source_id, max_hops=max_hops)
        
        if source_id not in self.graph:
            raise NotFoundError(f"Node {source_id} not found")
        
        paths = []
        try:
            for target in self.graph.successors(source_id):
                edge_data = self.graph[source_id][target]
                if edge_data.get("amount", 0) >= min_amount:
                    paths.append({
                        "from": source_id,
                        "to": target,
                        "data": edge_data
                    })
        except Exception as e:
            raise GraphTraversalError(f"Failed to traverse graph: {str(e)}")
        
        return {
            "source_id": source_id,
            "paths": paths,
            "total_paths": len(paths)
        }
