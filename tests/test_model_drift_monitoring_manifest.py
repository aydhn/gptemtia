# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Model Drift Monitoring Manifest."""

import pytest
from advanced_model_drift_monitoring.model_drift_monitoring_manifest import (
    build_model_drift_monitoring_manifest,
    summarize_model_drift_monitoring_manifest,
    validate_model_drift_monitoring_manifest,
)


def test_model_drift_manifest():
    manifest = build_model_drift_monitoring_manifest()
    assert manifest.phase == 142
    assert len(manifest.contracts) >= 20
    assert len(manifest.linkages) >= 10
    assert len(manifest.window_policies) >= 15
    assert len(manifest.thresholds) >= 6
    assert len(manifest.metric_placeholders) >= 20
    assert len(manifest.disabled_executions) >= 5

    val = validate_model_drift_monitoring_manifest(manifest)
    assert val["valid"] is True, f"Manifest validation failed: {val['errors']}"

    summary = summarize_model_drift_monitoring_manifest(manifest)
    assert summary["phase"] == 142
    assert summary["all_calculation_disabled"] is True
    assert summary["non_executing_compliance"] is True
