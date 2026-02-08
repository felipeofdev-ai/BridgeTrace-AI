# Development Guide

## Setup Development Environment

### Prerequisites
- Python 3.9+
- PostgreSQL 16+
- Redis 7+
- Docker (optional)

### Initial Setup
```bash
# Clone repository
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Setup pre-commit hooks
pre-commit install

# Copy environment file
cp .env.example .env
# Edit .env with your settings
```

## Development Workflow

### Running Locally
```bash
# Start API with auto-reload
make dev

# Or directly with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Code Quality

#### Formatting
```bash
# Format with black
black app/

# Sort imports
isort app/
```

#### Linting
```bash
# Lint with ruff
ruff check app/

# Type checking
mypy app/
```

#### Security
```bash
# Security scan
bandit -r app/

# Dependency check
safety check
```

### Testing

#### Run Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=app --cov-report=html

# Specific test
pytest tests/unit/test_trace.py -v

# Integration tests only
pytest tests/integration/ -v
```

#### Writing Tests
```python
# tests/unit/test_my_feature.py
import pytest

def test_my_feature(client):
    response = client.get("/api/v2/my-endpoint")
    assert response.status_code == 200
    assert "expected_key" in response.json()
```

## Architecture Patterns

### Service Layer
```python
# app/services/my_service.py
from app.core.logging import get_logger

logger = get_logger(__name__)

class MyService:
    async def do_something(self, param: str) -> dict:
        logger.info("operation_started", param=param)
        # Business logic here
        return {"result": "success"}
```

### API Route
```python
# app/api/routes/my_route.py
from fastapi import APIRouter, Depends
from app.services.my_service import MyService

router = APIRouter(prefix="/my", tags=["My Feature"])

@router.post("/")
async def my_endpoint(
    service: MyService = Depends(get_my_service)
):
    return await service.do_something("param")
```

## Database Migrations

### Create Migration
```bash
alembic revision --autogenerate -m "Add new table"
```

### Apply Migrations
```bash
alembic upgrade head
```

### Rollback
```bash
alembic downgrade -1
```

## Debugging

### VS Code
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["app.main:app", "--reload"],
      "jinja": true
    }
  ]
}
```

### IPython
```bash
pip install ipython ipdb

# Add breakpoint in code
import ipdb; ipdb.set_trace()
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines.
