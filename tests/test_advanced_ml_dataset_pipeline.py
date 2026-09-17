"""Test suite for Phase 137 Advanced ML Dataset Pipeline."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_pipeline import (
    AdvancedMlDatasetPipeline,
)


def test_pipeline_dry_run_execution():
    pipeline = AdvancedMlDatasetPipeline()
    tables, summaries = pipeline.run_all(save=False)

    assert "profiles" in tables
    assert "contracts" in tables
    assert "schemas" in tables
    assert "experiments" in tables
    assert "manifest" in tables
    assert "status" in tables

    assert summaries["manifest"]["current_phase"] == 137
    assert summaries["manifest"]["next_phase"] == 138
    assert summaries["manifest"]["dataset_materialized"] is False
    assert summaries["manifest"]["model_training_executed"] is False
    assert summaries["manifest"]["non_signal"] is True
