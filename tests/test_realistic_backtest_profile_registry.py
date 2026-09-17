# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Profile Registry."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_profile_registry import (
    build_realistic_backtest_profile_registry,
    summarize_realistic_backtest_profile_registry,
)


def test_build_profile_registry():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_realistic_backtest_profile_registry(prof)
    assert not df.empty
    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["all_local_only"] is True
    assert summary["non_signal"] is True
    assert (df["allow_live_trading"] == False).all()
    assert (df["allow_broker_integration"] == False).all()
