# -*- coding: utf-8 -*-
"""Unit tests for Calibration Forbidden Column Policies."""

from advanced_calibration_uncertainty.calibration_forbidden_column_policies import (
    build_calibration_forbidden_column_policy_registry,
    summarize_calibration_forbidden_column_policies,
)


def test_calibration_forbidden_column_policies():
    df, summary = build_calibration_forbidden_column_policy_registry()
    assert isinstance(summary, dict)
    assert summary.get("all_blocking", True) is True
