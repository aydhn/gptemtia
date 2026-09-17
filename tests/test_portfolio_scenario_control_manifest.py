# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_manifest import build_portfolio_scenario_control_manifest

def test_build_portfolio_scenario_control_manifest():
    df, summary = build_portfolio_scenario_control_manifest()
    assert not df.empty
    assert "manifest_id" in df.columns
    if "ANY" != "ANY":
        assert (df["manifest_id"] == ANY).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
