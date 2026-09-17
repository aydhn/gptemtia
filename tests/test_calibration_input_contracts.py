# -*- coding: utf-8 -*-
"""Unit tests for Calibration Input Contracts."""

from advanced_calibration_uncertainty.calibration_input_contracts import (
    build_calibration_input_contract_registry,
    summarize_calibration_input_contracts,
)


def test_calibration_input_contracts():
    df, summary = build_calibration_input_contract_registry()
    assert isinstance(summary, dict)
    assert summary.get("all_no_lookahead", True) is True
    assert summary.get("all_metadata_only_news", True) is True
