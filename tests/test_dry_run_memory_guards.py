"""Test suite for Phase 139 Dry-Run Memory Guards."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.dry_run_memory_guards import (
    build_dry_run_memory_guard_report,
    summarize_dry_run_memory_guards,
    validate_dry_run_memory_request,
)


def test_build_dry_run_memory_guard_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_dry_run_memory_guard_report(profile)

    assert len(df) == 4
    assert summary["total_tests"] == 4
    assert summary["all_dry_run"] is True
    assert summary["guards_enforced"] is True
    assert summary["non_signal"] is True


def test_validate_dry_run_memory_request():
    valid = validate_dry_run_memory_request({"requested_fraction": 0.60})
    assert valid["is_valid"] is True
    assert valid["blocked"] is False

    invalid = validate_dry_run_memory_request({"requested_fraction": 0.90})
    assert invalid["is_valid"] is False
    assert invalid["blocked"] is True
