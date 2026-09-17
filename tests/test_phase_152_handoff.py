# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Phase 152 Handoff."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.phase_152_handoff import (
    build_phase_152_backtest_acceptance_report_handoff_report,
    summarize_phase_152_handoff,
)


def test_phase_152_handoff():
    profile = get_default_benchmark_evaluation_profile()
    df, s = build_phase_152_backtest_acceptance_report_handoff_report(profile)

    assert not df.empty
    assert len(df) == 10
    assert "prerequisite_id" in df.columns
    assert (df["status"] == "READY").all()
    assert s["all_prerequisites_satisfied"] is True
    assert s["phase_152_handoff_ready"] is True
    assert s["next_phase"] == 152
    assert s["target_final_phase"] == 160
    assert s["non_signal"] is True
