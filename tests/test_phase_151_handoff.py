# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Phase 151 Handoff."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.phase_151_handoff import (
    build_phase_151_benchmark_strategy_evaluation_handoff_report,
    summarize_phase_151_handoff,
)


def test_phase_151_handoff():
    prof = get_default_backtest_governance_profile()
    df, summary = build_phase_151_benchmark_strategy_evaluation_handoff_report(prof)

    assert not df.empty
    assert len(df) == 10
    assert summary["phase_151_handoff_ready"] is True
    assert summary["handoff_status"] == "READY_FOR_PHASE_151"
    assert summary["current_phase"] == 150
    assert summary["next_phase"] == 151
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
    assert summary["local_only"] is True
