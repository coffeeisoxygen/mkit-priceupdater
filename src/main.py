from pathlib import Path

from loguru import logger

from config.settings import get_settings
from mlogging.setup import setup_logging

settings = get_settings()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOG_CONFIG_PATH = BASE_DIR / "log_config.yaml"
setup_logging(config_path=LOG_CONFIG_PATH, env=settings.APP.ENVIRONMENT)


def main():
    logger.bind(env=settings.APP.ENVIRONMENT).debug(
        f"APP settings: {settings.APP.model_dump()}"
    )


if __name__ == "__main__":
    main()
