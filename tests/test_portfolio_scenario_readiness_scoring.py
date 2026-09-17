# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_readiness_scoring import build_portfolio_scenario_readiness_score_report

def test_build_portfolio_scenario_readiness_score_report():
    df, summary = build_portfolio_scenario_readiness_score_report()
    assert not df.empty
    assert "component" in df.columns
    if "ANY" != "ANY":
        assert (df["component"] == ANY).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
