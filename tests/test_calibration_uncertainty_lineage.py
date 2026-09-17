# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Lineage."""

from advanced_calibration_uncertainty.calibration_uncertainty_lineage import (
    build_calibration_uncertainty_lineage_registry,
    summarize_calibration_uncertainty_lineage,
)


def test_calibration_uncertainty_lineage():
    df, summary = build_calibration_uncertainty_lineage_registry()
    assert summary["all_verified"] is True
    assert summary["all_non_signal"] is True
