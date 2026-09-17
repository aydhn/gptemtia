# -*- coding: utf-8 -*-
"""Unit tests for baseline model regime inputs."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_regime_inputs import (
    REGIME_INPUT_CATALOG,
    build_baseline_model_regime_input_registry,
    summarize_baseline_model_regime_inputs,
)


def test_build_baseline_model_regime_input_registry():
    df, summary = build_baseline_model_regime_input_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(REGIME_INPUT_CATALOG)
    assert len(df) == 5
    assert summary["total_regime_inputs"] == 5
    assert summary["all_certified_non_signal"] is True
    assert summary["all_materialization_blocked"] is True
    assert summary["non_signal"] is True
    assert (df["materialized"] == False).all()
    assert (df["non_signal_certified"] == True).all()


def test_summarize_baseline_model_regime_inputs_empty():
    empty_df = pd.DataFrame(columns=[
        "regime_context", "source_phase", "manifest_ref",
        "non_signal_certified", "materialized", "non_signal",
        "production_ready", "broker_ready"
    ])
    summary = summarize_baseline_model_regime_inputs(empty_df)
    assert summary["total_regime_inputs"] == 0
    assert summary["all_certified_non_signal"] is True
    assert summary["all_materialization_blocked"] is True
