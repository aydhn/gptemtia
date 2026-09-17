# -*- coding: utf-8 -*-
"""Unit tests for Calibration Quality Gates."""

from advanced_calibration_uncertainty.calibration_quality_gates import (
    build_calibration_quality_gate_registry,
    summarize_calibration_quality_gates,
)


def test_calibration_quality_gates():
    df, summary = build_calibration_quality_gate_registry()
    assert summary["total_gates"] >= 5
    assert summary["all_blocking"] is True
