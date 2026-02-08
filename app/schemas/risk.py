"""Risk analysis schemas."""
from typing import List
from pydantic import BaseModel, Field

class RiskAnalysisRequest(BaseModel):
    entity_id: str
    time_range_days: int = Field(default=30, ge=1, le=365)

class RiskMetrics(BaseModel):
    transaction_count: int
    total_volume: float
    average_risk_score: float
    high_risk_count: int
    channels_used: List[str]

class RiskAnalysisResponse(BaseModel):
    entity_id: str
    risk_level: str
    risk_score: float
    metrics: RiskMetrics
    recommendations: List[str]
