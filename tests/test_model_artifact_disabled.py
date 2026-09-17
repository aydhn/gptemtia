"""Test suite for Phase 138 Model Artifact Persistence Disabled."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.model_artifact_disabled import (
    build_model_artifact_disabled_report,
    summarize_model_artifact_disabled,
    validate_no_model_artifact_request,
)


def test_build_model_artifact_disabled_report():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_model_artifact_disabled_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["artifact_persisted"] is False
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_validate_no_model_artifact_request():
    assert validate_no_model_artifact_request("check_status")["blocked"] is False
    assert validate_no_model_artifact_request("joblib.dump(model, path)")["blocked"] is True
    assert validate_no_model_artifact_request("save_model to disk")["blocked"] is True
