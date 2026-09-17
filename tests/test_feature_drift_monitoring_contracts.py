# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Feature Drift Contracts."""

import pytest
from advanced_model_drift_monitoring.feature_drift_monitoring_contracts import (
    build_feature_drift_monitoring_contracts,
    validate_feature_drift_monitoring_contract,
)


def test_feature_drift_monitoring_contracts():
    contracts = build_feature_drift_monitoring_contracts()
    assert len(contracts) == 6
    for c in contracts:
        val = validate_feature_drift_monitoring_contract(c)
        assert val["valid"] is True, f"Contract {c.contract_id} failed: {val['errors']}"
