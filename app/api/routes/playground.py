"""Public hosted playground routes."""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix="/playground", tags=["Playground"])


@router.get("/ping")
async def ping() -> dict:
    return {"status": "ok", "message": "BridgeTrace hosted playground is online"}


@router.get("/sample-trace")
async def sample_trace() -> dict:
    return {
        "source_id": "bank_001",
        "paths": [
            {"from": "bank_001", "to": "pix_001", "data": {"amount": 5000, "channel": "pix"}},
            {"from": "pix_001", "to": "crypto_001", "data": {"amount": 4800, "channel": "bridge"}},
        ],
        "total_paths": 2,
    }


@router.get("/sample-risk")
async def sample_risk() -> dict:
    return {
        "entity_id": "entity_001",
        "risk_level": "MEDIUM",
        "risk_score": 0.64,
        "explanations": [
            "propagated_risk_from=wallet_sanctioned_01",
            "temporal_decay=0.92",
            "risk_cascade_detected=true",
        ],
    }
