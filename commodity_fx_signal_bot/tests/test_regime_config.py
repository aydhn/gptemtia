import pytest
from portfolio_regime.regime_config import get_portfolio_regime_profile, list_portfolio_regime_profiles, validate_portfolio_regime_profiles, get_default_portfolio_regime_profile, ConfigError

def test_validate_portfolio_regime_profiles():
    # Should not raise
    validate_portfolio_regime_profiles()

def test_get_default_portfolio_regime_profile():
    profile = get_default_portfolio_regime_profile()
    assert profile is not None
    assert profile.name == "balanced_regime_portfolio_research"

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_portfolio_regime_profile("non_existent_profile")
