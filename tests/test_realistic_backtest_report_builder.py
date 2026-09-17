# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Report Builder."""

import pandas as pd
from advanced_realistic_backtest.realistic_backtest_report_builder import (
    build_realistic_backtest_profile_markdown_report,
    build_backtest_engine_contract_markdown_report,
    build_order_simulation_contract_markdown_report,
    build_transaction_cost_model_markdown_report,
    build_slippage_model_markdown_report,
    build_backtest_guard_markdown_report,
    build_backtest_readiness_score_markdown_report,
    build_realistic_backtest_manifest_markdown_report,
    build_realistic_backtest_safety_markdown_report,
    build_phase_147_handoff_markdown_report,
)


def test_markdown_report_builders():
    summary = {
        "active_profile": "balanced_local_realistic_backtest_contracts",
        "total_profiles": 3,
        "readiness_score": 0.85,
        "classification": "ready",
        "safety_status": "SECURE",
        "manifest_id": "man_146",
    }
    df = pd.DataFrame([{"col1": "val1"}])

    rep_prof = build_realistic_backtest_profile_markdown_report(summary, df)
    assert "Phase 146" in rep_prof
    assert "YASAL UYARI" in rep_prof

    rep_eng = build_backtest_engine_contract_markdown_report(summary, df)
    assert "Phase 146" in rep_eng

    rep_ord = build_order_simulation_contract_markdown_report(summary, df)
    assert "Phase 146" in rep_ord

    rep_cost = build_transaction_cost_model_markdown_report(summary, df)
    assert "Phase 146" in rep_cost

    rep_slip = build_slippage_model_markdown_report(summary, df)
    assert "Phase 146" in rep_slip

    rep_grd = build_backtest_guard_markdown_report(summary, df)
    assert "Phase 146" in rep_grd

    rep_scr = build_backtest_readiness_score_markdown_report(summary, df)
    assert "Phase 146" in rep_scr

    rep_man = build_realistic_backtest_manifest_markdown_report(summary, df)
    assert "Phase 146" in rep_man

    rep_sft = build_realistic_backtest_safety_markdown_report(summary, df)
    assert "Phase 146" in rep_sft

    rep_hnd = build_phase_147_handoff_markdown_report(summary, df)
    assert "Phase 146" in rep_hnd
