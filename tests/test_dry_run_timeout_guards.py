"""Test suite for Phase 139 Dry-Run Timeout Guards."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.dry_run_timeout_guards import (
    build_dry_run_timeout_guard_report,
    summarize_dry_run_timeout_guards,
    validate_dry_run_timeout_request,
)


def test_build_dry_run_timeout_guard_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_dry_run_timeout_guard_report(profile)

    assert len(df) == 5
    assert summary["total_tests"] == 5
    assert summary["all_dry_run"] is True
    assert summary["guards_enforced"] is True
    assert summary["non_signal"] is True


def test_validate_dry_run_timeout_request():
    valid = validate_dry_run_timeout_request({"requested_timeout": 1200})
    assert valid["is_valid"] is True
    assert valid["blocked"] is False

    invalid_high = validate_dry_run_timeout_request({"requested_timeout": 5000})
    assert invalid_high["is_valid"] is False
    assert invalid_high["blocked"] is True

    invalid_zero = validate_dry_run_timeout_request({"requested_timeout": 0})
    assert invalid_zero["is_valid"] is False
    assert invalid_zero["blocked"] is True
