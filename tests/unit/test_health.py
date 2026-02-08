"""Test health endpoints."""

def test_health_check(client):
    response = client.get("/api/v2/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_readiness(client):
    response = client.get("/api/v2/health/ready")
    assert response.status_code == 200
    assert response.json()["ready"] is True
