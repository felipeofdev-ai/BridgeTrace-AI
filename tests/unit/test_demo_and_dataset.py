"""Tests for interactive demo endpoints and public dataset generator."""

from pathlib import Path

from scripts.generate_public_dataset_v1 import generate_rows


def test_demo_graph_endpoint(client):
    response = client.get("/api/v2/demo/graph")
    assert response.status_code == 200
    payload = response.json()
    assert "nodes" in payload and "links" in payload
    assert len(payload["nodes"]) > 0


def test_demo_timeline_endpoint(client):
    response = client.get("/api/v2/demo/timeline")
    assert response.status_code == 200
    payload = response.json()
    assert "events" in payload
    assert len(payload["events"]) >= 1


def test_dataset_generator_deterministic():
    rows_a = generate_rows(5, 7)
    rows_b = generate_rows(5, 7)
    assert rows_a == rows_b
    assert all("pattern" in row for row in rows_a)


def test_dashboard_page_served(client):
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert "Interactive Tier-1 Demo" in response.text
    assert Path("frontend/tier1_dashboard.html").exists()


def test_demo_replay_endpoint(client):
    response = client.get("/api/v2/demo/replay")
    assert response.status_code == 200
    payload = response.json()
    assert "replay" in payload
    assert len(payload["replay"]) >= 1
