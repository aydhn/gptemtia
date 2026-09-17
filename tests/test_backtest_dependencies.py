# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Dependencies."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_dependencies import (
    build_backtest_dependency_registry,
)


def test_build_dependencies():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_dependency_registry(prof)
    assert not df.empty
    assert len(df) >= 7
    assert summary["total_dependencies"] >= 7
    assert summary["all_satisfied"] is True
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
