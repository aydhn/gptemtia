# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest No-Lookahead Guards."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_no_lookahead_guards import (
    build_backtest_no_lookahead_guard_registry,
    validate_backtest_no_lookahead_columns,
)


def test_build_no_lookahead_guards():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_no_lookahead_guard_registry(prof)
    assert not df.empty
    assert len(df) >= 2
    assert summary["all_active"] is True
    assert summary["lookahead_strictly_prohibited"] is True
    assert summary["non_signal"] is True
    assert (df["active"] == True).all()


def test_validate_no_lookahead_columns():
    clean_cols = ["timestamp", "open", "high", "low", "close", "volume"]
    res_clean = validate_backtest_no_lookahead_columns(clean_cols)
    assert res_clean["is_clean"] is True

    dirty_cols = ["open", "future_return", "target_price"]
    res_dirty = validate_backtest_no_lookahead_columns(dirty_cols)
    assert res_dirty["is_clean"] is False
    assert "future_return" in res_dirty["violations"]
