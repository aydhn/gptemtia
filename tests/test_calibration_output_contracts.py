# -*- coding: utf-8 -*-
"""Unit tests for Calibration Output Contracts."""

from advanced_calibration_uncertainty.calibration_output_contracts import (
    build_calibration_output_contract_registry,
    summarize_calibration_output_contracts,
)


def test_calibration_output_contracts():
    df, summary = build_calibration_output_contract_registry()
    assert isinstance(summary, dict)
    assert summary.get("all_non_signal", True) is True
    assert summary.get("all_zero_prediction", True) is True
