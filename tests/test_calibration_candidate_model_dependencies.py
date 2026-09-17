# -*- coding: utf-8 -*-
"""Unit tests for Calibration Candidate Model Dependencies."""

from advanced_calibration_uncertainty.calibration_candidate_model_dependencies import (
    build_calibration_candidate_model_dependency_registry,
    summarize_calibration_candidate_model_dependencies,
)


def test_calibration_candidate_model_dependencies():
    df, summary = build_calibration_candidate_model_dependency_registry()
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
