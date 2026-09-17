# -*- coding: utf-8 -*-
"""Unit tests for Calibration Metric Placeholders."""

from advanced_calibration_uncertainty.calibration_metric_placeholders import (
    build_calibration_metric_placeholder_registry,
    summarize_calibration_metric_placeholders,
)


def test_calibration_metric_placeholders():
    df, summary = build_calibration_metric_placeholder_registry()
    assert summary["all_uncalculated"] is True
    assert summary["all_zero_performance_claim"] is True
    assert summary["all_non_signal"] is True
