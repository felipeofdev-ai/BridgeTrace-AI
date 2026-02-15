# BridgeTrace Technical Paper v1

## Abstract
BridgeTrace-AI addresses cross-rail financial traceability by combining graph-native risk propagation, explainable risk maps, and simulation APIs.

## 1. Problem
Fraud and AML investigations span heterogeneous rails (banking, PIX, crypto), where direct links are often obscured by layering and mixers.

## 2. Approach
BridgeTrace models transfers as directed weighted graph edges and computes propagated risk from multi-source seeds using decay, min-signal pruning, and adaptive explainability thresholds.

## 3. Equation
For edge `u -> v`:

`R(v, k+1) = max(R(v, k+1), R(u, k) * w(u,v) * d * T)`

where `w` is edge risk transfer, `d` is global decay, and `T` is temporal decay.

## 4. Evaluation
We benchmark propagation against BFS and local-only baselines on synthetic graphs (`scripts/benchmark_risk_engine.py`), reporting:
- precision
- recall
- latency (ms)
- scalability (nodes/edges)

## 5. Benchmark Snapshot
Example output (environment-dependent):
- propagation: better global context than local baseline, with small latency overhead.
- bfs: stronger recall, lower explainability granularity.
- local: fastest but weakest analytical depth.

## 6. Limitations
- Current benchmark is synthetic and pseudo-labeled.
- Neo4j backend is contract-defined but not fully integrated.
- Rate limiting is in-memory baseline; distributed limits are pending.

## 7. Roadmap
- Publish signed benchmark artifacts.
- Add deterministic replay and model versioning.
- Add production graph backends and streaming ingestion.
