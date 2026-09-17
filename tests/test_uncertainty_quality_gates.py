# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Quality Gates."""

from advanced_calibration_uncertainty.uncertainty_quality_gates import (
    build_uncertainty_quality_gate_registry,
    summarize_uncertainty_quality_gates,
)


def test_uncertainty_quality_gates():
    df, summary = build_uncertainty_quality_gate_registry()
    assert summary["total_gates"] >= 5
    assert summary["all_blocking"] is True
