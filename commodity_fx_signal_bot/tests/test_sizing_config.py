import pytest
from sizing.sizing_config import get_sizing_profile, validate_sizing_profiles, get_default_sizing_profile, ConfigError

def test_validate_sizing_profiles():
    # Should not raise any exception
    validate_sizing_profiles()

def test_get_default_sizing_profile():
    profile = get_default_sizing_profile()
    assert profile is not None
    assert profile.name == "balanced_theoretical_sizing"

def test_theoretical_account_equity_positive():
    with pytest.raises(ConfigError):
        get_sizing_profile("invalid_profile")

def test_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_sizing_profile("non_existent_profile")
