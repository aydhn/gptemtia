# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Evaluation Placeholders."""

from advanced_calibration_uncertainty.uncertainty_evaluation_placeholders import (
    build_uncertainty_evaluation_placeholder_registry,
    summarize_uncertainty_evaluation_placeholders,
)


def test_uncertainty_evaluation_placeholders():
    df, summary = build_uncertainty_evaluation_placeholder_registry()
    assert summary["all_unexecuted"] is True
    assert summary["all_zero_performance_claim"] is True
    assert summary["all_non_signal"] is True
