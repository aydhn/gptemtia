"""Test suite for Phase 138 and Phase 139 No Prediction Execution."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.no_prediction_execution import (
    build_no_prediction_execution_report,
    summarize_no_prediction_execution,
    validate_no_prediction_request,
)
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.no_prediction_execution import (
    build_no_prediction_execution_report as build_phase_139_no_prediction_execution_report,
    summarize_no_prediction_execution as summarize_phase_139_no_prediction_execution,
    validate_no_prediction_request as validate_phase_139_no_prediction_request,
)


def test_build_no_prediction_execution_report():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_no_prediction_execution_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["model_predict_executed"] is False
    assert summary["model_inference_executed"] is False
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_validate_no_prediction_request():
    assert validate_no_prediction_request("metadata_only_check")["blocked"] is False
    assert validate_no_prediction_request("call predict on sample")["blocked"] is True
    assert validate_no_prediction_request("forward inference pass")["blocked"] is True


def test_phase_139_build_no_prediction_execution_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_phase_139_no_prediction_execution_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["model_predict_executed"] is False
    assert summary["model_inference_executed"] is False
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_phase_139_validate_no_prediction_request():
    assert validate_phase_139_no_prediction_request("inspect_harness_contracts")["blocked"] is False
    assert validate_phase_139_no_prediction_request("predict_proba request")["blocked"] is True
    assert validate_phase_139_no_prediction_request("run neural forward pass")["blocked"] is True
