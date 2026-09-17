# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 JS Divergence Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.js_divergence_metric_placeholders import (
    build_js_divergence_metric_placeholders,
    validate_js_divergence_metric_placeholder,
)


def test_js_divergence_metric_placeholders():
    metrics = build_js_divergence_metric_placeholders()
    assert len(metrics) == 2
    for m in metrics:
        val = validate_js_divergence_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
