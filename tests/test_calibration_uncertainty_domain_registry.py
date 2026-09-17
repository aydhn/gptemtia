# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Domain Registry."""

from advanced_calibration_uncertainty.calibration_uncertainty_domain_registry import (
    build_calibration_uncertainty_domain_registry,
    summarize_calibration_uncertainty_domains,
)


def test_domain_registry_generation():
    df, summary = build_calibration_uncertainty_domain_registry()
    assert len(df) >= 40
    assert summary["total_domains"] >= 40
    assert summary["all_non_signal"] is True
    assert summary["all_zero_execution"] is True
