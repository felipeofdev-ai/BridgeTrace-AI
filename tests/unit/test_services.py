"""Test services."""
import pytest
from app.services.trace_service import TraceService
from app.services.risk_service import RiskService

@pytest.mark.asyncio
async def test_trace_service():
    service = TraceService()
    result = await service.trace_flow("bank_001", max_hops=5)
    assert "source_id" in result
    assert result["source_id"] == "bank_001"

@pytest.mark.asyncio
async def test_risk_service():
    service = RiskService()
    result = await service.analyze_entity_risk("entity_001")
    assert "risk_level" in result
    assert result["risk_level"] in ["LOW", "MEDIUM", "HIGH"]
