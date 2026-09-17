# -*- coding: utf-8 -*-
"""Unit tests for baseline ML model health."""

import pytest
import pandas as pd
from pathlib import Path
from advanced_baseline_ml_models.baseline_ml_model_health import (
    build_baseline_ml_model_health_check,
    summarize_baseline_ml_model_health,
)


def test_build_baseline_ml_model_health_check():
    df, summary = build_baseline_ml_model_health_check()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 11
    assert summary["all_healthy"] is True
    assert summary["health_status"] == "SYSTEM_HEALTHY"
    assert summary["unhealthy_count"] == 0
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert (df["status"] == "HEALTHY").all()


def test_summarize_baseline_ml_model_health_empty():
    empty_df = pd.DataFrame(columns=["check_item", "status", "passed", "non_signal"])
    summary = summarize_baseline_ml_model_health(empty_df)
    assert summary["healthy_count"] == 0
    assert summary["all_healthy"] is True
    assert summary["health_status"] == "SYSTEM_HEALTHY"
