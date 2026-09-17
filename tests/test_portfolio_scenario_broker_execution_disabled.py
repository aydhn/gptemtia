# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_broker_execution_disabled import build_portfolio_scenario_broker_execution_disabled_report

def test_build_portfolio_scenario_broker_execution_disabled_report():
    df, summary = build_portfolio_scenario_broker_execution_disabled_report()
    assert not df.empty
    assert "execution_blocked" in df.columns
    if "True" != "ANY":
        assert (df["execution_blocked"] == True).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
