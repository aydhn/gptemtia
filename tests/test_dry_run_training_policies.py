"""Test suite for Phase 138 Dry-Run Training Policies."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.dry_run_training_policies import (
    DRY_RUN_POLICIES,
    build_dry_run_training_policy_registry,
    summarize_dry_run_training_policies,
    validate_dry_run_training_request,
)


def test_dry_run_policies_data():
    assert len(DRY_RUN_POLICIES) == 6
    policy_ids = [p["policy_id"] for p in DRY_RUN_POLICIES]
    assert "policy_zero_real_training" in policy_ids
    assert "policy_zero_model_fit" in policy_ids
    assert "policy_zero_prediction" in policy_ids


def test_build_dry_run_training_policy_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_dry_run_training_policy_registry(profile)

    assert len(df) == 6
    assert summary["total_policies"] == 6
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True


def test_validate_dry_run_training_request():
    clean_req = {"mode": "dry_run_mock", "contracts": ["contract_rf"]}
    assert validate_dry_run_training_request(clean_req)["blocked"] is False

    fit_req = {"action": "call_fit_on_data"}
    assert validate_dry_run_training_request(fit_req)["blocked"] is True

    predict_req = {"action": "generate_predict"}
    assert validate_dry_run_training_request(predict_req)["blocked"] is True
