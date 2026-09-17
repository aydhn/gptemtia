# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Output Contracts."""

import pytest
from advanced_model_drift_monitoring.drift_monitoring_output_contracts import (
    build_drift_monitoring_output_contracts,
    validate_drift_monitoring_output,
)


def test_output_contracts():
    contracts = build_drift_monitoring_output_contracts()
    assert len(contracts) == 2

    valid_output = {"target_name": "drift_finding_structure", "is_trading_signal": False}
    res = validate_drift_monitoring_output(valid_output)
    assert res["valid"] is True

    # Attempt signal output
    signal_output = {"target_name": "drift_finding_structure", "is_trading_signal": True}
    res_signal = validate_drift_monitoring_output(signal_output)
    assert res_signal["valid"] is False
