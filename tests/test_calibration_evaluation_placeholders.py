# -*- coding: utf-8 -*-
"""Unit tests for Calibration Evaluation Placeholders."""

from advanced_calibration_uncertainty.calibration_evaluation_placeholders import (
    build_calibration_evaluation_placeholder_registry,
    summarize_calibration_evaluation_placeholders,
)


def test_calibration_evaluation_placeholders():
    df, summary = build_calibration_evaluation_placeholder_registry()
    assert summary["all_unexecuted"] is True
    assert summary["all_zero_performance_claim"] is True
    assert summary["all_non_signal"] is True
