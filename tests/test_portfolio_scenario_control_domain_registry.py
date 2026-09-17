# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_domain_registry import build_portfolio_scenario_control_domain_registry

def test_build_portfolio_scenario_control_domain_registry():
    df, summary = build_portfolio_scenario_control_domain_registry()
    assert not df.empty
    assert "is_contract_only" in df.columns
    if "True" != "ANY":
        assert (df["is_contract_only"] == True).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
