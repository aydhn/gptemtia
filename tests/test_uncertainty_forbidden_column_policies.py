# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Forbidden Column Policies."""

from advanced_calibration_uncertainty.uncertainty_forbidden_column_policies import (
    build_uncertainty_forbidden_column_policy_registry,
    summarize_uncertainty_forbidden_column_policies,
)


def test_uncertainty_forbidden_column_policies():
    df, summary = build_uncertainty_forbidden_column_policy_registry()
    assert isinstance(summary, dict)
    assert summary.get("all_blocking", True) is True
