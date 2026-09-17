# -*- coding: utf-8 -*-
"""Unit tests for baseline model lineage."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_lineage import (
    LINEAGE_STAGES,
    build_baseline_model_lineage_registry,
    summarize_baseline_model_lineage,
)


def test_build_baseline_model_lineage_registry():
    df, summary = build_baseline_model_lineage_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(LINEAGE_STAGES)
    assert len(df) == 5
    assert summary["total_lineage_stages"] == 5
    assert summary["all_source_preserved"] is True
    assert summary["non_signal"] is True
    assert (df["source_preserved"] == True).all()
    assert (df["non_signal"] == True).all()


def test_summarize_baseline_model_lineage_empty():
    empty_df = pd.DataFrame(columns=[
        "stage", "layer_name", "output_type", "target",
        "source_preserved", "non_signal", "production_ready", "broker_ready"
    ])
    summary = summarize_baseline_model_lineage(empty_df)
    assert summary["total_lineage_stages"] == 0
    assert summary["all_source_preserved"] is True
