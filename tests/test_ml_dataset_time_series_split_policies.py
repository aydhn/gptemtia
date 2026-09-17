"""Test suite for Phase 137 ML Dataset Time Series Split Policies."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_time_series_split_policies import (
    build_ml_dataset_time_series_split_policy_registry,
    summarize_ml_dataset_time_series_split_policies,
)


def test_build_time_series_split_policies():
    df, summary = build_ml_dataset_time_series_split_policy_registry()
    assert not df.empty
    assert summary["total_split_policies"] >= 4
    assert summary["all_placeholder_only"] is True
    assert summary["materialized"] is False
    assert summary["train_test_split_executed"] is False
