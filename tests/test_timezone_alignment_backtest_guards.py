# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Timezone Alignment Backtest Guards."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.timezone_alignment_backtest_guards import (
    build_timezone_alignment_backtest_guard_registry,
)


def test_build_timezone_guards():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_timezone_alignment_backtest_guard_registry(prof)
    assert not df.empty
    assert len(df) >= 2
    assert summary["non_signal"] is True
    assert (df["non_signal"] == True).all()
