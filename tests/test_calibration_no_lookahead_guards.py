# -*- coding: utf-8 -*-
"""Unit tests for Calibration No-Lookahead Guards."""

from advanced_calibration_uncertainty.calibration_no_lookahead_guards import (
    build_calibration_no_lookahead_guard_registry,
    summarize_calibration_no_lookahead_guards,
)


def test_calibration_no_lookahead_guards():
    df, summary = build_calibration_no_lookahead_guard_registry()
    assert summary["all_active"] is True
    assert summary["all_blocking"] is True
