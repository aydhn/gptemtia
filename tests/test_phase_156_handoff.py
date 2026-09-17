# -*- coding: utf-8 -*-
"""Unit tests for Phase 156 Handoff Report."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.phase_156_handoff import build_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report


def test_build_phase_156_handoff_report():
    profile = get_default_risk_reporting_profile()
    df, summary = build_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report(profile)

    assert not df.empty
    assert summary["handoff_ready"] is True
    assert summary["current_phase"] == 155
    assert summary["next_phase"] == 156
    assert summary["target_final_phase"] == 160
    assert summary["total_items"] >= 10
    assert (df["status"] == "SATISFIED").all()
