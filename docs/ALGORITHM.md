# Risk Propagation Algorithm (BridgeTrace-AI)

## 1. Formula
For an edge `u -> v` with transfer weight `w(u,v)` and global decay `d`, the propagated risk at hop `k+1` is:

`R(v, k+1) = max(R(v, k+1), R(u, k) * w(u,v) * d * T)`

Where:
- `R(node, k)` = risk reaching `node` at hop `k`
- `w(u,v)` = `risk_transfer` edge weight in `[0,1]`
- `d` = base decay factor
- `T` = temporal decay factor in `[0,1]`

## 2. Variables
- `seed_scores`: dictionary of initial high-risk entities
- `max_hops`: traversal depth limit
- `min_signal`: minimum propagated signal accepted
- `adaptive_threshold`: dynamic explainability cutoff based on graph density

## 3. Complexity
- Time: `O(V + E)` for bounded BFS-style traversal in sparse graphs
- Space: `O(V)` for risk score and frontier state

## 4. Guarantees
- Monotonic update rule: node score only updates when a stronger signal appears.
- Bounded propagation: no traversal beyond `max_hops`.
- Noise control: signals under `min_signal` are ignored.

## 5. Edge Cases
- Missing seed in graph: ignored safely.
- Cycles: allowed, but bounded by `max_hops` and monotonic score overwrite.
- Dense graph explosion: mitigated via `min_signal` + adaptive threshold for maps.

## 6. Explainability Outputs
The propagation map endpoint returns:
- `influence`: node -> propagated score
- `dominant_source`: node -> strongest source seed
- `adaptive_threshold`: threshold used to filter weak signals

This keeps outputs auditable and human-review friendly.
