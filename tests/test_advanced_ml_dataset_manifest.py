"""Test suite for Phase 137 Advanced ML Dataset Manifest."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_manifest import (
    build_advanced_ml_dataset_manifest,
    create_advanced_ml_dataset_manifest,
    summarize_advanced_ml_dataset_manifest,
)


def test_build_manifest():
    df, summary = build_advanced_ml_dataset_manifest()
    assert not df.empty
    assert summary["current_phase"] == 137
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 138
    assert summary["dataset_materialized"] is False
    assert summary["feature_snapshot_materialized"] is False
    assert summary["model_training_executed"] is False
    assert summary["model_predict_executed"] is False
    assert summary["clustering_executed"] is False
    assert summary["artifact_persisted"] is False
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
