"""Test service layer."""

import asyncio

from app.services.risk_service import RiskService
from app.services.trace_service import TraceService


def test_trace_service() -> None:
    service = TraceService()
    result = asyncio.run(service.trace_flow("bank_001", max_hops=5))

    assert "source_id" in result
    assert result["source_id"] == "bank_001"


def test_risk_service() -> None:
    service = RiskService()
    result = asyncio.run(service.analyze_entity_risk("entity_001"))

    assert "risk_level" in result
    assert result["risk_level"] in ["LOW", "MEDIUM", "HIGH"]
