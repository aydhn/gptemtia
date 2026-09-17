"""Test suite for Phase 137 ML Dataset Validation Dependencies."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_validation_dependencies import (
    build_ml_dataset_validation_dependency_registry,
    summarize_ml_dataset_validation_dependencies,
)


def test_build_validation_dependencies():
    df, summary = build_ml_dataset_validation_dependency_registry()
    assert not df.empty
    assert summary["total_validation_dependencies"] >= 5
    assert summary["non_signal"] is True
