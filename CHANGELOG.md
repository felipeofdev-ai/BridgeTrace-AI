# Changelog

All notable changes to BridgeTrace AI are documented in this file.

The format follows Keep a Changelog and Semantic Versioning.

## [Unreleased]

### Added
- Enterprise credibility docs: `SECURITY.md`, `SLA.md`, `VERSIONING.md`, `THREAT_MODEL.md`.
- Compliance readiness and architecture artifacts: `docs/COMPLIANCE_READINESS.md`, `SYSTEM_DESIGN.md`, `SCALING_STRATEGY.md`, `FAILURE_SCENARIOS.md`.
- Business metrics endpoint `GET /metrics/business` and audit endpoint `GET /audit/logs`.
- Tenant-aware quota controls and audit logging primitives.

### Changed
- Main middleware now supports tenant headers, optional auth enforcement, and enterprise audit trails.
- Security module now supports API key validation and bearer-token based request authentication.

### Documentation
- Added `docs/PERFORMANCE_PROOF.md` with engine comparison matrix.
- Added `docs/DISTRIBUTION_ROADMAP.md` for adoption strategy.

## [2.0.0] - 2026-02-08

### Added
- Complete enterprise architecture refactor
- Clean Architecture implementation
- PostgreSQL database integration
- Redis caching layer
- Prometheus + Grafana monitoring
- Structured logging with structlog
- JWT authentication and authorization
- Comprehensive test suite
- CI/CD with GitHub Actions
- Docker and Kubernetes support
- API versioning (v2)
- Health check endpoints
- Metrics endpoint
- OpenTelemetry instrumentation

### Changed
- Migrated to FastAPI async patterns
- Improved error handling
- Enhanced security measures
- Updated documentation

### Performance
- Added Redis caching
- Optimized database queries
- Implemented connection pooling

## [1.0.0] - 2026-02-06

### Added
- Initial release
- Basic tracing functionality
- Risk analysis
- Simple web dashboard
- Synthetic data examples
