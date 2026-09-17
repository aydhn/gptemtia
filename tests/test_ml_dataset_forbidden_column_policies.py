"""Test suite for Phase 137 ML Dataset Forbidden Column Policies."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_forbidden_column_policies import (
    build_ml_dataset_forbidden_column_policy_registry,
    validate_ml_dataset_forbidden_columns,
    summarize_ml_dataset_forbidden_column_policies,
)


def test_build_forbidden_column_policies():
    df, summary = build_ml_dataset_forbidden_column_policy_registry()
    assert not df.empty
    assert summary["total_forbidden_columns"] >= 20


def test_validate_forbidden_columns():
    good_cols = ["timestamp_utc", "ml_feature_rsi", "entity_id"]
    v_good = validate_ml_dataset_forbidden_columns(good_cols)
    assert v_good["valid"] is True

    bad_cols = ["timestamp_utc", "target_return", "buy_signal"]
    v_bad = validate_ml_dataset_forbidden_columns(bad_cols)
    assert v_bad["valid"] is False
    assert len(v_bad["forbidden_found"]) >= 2
