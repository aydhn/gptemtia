# -*- coding: utf-8 -*-
"""Unit tests for Calibration Source Preservation Guards."""

from advanced_calibration_uncertainty.calibration_source_preservation_guards import (
    build_calibration_source_preservation_guard_registry,
    summarize_calibration_source_preservation_guards,
)


def test_calibration_source_preservation_guards():
    df, summary = build_calibration_source_preservation_guard_registry()
    assert summary["all_active"] is True
    assert summary["all_blocking"] is True
