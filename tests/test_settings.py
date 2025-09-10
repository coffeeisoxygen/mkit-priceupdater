from pathlib import Path

from config.settings import Settings, get_settings


def test_get_settings_with_test_env():
    base_dir = Path(__file__).resolve().parent.parent
    env_file = base_dir / ".env.test"
    settings = get_settings(_env_file=env_file)
    assert isinstance(settings, Settings)
    assert settings.APP.ENVIRONMENT == "testing"
    assert settings.APP.DEBUG is False


def test_get_settings_with_dev_env():
    base_dir = Path(__file__).resolve().parent.parent
    env_file = base_dir / ".env.dev"
    settings = get_settings(_env_file=env_file)
    assert isinstance(settings, Settings)
    assert settings.APP.ENVIRONMENT == "development"
    assert settings.APP.DEBUG is False
