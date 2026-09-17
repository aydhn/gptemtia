# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.currency_shock_portfolio_scenario_contracts import build_currency_shock_portfolio_scenario_contract_registry

def test_build_currency_shock_portfolio_scenario_contract_registry():
    df, summary = build_currency_shock_portfolio_scenario_contract_registry()
    assert not df.empty
    assert "execution_allowed" in df.columns
    if "False" != "ANY":
        assert (df["execution_allowed"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
