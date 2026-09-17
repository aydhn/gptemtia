# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Categorical Drift Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.categorical_drift_metric_placeholders import (
    build_categorical_drift_metric_placeholders,
    validate_categorical_drift_metric_placeholder,
)


def test_categorical_drift_metric_placeholders():
    metrics = build_categorical_drift_metric_placeholders()
    assert len(metrics) == 2
    for m in metrics:
        val = validate_categorical_drift_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
