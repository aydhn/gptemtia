import pytest
from core.exceptions import ConfigError
from portfolio_research.portfolio_config import (
    get_portfolio_research_profile,
    list_portfolio_research_profiles,
    validate_portfolio_research_profiles,
    get_default_portfolio_research_profile,
    _PROFILES,
    PortfolioResearchProfile
)

def test_validate_portfolio_research_profiles():
    validate_portfolio_research_profiles()

def test_get_default_portfolio_research_profile():
    p = get_default_portfolio_research_profile()
    assert p.name == "balanced_portfolio_research"

def test_min_symbols_positive():
    p = PortfolioResearchProfile("test", "test", min_symbols=-1)
    _PROFILES["test"] = p
    with pytest.raises(ConfigError):
        validate_portfolio_research_profiles()
    del _PROFILES["test"]

def test_weight_limits():
    p = PortfolioResearchProfile("test", "test", max_single_symbol_weight=1.5)
    _PROFILES["test"] = p
    with pytest.raises(ConfigError):
        validate_portfolio_research_profiles()
    del _PROFILES["test"]

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_portfolio_research_profile("non_existent_profile")
