"""AI/LLM endpoints."""
from fastapi import APIRouter, Depends
from app.services.ai_service import AIService
from app.api.dependencies import get_ai_service

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/explain")
async def generate_explanation(
    trace_data: dict,
    service: AIService = Depends(get_ai_service)
):
    return await service.generate_explanation(trace_data)
