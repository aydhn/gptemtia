# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Market Impact Placeholders."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.market_impact_placeholders import (
    build_market_impact_placeholder_registry,
)


def test_build_market_impact_placeholders():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_market_impact_placeholder_registry(prof)
    assert not df.empty
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
