# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Input Contracts."""

import pytest
from advanced_model_drift_monitoring.drift_monitoring_input_contracts import (
    build_drift_monitoring_input_contracts,
    validate_drift_monitoring_input,
)


def test_input_contracts():
    contracts = build_drift_monitoring_input_contracts()
    assert len(contracts) == 3

    valid_input = {"target_name": "reference_dataset_manifest", "dataset_id": "ds_ref_01"}
    res = validate_drift_monitoring_input(valid_input)
    assert res["valid"] is True

    # Forward looking key
    leaky_input = {"target_name": "current_data", "target_forward": 1.05}
    res_leaky = validate_drift_monitoring_input(leaky_input)
    assert res_leaky["valid"] is False
