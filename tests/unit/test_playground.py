"""Tests for hosted playground public endpoints."""


def test_playground_page_served(client):
    response = client.get('/playground')
    assert response.status_code == 200
    assert 'Hosted Playground' in response.text


def test_playground_ping(client):
    response = client.get('/api/v2/playground/ping')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_playground_sample_trace(client):
    response = client.get('/api/v2/playground/sample-trace')
    assert response.status_code == 200
    assert response.json()['total_paths'] >= 1
