"""BridgeTrace CLI tool for quick API usage."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from bridge_trace_sdk import BridgeTraceSDK


def main() -> None:
    parser = argparse.ArgumentParser(description="BridgeTrace CLI")
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--tenant", default="public")

    sub = parser.add_subparsers(dest="command", required=True)

    trace_cmd = sub.add_parser("trace")
    trace_cmd.add_argument("--source", required=True)
    trace_cmd.add_argument("--max-hops", type=int, default=5)
    trace_cmd.add_argument("--min-amount", type=float, default=0.0)

    risk_cmd = sub.add_parser("risk")
    risk_cmd.add_argument("--entity", required=True)
    risk_cmd.add_argument("--days", type=int, default=30)

    args = parser.parse_args()
    sdk = BridgeTraceSDK(args.base_url, api_key=args.api_key, tenant_id=args.tenant)

    if args.command == "trace":
        out = sdk.trace(args.source, max_hops=args.max_hops, min_amount=args.min_amount)
    else:
        out = sdk.risk(args.entity, days=args.days)

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
