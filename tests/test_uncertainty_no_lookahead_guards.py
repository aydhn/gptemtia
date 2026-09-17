# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty No-Lookahead Guards."""

from advanced_calibration_uncertainty.uncertainty_no_lookahead_guards import (
    build_uncertainty_no_lookahead_guard_registry,
    summarize_uncertainty_no_lookahead_guards,
)


def test_uncertainty_no_lookahead_guards():
    df, summary = build_uncertainty_no_lookahead_guard_registry()
    assert summary["all_active"] is True
    assert summary["all_blocking"] is True
