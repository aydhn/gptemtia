# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_safety_boundary import build_portfolio_scenario_control_safety_boundary

def test_build_portfolio_scenario_control_safety_boundary():
    df, summary = build_portfolio_scenario_control_safety_boundary()
    assert not df.empty
    assert "enforced" in df.columns
    if "True" != "ANY":
        assert (df["enforced"] == True).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
