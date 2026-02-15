"""Simulation schemas."""

from pydantic import BaseModel, Field


class SimulationRequest(BaseModel):
    source_id: str
    target_id: str
    amount: float = Field(gt=0)
    risk_transfer: float = Field(default=0.7, ge=0.0, le=1.0)
