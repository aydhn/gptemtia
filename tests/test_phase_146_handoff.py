# -*- coding: utf-8 -*-
"""Unit tests for Phase 146 Realistic Backtest Handoff Specification."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.phase_146_handoff import (
    build_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report,
    summarize_phase_146_handoff,
)


def test_phase_146_handoff_report():
    prof = get_advanced_ml_acceptance_profile()
    df, summary = build_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report(prof)

    assert len(df) >= 10
    assert summary["source_phase"] == 145
    assert summary["next_phase"] == 146
    assert summary["target_final_phase"] == 160
    assert summary["next_phase_title"] == "Realistic Backtest, Transaction Cost and Slippage Modeling"
    assert summary["status"] == "READY"
    assert summary["all_satisfied"] is True
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s = summarize_phase_146_handoff(df)
    assert s["prerequisite_count"] >= 10
    assert s["all_satisfied"] is True
    assert s["non_signal"] is True
