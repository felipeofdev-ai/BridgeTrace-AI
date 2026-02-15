#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p artifacts

python scripts/generate_public_dataset_v1.py --rows 500 --seed 42 --output artifacts/dataset_v1_500_seed42.jsonl
python scripts/benchmark_risk_engine.py --seed 42 --runs 10 --json-output artifacts/benchmark_seed42.json

sha256sum artifacts/dataset_v1_500_seed42.jsonl artifacts/benchmark_seed42.json > artifacts/proof_checksums.sha256

echo "External proof artifacts generated:"
cat artifacts/proof_checksums.sha256
