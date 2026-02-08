"""Trace endpoints."""
from fastapi import APIRouter, Depends
from app.schemas.trace import TraceRequest, TraceResponse
from app.services.trace_service import TraceService
from app.api.dependencies import get_trace_service

router = APIRouter(prefix="/trace", tags=["Trace"])

@router.post("/", response_model=dict)
async def trace_flow(
    request: TraceRequest,
    service: TraceService = Depends(get_trace_service)
):
    return await service.trace_flow(
        request.source_id,
        request.max_hops,
        request.min_amount
    )
