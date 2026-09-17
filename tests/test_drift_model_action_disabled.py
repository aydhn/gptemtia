# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Model Action Disabled Enforcer."""

import pytest
from advanced_model_drift_monitoring.drift_model_action_disabled import (
    assert_drift_model_action_disabled,
    build_drift_model_action_disabled_item,
)


def test_model_action_disabled():
    item = build_drift_model_action_disabled_item()
    assert item.is_disabled is True

    res = assert_drift_model_action_disabled({"mode": "contract_only"})
    assert res["status"] == "passed"
    assert res["model_action_blocked"] is True

    with pytest.raises(RuntimeError):
        assert_drift_model_action_disabled({"deactivate_model": True})

    with pytest.raises(RuntimeError):
        assert_drift_model_action_disabled({"hot_swap_model": True})
