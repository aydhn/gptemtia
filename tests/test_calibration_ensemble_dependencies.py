# -*- coding: utf-8 -*-
"""Unit tests for Calibration Ensemble Dependencies."""

from advanced_calibration_uncertainty.calibration_ensemble_dependencies import (
    build_calibration_ensemble_dependency_registry,
    summarize_calibration_ensemble_dependencies,
)


def test_calibration_ensemble_dependencies():
    df, summary = build_calibration_ensemble_dependency_registry()
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
