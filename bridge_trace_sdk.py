"""Minimal Python SDK for BridgeTrace API quick integrations."""

from __future__ import annotations

from typing import Any, Dict

import httpx


class BridgeTraceSDK:
    def __init__(self, base_url: str, api_key: str | None = None, tenant_id: str = "public"):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.tenant_id = tenant_id

    def _headers(self) -> Dict[str, str]:
        headers = {"X-Tenant-ID": self.tenant_id}
        if self.api_key:
            headers["X-API-Key"] = self.api_key
        return headers

    def trace(self, source_id: str, max_hops: int = 5, min_amount: float = 0.0) -> Dict[str, Any]:
        response = httpx.post(
            f"{self.base_url}/api/v2/trace",
            json={"source_id": source_id, "max_hops": max_hops, "min_amount": min_amount},
            headers=self._headers(),
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def risk(self, entity_id: str, days: int = 30) -> Dict[str, Any]:
        response = httpx.get(
            f"{self.base_url}/api/v2/risk/{entity_id}",
            params={"days": days},
            headers=self._headers(),
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
