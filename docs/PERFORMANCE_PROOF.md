# Performance Proof Matrix

Synthetic benchmark snapshot (indicative):

| Engine/Approach | Latency | Scale | Memory | Recall |
|---|---:|---:|---:|---:|
| NetworkX + Propagation | 0.80 ms | 300 nodes / 1188 edges | Low | 0.033 |
| NetworkX + BFS | 0.09 ms | 300 nodes / 1188 edges | Low | 0.483 |
| Local-only baseline | 0.02 ms | 300 nodes / 1188 edges | Very low | 0.000 |
| Neo4j (planned benchmark) | TBD | TBD | TBD | TBD |
| TigerGraph (planned benchmark) | TBD | TBD | TBD | TBD |

Notes:
- Current measured results come from `scripts/benchmark_risk_engine.py`.
- Neo4j/TigerGraph comparison will be published once production adapters are fully integrated.
