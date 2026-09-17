# -*- coding: utf-8 -*-
"""Unit tests for baseline ML model validation."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_ml_model_validation import (
    validate_baseline_ml_model_profile_registry,
    validate_baseline_model_contracts,
    validate_dry_run_training_harness_contracts,
    validate_disabled_execution_reports,
    validate_baseline_ml_model_manifest,
    validate_no_forbidden_baseline_ml_claims,
    build_baseline_ml_model_validation_report,
    run_baseline_ml_model_validation,
)


def test_validate_baseline_ml_model_profile_registry():
    valid_df = pd.DataFrame([{
        "dry_run_default": True,
        "local_only": True,
        "allow_real_model_training": False,
        "allow_model_predict": False,
    }])
    assert validate_baseline_ml_model_profile_registry(valid_df)["passed"] is True

    invalid_df = pd.DataFrame([{
        "dry_run_default": False,
        "local_only": True,
        "allow_real_model_training": True,
        "allow_model_predict": True,
    }])
    assert validate_baseline_ml_model_profile_registry(invalid_df)["passed"] is False


def test_validate_no_forbidden_baseline_ml_claims():
    clean_text = "This is a contract-only dry-run harness for baseline models without real execution."
    assert validate_no_forbidden_baseline_ml_claims(text=clean_text)["valid"] is True

    dirty_text = "Here is our trade_signal and guaranteed_return recommendation."
    res_dirty = validate_no_forbidden_baseline_ml_claims(text=dirty_text)
    assert res_dirty["valid"] is False
    assert len(res_dirty["violations"]) >= 2


def test_run_baseline_ml_model_validation():
    df, summary = run_baseline_ml_model_validation()
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 5
    assert summary["all_passed"] is True
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["clean_of_forbidden_claims"] is True
    assert summary["non_signal"] is True
