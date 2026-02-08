"""Health check endpoints."""
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "2.0.0"
    }

@router.get("/health/ready")
async def readiness_check():
    return {"ready": True}

@router.get("/health/live")
async def liveness_check():
    return {"alive": True}
