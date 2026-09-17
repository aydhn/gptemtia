# -*- coding: utf-8 -*-
"""Unit tests for Calibration Method Placeholders."""

from advanced_calibration_uncertainty.calibration_method_placeholders import (
    build_calibration_method_placeholder_registry,
    summarize_calibration_method_placeholders,
)


def test_calibration_method_placeholders():
    df, summary = build_calibration_method_placeholder_registry()
    assert len(df) >= 5
    assert summary["total_methods"] >= 5
    assert summary["all_execution_blocked"] is True
    assert summary["all_fit_blocked"] is True
    assert summary["all_transform_blocked"] is True
    assert summary["all_non_signal"] is True
