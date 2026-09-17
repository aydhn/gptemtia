# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.recovery_plan_placeholders import build_recovery_plan_placeholder_registry

def test_build_recovery_plan_placeholder_registry():
    df, summary = build_recovery_plan_placeholder_registry()
    assert not df.empty
    assert "plan_active" in df.columns
    if "False" != "ANY":
        assert (df["plan_active"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
