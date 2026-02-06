from typing import Dict, List


class ExplainabilityEngine:
    """
    Generates human-readable explanations for trace and risk decisions.
    """

    def build_explanation(
        self,
        entity_id: str,
        risk_score: float,
        contributing_factors: Dict[str, float],
        linked_entities: List[str]
    ) -> Dict[str, str]:
        """
        Builds a structured explanation payload.
        """

        factors_text = ", ".join(
            f"{k} ({v:.2f})" for k, v in contributing_factors.items()
        )

        explanation = {
            "entity_id": entity_id,
            "summary": self._risk_summary(risk_score),
            "risk_score": f"{risk_score:.2f}",
            "key_factors": factors_text,
            "linked_entities": ", ".join(linked_entities)
        }

        return explanation

    def _risk_summary(self, score: float) -> str:
        if score >= 0.85:
            return "High risk behavior detected based on network and transaction patterns."
        elif score >= 0.60:
            return "Moderate risk indicators observed requiring further review."
        else:
            return "Low risk profile with no significant anomalies detected."
