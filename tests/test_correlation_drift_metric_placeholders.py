# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Correlation Drift Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.correlation_drift_metric_placeholders import (
    build_correlation_drift_metric_placeholders,
    validate_correlation_drift_metric_placeholder,
)


def test_correlation_drift_metric_placeholders():
    metrics = build_correlation_drift_metric_placeholders()
    assert len(metrics) == 2
    for m in metrics:
        val = validate_correlation_drift_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
