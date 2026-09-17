"""Test suite for Phase 139 Dry-Run Resource Checks."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.dry_run_resource_checks import (
    build_dry_run_resource_check_report,
    run_dry_run_resource_check,
    summarize_dry_run_resource_checks,
)


def test_build_dry_run_resource_check_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_dry_run_resource_check_report(profile)

    assert len(df) == 4
    assert summary["total_checks"] == 4
    assert summary["all_passed"] is True
    assert summary["all_dry_run"] is True
    assert summary["non_signal"] is True


def test_run_dry_run_resource_check():
    valid_res = run_dry_run_resource_check({"memory_fraction": 0.70, "timeout_seconds": 600})
    assert valid_res["check_passed"] is True
    assert valid_res["real_training_executed"] is False
    assert valid_res["model_fit_executed"] is False
    assert valid_res["non_signal"] is True
    assert valid_res["status"] == "PASS"

    invalid_res = run_dry_run_resource_check({"memory_fraction": 0.95, "timeout_seconds": 5000})
    assert invalid_res["check_passed"] is False
    assert len(invalid_res["reasons"]) == 2
    assert invalid_res["status"] == "BLOCKED"
