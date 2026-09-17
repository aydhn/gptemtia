# -*- coding: utf-8 -*-
"""Unit tests for baseline model forbidden column policies."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_forbidden_column_policies import (
    FORBIDDEN_COLUMNS_LIST,
    build_baseline_model_forbidden_column_policy_registry,
    summarize_baseline_model_forbidden_column_policies,
    validate_baseline_model_forbidden_columns,
)


def test_build_baseline_model_forbidden_column_policy_registry():
    df, summary = build_baseline_model_forbidden_column_policy_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(FORBIDDEN_COLUMNS_LIST)
    assert len(df) == 23
    assert summary["total_forbidden_columns"] == 23
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
    assert (df["enforced"] == True).all()


def test_validate_baseline_model_forbidden_columns():
    clean_cols = ["date", "feature_rsi", "feature_vol", "feature_momentum"]
    res_clean = validate_baseline_model_forbidden_columns(clean_cols)
    assert res_clean["valid"] is True
    assert res_clean["violations"] == []
    assert res_clean["status"] == "PASS_CLEAN_COLUMNS"

    dirty_cols = ["date", "signal", "buy", "sell", "target", "future_return", "sentiment_score"]
    res_dirty = validate_baseline_model_forbidden_columns(dirty_cols)
    assert res_dirty["valid"] is False
    assert len(res_dirty["violations"]) >= 6
    assert res_dirty["status"] == "FAIL_FORBIDDEN_COLUMNS_DETECTED"
