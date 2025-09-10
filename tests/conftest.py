# testing environment
from pathlib import Path

from config.settings import get_settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEST_ENV_FILE = BASE_DIR / ".env.test"


test_settings = get_settings(_env_file=TEST_ENV_FILE)
