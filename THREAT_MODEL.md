# Threat Model

## Assets
- financial transaction metadata
- risk scores and propagation maps
- tenant usage/audit logs

## Trust Boundaries
- external client -> API gateway
- API -> graph engine / storage
- API -> monitoring / logging

## Main Threats (STRIDE)
- **Spoofing**: stolen API keys/JWT
- **Tampering**: request payload manipulation
- **Repudiation**: missing or forged audit trail
- **Information Disclosure**: tenant data leakage
- **Denial of Service**: request floods or expensive graph traversals
- **Elevation of Privilege**: cross-tenant access via weak isolation

## Mitigations (Current)
- request ID + audit logs
- baseline auth support (JWT/API key)
- quota controls per tenant and global rate limiting
- structured logging and observability

## Priority Mitigations (Next)
- enforced auth in production profiles
- distributed quotas and WAF
- data encryption at rest and in transit hardening
