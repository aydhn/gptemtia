# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Prediction Disabled Enforcer."""

import pytest
from advanced_model_drift_monitoring.drift_prediction_disabled import (
    assert_drift_prediction_disabled,
    build_drift_prediction_disabled_item,
)


def test_prediction_disabled():
    item = build_drift_prediction_disabled_item()
    assert item.is_disabled is True

    res = assert_drift_prediction_disabled({"dry_run": True})
    assert res["status"] == "passed"
    assert res["prediction_blocked"] is True

    with pytest.raises(RuntimeError):
        assert_drift_prediction_disabled({"predict": True})

    with pytest.raises(RuntimeError):
        assert_drift_prediction_disabled({"generate_signals": True})
