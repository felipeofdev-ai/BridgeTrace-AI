# Official Comparison: BridgeTrace vs Alternatives

| Engine | Explainability | Deterministic | Replay | Propagation |
|---|---|---|---|---|
| BridgeTrace | Native visual + API replay | Yes (seeded benchmark) | Yes (`/api/v2/demo/replay`) | Yes (multi-source + temporal decay) |
| Plain BFS stack | Limited | Depends | No | Partial |
| Local-score only | Low | Usually | No | No |
| Black-box anomaly API | Low/opaque | Unknown | Rare | Unknown |

BridgeTrace is positioned as an explainable, deterministic propagation platform rather than a black-box risk score API.
