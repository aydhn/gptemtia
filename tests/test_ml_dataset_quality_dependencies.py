"""Test suite for Phase 137 ML Dataset Quality Dependencies."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_quality_dependencies import (
    build_ml_dataset_quality_dependency_registry,
    summarize_ml_dataset_quality_dependencies,
)


def test_build_quality_dependencies():
    df, summary = build_ml_dataset_quality_dependency_registry()
    assert not df.empty
    assert summary["total_quality_dependencies"] >= 4
    assert summary["non_signal"] is True
