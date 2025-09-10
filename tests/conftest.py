# testing environment

import logging
from pathlib import Path

import pytest
from loguru import logger

from config.settings import get_settings
from mlogging.setup import setup_logging

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEST_ENV_FILE = BASE_DIR / ".env.test"
LOG_CONFIG_PATH = BASE_DIR / "log_config.yaml"

test_settings = get_settings(_env_file=TEST_ENV_FILE)


# intercept logging to loguru
@pytest.fixture(autouse=True)
def intercept_loguru(caplog: pytest.LogCaptureFixture):
    """
    Use the main loguru config for tests, and add a temporary loguru handler for caplog so loguru logs are captured by pytest.
    """
    setup_logging(config_path=LOG_CONFIG_PATH, env=test_settings.APP.ENVIRONMENT)

    # Silence noisy libraries
    for noisy_logger in ["aiosqlite", "asyncio"]:
        logging.getLogger(noisy_logger).setLevel(logging.INFO)

    handler_id = logger.add(
        sink=caplog.handler,
        level="DEBUG",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        enqueue=False,
        colorize=True,
    )
    yield
    logger.remove(handler_id)
