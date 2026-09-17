"""Test suite for Phase 138 and Phase 139 No Real Training Execution."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.no_real_training_execution import (
    build_no_real_training_execution_report,
    summarize_no_real_training_execution,
    validate_no_real_training_request,
)
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.no_real_training_execution import (
    build_no_real_training_execution_report as build_phase_139_no_real_training_execution_report,
    summarize_no_real_training_execution as summarize_phase_139_no_real_training_execution,
    validate_no_real_training_request as validate_phase_139_no_real_training_request,
)


def test_build_no_real_training_execution_report():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_no_real_training_execution_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["real_training_executed"] is False
    assert summary["model_fit_executed"] is False
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_validate_no_real_training_request():
    assert validate_no_real_training_request("inspect_contracts")["blocked"] is False
    assert validate_no_real_training_request("please run fit and train")["blocked"] is True
    assert validate_no_real_training_request("train_model_now")["blocked"] is True


def test_phase_139_build_no_real_training_execution_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_phase_139_no_real_training_execution_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["real_training_executed"] is False
    assert summary["model_fit_executed"] is False
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_phase_139_validate_no_real_training_request():
    assert validate_phase_139_no_real_training_request("inspect_governance_contracts")["blocked"] is False
    assert validate_phase_139_no_real_training_request("please run fit and backward pass")["blocked"] is True
    assert validate_phase_139_no_real_training_request("optimizer_step call")["blocked"] is True
