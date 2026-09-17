# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Input Contracts."""

from advanced_calibration_uncertainty.uncertainty_input_contracts import (
    build_uncertainty_input_contract_registry,
    summarize_uncertainty_input_contracts,
)


def test_uncertainty_input_contracts():
    df, summary = build_uncertainty_input_contract_registry()
    assert isinstance(summary, dict)
    assert summary.get("all_no_lookahead", True) is True
    assert summary.get("all_metadata_only_news", True) is True
