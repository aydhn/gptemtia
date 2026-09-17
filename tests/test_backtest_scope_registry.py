# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Scope Registry."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_scope_registry import (
    build_backtest_scope_registry,
    summarize_backtest_scope_registry,
)


def test_build_scope_registry():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_scope_registry(prof)
    assert not df.empty
    assert "IN_SCOPE" in df["status"].values
    assert "OUT_OF_SCOPE" in df["status"].values
    assert summary["non_signal"] is True
    assert summary["live_trading_prohibited"] is True
    # Verify live trading is strictly out of scope
    live_scope = df[df["name"].str.contains("Live Trading", case=False, na=False)]
    assert not live_scope.empty
    assert (live_scope["status"] == "OUT_OF_SCOPE").all()
