"""Tests for professional API endpoints and middleware behavior."""


def test_request_id_is_echoed(client, sample_trace_request):
    response = client.post(
        "/api/v2/trace",
        json=sample_trace_request,
        headers={"X-Request-ID": "req-test-123"},
    )
    assert response.status_code == 200
    assert response.headers.get("X-Request-ID") == "req-test-123"


def test_get_risk_by_entity(client):
    response = client.get("/api/v2/risk/entity_001")
    assert response.status_code == 200
    payload = response.json()
    assert payload["entity_id"] == "entity_001"
    assert "explanations" in payload


def test_get_graph_by_entity(client):
    response = client.get("/api/v2/graph/bank_001")
    assert response.status_code == 200
    payload = response.json()
    assert payload["graph"]["entity"] == "bank_001"
    assert "graph_size" in payload


def test_propagation_map_endpoint(client):
    response = client.get("/api/v2/risk/propagation-map/entity_001")
    assert response.status_code == 200
    payload = response.json()
    assert payload["entity_id"] == "entity_001"
    assert "influence" in payload


def test_simulate_endpoint(client):
    response = client.post(
        "/api/v2/simulate",
        json={
            "source_id": "entity_001",
            "target_id": "wallet_new",
            "amount": 25000,
            "risk_transfer": 0.82,
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["simulation"]["target_id"] == "wallet_new"
    assert "projected_risk" in payload
