"""API dependencies."""

from app.backends import InMemoryGraphBackend
from app.services.ai_service import AIService
from app.services.risk_service import RiskService
from app.services.trace_service import TraceService

_graph_backend = InMemoryGraphBackend()
_trace_service = TraceService(backend=_graph_backend)
_risk_service = RiskService()
_ai_service = AIService()


def get_trace_service() -> TraceService:
    return _trace_service


def get_risk_service() -> RiskService:
    return _risk_service


def get_ai_service() -> AIService:
    return _ai_service
