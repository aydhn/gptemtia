"""
Tests for configuration logic.
"""

from config.settings import settings


def test_live_trading_is_false_by_default():
    """Ensure live trading is forcefully disabled."""
    assert settings.live_trading_enabled is False


def test_paper_trading_enabled_by_default():
    """Ensure paper trading is generally enabled."""
    assert settings.paper_trading_enabled is True
