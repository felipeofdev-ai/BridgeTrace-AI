# BridgeTrace AI

Financial transaction tracing engine using graph analysis and AI-generated compliance explanations.

Models transaction flows across banking systems (PIX), blockchain networks, and traditional payments. Designed for traceability and risk analysis using synthetic data.

> All data is synthetic. This project does not connect to real banking infrastructure.

---

## What it does

- **Multi-hop tracing** — follow transaction chains across entities with configurable depth
- **Risk scoring** — per-entity behavioral risk analysis with time-range filtering
- **AI explanations** — natural language compliance reports via LLM integration
- **Graph visualization** — interactive dashboard for exploring transaction relationships
- **SDK + CLI** — Python SDK and CLI for integration and scripting

---

## Stack

Python · FastAPI · PostgreSQL · Redis · NetworkX · Prometheus · Grafana · Docker

---

## Quickstart

```bash
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI
docker-compose up -d
curl http://localhost:8000/api/v2/health
```

**Trace a transaction chain:**
```bash
curl -X POST http://localhost:8000/api/v2/trace \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-key-1" \
  -H "X-Tenant-ID: demo" \
  -d '{"source_id": "bank_001", "max_hops": 5, "min_amount": 0}'
```

**Python SDK:**
```python
from bridge_trace_sdk import BridgeTraceSDK

sdk = BridgeTraceSDK("http://localhost:8000", api_key="dev-key-1", tenant_id="demo")
sdk.trace("bank_001")
sdk.risk("entity_001")
```

**Generate synthetic demo data:**
```bash
python scripts/generate_synthetic_data.py --count 1000
python examples/scripts/basic_trace.py
```

---

## API

```
GET  /api/v2/health
POST /api/v2/trace
POST /api/v2/risk/analyze
GET  /api/v2/risk/{entity_id}
GET  /api/v2/graph/{entity_id}
POST /api/v2/ai/explain
GET  /api/v2/docs          # Swagger UI
```

---

## Monitoring

```bash
docker-compose up -d  # includes Prometheus + Grafana
# Grafana: http://localhost:3000 (admin/admin)
# Prometheus: http://localhost:9090
```

---

## Testing

```bash
make test
pytest --cov=app --cov-report=html
```

---

## Project structure

```
app/
  api/            # FastAPI routes
  services/       # Business logic
  repositories/   # Data access
  models/         # Domain models
  schemas/        # Pydantic schemas
sdk/              # Python SDK
tests/            # Unit, integration, E2E
monitoring/       # Prometheus + Grafana configs
docs/             # Architecture, security, system design
```

---

MIT License · [@felipeofdev-ai](https://github.com/felipeofdev-ai)
