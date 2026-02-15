"""Tests for enterprise controls and security helpers."""

from app.core.security import authenticate_request, create_access_token, validate_api_key


def test_validate_api_key_default_dev_key() -> None:
    assert validate_api_key("dev-key-1") is True
    assert validate_api_key("invalid-key") is False


def test_authenticate_with_bearer_token() -> None:
    token = create_access_token({"sub": "test-user"})
    assert authenticate_request(None, f"Bearer {token}") is True


def test_business_metrics_endpoint(client) -> None:
    response = client.get("/metrics/business")
    assert response.status_code == 200
    payload = response.json()
    assert "avg_trace_seconds" in payload
    assert "detection_rate" in payload


def test_audit_logs_endpoint(client) -> None:
    response = client.get("/audit/logs")
    assert response.status_code == 200
    payload = response.json()
    assert "entries" in payload
