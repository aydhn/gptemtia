# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Output Contracts."""

from advanced_calibration_uncertainty.uncertainty_output_contracts import (
    build_uncertainty_output_contract_registry,
    summarize_uncertainty_output_contracts,
)


def test_uncertainty_output_contracts():
    df, summary = build_uncertainty_output_contract_registry()
    assert isinstance(summary, dict)
    assert summary.get("all_non_signal", True) is True
    assert summary.get("all_zero_uncertainty", True) is True
