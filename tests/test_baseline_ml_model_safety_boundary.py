# -*- coding: utf-8 -*-
"""Unit tests for baseline ML model safety boundary."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_ml_model_safety_boundary import (
    NO_GO_RULES,
    SAFE_GO_RULES,
    build_baseline_ml_model_no_go_conditions,
    build_baseline_ml_model_safe_go_conditions,
    build_baseline_ml_model_safety_boundary,
    summarize_baseline_ml_model_safety_boundary,
)


def test_safety_boundary_rules_definition():
    assert len(NO_GO_RULES) == 24
    assert len(SAFE_GO_RULES) == 9

    df_nogo = build_baseline_ml_model_no_go_conditions()
    assert len(df_nogo) == 24
    assert (df_nogo["rule_type"] == "NO-GO").all()

    df_safego = build_baseline_ml_model_safe_go_conditions()
    assert len(df_safego) == 9
    assert (df_safego["rule_type"] == "SAFE-GO").all()


def test_build_baseline_ml_model_safety_boundary():
    df, summary = build_baseline_ml_model_safety_boundary()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 33
    assert summary["total_rules"] == 33
    assert summary["no_go_count"] == 24
    assert summary["safe_go_count"] == 9
    assert summary["safety_status"] == "SECURE"
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
