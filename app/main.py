"""FastAPI application entrypoint."""

from __future__ import annotations

import time
import uuid
from collections import defaultdict, deque

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.responses import FileResponse, Response

from app.api.routes import ai, demo, health, playground, professional, risk, trace
from app.core.config import settings
from app.core.enterprise import AuditEntry, TenantContext, audit_logger, business_metrics, tenant_quota_manager
from app.core.exceptions import BridgeTraceException, exception_to_http
from app.core.logging import get_logger, setup_logging
from app.core.security import authenticate_request

# Setup logging
setup_logging()
logger = get_logger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Enterprise Financial Traceability Engine",
    docs_url=f"{settings.api_prefix}/docs",
    redoc_url=f"{settings.api_prefix}/redoc",
    openapi_url=f"{settings.api_prefix}/openapi.json",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_REQUEST_LIMIT = 120
_REQUEST_WINDOW_SECONDS = 60
_request_counters: dict[str, deque] = defaultdict(deque)


@app.middleware("http")
async def request_id_and_rate_limit(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    client_ip = request.client.host if request.client else "unknown"
    tenant_id = request.headers.get("X-Tenant-ID", "public")
    tenant = TenantContext(tenant_id=tenant_id, quota_per_minute=settings.default_tenant_quota_per_minute)

    now = time.time()
    queue = _request_counters[client_ip]
    while queue and queue[0] < now - _REQUEST_WINDOW_SECONDS:
        queue.popleft()
    if len(queue) >= _REQUEST_LIMIT:
        return JSONResponse(
            status_code=429,
            content={"message": "Rate limit exceeded", "request_id": request_id},
            headers={"X-Request-ID": request_id},
        )

    protected_path = request.url.path.startswith(settings.api_prefix)
    is_public_endpoint = any(
        request.url.path.startswith(p)
        for p in [
            f"{settings.api_prefix}/health",
            f"{settings.api_prefix}/docs",
            f"{settings.api_prefix}/openapi.json",
            f"{settings.api_prefix}/demo",
            f"{settings.api_prefix}/playground",
        ]
    )

    if protected_path and not is_public_endpoint:
        api_key = request.headers.get("X-API-Key")
        auth_header = request.headers.get("Authorization")
        is_authenticated = authenticate_request(api_key, auth_header)
        if settings.enterprise_auth_enforced and not is_authenticated:
            return JSONResponse(
                status_code=401,
                content={"message": "Authentication required", "request_id": request_id},
                headers={"X-Request-ID": request_id},
            )

        if not tenant_quota_manager.allow(tenant):
            audit_logger.log(
                AuditEntry(
                    at=time.time(),
                    tenant_id=tenant_id,
                    action="quota_check",
                    request_id=request_id,
                    outcome="denied",
                    metadata={"path": request.url.path},
                )
            )
            return JSONResponse(
                status_code=429,
                content={"message": "Tenant quota exceeded", "request_id": request_id},
                headers={"X-Request-ID": request_id},
            )

    queue.append(now)
    started = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - started

    if request.url.path.startswith(f"{settings.api_prefix}/trace"):
        business_metrics.record_trace(elapsed)
    if request.url.path.startswith(f"{settings.api_prefix}/risk"):
        business_metrics.record_risk(detected=response.status_code == 200)

    audit_logger.log(
        AuditEntry(
            at=time.time(),
            tenant_id=tenant_id,
            action="api_call",
            request_id=request_id,
            outcome=str(response.status_code),
            metadata={"path": request.url.path, "method": request.method},
        )
    )

    response.headers["X-Request-ID"] = request_id
    response.headers["X-Tenant-ID"] = tenant_id
    return response


# Include routers
app.include_router(health.router, prefix=settings.api_prefix)
app.include_router(trace.router, prefix=settings.api_prefix)
app.include_router(risk.router, prefix=settings.api_prefix)
app.include_router(ai.router, prefix=settings.api_prefix)
app.include_router(professional.router, prefix=settings.api_prefix)
app.include_router(demo.router, prefix=settings.api_prefix)
app.include_router(playground.router, prefix=settings.api_prefix)


# Exception handler
@app.exception_handler(BridgeTraceException)
async def bridgetrace_exception_handler(request, exc: BridgeTraceException):
    logger.error("application_error", error=exc.message, code=exc.code)
    http_exc = exception_to_http(exc)
    return JSONResponse(status_code=http_exc.status_code, content=http_exc.detail)


# Metrics endpoint
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/metrics/business")
async def business_metrics_snapshot():
    return business_metrics.snapshot()


@app.get("/audit/logs")
async def audit_logs(limit: int = 50):
    return {"entries": audit_logger.tail(limit)}


@app.get("/dashboard")
async def dashboard():
    return FileResponse("frontend/tier1_dashboard.html")


@app.get("/playground")
async def hosted_playground():
    return FileResponse("frontend/playground.html")


# Root endpoint
@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "docs": f"{settings.api_prefix}/docs",
    }


# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info(
        "application_startup",
        app_name=settings.app_name,
        version=settings.app_version,
        environment=settings.app_env,
    )


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("application_shutdown")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug,
    )
