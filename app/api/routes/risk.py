"""Risk analysis endpoints."""
from fastapi import APIRouter, Depends
from app.schemas.risk import RiskAnalysisRequest, RiskAnalysisResponse
from app.services.risk_service import RiskService
from app.api.dependencies import get_risk_service

router = APIRouter(prefix="/risk", tags=["Risk"])

@router.post("/analyze", response_model=dict)
async def analyze_risk(
    request: RiskAnalysisRequest,
    service: RiskService = Depends(get_risk_service)
):
    return await service.analyze_entity_risk(
        request.entity_id,
        request.time_range_days
    )
