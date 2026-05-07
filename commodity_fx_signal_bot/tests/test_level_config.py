import pytest
from levels.level_config import (
    get_level_profile,
    list_level_profiles,
    validate_level_profiles,
    get_default_level_profile,
)
from core.exceptions import ConfigError


def test_validate_level_profiles_passes():
    # Should not raise any error
    validate_level_profiles()


def test_get_default_level_profile():
    prof = get_default_level_profile()
    assert prof.name == "balanced_theoretical_levels"
    assert prof.min_reward_risk > 0


def test_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_level_profile("unknown_profile_name")


def test_profile_attributes():
    prof = get_level_profile("wide_volatility_levels")
    assert prof.use_volatility_adjustment is True
    assert prof.max_stop_distance_pct > prof.min_stop_distance_pct
    assert all(m > 0 for m in prof.atr_multipliers)
