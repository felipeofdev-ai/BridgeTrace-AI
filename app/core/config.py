"""Application configuration management."""

from functools import lru_cache
from typing import Optional

from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    # App
    app_name: str = "BridgeTrace AI"
    app_version: str = "2.0.0"
    app_env: str = "development"
    debug: bool = False

    # API
    api_prefix: str = "/api/v2"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # Security
    secret_key: str = "CHANGE_IN_PRODUCTION"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    api_keys_csv: str = "dev-key-1,dev-key-2"
    api_key_rotation_days: int = 30
    enterprise_auth_enforced: bool = False

    # Enterprise tenancy
    default_tenant_quota_per_minute: int = 120

    # Database
    database_url: Optional[PostgresDsn] = None

    # Redis
    redis_url: Optional[RedisDsn] = None

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"

    # AI
    openai_api_key: Optional[str] = None
    llm_model: str = "gpt-4"

    # Tracing
    max_trace_hops: int = 10

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
