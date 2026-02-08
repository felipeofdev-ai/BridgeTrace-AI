"""Node schemas."""
from pydantic import BaseModel
from typing import Dict, Any

class NodeCreate(BaseModel):
    type: str
    name: str
    metadata: Dict[str, Any]

class NodeResponse(BaseModel):
    id: str
    type: str
    name: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
