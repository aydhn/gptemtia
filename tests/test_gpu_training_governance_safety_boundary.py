"""Test suite for Phase 139 GPU Training Governance Safety Boundary."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_safety_boundary import (
    NO_GO_CONDITIONS,
    SAFE_GO_CONDITIONS,
    build_gpu_training_governance_no_go_conditions,
    build_gpu_training_governance_safe_go_conditions,
    build_gpu_training_governance_safety_boundary,
    summarize_gpu_training_governance_safety_boundary,
)


def test_build_gpu_training_governance_no_go_conditions():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_governance_no_go_conditions(profile)

    assert len(df) == len(NO_GO_CONDITIONS)
    assert summary["total_no_go_rules"] == 24
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True


def test_build_gpu_training_governance_safe_go_conditions():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_governance_safe_go_conditions(profile)

    assert len(df) == len(SAFE_GO_CONDITIONS)
    assert summary["total_safe_go_rules"] == 10
    assert summary["all_active"] is True
    assert summary["non_signal"] is True


def test_build_gpu_training_governance_safety_boundary():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_governance_safety_boundary(profile)

    assert len(df) == 34
    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] == 24
    assert summary["safe_go_count"] == 10
    assert summary["live_trading_prohibited"] is True
    assert summary["zero_model_execution"] is True
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True
