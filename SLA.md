# Service Level Agreement (SLA)

## Availability Targets
- API availability: **99.9%** monthly
- Critical endpoints (`/api/v2/trace`, `/api/v2/risk/*`): **99.95%** objective (enterprise tier)

## Performance Targets
- `POST /api/v2/trace`: p95 < 1.5s
- `GET /api/v2/risk/{entity}`: p95 < 800ms
- `GET /metrics/business`: p95 < 300ms

## Support Windows
- P1 incidents: 24/7 response, first response within 30 minutes
- P2 incidents: business hours, first response within 4 hours

## Exclusions
Planned maintenance windows and upstream cloud outages are excluded and communicated in advance.
