"""Generate synthetic PIX transactions for local testing and demos."""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta
from pathlib import Path


def generate_pix_transactions(count: int = 1000) -> list[dict]:
    """Generate synthetic PIX-like transactions."""

    now = datetime.utcnow()
    rows: list[dict] = []

    for idx in range(count):
        created_at = now - timedelta(minutes=random.randint(1, 60 * 24 * 120))
        rows.append(
            {
                "id": f"PIX_{idx:07d}",
                "source_account": f"ACC_{random.randint(1000, 9999)}",
                "target_account": f"ACC_{random.randint(1000, 9999)}",
                "amount": round(random.uniform(5.0, 100000.0), 2),
                "timestamp": created_at.isoformat() + "Z",
                "pix_key_type": random.choice(["CPF", "CNPJ", "EMAIL", "PHONE", "RANDOM"]),
                "channel": random.choice(["PIX", "TED", "CRYPTO_BRIDGE"]),
            }
        )

    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate synthetic financial transactions")
    parser.add_argument("--count", type=int, default=1000, help="Number of records to generate")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/raw/pix_transactions.json"),
        help="Output path for generated JSON",
    )
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = generate_pix_transactions(args.count)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"Generated {len(payload)} transactions at {args.output}")


if __name__ == "__main__":
    main()
