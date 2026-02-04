from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class RiskWeights:
    transaction_velocity: float = 0.25
    entity_connectivity: float = 0.30
    cross_domain_links: float = 0.25
    anomaly_score: float = 0.20


@dataclass(frozen=True)
class RiskThresholds:
    low: float = 0.30
    medium: float = 0.60
    high: float = 0.85


@dataclass(frozen=True)
class ComplianceFlags:
    enable_pix_trace: bool = True
    enable_crypto_trace: bool = True
    allow_cross_domain_analysis: bool = True
    log_all_events: bool = True


SYSTEM_METADATA: Dict[str, str] = {
    "system_name": "BridgeTrace AI",
    "engine_version": "0.1.0",
    "risk_model": "hybrid_graph_ai",
    "regulatory_scope": "research_only"
}
