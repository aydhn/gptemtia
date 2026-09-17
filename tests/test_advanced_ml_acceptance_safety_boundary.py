# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Acceptance Safety Boundaries."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_safety_boundary import (
    build_advanced_ml_acceptance_safety_boundary,
    build_advanced_ml_acceptance_no_go_conditions,
    build_advanced_ml_acceptance_safe_go_conditions,
    summarize_advanced_ml_acceptance_safety_boundary,
)


def test_safety_boundary():
    df, summary = build_advanced_ml_acceptance_safety_boundary()
    assert not df.empty
    assert summary["no_go_count"] >= 20
    assert summary["safe_go_count"] >= 5
    assert summary["status"] == "SECURE"

    no_go = build_advanced_ml_acceptance_no_go_conditions()
    assert "live trading" in no_go
    assert "broker integration" in no_go
    assert "model deployment" in no_go

    safe_go = build_advanced_ml_acceptance_safe_go_conditions()
    assert len(safe_go) >= 5

    s = summarize_advanced_ml_acceptance_safety_boundary(df)
    assert s["condition_count"] >= 25
    assert s["non_signal"] is True
