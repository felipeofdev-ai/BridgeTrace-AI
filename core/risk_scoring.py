from typing import Dict, List
import math


class RiskScorer:
    """
    Computes financial risk scores for entities based on graph metrics
    and transactional behavior.
    """

    def __init__(self, config: Dict = None):
        self.config = config or {}

    def score_entity(
        self,
        entity_id: str,
        metrics: Dict,
        exposure: List[float]
    ) -> float:
        """
        Calculate final risk score for an entity.

        :param entity_id: Unique entity identifier
        :param metrics: Graph and transaction metrics
        :param exposure: Risk scores of connected entities
        :return: Normalized risk score (0.0 - 1.0)
        """

        transaction_score = self._transaction_risk(metrics)
        network_score = self._network_risk(metrics)
        exposure_score = self._exposure_risk(exposure)

        raw_score = (
            0.4 * transaction_score +
            0.35 * network_score +
            0.25 * exposure_score
        )

        return round(self._normalize(raw_score), 4)

    def _transaction_risk(self, metrics: Dict) -> float:
        volume = metrics.get("total_volume", 0)
        frequency = metrics.get("tx_frequency", 0)
        variance = metrics.get("value_variance", 0)

        return math.log1p(volume) * 0.4 + frequency * 0.3 + variance * 0.3

    def _network_risk(self, metrics: Dict) -> float:
        degree = metrics.get("degree", 0)
        centrality = metrics.get("centrality", 0)
        clustering = metrics.get("clustering", 0)

        return degree * 0.4 + centrality * 0.4 + clustering * 0.2

    def _exposure_risk(self, exposure: List[float]) -> float:
        if not exposure:
            return 0.0
        return sum(exposure) / len(exposure)

    def _normalize(self, score: float) -> float:
        return min(1.0, max(0.0, score / 10))
