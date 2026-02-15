# BridgeTrace Synthetic Financial Dataset v1

## License
MIT (same repository license).

## Purpose
Open synthetic dataset for benchmarking traceability and risk propagation workflows.

## Scenarios Included
- layering chains
- loop laundering
- mixer transfers
- high-value cashout branches

## Schema
Each JSONL row contains:
- `tx_id`
- `source`
- `target`
- `amount`
- `timestamp`
- `pattern`
- `risk_transfer`

## Files
- `data/public/bridgetrace_synthetic_financial_dataset_v1.jsonl`

## Reproducibility
Generate with:
```bash
python scripts/generate_public_dataset_v1.py --rows 500 --seed 42
```
