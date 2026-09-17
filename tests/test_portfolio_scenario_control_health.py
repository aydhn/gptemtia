# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_health import build_portfolio_scenario_control_health_check

def test_build_portfolio_scenario_control_health_check():
    df, summary = build_portfolio_scenario_control_health_check()
    assert not df.empty
    assert "status" in df.columns
    if "'HEALTHY'" != "ANY":
        assert (df["status"] == 'HEALTHY').all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
