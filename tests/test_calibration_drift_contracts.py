# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Calibration Drift Contracts."""

import pytest
from advanced_model_drift_monitoring.calibration_drift_contracts import (
    build_calibration_drift_contracts,
    validate_calibration_drift_contract,
)


def test_calibration_drift_contracts():
    contracts = build_calibration_drift_contracts()
    assert len(contracts) >= 3
    for c in contracts:
        val = validate_calibration_drift_contract(c)
        assert val["valid"] is True
