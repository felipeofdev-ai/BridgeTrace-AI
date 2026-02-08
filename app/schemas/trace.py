"""Trace schemas."""
from typing import Optional, List
from pydantic import BaseModel, Field

class TraceRequest(BaseModel):
    source_id: str = Field(..., description="Source node ID")
    max_hops: int = Field(default=5, ge=1, le=10)
    min_amount: float = Field(default=0.0, ge=0)

class NodeInfo(BaseModel):
    id: str
    type: str
    name: str
    metadata: dict

class TransactionHop(BaseModel):
    transaction_id: str
    from_node: str
    to_node: str
    amount: float
    currency: str
    timestamp: str
    channel: str
    risk_score: float

class TraceResponse(BaseModel):
    source: NodeInfo
    hops: List[TransactionHop]
    total_amount: float
    max_risk_score: float
    path_length: int
