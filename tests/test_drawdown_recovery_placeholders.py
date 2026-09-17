# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.drawdown_recovery_placeholders import build_drawdown_recovery_placeholder_registry

def test_build_drawdown_recovery_placeholder_registry():
    df, summary = build_drawdown_recovery_placeholder_registry()
    assert not df.empty
    assert "in_recovery" in df.columns
    if "False" != "ANY":
        assert (df["in_recovery"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
