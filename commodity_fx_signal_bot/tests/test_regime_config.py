import pytest
from regimes.regime_config import (
    get_regime_profile,
    get_default_regime_profile,
    validate_regime_profiles,
    list_regime_profiles,
)
from core.exceptions import ConfigError


def test_validate_regime_profiles():
    # Should not raise any exception for default profiles
    validate_regime_profiles()


def test_get_default_regime_profile():
    prof = get_default_regime_profile()
    assert prof.name == "balanced_regime"
    assert "trend" in prof.feature_sets


def test_get_regime_profile():
    prof = get_regime_profile("volatility_sensitive")
    assert prof.name == "volatility_sensitive"

    with pytest.raises(ConfigError):
        get_regime_profile("unknown_profile")


def test_list_regime_profiles():
    profs = list_regime_profiles()
    assert len(profs) >= 4
    names = [p.name for p in profs]
    assert "balanced_regime" in names
    assert "trend_sensitive" in names
