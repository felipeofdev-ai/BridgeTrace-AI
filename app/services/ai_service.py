"""AI/LLM service for explanations."""
from typing import Dict, Any
from app.core.logging import get_logger
from app.core.config import settings

logger = get_logger(__name__)

class AIService:
    def __init__(self):
        self.provider = settings.llm_model
    
    async def generate_explanation(
        self,
        trace_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate AI explanation for trace."""
        logger.info("ai_explanation_started", provider=self.provider)
        
        # Simulated AI response
        explanation = {
            "summary": "Financial flow analysis completed",
            "narrative": f"Detected {len(trace_data.get('paths', []))} transaction paths. "
                        "Pattern suggests standard PIX to crypto conversion flow.",
            "risk_assessment": "Medium risk detected in bridge transaction",
            "recommendations": [
                "Verify wallet ownership",
                "Check transaction frequency"
            ]
        }
        
        return explanation
