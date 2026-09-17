# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Rolling Window Policies."""

import pytest
from advanced_model_drift_monitoring.rolling_window_placeholder_policies import (
    build_rolling_window_placeholder_policies,
    validate_rolling_window_placeholder_policy,
)


def test_rolling_window_placeholder_policies():
    windows = build_rolling_window_placeholder_policies()
    assert len(windows) == 4
    for w in windows:
        val = validate_rolling_window_placeholder_policy(w)
        assert val["valid"] is True
        assert w.execution_enabled is False
