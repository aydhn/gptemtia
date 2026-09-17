"""Test suite for Phase 137 ML Dataset Version Policies."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_version_policies import (
    build_ml_dataset_version_policy_registry,
    summarize_ml_dataset_version_policies,
)


def test_build_version_policies():
    df, summary = build_ml_dataset_version_policy_registry()
    assert not df.empty
    assert summary["total_version_policies"] >= 3
    assert summary["destructive_overwrite_allowed"] is False
    assert summary["production_tag_allowed"] is False
