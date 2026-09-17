# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Alerting Disabled Enforcer."""

import pytest
from advanced_model_drift_monitoring.drift_alerting_disabled import (
    assert_drift_alerting_disabled,
    build_drift_alerting_disabled_item,
)


def test_alerting_disabled():
    item = build_drift_alerting_disabled_item()
    assert item.is_disabled is True

    res = assert_drift_alerting_disabled({"test": "value"})
    assert res["status"] == "passed"
    assert res["alerting_blocked"] is True

    with pytest.raises(RuntimeError):
        assert_drift_alerting_disabled({"send_alert": True})

    with pytest.raises(RuntimeError):
        assert_drift_alerting_disabled({"trigger_webhook": True})
