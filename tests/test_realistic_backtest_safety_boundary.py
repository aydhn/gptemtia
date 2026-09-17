# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Safety Boundaries."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_safety_boundary import (
    build_realistic_backtest_safety_boundary,
    build_realistic_backtest_no_go_conditions,
    build_realistic_backtest_safe_go_conditions,
)


def test_build_safety_boundary():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_realistic_backtest_safety_boundary(prof)
    assert not df.empty
    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] >= 15
    assert summary["safe_go_count"] >= 7
    assert summary["live_trading_prohibited"] is True
    assert summary["non_signal"] is True
    assert (df["enforced"] == True).all()


def test_conditions_counts():
    prof = get_default_realistic_backtest_profile()
    no_go = build_realistic_backtest_no_go_conditions(prof)
    safe_go = build_realistic_backtest_safe_go_conditions(prof)
    assert len(no_go) >= 15
    assert len(safe_go) >= 7
