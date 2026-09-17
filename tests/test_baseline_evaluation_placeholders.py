# -*- coding: utf-8 -*-
"""Unit tests for baseline evaluation placeholders."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_evaluation_placeholders import (
    EVALUATION_PLACEHOLDERS_DATA,
    build_baseline_evaluation_placeholder_registry,
    summarize_baseline_evaluation_placeholders,
)


def test_build_baseline_evaluation_placeholder_registry():
    df, summary = build_baseline_evaluation_placeholder_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(EVALUATION_PLACEHOLDERS_DATA)
    assert len(df) == 7
    assert summary["total_evaluation_placeholders"] == 7
    assert summary["all_unexecuted"] is True
    assert summary["performance_claims_prohibited"] is True
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    assert (df["is_executed"] == False).all()
    assert (df["performance_claim_allowed"] == False).all()
    assert (df["non_signal"] == True).all()


def test_summarize_baseline_evaluation_placeholders_empty():
    empty_df = pd.DataFrame(columns=[
        "evaluation_placeholder_id", "evaluation_scope", "description",
        "is_executed", "performance_claim_allowed", "non_signal",
        "production_ready", "broker_ready"
    ])
    summary = summarize_baseline_evaluation_placeholders(empty_df)
    assert summary["total_evaluation_placeholders"] == 0
    assert summary["all_unexecuted"] is True
    assert summary["performance_claims_prohibited"] is True
