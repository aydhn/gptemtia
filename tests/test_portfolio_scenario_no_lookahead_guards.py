# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_no_lookahead_guards import build_portfolio_scenario_no_lookahead_guard_registry

def test_build_portfolio_scenario_no_lookahead_guard_registry():
    df, summary = build_portfolio_scenario_no_lookahead_guard_registry()
    assert not df.empty
    assert "enforced" in df.columns
    if "True" != "ANY":
        assert (df["enforced"] == True).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
