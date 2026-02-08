"""Pytest configuration and fixtures."""
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_trace_request():
    return {
        "source_id": "bank_001",
        "max_hops": 5,
        "min_amount": 0.0
    }
