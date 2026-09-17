"""Test suite for Phase 137 ML Dataset Walk Forward Split Policies."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_walk_forward_split_policies import (
    build_ml_dataset_walk_forward_split_policy_registry,
    summarize_ml_dataset_walk_forward_split_policies,
)


def test_build_walk_forward_split_policies():
    df, summary = build_ml_dataset_walk_forward_split_policy_registry()
    assert not df.empty
    assert summary["total_walk_forward_policies"] >= 3
    assert summary["materialized"] is False
    assert summary["backtest_executed"] is False
