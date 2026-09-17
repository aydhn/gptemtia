# -*- coding: utf-8 -*-
"""Unit tests for baseline metric placeholders."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_metric_placeholders import (
    METRIC_PLACEHOLDERS_DATA,
    build_baseline_metric_placeholder_registry,
    summarize_baseline_metric_placeholders,
)


def test_build_baseline_metric_placeholder_registry():
    df, summary = build_baseline_metric_placeholder_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(METRIC_PLACEHOLDERS_DATA)
    assert len(df) == 8
    assert summary["total_placeholders"] == 8
    assert summary["all_uncalculated"] is True
    assert summary["performance_claims_prohibited"] is True
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    # Check columns and placeholder constraints
    assert (df["is_calculated"] == False).all()
    assert df["calculated_value"].isna().all()
    assert (df["performance_claim_allowed"] == False).all()
    assert (df["non_signal"] == True).all()


def test_summarize_baseline_metric_placeholders_empty():
    empty_df = pd.DataFrame(columns=[
        "metric_placeholder_id", "metric_category", "description",
        "is_calculated", "calculated_value", "performance_claim_allowed",
        "non_signal", "production_ready", "broker_ready"
    ])
    summary = summarize_baseline_metric_placeholders(empty_df)
    assert summary["total_placeholders"] == 0
    assert summary["all_uncalculated"] is True
    assert summary["performance_claims_prohibited"] is True
