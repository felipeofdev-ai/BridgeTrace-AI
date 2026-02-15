# BridgeTrace Whitepaper (Formal) — v1.0.0

**DOI (planned):** `10.5281/zenodo.BRIDGETRACE-WP-V1` (to be minted at release)

## Citation
BridgeTrace Team. *BridgeTrace Whitepaper (Formal) v1.0.0*. 2026. DOI: pending mint.

## 1. Problem Statement
Cross-rail financial investigations require explainable, deterministic methods that connect weakly linked transaction paths under uncertainty.

## 2. Method
BridgeTrace combines:
- directed weighted propagation,
- temporal decay,
- multi-source risk seeding,
- explainability replay outputs.

## 3. Formalism
Given edge `u -> v`, risk update at step `k+1`:

`R(v,k+1)=max(R(v,k+1), R(u,k)*w(u,v)*d*T)`

## 4. Evaluation Protocol
- deterministic synthetic dataset generation (fixed seed)
- deterministic benchmark script
- reproducible artifacts + checksums

## 5. Results Snapshot
See:
- `scripts/benchmark_risk_engine.py`
- `scripts/run_external_proof.sh`
- `docs/PERFORMANCE_PROOF.md`

## 6. Limitations
- external third-party benchmark execution still pending
- graph-db adapters (Neo4j/TigerGraph) not yet benchmarked end-to-end

## 7. Scientific Changelog
Tracked in `docs/papers/SCIENTIFIC_CHANGELOG.md`.
