"""Test suite for Phase 139 GPU Training Governance Health Check."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_health import (
    build_gpu_training_governance_health_check,
    summarize_gpu_training_governance_health,
)


def test_build_gpu_training_governance_health_check():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_governance_health_check(profile=profile)

    assert len(df) >= 10
    assert summary["health_status"] == "SYSTEM_HEALTHY"
    assert summary["all_healthy"] is True
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True


def test_summarize_gpu_training_governance_health():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_gpu_training_governance_health_check(profile=profile)
    summary = summarize_gpu_training_governance_health(df)

    assert summary["health_status"] == "SYSTEM_HEALTHY"
    assert summary["all_healthy"] is True
    assert summary["non_signal"] is True
