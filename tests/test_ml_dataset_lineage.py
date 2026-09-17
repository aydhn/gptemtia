"""Test suite for Phase 137 ML Dataset Lineage Registry."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_lineage import (
    build_ml_dataset_lineage_registry,
    summarize_ml_dataset_lineage,
)


def test_build_lineage():
    df, summary = build_ml_dataset_lineage_registry()
    assert not df.empty
    assert summary["total_lineage_records"] >= 4
    assert summary["non_signal"] is True
