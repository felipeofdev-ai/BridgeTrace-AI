from core.graph_builder import GraphBuilder
from core.entity_linker import EntityLinker
from core.trace_engine import TraceEngine
from core.risk_scoring import RiskScorer
from core.explainability import ExplainabilityEngine
from core.audit_logger import AuditLogger


class BridgeTracePipeline:
    """
    End-to-end orchestration pipeline for unified financial traceability.
    """

    def __init__(self):
        self.graph_builder = GraphBuilder()
        self.entity_linker = EntityLinker()
        self.trace_engine = TraceEngine()
        self.risk_scorer = RiskScorer()
        self.explainer = ExplainabilityEngine()
        self.audit = AuditLogger()

    def run(self, raw_records: list) -> dict:
        """
        Executes the full analysis pipeline.
        """

        entities = self.entity_linker.link(raw_records)
        graph = self.graph_builder.build(entities)

        trace_results = self.trace_engine.trace(graph)
        risk_score, factors = self.risk_scorer.score(trace_results)

        explanation = self.explainer.build_explanation(
            entity_id=trace_results["root_entity"],
            risk_score=risk_score,
            contributing_factors=factors,
            linked_entities=trace_results["linked_entities"]
        )

        self.audit.log_event(
            event_type="analysis_complete",
            entity_id=trace_results["root_entity"],
            payload={
                "risk_score": risk_score,
                "factors": factors,
                "explanation": explanation
            }
        )

        return {
            "risk_score": risk_score,
            "explanation": explanation
        }
