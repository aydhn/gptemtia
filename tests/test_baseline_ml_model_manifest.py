# -*- coding: utf-8 -*-
"""Unit tests for baseline ML model manifest."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_ml_model_manifest import (
    create_baseline_ml_model_manifest,
    build_baseline_ml_model_manifest,
    summarize_baseline_ml_model_manifest,
)


def test_create_baseline_ml_model_manifest():
    mf = create_baseline_ml_model_manifest()
    assert mf.current_phase == 138
    assert mf.next_phase == 139
    assert mf.target_final_phase == 160
    assert mf.model_contract_count == 10
    assert mf.harness_contract_count == 5
    assert mf.real_training_executed is False
    assert mf.model_fit_executed is False
    assert mf.model_predict_executed is False
    assert mf.metric_calculation_executed is False
    assert mf.artifact_persisted is False
    assert mf.model_registry_written is False
    assert mf.non_signal is True
    assert mf.production_ready is False
    assert mf.broker_ready is False


def test_build_baseline_ml_model_manifest():
    df, summary = build_baseline_ml_model_manifest()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert summary["current_phase"] == 138
    assert summary["next_phase"] == 139
    assert summary["target_final_phase"] == 160
    assert summary["model_contract_count"] == 10
    assert summary["harness_contract_count"] == 5
    assert summary["real_training_executed"] is False
    assert summary["model_fit_executed"] is False
    assert summary["model_predict_executed"] is False
    assert summary["metric_calculation_executed"] is False
    assert summary["artifact_persisted"] is False
    assert summary["model_registry_written"] is False
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
