# -*- coding: utf-8 -*-
"""Unit tests for baseline model featurestore inputs."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_featurestore_inputs import (
    FEATURESTORE_INPUT_CATALOG,
    build_baseline_model_featurestore_input_registry,
    summarize_baseline_model_featurestore_inputs,
)


def test_build_baseline_model_featurestore_input_registry():
    df, summary = build_baseline_model_featurestore_input_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(FEATURESTORE_INPUT_CATALOG)
    assert len(df) == 5
    assert summary["total_namespaces"] == 5
    assert summary["all_no_lookahead_verified"] is True
    assert summary["all_materialization_blocked"] is True
    assert summary["non_signal"] is True
    assert (df["materialized"] == False).all()
    assert (df["no_lookahead_verified"] == True).all()


def test_summarize_baseline_model_featurestore_inputs_empty():
    empty_df = pd.DataFrame(columns=[
        "feature_namespace", "feature_count_placeholder", "catalog_ref",
        "no_lookahead_verified", "materialized", "non_signal",
        "production_ready", "broker_ready"
    ])
    summary = summarize_baseline_model_featurestore_inputs(empty_df)
    assert summary["total_namespaces"] == 0
    assert summary["all_no_lookahead_verified"] is True
    assert summary["all_materialization_blocked"] is True
