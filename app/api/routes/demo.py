"""Interactive demo endpoints for graph and timeline visualization."""

from __future__ import annotations

from datetime import datetime, timedelta

from fastapi import APIRouter

router = APIRouter(prefix="/demo", tags=["Demo"])


def _demo_links() -> list[dict]:
    return [
        {"source": "wallet_sanctioned_01", "target": "mixer_01", "amount": 92000},
        {"source": "mixer_01", "target": "entity_001", "amount": 85000},
        {"source": "entity_001", "target": "merchant_991", "amount": 42000},
        {"source": "entity_001", "target": "exchange_004", "amount": 21000},
    ]


@router.get("/graph")
async def demo_graph() -> dict:
    nodes = [
        {"id": "wallet_sanctioned_01", "risk": 0.95, "kind": "sanctioned"},
        {"id": "mixer_01", "risk": 0.78, "kind": "mixer"},
        {"id": "entity_001", "risk": 0.64, "kind": "entity"},
        {"id": "merchant_991", "risk": 0.32, "kind": "merchant"},
        {"id": "exchange_004", "risk": 0.41, "kind": "exchange"},
    ]
    return {"nodes": nodes, "links": _demo_links()}


@router.get("/timeline")
async def demo_timeline() -> dict:
    now = datetime.utcnow()
    events = []
    for idx, evt in enumerate(
        [
            ("wallet_sanctioned_01", "mixer_01", 92000, "layering-start"),
            ("mixer_01", "entity_001", 87000, "mixing-hop"),
            ("entity_001", "merchant_991", 42000, "cashout"),
            ("entity_001", "exchange_004", 21000, "exchange-transfer"),
        ]
    ):
        src, dst, amount, label = evt
        events.append(
            {
                "at": (now - timedelta(minutes=(len(events) - idx) * 9)).isoformat() + "Z",
                "source": src,
                "target": dst,
                "amount": amount,
                "label": label,
                "step": idx + 1,
            }
        )

    return {"events": events}


@router.get("/replay")
async def demo_replay() -> dict:
    """Return ordered risk cascade replay steps for animated explainability."""

    steps = []
    cumulative_risk = 0.0
    for idx, link in enumerate(_demo_links(), start=1):
        risk_delta = round((link["amount"] / 100000) * (0.25 / idx), 4)
        cumulative_risk = round(min(cumulative_risk + risk_delta, 0.99), 4)
        steps.append(
            {
                "step": idx,
                "source": link["source"],
                "target": link["target"],
                "risk_delta": risk_delta,
                "cumulative_risk": cumulative_risk,
            }
        )
    return {"replay": steps}
