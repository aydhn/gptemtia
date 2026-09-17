# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.hedge_derisk_claim_guards import build_hedge_derisk_claim_guard_registry

def test_build_hedge_derisk_claim_guard_registry():
    df, summary = build_hedge_derisk_claim_guard_registry()
    assert not df.empty
    assert "enforced" in df.columns
    if "True" != "ANY":
        assert (df["enforced"] == True).all()
    if "None" and "None" in summary:
        assert summary["None"] is not None
