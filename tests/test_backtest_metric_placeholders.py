# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Metric Placeholders."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_metric_placeholders import (
    build_backtest_metric_placeholder_registry,
)


def test_build_backtest_metric_placeholders():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_metric_placeholder_registry(prof)
    assert not df.empty
    assert len(df) == 10
    assert summary["total_metric_placeholders"] == 10
    assert summary["all_placeholders"] is True
    assert summary["all_zero_calculated"] is True
    assert summary["non_signal"] is True
    assert (df["calculated"] == False).all()
    assert (df["is_placeholder"] == True).all()
    assert (df["non_signal"] == True).all()
