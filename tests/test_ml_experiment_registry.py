"""Test suite for Phase 137 ML Experiment Registry."""

import pytest
from advanced_ml_dataset_registry.ml_experiment_registry import (
    build_ml_experiment_registry,
    validate_ml_experiment_registry_item,
    summarize_ml_experiment_registry,
)


def test_build_experiment_registry():
    df, summary = build_ml_experiment_registry()
    assert not df.empty
    assert summary["total_experiments"] >= 6
    assert summary["training_blocked"] is True
    assert summary["prediction_blocked"] is True
    assert summary["artifact_persistence_blocked"] is True


def test_validate_experiment_item():
    v_clean = validate_ml_experiment_registry_item({
        "no_training_required": True,
        "no_prediction_required": True,
        "artifact_persistence_allowed": False,
    })
    assert v_clean["valid"] is True

    v_bad = validate_ml_experiment_registry_item({
        "no_training_required": False,
        "artifact_persistence_allowed": True,
    })
    assert v_bad["valid"] is False
