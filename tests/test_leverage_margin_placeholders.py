# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Leverage and Margin Placeholders."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.leverage_margin_placeholders import (
    build_leverage_margin_placeholder_registry,
)


def test_build_leverage_margin_placeholders():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_leverage_margin_placeholder_registry(prof)
    assert not df.empty
    assert len(df) == 3
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
