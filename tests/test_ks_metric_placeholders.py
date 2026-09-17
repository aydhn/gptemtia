# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 KS Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.ks_metric_placeholders import (
    build_ks_metric_placeholders,
    validate_ks_metric_placeholder,
)


def test_ks_metric_placeholders():
    metrics = build_ks_metric_placeholders()
    assert len(metrics) == 2
    for m in metrics:
        val = validate_ks_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
