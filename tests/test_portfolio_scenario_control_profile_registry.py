# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_profile_registry import build_portfolio_scenario_control_profile_registry

def test_build_portfolio_scenario_control_profile_registry():
    df, summary = build_portfolio_scenario_control_profile_registry()
    assert not df.empty
    assert "profile_name" in df.columns
    if "ANY" != "ANY":
        assert (df["profile_name"] == ANY).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
