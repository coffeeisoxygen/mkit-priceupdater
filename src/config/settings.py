import os
from functools import lru_cache
from pathlib import Path

from loguru import logger
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_ENV_FILE = BASE_DIR / ".env.dev"


class ConfigEnvironment(BaseModel):
    ENVIRONMENT: str = "production"  # default production
    NAME: str = "mkit-priceupdater"
    VERSION: str = "0.1.0"
    DEBUG: bool = True


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=DEFAULT_ENV_FILE,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
        case_sensitive=False,
    )
    APP: ConfigEnvironment = ConfigEnvironment()


@lru_cache
def get_settings(_env_file: str | Path | None = None) -> Settings:
    """Prioritas:.

    1. Argumen _env_file
    2. ENV_FILE dari environment variable
    3. DEFAULT_ENV_FILE (.env)
    """
    env_file = _env_file or os.getenv("ENV_FILE", DEFAULT_ENV_FILE)
    logger.trace(f"Loading settings from {env_file}")
    return Settings(_env_file=env_file, _env_file_encoding="utf-8")  # type: ignore
