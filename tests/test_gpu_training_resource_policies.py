"""Test suite for Phase 139 GPU Training Resource Policies."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_resource_policies import (
    build_gpu_training_resource_policy_registry,
    summarize_gpu_training_resource_policies,
    validate_gpu_training_resource_policy,
)


def test_build_gpu_training_resource_policy_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_resource_policy_registry(profile)

    assert len(df) == 4
    assert summary["total_policies"] == 4
    assert summary["all_contract_only"] is True
    assert summary["all_real_training_disabled"] is True
    assert summary["all_prediction_disabled"] is True
    assert summary["all_manual_review_required"] is True
    assert summary["non_signal"] is True


def test_validate_gpu_training_resource_policy():
    valid_policy = {
        "policy_name": "valid_test_policy",
        "allowed_mode": "contract_only",
        "dry_run_required": True,
        "real_training_allowed": False,
        "prediction_allowed": False,
        "artifact_persistence_allowed": False,
        "model_registry_write_allowed": False,
    }
    res = validate_gpu_training_resource_policy(valid_policy)
    assert res["is_valid"] is True
    assert len(res["violations"]) == 0

    invalid_policy = {
        "policy_name": "invalid_test_policy",
        "allowed_mode": "real_execution",
        "dry_run_required": False,
        "real_training_allowed": True,
        "prediction_allowed": True,
        "artifact_persistence_allowed": True,
        "model_registry_write_allowed": True,
    }
    res_inv = validate_gpu_training_resource_policy(invalid_policy)
    assert res_inv["is_valid"] is False
    assert len(res_inv["violations"]) >= 5
