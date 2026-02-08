# 🌉 BridgeTrace AI v2.0 - Enterprise Edition

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-teal?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![CI](https://img.shields.io/github/workflow/status/felipeofdev-ai/BridgeTrace-AI/CI?style=for-the-badge)

**Enterprise-Grade Financial Traceability Engine**

Unified platform for tracing financial flows across banking systems (PIX), blockchain networks, and traditional payments using graph theory, AI, and advanced analytics.

[📖 Documentation](#documentation) • [🚀 Quick Start](#quick-start) • [🏗️ Architecture](#architecture) • [🤝 Contributing](#contributing)

</div>

---

## ✨ Features

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

### Access Services
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/api/v2/docs
- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090

---

## 📖 Documentation

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
- LinkedIn: [Felipe Fernandes](https://linkedin.com/in/felipe-fernandes)
- Email: felipe@bridgetrace.ai

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
