# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_library_contracts import build_portfolio_scenario_library_contract_registry

def test_build_portfolio_scenario_library_contract_registry():
    df, summary = build_portfolio_scenario_library_contract_registry()
    assert not df.empty
    assert "contract_status" in df.columns
    if "'CONTRACT_ONLY'" != "ANY":
        assert (df["contract_status"] == 'CONTRACT_ONLY').all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
