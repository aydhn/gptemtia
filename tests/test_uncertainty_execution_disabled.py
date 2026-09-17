# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Execution Disabled Guarantees."""

from advanced_calibration_uncertainty.uncertainty_execution_disabled import (
    build_uncertainty_execution_disabled_report,
    summarize_uncertainty_execution_disabled,
)


def test_uncertainty_execution_disabled():
    df, summary = build_uncertainty_execution_disabled_report()
    assert summary["all_disabled"] is True
    assert summary["all_enforced"] is True
