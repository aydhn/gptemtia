# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.scenario_output_contracts import build_scenario_output_contract_registry

def test_build_scenario_output_contract_registry():
    df, summary = build_scenario_output_contract_registry()
    assert not df.empty
    assert "materialization_allowed" in df.columns
    if "False" != "ANY":
        assert (df["materialization_allowed"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
