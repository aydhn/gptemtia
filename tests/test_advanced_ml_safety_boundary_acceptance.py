# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Safety Boundary Acceptance."""

import pytest
from advanced_ml_acceptance.advanced_ml_safety_boundary_acceptance import (
    build_advanced_ml_safety_boundary_acceptance_registry,
    summarize_advanced_ml_safety_boundary_acceptance,
)


def test_safety_boundary_acceptance():
    df, summary = build_advanced_ml_safety_boundary_acceptance_registry()
    assert not df.empty
    assert len(df) >= 10
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "SECURE"

    s = summarize_advanced_ml_safety_boundary_acceptance(df)
    assert s["boundary_count"] >= 10
    assert s["all_enforced"] is True
