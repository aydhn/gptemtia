"""Test suite for Phase 137 Advanced ML Dataset Validation Engine."""

import pytest
import pandas as pd
from advanced_ml_dataset_registry.advanced_ml_dataset_validation import (
    validate_advanced_ml_dataset_profile_registry,
    validate_ml_dataset_contracts,
    validate_ml_dataset_schema_registry,
    validate_ml_dataset_guards,
    validate_ml_experiment_registry,
    validate_advanced_ml_dataset_manifest,
    validate_no_forbidden_advanced_ml_dataset_claims,
    build_advanced_ml_dataset_validation_report,
)


def test_validate_forbidden_claims():
    v_clean = validate_no_forbidden_advanced_ml_dataset_claims(
        text="Phase 137 ML dataset contracts",
        summary={"signal_generated": False},
    )
    assert v_clean["valid"] is True

    v_dirty = validate_no_forbidden_advanced_ml_dataset_claims(
        text="this model generates buy signals",
    )
    assert v_dirty["valid"] is False


def test_build_validation_report():
    tables = {
        "profiles": pd.DataFrame({"current_phase": [137], "target_final_phase": [160], "next_phase": [138], "non_signal": [True]}),
        "contracts": pd.DataFrame({"materialization_allowed": [False], "target_label_generation_allowed": [False], "model_training_allowed": [False], "prediction_allowed": [False]}),
        "schemas": pd.DataFrame({"timestamp_field": ["timestamp_utc"], "non_signal": [True]}),
        "experiments": pd.DataFrame({"no_training_required": [True], "no_prediction_required": [True], "artifact_persistence_allowed": [False]}),
        "manifest": pd.DataFrame([{"current_phase": 137, "target_final_phase": 160, "next_phase": 138, "dataset_materialized": False, "feature_snapshot_materialized": False, "model_training_executed": False, "model_predict_executed": False, "non_signal": True, "official_approval": False, "production_ready": False, "broker_ready": False}]),
    }
    df, summary = build_advanced_ml_dataset_validation_report(tables)
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["validation_status"] == "VALIDATION_PASS"
