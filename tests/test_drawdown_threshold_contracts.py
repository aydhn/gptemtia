# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.drawdown_threshold_contracts import build_drawdown_threshold_contract_registry

def test_build_drawdown_threshold_contract_registry():
    df, summary = build_drawdown_threshold_contract_registry()
    assert not df.empty
    assert "contract_status" in df.columns
    if "'CONTRACT_ONLY'" != "ANY":
        assert (df["contract_status"] == 'CONTRACT_ONLY').all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
