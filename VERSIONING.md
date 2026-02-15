# Versioning Policy

BridgeTrace-AI follows **Semantic Versioning 2.0.0**.

## Format
`MAJOR.MINOR.PATCH`

- **MAJOR**: incompatible API or behavior changes
- **MINOR**: backward-compatible features
- **PATCH**: backward-compatible bug fixes

## API Compatibility
- API version prefix (`/api/v2`) is stable for all `2.x` releases.
- Breaking API changes require a new prefix (`/api/v3`).

## Deprecation Policy
- Deprecated endpoints are announced in `CHANGELOG.md`.
- Minimum deprecation window: 2 minor releases.
