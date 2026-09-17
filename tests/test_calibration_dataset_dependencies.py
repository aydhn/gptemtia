# -*- coding: utf-8 -*-
"""Unit tests for Calibration Dataset Dependencies."""

from advanced_calibration_uncertainty.calibration_dataset_dependencies import (
    build_calibration_dataset_dependency_registry,
    summarize_calibration_dataset_dependencies,
)


def test_calibration_dataset_dependencies():
    df, summary = build_calibration_dataset_dependency_registry()
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
