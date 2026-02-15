# Architecture Decisions

## Why BridgeTrace-AI
**BridgeTrace-AI combines graph-native risk propagation with explainable outputs so compliance teams can act in minutes, not days.**

## Core layers
1. **API Layer** (`app/api`) for HTTP contracts and routing.
2. **Service Layer** (`app/services`) for domain logic.
3. **Analytics Layer** (`app/analytics`) for graph intelligence (risk propagation).
4. **Core Layer** (`app/core`) for config, logging, security, exceptions.

## Current differentiator
- Graph-based **risk propagation engine** that transfers seed risk across transaction paths with decay and edge weights.
- Explanations returned with risk responses to support auditability.

## Next architectural milestones
- Add streaming ingestion boundary (`ingestion/`) with idempotent consumers.
- Add pluggable graph backend interface (NetworkX/Neo4j).
- Add audit replay store for deterministic decision reconstruction.


## Tier-1 additions in this iteration
- Graph backend interface (`GraphBackend`) with in-memory, mock and Neo4j-ready adapter stubs.
- Observability metrics modules for latency, graph size, and tracing quality indicators.
- API middleware with request-id propagation and in-memory rate limiting baseline.
