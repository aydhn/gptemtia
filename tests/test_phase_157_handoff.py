# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.phase_157_handoff import build_phase_157_portfolio_acceptance_report_handoff_report

def test_phase_157_handoff():
    df, summary = build_phase_157_portfolio_acceptance_report_handoff_report()
    assert not df.empty
    assert summary["handoff_ready"] is True
    assert summary["current_phase"] == 156
    assert summary["next_phase"] == 157
    assert summary["target_final_phase"] == 160
    assert (df["status"] == "SATISFIED").all()
