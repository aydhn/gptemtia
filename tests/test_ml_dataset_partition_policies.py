"""Test suite for Phase 137 ML Dataset Partition Policies."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_partition_policies import (
    build_ml_dataset_partition_policy_registry,
    summarize_ml_dataset_partition_policies,
)


def test_build_partition_policies():
    df, summary = build_ml_dataset_partition_policy_registry()
    assert not df.empty
    assert summary["total_partition_policies"] >= 5
    assert summary["non_signal"] is True
