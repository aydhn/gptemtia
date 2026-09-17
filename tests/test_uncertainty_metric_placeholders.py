# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Metric Placeholders."""

from advanced_calibration_uncertainty.uncertainty_metric_placeholders import (
    build_uncertainty_metric_placeholder_registry,
    summarize_uncertainty_metric_placeholders,
)


def test_uncertainty_metric_placeholders():
    df, summary = build_uncertainty_metric_placeholder_registry()
    assert summary["all_uncalculated"] is True
    assert summary["all_zero_performance_claim"] is True
    assert summary["all_non_signal"] is True
