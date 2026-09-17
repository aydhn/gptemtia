"""Test suite for Phase 139 GPU Memory Budget Policies."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_memory_budget_policies import (
    build_gpu_memory_budget_policy_registry,
    summarize_gpu_memory_budget_policies,
    validate_gpu_memory_budget_request,
)


def test_build_gpu_memory_budget_policy_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_memory_budget_policy_registry(profile)

    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["all_dry_run"] is True
    assert summary["max_fraction_limit"] <= 0.85
    assert summary["non_signal"] is True


def test_validate_gpu_memory_budget_request():
    valid_res = validate_gpu_memory_budget_request({"requested_fraction": 0.70})
    assert valid_res["is_valid"] is True
    assert valid_res["blocked"] is False
    assert valid_res["real_memory_allocated"] is False

    invalid_res = validate_gpu_memory_budget_request({"requested_fraction": 0.95})
    assert invalid_res["is_valid"] is False
    assert invalid_res["blocked"] is True

    invalid_zero = validate_gpu_memory_budget_request({"requested_fraction": -0.1})
    assert invalid_zero["is_valid"] is False
    assert invalid_zero["blocked"] is True
