# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 PSI Metric Placeholders."""

import pytest
from advanced_model_drift_monitoring.psi_metric_placeholders import (
    build_psi_metric_placeholders,
    validate_psi_metric_placeholder,
)


def test_psi_metric_placeholders():
    metrics = build_psi_metric_placeholders()
    assert len(metrics) == 3
    for m in metrics:
        val = validate_psi_metric_placeholder(m)
        assert val["valid"] is True
        assert m.calculation_enabled is False
