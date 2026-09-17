# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Numerical Drift Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.numerical_drift_metric_placeholders import (
    build_numerical_drift_metric_placeholders,
    validate_numerical_drift_metric_placeholder,
)


def test_numerical_drift_metric_placeholders():
    metrics = build_numerical_drift_metric_placeholders()
    assert len(metrics) == 3
    for m in metrics:
        val = validate_numerical_drift_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
