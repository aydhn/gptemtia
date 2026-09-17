"""Test suite for Phase 137 Advanced ML Dataset Profile Registry."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_profile_registry import (
    build_advanced_ml_dataset_profile_registry,
    summarize_advanced_ml_dataset_profiles,
)


def test_build_profile_registry():
    df, summary = build_advanced_ml_dataset_profile_registry()
    assert not df.empty
    assert summary["total_profiles"] >= 3
    assert summary["current_phase"] == 137
    assert summary["next_phase"] == 138
    assert summary["non_signal"] is True
    assert summary["dataset_materialization_allowed"] is False
    assert summary["model_training_allowed"] is False
