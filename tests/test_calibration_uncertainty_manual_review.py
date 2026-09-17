# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Manual Review."""

from advanced_calibration_uncertainty.calibration_uncertainty_manual_review import (
    build_calibration_uncertainty_manual_review_queue,
    summarize_calibration_uncertainty_manual_review_queue,
)


def test_calibration_uncertainty_manual_review():
    df, summary = build_calibration_uncertainty_manual_review_queue()
    assert summary["all_auto_prohibited"] is True
    assert summary["all_non_signal"] is True
