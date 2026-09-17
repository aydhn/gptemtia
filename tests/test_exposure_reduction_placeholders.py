# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.exposure_reduction_placeholders import build_exposure_reduction_placeholder_registry

def test_build_exposure_reduction_placeholder_registry():
    df, summary = build_exposure_reduction_placeholder_registry()
    assert not df.empty
    assert "execution_enabled" in df.columns
    if "False" != "ANY":
        assert (df["execution_enabled"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
