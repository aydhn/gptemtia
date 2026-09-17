# -*- coding: utf-8 -*-
"""Unit tests for Calibration Runtime Dependencies."""

from advanced_calibration_uncertainty.calibration_runtime_dependencies import (
    build_calibration_runtime_dependency_registry,
    summarize_calibration_runtime_dependencies,
)


def test_calibration_runtime_dependencies():
    df, summary = build_calibration_runtime_dependency_registry()
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
