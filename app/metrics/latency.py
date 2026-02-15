"""Latency metrics helpers."""

from __future__ import annotations

import time
from contextlib import contextmanager

from prometheus_client import Histogram

TRACE_LATENCY_SECONDS = Histogram(
    "trace_latency_seconds",
    "Latency of trace and simulation operations",
    ["operation"],
)


@contextmanager
def track_latency(operation: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        TRACE_LATENCY_SECONDS.labels(operation=operation).observe(time.perf_counter() - start)
