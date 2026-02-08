"""Test trace endpoints."""

def test_trace_flow(client, sample_trace_request):
    response = client.post("/api/v2/trace/", json=sample_trace_request)
    assert response.status_code == 200
    data = response.json()
    assert "source_id" in data
    assert data["source_id"] == "bank_001"
