# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Missingness Drift Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.missingness_drift_metric_placeholders import (
    build_missingness_drift_metric_placeholders,
    validate_missingness_drift_metric_placeholder,
)


def test_missingness_drift_metric_placeholders():
    metrics = build_missingness_drift_metric_placeholders()
    assert len(metrics) == 2
    for m in metrics:
        val = validate_missingness_drift_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
