"""Test suite for Phase 137 ML Experiment Templates."""

import pytest
from advanced_ml_dataset_registry.ml_experiment_templates import (
    build_ml_experiment_template_registry,
    summarize_ml_experiment_templates,
)


def test_build_experiment_templates():
    df, summary = build_ml_experiment_template_registry()
    assert not df.empty
    assert summary["total_templates"] >= 4
    assert summary["non_signal"] is True
