import pytest
from paper.paper_config import get_paper_trading_profile, validate_paper_trading_profiles, get_default_paper_trading_profile
from core.exceptions import ConfigError

def test_validate_paper_trading_profiles():
    # Should not raise any error with default setup
    validate_paper_trading_profiles()

def test_get_default_paper_trading_profile():
    profile = get_default_paper_trading_profile()
    assert profile.name == "balanced_virtual_paper"

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_paper_trading_profile("non_existent_profile")
