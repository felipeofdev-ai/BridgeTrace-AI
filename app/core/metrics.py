"""Prometheus metrics."""
from prometheus_client import Counter, Histogram, Gauge

api_requests_total = Counter(
    "api_requests_total",
    "Total API requests",
    ["method", "endpoint", "status"]
)

api_request_duration = Histogram(
    "api_request_duration_seconds",
    "API request duration",
    ["method", "endpoint"]
)

trace_operations_total = Counter(
    "trace_operations_total",
    "Total trace operations",
    ["operation_type"]
)

active_traces = Gauge(
    "active_traces",
    "Number of active trace operations"
)
