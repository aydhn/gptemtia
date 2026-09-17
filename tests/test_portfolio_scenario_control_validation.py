# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_validation import build_portfolio_scenario_control_validation_report

def test_build_portfolio_scenario_control_validation_report():
    df, summary = build_portfolio_scenario_control_validation_report()
    assert not df.empty
    assert "status" in df.columns
    if "'PASS'" != "ANY":
        assert (df["status"] == 'PASS').all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
