import pytest
from notifications.notification_config import get_notification_profile, list_notification_profiles, validate_notification_profiles, get_default_notification_profile, ConfigError

def test_validate_notification_profiles_no_error():
    validate_notification_profiles() # Should not raise

def test_get_default_notification_profile():
    profile = get_default_notification_profile()
    assert profile is not None
    assert profile.name == "balanced_telegram_reporting"

def test_message_max_chars_positive():
    profile = get_notification_profile("balanced_telegram_reporting")
    assert profile.message_max_chars > 0

def test_unknown_profile_raises_error():
    with pytest.raises(ConfigError):
        get_notification_profile("non_existent_profile")
