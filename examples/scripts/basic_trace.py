"""Basic example for tracing a transaction path using the service layer."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.services.trace_service import TraceService


async def main() -> None:
    service = TraceService()

    trace = await service.trace_flow(source_id="bank_001", max_hops=5, min_amount=100.0)

    print("=== BridgeTrace Basic Trace Example ===")
    print(f"Source: {trace['source_id']}")
    print(f"Paths found: {trace['total_paths']}")
    for path in trace["paths"]:
        print(f" - {path['from']} -> {path['to']} | amount={path['data'].get('amount')}")


if __name__ == "__main__":
    asyncio.run(main())
