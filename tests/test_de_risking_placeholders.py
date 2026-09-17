# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.de_risking_placeholders import build_de_risking_placeholder_registry

def test_build_de_risking_placeholder_registry():
    df, summary = build_de_risking_placeholder_registry()
    assert not df.empty
    assert "execution_enabled" in df.columns
    if "False" != "ANY":
        assert (df["execution_enabled"] == False).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
