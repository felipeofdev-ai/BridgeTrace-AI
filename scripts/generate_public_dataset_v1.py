"""Generate BridgeTrace Synthetic Financial Dataset v1 (JSONL)."""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta
from pathlib import Path


PATTERNS = ["layering", "loop", "mixer", "cashout"]


def generate_rows(rows: int, seed: int) -> list[dict]:
    random.seed(seed)
    now = datetime(2026, 1, 1) + timedelta(days=seed % 365)
    output = []
    for i in range(rows):
        pattern = random.choice(PATTERNS)
        if pattern == "loop":
            src = f"entity_{random.randint(100,199)}"
            dst = src if random.random() < 0.2 else f"entity_{random.randint(100,199)}"
        elif pattern == "mixer":
            src = f"wallet_{random.randint(1000,1999)}"
            dst = f"mixer_{random.randint(1,9)}"
        elif pattern == "cashout":
            src = f"entity_{random.randint(200,299)}"
            dst = f"merchant_{random.randint(1,50)}"
        else:
            src = f"wallet_{random.randint(2000,2999)}"
            dst = f"entity_{random.randint(300,399)}"

        output.append(
            {
                "tx_id": f"BTX_{i:07d}",
                "source": src,
                "target": dst,
                "amount": round(random.uniform(500, 150000), 2),
                "timestamp": (now - timedelta(minutes=random.randint(1, 60 * 24 * 120))).isoformat() + "Z",
                "pattern": pattern,
                "risk_transfer": round(random.uniform(0.2, 1.0), 3),
            }
        )
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/public/bridgetrace_synthetic_financial_dataset_v1.jsonl"),
    )
    args = parser.parse_args()

    rows = generate_rows(args.rows, args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Generated {len(rows)} rows at {args.output}")


if __name__ == "__main__":
    main()
