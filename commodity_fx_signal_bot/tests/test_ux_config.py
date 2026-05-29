import pytest
from analyst_ux.ux_config import (
    get_analyst_ux_profile, list_analyst_ux_profiles,
    validate_analyst_ux_profiles, get_default_analyst_ux_profile,
    AnalystUXProfile, ConfigError
)

def test_get_default_analyst_ux_profile():
    profile = get_default_analyst_ux_profile()
    assert profile.name == "balanced_analyst_productivity"
    assert profile.language == "tr"
    assert not profile.allow_live_commands
    assert profile.generate_aliases

def test_validate_analyst_ux_profiles():
    validate_analyst_ux_profiles()

def test_validate_invalid_language():
    invalid_profile = AnalystUXProfile(name="test", description="test", language="")
    import analyst_ux.ux_config as uc
    uc._UX_PROFILES["test"] = invalid_profile
    with pytest.raises(ConfigError):
        validate_analyst_ux_profiles()
    del uc._UX_PROFILES["test"]

def test_validate_live_trading_prevented():
    invalid_profile = AnalystUXProfile(name="test", description="test", allow_live_commands=True)
    import analyst_ux.ux_config as uc
    uc._UX_PROFILES["test"] = invalid_profile
    with pytest.raises(ConfigError):
        validate_analyst_ux_profiles()
    del uc._UX_PROFILES["test"]
