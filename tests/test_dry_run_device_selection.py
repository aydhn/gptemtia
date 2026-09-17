"""Test suite for Phase 139 Dry-Run Device Selection."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.dry_run_device_selection import (
    build_dry_run_device_selection_report,
    summarize_dry_run_device_selection,
)


def test_build_dry_run_device_selection_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_dry_run_device_selection_report(profile)

    assert len(df) == 3
    assert summary["total_simulations"] == 3
    assert summary["all_dry_run"] is True
    assert summary["all_zero_allocation"] is True
    assert summary["non_signal"] is True


def test_summarize_dry_run_device_selection():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_dry_run_device_selection_report(profile)
    summary = summarize_dry_run_device_selection(df)

    assert summary["total_simulations"] == 3
    assert summary["all_zero_allocation"] is True
    assert summary["non_signal"] is True
