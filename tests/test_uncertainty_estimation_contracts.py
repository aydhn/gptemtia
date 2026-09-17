# -*- coding: utf-8 -*-
"""Unit tests for Uncertainty Estimation Contracts."""

from advanced_calibration_uncertainty.uncertainty_estimation_contracts import (
    build_uncertainty_estimation_contract_registry,
    validate_uncertainty_estimation_contract,
    summarize_uncertainty_estimation_contracts,
)


def test_uncertainty_estimation_contracts():
    df, summary = build_uncertainty_estimation_contract_registry()
    assert len(df) >= 5
    assert summary["total_contracts"] >= 5
    assert summary["all_zero_uncertainty"] is True
    assert summary["all_zero_prediction_interval"] is True
    assert summary["all_zero_conformal"] is True
    assert summary["all_non_signal"] is True

    valid = validate_uncertainty_estimation_contract(df.iloc[0].to_dict())
    assert valid["is_valid"] is True
