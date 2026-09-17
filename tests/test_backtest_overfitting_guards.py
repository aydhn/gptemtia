# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Overfitting Guards."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_overfitting_guards import (
    build_backtest_overfitting_guard_registry,
)


def test_build_overfitting_guards():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_overfitting_guard_registry(prof)
    assert not df.empty
    assert len(df) >= 2
    assert summary["overfitting_mitigation_enforced"] is True
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
