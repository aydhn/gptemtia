# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.hedge_control_placeholders import build_hedge_control_placeholder_registry

def test_build_hedge_control_placeholder_registry():
    df, summary = build_hedge_control_placeholder_registry()
    assert not df.empty
    assert "execution_enabled" in df.columns
    if "False" != "ANY":
        assert (df["execution_enabled"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
