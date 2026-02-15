"""Tracing operation metrics."""

from __future__ import annotations

from prometheus_client import Counter, Gauge

TRACE_REQUESTS_TOTAL = Counter(
    "trace_requests_total",
    "Total trace requests by status",
    ["status"],
)

TRACE_AVG_HOPS = Gauge("trace_avg_hops", "Average hops in trace responses")
TRACE_ERROR_RATE = Gauge("trace_error_rate", "Trace error rate over process lifetime")

_total_requests = 0
_total_errors = 0
_total_hops = 0.0


def record_trace_result(hops: int, success: bool) -> None:
    global _total_requests, _total_errors, _total_hops

    _total_requests += 1
    if success:
        TRACE_REQUESTS_TOTAL.labels(status="success").inc()
    else:
        _total_errors += 1
        TRACE_REQUESTS_TOTAL.labels(status="error").inc()

    _total_hops += float(hops)
    TRACE_AVG_HOPS.set(_total_hops / _total_requests)
    TRACE_ERROR_RATE.set(_total_errors / _total_requests)
