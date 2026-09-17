"""Test suite for Phase 138 Dry-Run Training Harness Contracts."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.dry_run_training_harness_contracts import (
    DRY_RUN_HARNESS_CONTRACTS_DATA,
    build_dry_run_training_harness_contract_registry,
    summarize_dry_run_training_harness_contracts,
    validate_dry_run_training_harness_contract,
)


def test_dry_run_harness_contracts_data():
    assert len(DRY_RUN_HARNESS_CONTRACTS_DATA) == 5
    ids = [h["harness_id"] for h in DRY_RUN_HARNESS_CONTRACTS_DATA]
    assert "harness_contract_standard_linear" in ids
    assert "harness_contract_tree_ensemble" in ids


def test_build_dry_run_harness_contract_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_dry_run_training_harness_contract_registry(profile)

    assert len(df) == 5
    assert summary["total_harness_contracts"] == 5
    assert summary["all_real_training_blocked"] is True
    assert summary["all_model_fit_blocked"] is True
    assert summary["all_predict_blocked"] is True
    assert summary["all_artifact_blocked"] is True
    assert summary["all_registry_write_blocked"] is True
    assert summary["non_signal"] is True


def test_validate_dry_run_training_harness_contract():
    valid = {
        "harness_id": "h_1",
        "real_training_allowed": False,
        "model_fit_allowed": False,
        "model_predict_allowed": False,
        "artifact_persistence_allowed": False,
        "model_registry_write_allowed": False,
        "allowed_mode": "contract_only",
    }
    assert validate_dry_run_training_harness_contract(valid)["valid"] is True

    invalid = dict(valid, real_training_allowed=True)
    assert validate_dry_run_training_harness_contract(invalid)["valid"] is False
