# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Performance Claim Disabled Report."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_performance_claim_disabled import (
    build_backtest_performance_claim_disabled_report,
)


def test_build_performance_claim_disabled_report():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_performance_claim_disabled_report(prof)
    assert not df.empty
    assert summary["is_blocked"] is True
    assert summary["policy_active"] is True
    assert summary["non_signal"] is True
    assert (df["is_blocked"] == True).all()
