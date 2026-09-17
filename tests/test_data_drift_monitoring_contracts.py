# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Data Drift Contracts."""

import pytest
from advanced_model_drift_monitoring.data_drift_monitoring_contracts import (
    build_data_drift_monitoring_contracts,
    validate_data_drift_monitoring_contract,
)


def test_data_drift_monitoring_contracts():
    contracts = build_data_drift_monitoring_contracts()
    assert len(contracts) == 6
    for c in contracts:
        val = validate_data_drift_monitoring_contract(c)
        assert val["valid"] is True, f"Contract {c.contract_id} failed: {val['errors']}"
