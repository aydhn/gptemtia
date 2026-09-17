"""Test suite for Phase 137 ML Metric Placeholders."""

import pytest
from advanced_ml_dataset_registry.ml_metric_placeholders import (
    build_ml_metric_placeholder_registry,
    summarize_ml_metric_placeholders,
)


def test_build_metric_placeholders():
    df, summary = build_ml_metric_placeholder_registry()
    assert not df.empty
    assert summary["total_metric_families"] == 7
    assert summary["calculation_allowed"] is False
    assert summary["prediction_required"] is False
    assert summary["target_label_required"] is False
