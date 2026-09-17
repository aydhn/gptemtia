# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Model Governance Pipeline."""

import pytest
from advanced_model_governance.model_governance_pipeline import (
    ModelGovernancePipeline,
    run_model_governance_pipeline,
)


def test_model_governance_pipeline_end_to_end():
    pipe = ModelGovernancePipeline()
    status_df, summary = pipe.build_model_governance_status(save=False)
    assert len(status_df) == 10
    assert summary["phase"] == 144
    assert summary["next_phase"] == 145
    assert summary["target_final_phase"] == 160
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["live_trading"] is False
    assert summary["model_registry_write"] is False
    assert summary["artifact_persisted"] is False
    assert summary["non_signal"] is True


def test_run_model_governance_pipeline_helper():
    summary = run_model_governance_pipeline(save=False)
    assert summary["phase"] == 144
    assert summary["next_phase"] == 145
    assert summary["readiness_score"] == 1.0
