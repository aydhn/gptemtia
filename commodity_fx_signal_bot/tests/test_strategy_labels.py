import pytest

from strategies.strategy_labels import (
    is_directional_strategy_family,
    is_no_trade_strategy_family,
    list_strategy_families,
    validate_strategy_family,
)


def test_list_strategy_families():
    families = list_strategy_families()
    assert len(families) > 0
    assert "trend_following" in families


def test_validate_strategy_family():
    validate_strategy_family("trend_following")
    with pytest.raises(ValueError):
        validate_strategy_family("invalid_family")


def test_is_directional_strategy_family():
    assert is_directional_strategy_family("trend_following") is True
    assert is_directional_strategy_family("no_trade") is False


def test_is_no_trade_strategy_family():
    assert is_no_trade_strategy_family("no_trade") is True
    assert is_no_trade_strategy_family("trend_following") is False
