"""FastAPI application entrypoint."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

from app.core.config import settings
from app.core.logging import setup_logging, get_logger
from app.core.exceptions import BridgeTraceException, exception_to_http
from app.api.routes import health, trace, risk, ai

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
    openapi_url=f"{settings.api_prefix}/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix=settings.api_prefix)
app.include_router(trace.router, prefix=settings.api_prefix)
app.include_router(risk.router, prefix=settings.api_prefix)
app.include_router(ai.router, prefix=settings.api_prefix)

# Exception handler
@app.exception_handler(BridgeTraceException)
async def bridgetrace_exception_handler(request, exc: BridgeTraceException):
    logger.error("application_error", error=exc.message, code=exc.code)
    return JSONResponse(
        status_code=400,
        content={"error": exc.message, "code": exc.code}
    )

# Metrics endpoint
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Root endpoint
@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "docs": f"{settings.api_prefix}/docs"
    }

# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info(
        "application_startup",
        app_name=settings.app_name,
        version=settings.app_version,
        environment=settings.app_env
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
        reload=settings.debug
    )
