# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.scenario_metric_placeholders import build_scenario_metric_placeholder_registry

def test_build_scenario_metric_placeholder_registry():
    df, summary = build_scenario_metric_placeholder_registry()
    assert not df.empty
    assert "is_calculated" in df.columns
    if "False" != "ANY":
        assert (df["is_calculated"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
