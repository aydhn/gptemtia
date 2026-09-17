# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Uncertainty Drift Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.uncertainty_drift_metric_placeholders import (
    build_uncertainty_drift_metric_placeholders,
    validate_uncertainty_drift_metric_placeholder,
)


def test_uncertainty_drift_metric_placeholders():
    metrics = build_uncertainty_drift_metric_placeholders()
    assert len(metrics) == 3
    for m in metrics:
        val = validate_uncertainty_drift_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
