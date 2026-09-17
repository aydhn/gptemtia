"""Test suite for Phase 139 No Model Registry Write."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.no_model_registry_write import (
    build_no_model_registry_write_report,
    summarize_no_model_registry_write,
    validate_no_model_registry_write_request,
)


def test_build_no_model_registry_write_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_no_model_registry_write_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["model_registry_written"] is False
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_validate_no_model_registry_write_request():
    assert validate_no_model_registry_write_request("inspect_registry_contracts")["blocked"] is False
    assert validate_no_model_registry_write_request("register_model to mlflow")["blocked"] is True
    assert validate_no_model_registry_write_request("mlflow.register call")["blocked"] is True
    assert validate_no_model_registry_write_request("push_to_hub repo")["blocked"] is True


def test_summarize_no_model_registry_write():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_no_model_registry_write_report(profile)
    summary = summarize_no_model_registry_write(df)

    assert summary["total_checks"] == 3
    assert summary["all_disabled"] is True
    assert summary["model_registry_written"] is False
    assert summary["non_signal"] is True
