# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Forbidden Column Policies."""

import pytest
from advanced_model_drift_monitoring.drift_forbidden_column_policies import (
    FORBIDDEN_DRIFT_COLUMNS,
    build_drift_forbidden_column_guards,
    validate_drift_monitored_columns,
)


def test_forbidden_column_guards():
    guards = build_drift_forbidden_column_guards()
    assert len(guards) == 1
    assert len(FORBIDDEN_DRIFT_COLUMNS) >= 10


def test_validate_monitored_columns():
    safe_cols = ["returns_20d", "volatility_60d", "rsi_14d", "basis_spread"]
    res_safe = validate_drift_monitored_columns(safe_cols)
    assert res_safe["valid"] is True

    unsafe_cols = ["returns_20d", "target_future_return", "order_id"]
    res_unsafe = validate_drift_monitored_columns(unsafe_cols)
    assert res_unsafe["valid"] is False
    assert "target_future_return" in res_unsafe["violating_columns"]
