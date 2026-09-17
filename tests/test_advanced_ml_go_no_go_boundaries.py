# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Go / No-Go Boundaries."""

import pytest
from advanced_ml_acceptance.advanced_ml_go_no_go_boundaries import (
    build_advanced_ml_go_no_go_boundary_registry,
    validate_advanced_ml_go_no_go_request,
    summarize_advanced_ml_go_no_go_boundaries,
)


def test_go_no_go_boundaries():
    df, summary = build_advanced_ml_go_no_go_boundary_registry()
    assert not df.empty
    assert summary["go_count"] >= 3
    assert summary["no_go_count"] >= 8
    assert summary["non_signal"] is True
    assert summary["status"] == "SECURE"

    s = summarize_advanced_ml_go_no_go_boundaries(df)
    assert s["boundary_count"] >= 11

    # Allowed Go requests
    res_go = validate_advanced_ml_go_no_go_request("proceed_to_phase_146_contract_planning")
    assert res_go["decision"] == "GO"
    assert res_go["allowed"] is True

    # Blocked No-Go requests
    res_nogo1 = validate_advanced_ml_go_no_go_request("live_trading")
    assert res_nogo1["decision"] == "NO-GO"
    assert res_nogo1["allowed"] is False

    res_nogo2 = validate_advanced_ml_go_no_go_request("broker_execution")
    assert res_nogo2["decision"] == "NO-GO"
    assert res_nogo2["allowed"] is False

    res_nogo3 = validate_advanced_ml_go_no_go_request("model_training")
    assert res_nogo3["decision"] == "NO-GO"
    assert res_nogo3["allowed"] is False
