# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_testing_contracts import build_portfolio_scenario_testing_contract_registry

def test_build_portfolio_scenario_testing_contract_registry():
    df, summary = build_portfolio_scenario_testing_contract_registry()
    assert not df.empty
    assert "execution_allowed" in df.columns
    if "False" != "ANY":
        assert (df["execution_allowed"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
