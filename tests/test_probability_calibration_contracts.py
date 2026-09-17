# -*- coding: utf-8 -*-
"""Unit tests for Probability Calibration Contracts."""

from advanced_calibration_uncertainty.probability_calibration_contracts import (
    build_probability_calibration_contract_registry,
    validate_probability_calibration_contract,
    summarize_probability_calibration_contracts,
)


def test_probability_calibration_contracts():
    df, summary = build_probability_calibration_contract_registry()
    assert len(df) >= 5
    assert summary["total_contracts"] >= 5
    assert summary["all_zero_prediction"] is True
    assert summary["all_zero_fit"] is True
    assert summary["all_zero_transform"] is True
    assert summary["all_non_signal"] is True

    valid = validate_probability_calibration_contract(df.iloc[0].to_dict())
    assert valid["is_valid"] is True
