# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Forbidden Column Policies."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_forbidden_column_policies import (
    build_backtest_forbidden_column_policy_registry,
    validate_backtest_forbidden_columns,
    FORBIDDEN_COLUMNS,
)


def test_build_backtest_forbidden_column_policies():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_forbidden_column_policy_registry(profile)

    assert not df.empty
    assert len(df) == 40
    assert "column_name" in df.columns
    assert "policy" in df.columns
    assert (df["enforcement"] == "BLOCKING_ZERO_TOLERANCE").all()
    assert summary["all_strictly_forbidden"] is True
    assert summary["total_forbidden_columns"] == 40
    assert len(FORBIDDEN_COLUMNS) == 40


def test_validate_backtest_forbidden_columns():
    invalid_cols = ["timestamp", "actual_sharpe", "signal", "target"]
    res_inv = validate_backtest_forbidden_columns(invalid_cols)
    assert res_inv["is_clean"] is False
    assert res_inv["is_blocked"] is True
    assert len(res_inv["violating_columns"]) > 0

    valid_cols = ["timestamp", "open", "high", "low", "close", "volume"]
    res_val = validate_backtest_forbidden_columns(valid_cols)
    assert res_val["is_clean"] is True
    assert res_val["is_blocked"] is False
    assert len(res_val["violating_columns"]) == 0
