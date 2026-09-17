# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Model Drift Contracts."""

import pytest
from advanced_model_drift_monitoring.model_drift_monitoring_contracts import (
    build_model_drift_monitoring_contracts,
    validate_drift_monitoring_contract,
)


def test_model_drift_monitoring_contracts():
    contracts = build_model_drift_monitoring_contracts()
    assert len(contracts) == 6
    for c in contracts:
        val = validate_drift_monitoring_contract(c)
        assert val["valid"] is True, f"Contract {c.contract_id} failed validation: {val['errors']}"
        assert c.execution_mode == "non_executing_contract"
