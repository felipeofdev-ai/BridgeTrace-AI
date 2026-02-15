"""Professional API endpoints for tier-1 workflows."""

from fastapi import APIRouter, Depends

from app.api.dependencies import get_risk_service, get_trace_service
from app.schemas.simulate import SimulationRequest
from app.schemas.trace import TraceRequest
from app.services.risk_service import RiskService
from app.services.trace_service import TraceService

router = APIRouter(tags=["Professional API"])


@router.post("/trace")
async def trace_alias(
    request: TraceRequest,
    service: TraceService = Depends(get_trace_service),
):
    """Alias endpoint without trailing slash for external integrations."""

    return await service.trace_flow(request.source_id, request.max_hops, request.min_amount)


@router.get("/risk/{entity_id}")
async def get_risk(
    entity_id: str,
    days: int = 30,
    service: RiskService = Depends(get_risk_service),
):
    return await service.analyze_entity_risk(entity_id, time_range_days=days)


@router.get("/risk/propagation-map/{entity_id}")
async def get_propagation_map(
    entity_id: str,
    service: RiskService = Depends(get_risk_service),
):
    return await service.propagation_map(entity_id)


@router.get("/graph/{entity_id}")
async def get_graph_entity(
    entity_id: str,
    service: TraceService = Depends(get_trace_service),
):
    return await service.graph_snapshot(entity_id)


@router.post("/simulate")
async def simulate_transfer(
    request: SimulationRequest,
    service: RiskService = Depends(get_risk_service),
):
    return await service.simulate_transfer(
        source_id=request.source_id,
        target_id=request.target_id,
        amount=request.amount,
        risk_transfer=request.risk_transfer,
    )
