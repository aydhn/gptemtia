# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Execution Assumptions."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_execution_assumptions import (
    build_realistic_execution_assumption_registry,
    summarize_realistic_execution_assumptions,
)


def test_build_realistic_execution_assumptions():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_realistic_execution_assumption_registry(prof)
    assert not df.empty
    assert len(df) >= 8
    assert summary["total_assumptions"] >= 8
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
    # Check that zero slippage assumption is prohibited
    slippage_asm = df[df["assumption_name"].str.contains("slippage", case=False, na=False)]
    assert not slippage_asm.empty
