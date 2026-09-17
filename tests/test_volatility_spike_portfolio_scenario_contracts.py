# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.volatility_spike_portfolio_scenario_contracts import build_volatility_spike_portfolio_scenario_contract_registry

def test_build_volatility_spike_portfolio_scenario_contract_registry():
    df, summary = build_volatility_spike_portfolio_scenario_contract_registry()
    assert not df.empty
    assert "execution_allowed" in df.columns
    if "False" != "ANY":
        assert (df["execution_allowed"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
