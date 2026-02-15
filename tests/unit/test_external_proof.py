"""Tests for reproducible external proof artifacts."""

from scripts.benchmark_risk_engine import run_benchmark


def test_benchmark_is_deterministic_for_same_seed() -> None:
    a = run_benchmark(seed=42, runs_count=3)
    b = run_benchmark(seed=42, runs_count=3)

    assert a["seed"] == b["seed"] == 42
    assert a["rows"]["propagation"]["precision"] == b["rows"]["propagation"]["precision"]
    assert a["rows"]["bfs"]["recall"] == b["rows"]["bfs"]["recall"]
    assert a["scalability"] == b["scalability"]
