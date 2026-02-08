"""API dependencies."""
from fastapi import Depends
from app.services.trace_service import TraceService
from app.services.risk_service import RiskService
from app.services.ai_service import AIService

def get_trace_service() -> TraceService:
    return TraceService()

def get_risk_service() -> RiskService:
    return RiskService()

def get_ai_service() -> AIService:
    return AIService()
