import pytest
from backtesting.backtest_config import (
    validate_backtest_profiles,
    get_default_backtest_profile,
    get_backtest_profile,
    ConfigError,
)


def test_validate_backtest_profiles():
    # Should not raise
    validate_backtest_profiles()


def test_get_default_backtest_profile():
    profile = get_default_backtest_profile()
    assert profile is not None
    assert profile.name == "balanced_candidate_backtest"


def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_backtest_profile("non_existent_profile")
