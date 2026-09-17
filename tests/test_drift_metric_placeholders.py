# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Master Drift Metric Placeholders Aggregator."""

import pytest
from advanced_model_drift_monitoring.drift_metric_placeholders import (
    build_all_drift_metric_placeholders,
    summarize_drift_metric_placeholders,
)


def test_master_metric_placeholders():
    metrics = build_all_drift_metric_placeholders()
    assert len(metrics) >= 20
    summary = summarize_drift_metric_placeholders(metrics)
    assert summary["all_calculation_disabled"] is True
    assert summary["non_executing_compliance"] is True
    assert len(summary["by_type"]) >= 9
