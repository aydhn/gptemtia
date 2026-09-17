# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Report Builder."""

import pytest
from advanced_model_drift_monitoring.model_drift_monitoring_manifest import build_model_drift_monitoring_manifest
from advanced_model_drift_monitoring.model_drift_report_builder import (
    build_model_drift_markdown_report,
    build_model_drift_text_summary,
)


def test_model_drift_report_builder():
    manifest = build_model_drift_monitoring_manifest()
    md = build_model_drift_markdown_report(manifest)
    assert "# Phase 142" in md
    assert "SAFETY & COMPLIANCE DISCLAIMER" in md
    assert "Phase 143" in md

    txt = build_model_drift_text_summary(manifest)
    assert "Phase 142 Model Drift Monitoring Summary" in txt
    assert "Next Phase: 143" in txt
