"""Tests for custom exception mapping."""

from app.core.exceptions import GraphTraversalError, exception_to_http


def test_graph_traversal_error_maps_to_422() -> None:
    exc = GraphTraversalError("failed traversal")
    http_exc = exception_to_http(exc)

    assert http_exc.status_code == 422
    assert http_exc.detail["code"] == "GraphTraversalError"
