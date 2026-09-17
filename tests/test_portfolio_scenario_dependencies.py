# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_dependencies import build_portfolio_scenario_dependency_registry

def test_build_portfolio_scenario_dependency_registry():
    df, summary = build_portfolio_scenario_dependency_registry()
    assert not df.empty
    assert "status" in df.columns
    if "'SATISFIED'" != "ANY":
        assert (df["status"] == 'SATISFIED').all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
