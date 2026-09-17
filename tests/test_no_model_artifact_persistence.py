"""Test suite for Phase 139 No Model Artifact Persistence."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.no_model_artifact_persistence import (
    build_no_model_artifact_persistence_report,
    summarize_no_model_artifact_persistence,
    validate_no_model_artifact_request,
)


def test_build_no_model_artifact_persistence_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_no_model_artifact_persistence_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["artifact_persisted"] is False
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_validate_no_model_artifact_request():
    assert validate_no_model_artifact_request("check_artifact_policies")["blocked"] is False
    assert validate_no_model_artifact_request("call torch.save weights.pt")["blocked"] is True
    assert validate_no_model_artifact_request("joblib.dump model.pkl")["blocked"] is True
    assert validate_no_model_artifact_request("export_weights to onnx")["blocked"] is True


def test_summarize_no_model_artifact_persistence():
    profile = get_default_gpu_training_governance_profile()
    df, _ = build_no_model_artifact_persistence_report(profile)
    summary = summarize_no_model_artifact_persistence(df)

    assert summary["total_checks"] == 3
    assert summary["all_disabled"] is True
    assert summary["artifact_persisted"] is False
    assert summary["non_signal"] is True
