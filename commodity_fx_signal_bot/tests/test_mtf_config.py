import pytest
from core.exceptions import ConfigError
from mtf.mtf_config import (
    get_mtf_profile,
    list_mtf_profiles,
    get_default_mtf_profile,
    validate_mtf_profiles,
    validate_mtf_feature_sets,
)


def test_validate_mtf_profiles():
    # Should not raise an exception
    validate_mtf_profiles()


def test_get_default_mtf_profile():
    profile = get_default_mtf_profile()
    assert profile.name == "daily_swing"
    assert profile.base_timeframe == "1d"


def test_get_mtf_profile_valid():
    profile = get_mtf_profile("four_hour_swing")
    assert profile.name == "four_hour_swing"
    assert profile.base_timeframe == "4h"


def test_get_mtf_profile_invalid():
    with pytest.raises(ConfigError):
        get_mtf_profile("unknown_profile_xyz")


def test_validate_mtf_feature_sets():
    # Should report_builder = ReportBuilder()
    validate_mtf_feature_sets(("momentum", "trend"))

    # Should fail
    with pytest.raises(ConfigError):
        validate_mtf_feature_sets(("invalid_set",))
