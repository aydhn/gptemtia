# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Method Placeholders."""

from advanced_calibration_uncertainty.uncertainty_method_placeholders import (
    build_uncertainty_method_placeholder_registry,
    summarize_uncertainty_method_placeholders,
)


def test_uncertainty_method_placeholders():
    df, summary = build_uncertainty_method_placeholder_registry()
    assert len(df) >= 5
    assert summary["total_methods"] >= 5
    assert summary["all_execution_blocked"] is True
    assert summary["all_estimation_blocked"] is True
    assert summary["all_non_signal"] is True
