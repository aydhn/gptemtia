# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_findings import build_portfolio_scenario_findings_registry

def test_build_portfolio_scenario_findings_registry():
    df, summary = build_portfolio_scenario_findings_registry()
    assert not df.empty
    assert "finding_id" in df.columns
    if "ANY" != "ANY":
        assert (df["finding_id"] == ANY).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
