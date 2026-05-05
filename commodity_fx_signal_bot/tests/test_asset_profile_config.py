import pytest
from asset_profiles.asset_profile_config import (
    get_asset_profile,
    validate_asset_profiles,
    ConfigError,
)


def test_validate_asset_profiles():
    # Should run without raising any exceptions
    validate_asset_profiles()


def test_get_asset_profile():
    profile = get_asset_profile("metals")
    assert profile.name == "Metals"
    assert profile.asset_class == "metals"
    assert profile.macro_sensitivity == "high"


def test_forex_try_volume_reliability():
    profile = get_asset_profile("forex_try")
    assert profile.volume_reliability == "low"


def test_unknown_asset_class():
    with pytest.raises(ConfigError):
        get_asset_profile("unknown_asset_class")
