# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Metric Calculation Disabled Enforcer."""

import pytest
from advanced_model_drift_monitoring.drift_metric_calculation_disabled import (
    assert_drift_metric_calculation_disabled,
    build_drift_metric_calculation_disabled_item,
)


def test_metric_calculation_disabled():
    item = build_drift_metric_calculation_disabled_item()
    assert item.is_disabled is True
    assert item.execution_type == "drift_calculation_disabled"

    res = assert_drift_metric_calculation_disabled({"param": "dry_run"})
    assert res["status"] == "passed"
    assert res["calculation_blocked"] is True

    with pytest.raises(RuntimeError):
        assert_drift_metric_calculation_disabled({"calculate_drift": True})

    with pytest.raises(RuntimeError):
        assert_drift_metric_calculation_disabled({"compute_psi": True})
