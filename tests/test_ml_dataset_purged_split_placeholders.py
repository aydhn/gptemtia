"""Test suite for Phase 137 ML Dataset Purged Split Placeholders."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_purged_split_placeholders import (
    build_ml_dataset_purged_split_placeholder_registry,
    summarize_ml_dataset_purged_split_placeholders,
)


def test_build_purged_split_placeholders():
    df, summary = build_ml_dataset_purged_split_placeholder_registry()
    assert not df.empty
    assert summary["total_purged_split_placeholders"] >= 2
    assert summary["materialized"] is False
    assert summary["purging_execution_allowed"] is False
