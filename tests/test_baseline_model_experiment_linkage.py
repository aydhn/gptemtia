# -*- coding: utf-8 -*-
"""Unit tests for baseline model experiment linkage."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_experiment_linkage import (
    EXPERIMENT_LINKAGES,
    build_baseline_model_experiment_linkage_registry,
    summarize_baseline_model_experiment_linkage,
)


def test_build_baseline_model_experiment_linkage_registry():
    df, summary = build_baseline_model_experiment_linkage_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(EXPERIMENT_LINKAGES)
    assert len(df) == 4
    assert summary["total_linkages"] == 4
    assert summary["zero_runs_executed"] is True
    assert summary["zero_training_jobs"] is True
    assert summary["zero_predictions"] is True
    assert summary["non_signal"] is True
    assert (df["is_run_executed"] == False).all()
    assert (df["training_job_active"] == False).all()
    assert (df["prediction_active"] == False).all()
    assert (df["artifact_saved"] == False).all()


def test_summarize_baseline_model_experiment_linkage_empty():
    empty_df = pd.DataFrame(columns=[
        "linkage_id", "experiment_template_ref", "model_contract_ref",
        "phase_137_run_plan_ref", "phase_139_resource_governance_ref",
        "is_run_executed", "training_job_active", "prediction_active",
        "artifact_saved", "non_signal", "production_ready", "broker_ready"
    ])
    summary = summarize_baseline_model_experiment_linkage(empty_df)
    assert summary["total_linkages"] == 0
    assert summary["zero_runs_executed"] is True
    assert summary["zero_training_jobs"] is True
    assert summary["zero_predictions"] is True
