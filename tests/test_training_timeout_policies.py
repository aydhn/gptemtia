"""Test suite for Phase 139 Training Timeout Policies."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.training_timeout_policies import (
    build_training_timeout_policy_registry,
    summarize_training_timeout_policies,
    validate_training_timeout_policy,
)


def test_build_training_timeout_policy_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_training_timeout_policy_registry(profile)

    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["all_terminate_on_timeout"] is True
    assert summary["all_dry_run"] is True
    assert summary["max_ceiling_seconds"] <= 7200
    assert summary["non_signal"] is True


def test_validate_training_timeout_policy():
    valid_pol = {
        "policy_name": "valid_timeout",
        "max_timeout_seconds": 1800,
        "terminate_on_timeout": True,
    }
    res = validate_training_timeout_policy(valid_pol)
    assert res["is_valid"] is True
    assert len(res["violations"]) == 0

    invalid_pol = {
        "policy_name": "excessive_timeout",
        "max_timeout_seconds": 10000,
        "terminate_on_timeout": False,
    }
    res_inv = validate_training_timeout_policy(invalid_pol)
    assert res_inv["is_valid"] is False
    assert len(res_inv["violations"]) >= 2
