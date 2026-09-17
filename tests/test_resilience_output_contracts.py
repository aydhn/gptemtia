# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.resilience_output_contracts import build_resilience_output_contract_registry

def test_build_resilience_output_contract_registry():
    df, summary = build_resilience_output_contract_registry()
    assert not df.empty
    assert "materialization_allowed" in df.columns
    if "False" != "ANY":
        assert (df["materialization_allowed"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
