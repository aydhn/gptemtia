# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Source Preservation Guards."""

from advanced_calibration_uncertainty.uncertainty_source_preservation_guards import (
    build_uncertainty_source_preservation_guard_registry,
    summarize_uncertainty_source_preservation_guards,
)


def test_uncertainty_source_preservation_guards():
    df, summary = build_uncertainty_source_preservation_guard_registry()
    assert summary["all_active"] is True
    assert summary["all_blocking"] is True
