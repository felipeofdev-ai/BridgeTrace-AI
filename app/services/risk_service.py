"""Risk analysis service."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

import networkx as nx

from app.analytics import RiskPropagationEngine
from app.core.logging import get_logger
from app.metrics import track_latency

logger = get_logger(__name__)


class RiskService:
    """Service responsible for entity risk analysis and explainability."""

    def __init__(self):
        self.risk_thresholds = {"high": 0.7, "medium": 0.4}
        self.graph = self._build_reference_graph()
        self.propagation = RiskPropagationEngine(decay=0.75, min_signal=0.02)
        self._cache: Dict[str, Dict[str, Any]] = {}

    async def analyze_entity_risk(
        self,
        entity_id: str,
        time_range_days: int = 30,
    ) -> Dict[str, Any]:
        """Analyze risk for an entity."""

        logger.info("risk_analysis_started", entity_id=entity_id, days=time_range_days)
        cache_key = f"{entity_id}:{time_range_days}"
        if cache_key in self._cache:
            cached = dict(self._cache[cache_key])
            cached["cache_hit"] = True
            return cached

        with track_latency("risk_analysis"):
            seeds = self._seed_scores_for_entity(entity_id)
            propagation = self.propagation.run(self.graph, seed_scores=seeds, max_hops=4)
            propagated_score = propagation.scores.get(entity_id, 0.2)
            temporal_decay = self._temporal_decay_factor(time_range_days)
            behavioral_component = 0.15
            risk_score = min(round((propagated_score * temporal_decay * 0.7) + behavioral_component, 4), 0.99)
            risk_level = self._calculate_risk_level(risk_score)

            dominant_source = propagation.dominant_source.get(entity_id, "unknown")
            reasons = [
                f"propagated_risk_from={dominant_source}",
                f"time_window_days={time_range_days}",
                f"temporal_decay={temporal_decay}",
            ]

            result = {
                "entity_id": entity_id,
                "risk_level": risk_level,
                "risk_score": risk_score,
                "metrics": {
                    "transaction_count": 15,
                    "total_volume": 75000.0,
                    "average_risk_score": round((risk_score + propagated_score) / 2, 4),
                    "high_risk_count": 2,
                    "channels_used": ["PIX", "CRYPTO_BRIDGE"],
                },
                "recommendations": [
                    "Monitor large transactions",
                    "Verify beneficiary identity",
                    "Enable enhanced due diligence",
                ],
                "explanations": reasons,
                "cache_hit": False,
            }

        self._cache[cache_key] = dict(result)
        return result

    async def propagation_map(self, entity_id: str) -> Dict[str, Any]:
        """Return risk influence map for explainability."""

        seeds = self._seed_scores_for_entity(entity_id)
        propagation = self.propagation.run(self.graph, seed_scores=seeds, max_hops=5)

        influence = {
            node: score
            for node, score in propagation.scores.items()
            if score >= self._adaptive_threshold()
        }

        return {
            "entity_id": entity_id,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "adaptive_threshold": self._adaptive_threshold(),
            "influence": influence,
            "dominant_source": propagation.dominant_source,
        }

    async def simulate_transfer(
        self,
        source_id: str,
        target_id: str,
        amount: float,
        risk_transfer: float = 0.7,
    ) -> Dict[str, Any]:
        """Simulate a transfer and report projected risk for source and target."""

        sandbox_graph = self.graph.copy()
        sandbox_graph.add_node(source_id)
        sandbox_graph.add_node(target_id)
        sandbox_graph.add_edge(source_id, target_id, amount=amount, risk_transfer=risk_transfer)

        seeds = self._seed_scores_for_entity(source_id)
        projection = self.propagation.run(sandbox_graph, seed_scores=seeds, max_hops=5)

        return {
            "simulation": {
                "source_id": source_id,
                "target_id": target_id,
                "amount": amount,
                "risk_transfer": risk_transfer,
            },
            "projected_risk": {
                source_id: projection.scores.get(source_id, 0.0),
                target_id: projection.scores.get(target_id, 0.0),
            },
        }

    def _seed_scores_for_entity(self, entity_id: str) -> Dict[str, float]:
        """Multi-source seeds to represent sanctions + behavior based alerts."""

        seeds: Dict[str, float] = {"wallet_sanctioned_01": 0.92}
        if entity_id.startswith("entity_"):
            seeds["mixer_01"] = 0.55
        return seeds

    def _temporal_decay_factor(self, time_range_days: int) -> float:
        """Decay risk contribution as analysis window increases."""

        return max(0.55, round(1.0 - (time_range_days / 3650), 4))

    def _adaptive_threshold(self) -> float:
        """Adjust influence threshold by graph density."""

        nodes = max(self.graph.number_of_nodes(), 1)
        density = self.graph.number_of_edges() / nodes
        return 0.05 if density > 1 else 0.02

    def _calculate_risk_level(self, score: float) -> str:
        if score >= self.risk_thresholds["high"]:
            return "HIGH"
        if score >= self.risk_thresholds["medium"]:
            return "MEDIUM"
        return "LOW"

    def _build_reference_graph(self) -> nx.DiGraph:
        graph = nx.DiGraph()
        graph.add_edge("wallet_sanctioned_01", "mixer_01", risk_transfer=0.9)
        graph.add_edge("mixer_01", "entity_001", risk_transfer=0.85)
        graph.add_edge("entity_001", "merchant_991", risk_transfer=0.5)
        graph.add_edge("wallet_watchlist_77", "entity_001", risk_transfer=0.45)
        return graph
