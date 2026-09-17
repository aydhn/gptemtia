# -*- coding: utf-8 -*-
"""Unit tests for baseline model no-lookahead guards."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_no_lookahead_guards import (
    NO_LOOKAHEAD_GUARDS,
    build_baseline_model_no_lookahead_input_guard_registry,
    summarize_baseline_model_no_lookahead_guards,
    validate_baseline_model_no_lookahead_columns,
    validate_no_future_baseline_model_join,
)


def test_build_baseline_model_no_lookahead_input_guard_registry():
    df, summary = build_baseline_model_no_lookahead_input_guard_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(NO_LOOKAHEAD_GUARDS)
    assert len(df) == 4
    assert summary["total_guards"] == 4
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
    assert (df["enforced"] == True).all()


def test_validate_baseline_model_no_lookahead_columns():
    clean_cols = ["open", "high", "low", "close", "volume", "rsi_14", "atr_14"]
    res_clean = validate_baseline_model_no_lookahead_columns(clean_cols)
    assert res_clean["valid"] is True
    assert res_clean["violations"] == []
    assert res_clean["status"] == "VALID_NO_LOOKAHEAD"

    dirty_cols = ["open", "close", "future_return", "shift(-1)", "t+1_price"]
    res_dirty = validate_baseline_model_no_lookahead_columns(dirty_cols)
    assert res_dirty["valid"] is False
    assert len(res_dirty["violations"]) >= 3
    assert res_dirty["status"] == "LOOKAHEAD_VIOLATION_DETECTED"


def test_validate_no_future_baseline_model_join():
    df_left = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5, freq="D"),
        "price": [10, 11, 12, 13, 14],
    })
    df_right_valid = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5, freq="D"),
        "factor": [1, 2, 3, 4, 5],
    })
    res_valid = validate_no_future_baseline_model_join(df_left, df_right_valid, "timestamp", "timestamp")
    assert res_valid["valid"] is True

    df_right_future = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-02", periods=5, freq="D"),
        "factor": [1, 2, 3, 4, 5],
    })
    res_future = validate_no_future_baseline_model_join(df_left, df_right_future, "timestamp", "timestamp")
    assert res_future["valid"] is False
    assert len(res_future["violations"]) > 0
