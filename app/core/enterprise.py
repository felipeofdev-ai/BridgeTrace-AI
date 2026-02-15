"""Enterprise controls: tenant quotas, audit logs, and business metrics."""

from __future__ import annotations

import time
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class TenantContext:
    tenant_id: str
    plan: str = "free"
    quota_per_minute: int = 120


@dataclass
class AuditEntry:
    at: float
    tenant_id: str
    action: str
    request_id: str
    outcome: str
    metadata: Dict[str, Any] = field(default_factory=dict)


class TenantQuotaManager:
    def __init__(self):
        self._tenant_calls: Dict[str, deque] = defaultdict(deque)

    def allow(self, tenant: TenantContext, now: float | None = None) -> bool:
        now = now or time.time()
        queue = self._tenant_calls[tenant.tenant_id]
        while queue and queue[0] < now - 60:
            queue.popleft()
        if len(queue) >= tenant.quota_per_minute:
            return False
        queue.append(now)
        return True


class AuditLogger:
    def __init__(self):
        self._entries: List[AuditEntry] = []

    def log(self, entry: AuditEntry) -> None:
        self._entries.append(entry)

    def tail(self, limit: int = 100) -> List[Dict[str, Any]]:
        return [e.__dict__ for e in self._entries[-limit:]]


class BusinessMetrics:
    def __init__(self):
        self.trace_count = 0
        self.risk_count = 0
        self.false_positive_count = 0
        self.detected_count = 0
        self.total_trace_seconds = 0.0
        self.total_operations = 0

    def record_trace(self, duration_seconds: float) -> None:
        self.trace_count += 1
        self.total_operations += 1
        self.total_trace_seconds += duration_seconds

    def record_risk(self, detected: bool = False, false_positive: bool = False) -> None:
        self.risk_count += 1
        self.total_operations += 1
        if detected:
            self.detected_count += 1
        if false_positive:
            self.false_positive_count += 1

    def snapshot(self) -> Dict[str, Any]:
        avg_trace = self.total_trace_seconds / self.trace_count if self.trace_count else 0.0
        detection_rate = self.detected_count / self.risk_count if self.risk_count else 0.0
        false_positive_rate = self.false_positive_count / self.risk_count if self.risk_count else 0.0
        throughput_per_sec = self.total_operations / max(self.total_trace_seconds, 1.0)
        cost_per_million_ops = 12.5  # placeholder estimate for planning
        return {
            "avg_trace_seconds": round(avg_trace, 6),
            "detection_rate": round(detection_rate, 6),
            "false_positive_rate": round(false_positive_rate, 6),
            "throughput_per_second": round(throughput_per_sec, 4),
            "cost_per_1m_operations_usd": cost_per_million_ops,
        }


tenant_quota_manager = TenantQuotaManager()
audit_logger = AuditLogger()
business_metrics = BusinessMetrics()
