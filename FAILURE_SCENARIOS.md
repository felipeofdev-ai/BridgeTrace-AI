# Failure Scenarios

## Scenario 1: Traffic Spike / DoS-like burst
- symptom: elevated 429, latency spikes
- response: enforce stricter quota/rate limits, autoscale API

## Scenario 2: Graph backend latency regression
- symptom: trace p95 exceeds SLO
- response: degrade to cached responses, trigger incident policy

## Scenario 3: Cross-tenant data risk
- symptom: incorrect tenant headers or mixed audit entries
- response: block suspect requests, run audit replay, rotate keys

## Scenario 4: Key compromise
- symptom: unusual authenticated traffic
- response: revoke/rotate API keys, force JWT invalidation
