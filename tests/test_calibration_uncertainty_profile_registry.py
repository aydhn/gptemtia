# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Profile Registry."""

from advanced_calibration_uncertainty.calibration_uncertainty_profile_registry import (
    build_calibration_uncertainty_profile_registry,
    summarize_calibration_uncertainty_profiles,
)


def test_profile_registry_generation():
    df, summary = build_calibration_uncertainty_profile_registry()
    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["all_local_only"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_zero_execution"] is True
