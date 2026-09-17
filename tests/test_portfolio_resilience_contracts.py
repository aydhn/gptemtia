# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_resilience_contracts import build_portfolio_resilience_contract_registry

def test_build_portfolio_resilience_contract_registry():
    df, summary = build_portfolio_resilience_contract_registry()
    assert not df.empty
    assert "evaluation_enabled" in df.columns
    if "False" != "ANY":
        assert (df["evaluation_enabled"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
