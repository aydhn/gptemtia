# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_forbidden_column_policies import build_portfolio_scenario_forbidden_column_policy_registry

def test_build_portfolio_scenario_forbidden_column_policy_registry():
    df, summary = build_portfolio_scenario_forbidden_column_policy_registry()
    assert not df.empty
    assert "status" in df.columns
    if "'ENFORCED'" != "ANY":
        assert (df["status"] == 'ENFORCED').all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
