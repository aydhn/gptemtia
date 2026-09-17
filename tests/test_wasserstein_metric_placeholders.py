# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Wasserstein Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.wasserstein_metric_placeholders import (
    build_wasserstein_metric_placeholders,
    validate_wasserstein_metric_placeholder,
)


def test_wasserstein_metric_placeholders():
    metrics = build_wasserstein_metric_placeholders()
    assert len(metrics) == 2
    for m in metrics:
        val = validate_wasserstein_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
