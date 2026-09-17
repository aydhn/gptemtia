# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Current Window Policies."""

import pytest
from advanced_model_drift_monitoring.current_window_policies import (
    build_current_window_policies,
    validate_current_window_policy,
)


def test_current_window_policies():
    windows = build_current_window_policies()
    assert len(windows) == 4
    for w in windows:
        val = validate_current_window_policy(w)
        assert val["valid"] is True
        assert w.execution_enabled is False
