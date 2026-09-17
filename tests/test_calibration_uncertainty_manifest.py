# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Manifest."""

from advanced_calibration_uncertainty.calibration_uncertainty_manifest import (
    build_calibration_uncertainty_manifest,
    summarize_calibration_uncertainty_manifest,
)


def test_calibration_uncertainty_manifest():
    df, summary = build_calibration_uncertainty_manifest()
    assert summary["current_phase"] == 141
    assert summary["next_phase"] == 142
    assert summary["target_final_phase"] == 160
    assert summary["zero_execution_verified"] is True
    assert summary["non_signal"] is True
