# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Survivorship Bias Guards."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_survivorship_bias_guards import (
    build_backtest_survivorship_bias_guard_registry,
)


def test_build_survivorship_bias_guards():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_survivorship_bias_guard_registry(prof)
    assert not df.empty
    assert len(df) >= 2
    assert summary["survivorship_bias_prevented"] is True
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
