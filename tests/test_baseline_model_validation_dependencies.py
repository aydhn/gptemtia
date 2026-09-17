# -*- coding: utf-8 -*-
"""Unit tests for baseline model validation dependencies."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_validation_dependencies import (
    VALIDATION_DEPENDENCIES,
    build_baseline_model_validation_dependency_registry,
    summarize_baseline_model_validation_dependencies,
)


def test_build_baseline_model_validation_dependency_registry():
    df, summary = build_baseline_model_validation_dependency_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(VALIDATION_DEPENDENCIES)
    assert len(df) == 6
    assert summary["total_dependencies"] == 6
    assert summary["all_satisfied"] is True
    assert 121 in summary["source_phases"]
    assert 137 in summary["source_phases"]
    assert summary["non_signal"] is True
    assert (df["status"] == "SATISFIED").all()
    assert (df["non_signal"] == True).all()


def test_summarize_baseline_model_validation_dependencies_empty():
    empty_df = pd.DataFrame(columns=[
        "source_phase", "dependency_name", "status", "description",
        "non_signal", "production_ready", "broker_ready"
    ])
    summary = summarize_baseline_model_validation_dependencies(empty_df)
    assert summary["total_dependencies"] == 0
    assert summary["all_satisfied"] is True
    assert summary["source_phases"] == []
