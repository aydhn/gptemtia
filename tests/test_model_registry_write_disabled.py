"""Test suite for Phase 138 Model Registry Write Disabled."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.model_registry_write_disabled import (
    build_model_registry_write_disabled_report,
    summarize_model_registry_write_disabled,
    validate_no_model_registry_write_request,
)


def test_build_model_registry_write_disabled_report():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_model_registry_write_disabled_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["model_registry_written"] is False
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_validate_no_model_registry_write_request():
    assert validate_no_model_registry_write_request("view_manifest")["blocked"] is False
    assert validate_no_model_registry_write_request("write_model_registry entry")["blocked"] is True
    assert validate_no_model_registry_write_request("mlflow register model")["blocked"] is True
