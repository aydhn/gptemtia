"""Test suite for Phase 139 GPU Training Governance Validation."""

import pandas as pd
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_validation import (
    build_gpu_training_governance_validation_report,
    validate_gpu_training_governance_manifest,
    validate_gpu_training_governance_profile_registry,
    validate_gpu_training_harness_contracts,
    validate_gpu_training_resource_policies,
    validate_no_forbidden_gpu_training_claims,
)


def test_validate_no_forbidden_gpu_training_claims():
    clean_res = validate_no_forbidden_gpu_training_claims(text="normal offline research text")
    assert clean_res["is_clean"] is True
    assert len(clean_res["violations"]) == 0

    dirty_res = validate_no_forbidden_gpu_training_claims(text="This model is production ready with high sharpe ratio")
    assert dirty_res["is_clean"] is False
    assert len(dirty_res["violations"]) >= 2


def test_build_gpu_training_governance_validation_report():
    profile = get_default_gpu_training_governance_profile()

    # Pass empty dict to let validators default or create mock tables
    sample_tables = {
        "profiles": pd.DataFrame([{"real_training_allowed": False, "dry_run_default": True}]),
        "resource_policies": pd.DataFrame([{"allowed_mode": "contract_only", "real_training_allowed": False}]),
        "harness_contracts": pd.DataFrame([{"allowed_execution": False, "dry_run_only": True}]),
        "manifest": pd.DataFrame([{
            "current_phase": 139,
            "target_final_phase": 160,
            "next_phase": 140,
            "dry_run": True,
            "local_only": True,
            "real_training_executed": False,
            "model_fit_executed": False,
            "model_predict_executed": False,
            "metric_calculation_executed": False,
            "artifact_persisted": False,
            "model_registry_written": False,
            "dataset_materialized": False,
            "feature_snapshot_materialized": False,
            "production_ready": False,
            "broker_ready": False,
            "official_approval": False,
        }]),
    }

    df, summary = build_gpu_training_governance_validation_report(sample_tables, profile)

    assert len(df) == 5
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["all_passed"] is True
    assert summary["forbidden_claims_clean"] is True
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True
