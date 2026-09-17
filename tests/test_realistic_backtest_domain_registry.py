# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Domain Registry."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_domain_registry import (
    build_realistic_backtest_domain_registry,
    summarize_realistic_backtest_domain_registry,
)


def test_build_domain_registry():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_realistic_backtest_domain_registry(prof)
    assert not df.empty
    assert len(df) >= 30
    assert summary["total_domains"] >= 30
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
    assert (df["local_only"] == True).all()
    assert (df["is_active"] == True).all()
