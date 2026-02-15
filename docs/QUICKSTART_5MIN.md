# 5-Minute Quickstart

## Copy/Paste Flow
```bash
uvicorn app.main:app --reload
curl http://localhost:8000/api/v2/health
curl -X POST http://localhost:8000/api/v2/trace \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-key-1" \
  -H "X-Tenant-ID: demo" \
  -d '{"source_id":"bank_001","max_hops":5,"min_amount":0}'
```

## SDK (Python)
```python
from bridge_trace_sdk import BridgeTraceSDK
sdk = BridgeTraceSDK("http://localhost:8000", api_key="dev-key-1", tenant_id="demo")
print(sdk.risk("entity_001"))
```

## CLI
```bash
python scripts/bt_cli.py --base-url http://localhost:8000 --api-key dev-key-1 --tenant demo risk --entity entity_001
```
