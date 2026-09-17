# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Findings."""

from advanced_calibration_uncertainty.calibration_uncertainty_findings import (
    build_calibration_uncertainty_findings_registry,
    summarize_calibration_uncertainty_findings,
)


def test_calibration_uncertainty_findings():
    df, summary = build_calibration_uncertainty_findings_registry()
    assert summary["total_findings"] >= 1
    assert summary["all_non_signal"] is True
