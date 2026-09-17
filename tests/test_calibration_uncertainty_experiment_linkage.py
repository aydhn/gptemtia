# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Experiment Linkage."""

from advanced_calibration_uncertainty.calibration_uncertainty_experiment_linkage import (
    build_calibration_uncertainty_experiment_linkage_registry,
    summarize_calibration_uncertainty_experiment_linkage,
)


def test_calibration_uncertainty_experiment_linkage():
    df, summary = build_calibration_uncertainty_experiment_linkage_registry()
    assert summary["all_offline"] is True
    assert summary["all_non_signal"] is True
