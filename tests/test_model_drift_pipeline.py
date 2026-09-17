# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Pipeline Orchestrator."""

import pytest
from advanced_model_drift_monitoring.model_drift_pipeline import run_model_drift_monitoring_pipeline


def test_model_drift_pipeline_dry_run():
    res = run_model_drift_monitoring_pipeline(save=False)
    assert res["status"] == "success"
    assert res["phase"] == 142
    assert res["next_phase"] == 143
    assert res["validation"]["valid"] is True
