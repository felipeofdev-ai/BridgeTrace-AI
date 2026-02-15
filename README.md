# 🌉 BridgeTrace AI v2.0 - Enterprise Edition

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-teal?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![CI](https://img.shields.io/github/workflow/status/felipeofdev-ai/BridgeTrace-AI/CI?style=for-the-badge)
![Benchmark Reproducible](https://img.shields.io/badge/Benchmark-Reproducible-success?style=for-the-badge)
![Deterministic Engine](https://img.shields.io/badge/Deterministic%20Engine-Yes-success?style=for-the-badge)
![External Validation](https://img.shields.io/badge/External%20Validation-Pending-orange?style=for-the-badge)

**Enterprise-Grade Financial Traceability Engine**

Unified platform for tracing financial flows across banking systems (PIX), blockchain networks, and traditional payments using graph theory, AI, and advanced analytics.

[📖 Documentation](#documentation) • [🚀 Quick Start](#quick-start) • [🏗️ Architecture](#architecture) • [🤝 Contributing](#contributing)

</div>

---

## ✨ Features

## 🎯 Why BridgeTrace-AI

**BridgeTrace-AI combines graph-native risk propagation with explainable outputs so compliance teams can act in minutes, not days.**

---


### Core Capabilities
- 🔗 **Unified Graph Model** - Banking + PIX + Crypto in one graph
- 🔍 **Multi-Hop Tracing** - Follow money through complex transaction paths
- 🎯 **Risk Scoring** - AI-powered behavioral risk analysis
- 🤖 **AI Explanations** - Natural language compliance reports
- 📊 **Real-time Monitoring** - Prometheus + Grafana dashboards
- 🔐 **Enterprise Security** - JWT auth, encryption, audit logs

### Technical Excellence
- ⚡ **High Performance** - Async Python, Redis caching
- 🏗️ **Clean Architecture** - Separation of concerns, SOLID principles
- 🐳 **Container-Native** - Docker, Kubernetes-ready
- 📈 **Observable** - Structured logging, metrics, tracing
- 🧪 **Tested** - Unit, integration, and E2E tests
- 🔄 **CI/CD Ready** - GitHub Actions, automated deployments

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker & Docker Compose
- PostgreSQL 16+ (or use Docker)
- Redis 7+ (or use Docker)

### Installation

#### Option 1: Docker (Recommended)
```bash
# Clone repository
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# Start all services
docker-compose up -d

# Check health
curl http://localhost:8000/api/v2/health
```

#### Option 2: Local Development
```bash
# Clone repository
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your configuration

# Run migrations
alembic upgrade head

# Start API
uvicorn app.main:app --reload
```

### Generate Demo Data
```bash
python scripts/generate_synthetic_data.py --count 1000
python examples/scripts/basic_trace.py
```


### Generate Public Dataset v1
```bash
python scripts/generate_public_dataset_v1.py --rows 500 --seed 42
```

### Access Services
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/api/v2/docs
- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090
- **Dashboard Demo**: http://localhost:8000/dashboard
- **Business Metrics**: http://localhost:8000/metrics/business
- **Hosted Playground**: http://localhost:8000/playground

---


## ⚡ 5-Minute Integration

```bash
# 1) Start API
uvicorn app.main:app --reload

# 2) Health check
curl http://localhost:8000/api/v2/health

# 3) Functional trace call
curl -X POST http://localhost:8000/api/v2/trace \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-key-1" \
  -H "X-Tenant-ID: demo" \
  -d '{"source_id":"bank_001","max_hops":5,"min_amount":0}'

# 4) Risk by entity
curl "http://localhost:8000/api/v2/risk/entity_001?days=30" \
  -H "X-API-Key: dev-key-1" \
  -H "X-Tenant-ID: demo"
```

Python SDK minimal example:
```python
from bridge_trace_sdk import BridgeTraceSDK

sdk = BridgeTraceSDK("http://localhost:8000", api_key="dev-key-1", tenant_id="demo")
print(sdk.trace("bank_001"))
print(sdk.risk("entity_001"))
```

CLI example:
```bash
python scripts/bt_cli.py --base-url http://localhost:8000 --api-key dev-key-1 --tenant demo trace --source bank_001
python scripts/bt_cli.py --base-url http://localhost:8000 --api-key dev-key-1 --tenant demo risk --entity entity_001
```

---

## 🔬 External Reproducibility Proof

Run the exact public proof pipeline (dataset + benchmark + checksums):

```bash
./scripts/run_external_proof.sh
```

This generates reproducible artifacts and SHA256 fingerprints under `artifacts/`.

---

## 🌐 Hosted Playground (Public Mode)

Open instantly in browser:

- `GET /playground`
- `GET /api/v2/playground/ping`
- `GET /api/v2/playground/sample-trace`
- `GET /api/v2/playground/sample-risk`
- `GET /api/v2/demo/replay`

---

## 📖 Documentation

- [Fortune 500 Tier-1 Enhancements Roadmap](docs/FORTUNE500_TIER1_ENHANCEMENTS.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Installation Guide](docs/INSTALLATION.md)
- [API Reference](docs/API_REFERENCE.md)
- [Architecture Decisions](docs/ARCHITECTURE.md)
- [Algorithm Spec](docs/ALGORITHM.md)
- [BridgeTrace Technical Paper v1](docs/papers/BRIDGETRACE_TECHNICAL_PAPER_V1.md)
- [BridgeTrace Synthetic Dataset v1](docs/datasets/BRIDGETRACE_SYNTHETIC_DATASET_V1.md)
- [Security Policy](SECURITY.md)
- [SLA](SLA.md)
- [Versioning Policy](VERSIONING.md)
- [Threat Model](THREAT_MODEL.md)
- [Compliance Readiness](docs/COMPLIANCE_READINESS.md)
- [System Design](SYSTEM_DESIGN.md)
- [Scaling Strategy](SCALING_STRATEGY.md)
- [Failure Scenarios](FAILURE_SCENARIOS.md)
- [Performance Proof](docs/PERFORMANCE_PROOF.md)
- [Distribution Roadmap](docs/DISTRIBUTION_ROADMAP.md)
- [5-Minute Quickstart](docs/QUICKSTART_5MIN.md)
- [SDK Publishing Plan](docs/SDK_PUBLISHING.md)
- [Formal Whitepaper v1.0.0](docs/papers/WHITEPAPER_FORMAL_V1_0.md)
- [Scientific Changelog](docs/papers/SCIENTIFIC_CHANGELOG.md)
- [Official Competitive Comparison](docs/COMPETITIVE_COMPARISON.md)

### API Endpoints

#### Health Checks
```http
GET /api/v2/health          # Health status
GET /api/v2/health/ready    # Readiness probe
GET /api/v2/health/live     # Liveness probe
```

#### Tracing
```http
POST /api/v2/trace/
Content-Type: application/json

{
  "source_id": "bank_001",
  "max_hops": 5,
  "min_amount": 1000.0
}
```

#### Risk Analysis
```http
POST /api/v2/risk/analyze
Content-Type: application/json

{
  "entity_id": "entity_001",
  "time_range_days": 30
}
```

#### Professional API (Tier-1)
```http
POST /api/v2/trace
GET /api/v2/risk/{entity_id}
GET /api/v2/risk/propagation-map/{entity_id}
GET /api/v2/graph/{entity_id}
POST /api/v2/simulate
```

#### AI Explanations
```http
POST /api/v2/ai/explain
Content-Type: application/json

{
  "trace_data": { ... }
}
```

### Architecture

```
┌─────────────────────────────────────────────────────┐
│                   API Layer (FastAPI)                │
├─────────────────────────────────────────────────────┤
│              Services (Business Logic)              │
├─────────────────────────────────────────────────────┤
│         Repositories (Data Access Layer)            │
├─────────────────────────────────────────────────────┤
│    Models & Schemas (Domain & Contracts)           │
├─────────────────────────────────────────────────────┤
│   Infrastructure (PostgreSQL, Redis, Monitoring)   │
└─────────────────────────────────────────────────────┘
```

**Key Principles:**
- Clean Architecture with clear layer separation
- Dependency Injection for testability
- Domain-Driven Design patterns
- CQRS for complex operations

---

## 🏗️ Project Structure

```
BridgeTrace-AI/
├── app/
│   ├── core/              # Configuration, logging, security
│   ├── api/               # HTTP layer (routes, dependencies)
│   ├── services/          # Business logic
│   ├── repositories/      # Data access
│   ├── models/            # Domain models
│   ├── schemas/           # Pydantic schemas
│   └── utils/             # Utilities
├── tests/                 # Automated tests
├── alembic/              # Database migrations
├── monitoring/           # Prometheus, Grafana configs
├── docs/                 # Documentation
├── scripts/              # Utility scripts
└── frontend/             # Web dashboard

```

---

## 🧪 Testing

```bash
# Run all tests
make test

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test
pytest tests/unit/test_trace.py -v

# Run integration tests
pytest tests/integration/ -v
```

---

## 🔒 Security

- **Authentication**: JWT tokens with configurable expiration
- **Authorization**: Role-based access control (RBAC)
- **Encryption**: All sensitive data encrypted at rest
- **Audit Logs**: Complete audit trail of all operations
- **Security Scanning**: Automated vulnerability scanning in CI
- **OWASP Compliance**: Following security best practices

---

## 📊 Monitoring

### Metrics (Prometheus)
- API request duration
- Error rates
- Active traces
- Cache hit ratios
- Database connection pool

### Dashboards (Grafana)
- System health overview
- API performance
- Business metrics
- Alert management

### Logging
- Structured JSON logs
- Centralized log aggregation ready
- Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

---

## 🚢 Deployment

### Docker
```bash
docker build -t bridgetrace-ai:latest .
docker run -p 8000:8000 bridgetrace-ai:latest
```

### Kubernetes
```bash
kubectl apply -f k8s/
```

### Cloud Platforms
- **AWS**: ECS, EKS, or Elastic Beanstalk
- **GCP**: Cloud Run, GKE, or App Engine
- **Azure**: AKS, Container Instances, or App Service

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'feat: Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Commit Convention
```
feat: New feature
fix: Bug fix
docs: Documentation
style: Formatting
refactor: Code restructuring
test: Tests
chore: Maintenance
```

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## 👤 Author

**Felipe de Oliveira Fernandes**

- GitHub: [@felipeofdev-ai](https://github.com/felipeofdev-ai)
- LinkedIn:[https://linkedin.com/in/felipe-fernandes](https://www.linkedin.com/in/felipe-de-oliveira-fernandes-941763110/)
- Email: felipe.of.dev@gmail.com

---

## 🙏 Acknowledgments

- FastAPI framework and community
- NetworkX for graph algorithms
- Structlog for structured logging
- All contributors and supporters

---

## ⚠️ Disclaimer

This project uses 100% synthetic data for demonstration purposes. It does not connect to real banking systems, PIX infrastructure, or live blockchain networks.

**For educational, research, and demonstration purposes only.**

---

<div align="center">

**⭐ Star this repository if you find it useful!**

**Built with ❤️ by Felipe de Oliveira Fernandes**

</div>
