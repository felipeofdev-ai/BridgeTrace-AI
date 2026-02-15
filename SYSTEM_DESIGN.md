# System Design

BridgeTrace-AI is structured as:
- FastAPI API layer
- service layer for trace/risk/simulation
- analytics engine for risk propagation
- pluggable graph backend abstraction
- observability + business metrics

Data flow:
1. request enters middleware (request-id/auth/quota/audit)
2. routed to service method
3. graph traversal/propagation executed
4. metrics and audit entries emitted
5. response returned with tenant/request headers
