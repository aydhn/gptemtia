# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Retraining Trigger Disabled Enforcer."""

import pytest
from advanced_model_drift_monitoring.drift_retraining_trigger_disabled import (
    assert_drift_retraining_trigger_disabled,
    build_drift_retraining_trigger_disabled_item,
)


def test_retraining_trigger_disabled():
    item = build_drift_retraining_trigger_disabled_item()
    assert item.is_disabled is True

    res = assert_drift_retraining_trigger_disabled({"test": "value"})
    assert res["status"] == "passed"
    assert res["retraining_trigger_blocked"] is True

    with pytest.raises(RuntimeError):
        assert_drift_retraining_trigger_disabled({"trigger_retraining": True})

    with pytest.raises(RuntimeError):
        assert_drift_retraining_trigger_disabled({"auto_refit": True})
