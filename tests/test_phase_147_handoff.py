# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Phase 147 Handoff Package."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.phase_147_handoff import (
    build_phase_147_walk_forward_oos_benchmark_handoff_report,
)


def test_build_phase_147_handoff():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_phase_147_walk_forward_oos_benchmark_handoff_report(prof)
    assert not df.empty
    assert len(df) == 10
    assert summary["source_phase"] == 146
    assert summary["next_phase"] == 147
    assert summary["target_final_phase"] == 160
    assert summary["all_prerequisites_satisfied"] is True
    assert summary["phase_147_handoff_ready"] is True
    assert summary["live_trading_remains_prohibited"] is True
    assert summary["broker_execution_remains_prohibited"] is True
    assert summary["non_signal"] is True
    assert (df["is_satisfied"] == True).all()
