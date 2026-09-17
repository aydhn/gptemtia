# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Health."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_health import (
    build_realistic_backtest_health_check,
)


def test_build_health_check():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_realistic_backtest_health_check(profile=prof)
    assert not df.empty
    assert summary["all_healthy"] is True
    assert summary["non_signal"] is True
    assert (df["status"] == "HEALTHY").all()
