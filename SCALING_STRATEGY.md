# Scaling Strategy

## Horizontal API Scaling
- stateless API workers
- externalize quota/audit stores (Redis/Postgres)

## Compute Scaling
- offload heavy simulations to worker queue
- batch risk recomputation by tenant

## Graph Scaling
- in-memory for dev
- migrate to Neo4j/TigerGraph backend for production

## Observability Scaling
- Prometheus scraping + remote write
- business KPIs streamed to warehouse
