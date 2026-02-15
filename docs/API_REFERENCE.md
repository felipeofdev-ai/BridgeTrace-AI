# API Reference (v2)

Base path: `/api/v2`

## Health
- `GET /health`
- `GET /health/ready`
- `GET /health/live`

## Trace
### `POST /trace/`
Request:
```json
{
  "source_id": "bank_001",
  "max_hops": 5,
  "min_amount": 1000
}
```

## Risk
### `POST /risk/analyze`
Request:
```json
{
  "entity_id": "entity_001",
  "time_range_days": 30
}
```

Response highlights:
- `risk_level`
- `risk_score`
- `metrics`
- `recommendations`
- `explanations`

## AI
### `POST /ai/explain`
Request body: generic trace payload to receive narrative explanation.


## Professional Endpoints
- `POST /trace`
- `GET /risk/{entity_id}`
- `GET /risk/propagation-map/{entity_id}`
- `GET /graph/{entity_id}`
- `POST /simulate`

Headers:
- `X-Request-ID` is accepted and echoed in responses.


## Demo
- `GET /demo/graph`
- `GET /demo/timeline`
- `GET /demo/replay`

UI:
- `GET /dashboard`


## Business & Audit
- `GET /metrics/business`
- `GET /audit/logs?limit=50`

## Enterprise Headers
- `X-Tenant-ID`: tenant isolation context
- `X-API-Key`: rotating API key authentication
- `Authorization: Bearer <token>`: OAuth2/JWT compatible auth


## SDK & CLI
- Python SDK: `bridge_trace_sdk.py`
- CLI: `python scripts/bt_cli.py ...`


## Hosted Playground
- `GET /playground`
- `GET /playground/ping`
- `GET /playground/sample-trace`
- `GET /playground/sample-risk`
