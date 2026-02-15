# Installation Guide

## Prerequisites
- Python 3.9+
- `pip`
- Docker (optional, for full stack)

## Local setup
```bash
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Developer setup
```bash
pip install -r requirements-dev.txt
pre-commit install
pytest -q -o addopts=''
```

## Docker setup
```bash
docker-compose up -d --build
curl http://localhost:8000/api/v2/health
```
