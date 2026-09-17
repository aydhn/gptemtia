# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Uncertainty Drift Contracts."""

import pytest
from advanced_model_drift_monitoring.uncertainty_drift_contracts import (
    build_uncertainty_drift_contracts,
    validate_uncertainty_drift_contract,
)


def test_uncertainty_drift_contracts():
    contracts = build_uncertainty_drift_contracts()
    assert len(contracts) >= 3
    for c in contracts:
        val = validate_uncertainty_drift_contract(c)
        assert val["valid"] is True
