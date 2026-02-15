# Security Policy

## Supported Versions
- `2.x` receives active security updates.

## Reporting a Vulnerability
Please report vulnerabilities privately to: `security@bridgetrace.ai`.

Include:
- affected component and version
- proof of concept or reproduction steps
- impact assessment (CIA)

We follow coordinated disclosure:
- acknowledgement in 48h
- triage in 5 business days
- remediation timeline based on severity (Critical: 72h target)

## Security Controls (Current)
- JWT and API key authentication support
- Request ID propagation and audit logs
- Tenant quotas and rate limiting baseline
- Structured logging and metrics endpoints

## Hardening Roadmap
- key rotation automation
- secret manager integration
- distributed rate limiting
- mTLS for service-to-service communication
