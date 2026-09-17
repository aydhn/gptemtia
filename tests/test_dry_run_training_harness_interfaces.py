"""Test suite for Phase 138 Dry-Run Training Harness Interfaces."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.dry_run_training_harness_interfaces import (
    PERMITTED_INTERFACES,
    PROHIBITED_INTERFACES,
    build_dry_run_training_harness_interface_registry,
    summarize_dry_run_training_harness_interfaces,
    validate_interface_permission,
)


def test_interface_definitions():
    assert len(PERMITTED_INTERFACES) == 6
    assert len(PROHIBITED_INTERFACES) == 9
    prohibited_names = [p["method_name"] for p in PROHIBITED_INTERFACES]
    assert "fit" in prohibited_names
    assert "predict" in prohibited_names
    assert "train" in prohibited_names
    assert "write_model_registry" in prohibited_names


def test_build_dry_run_harness_interface_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_dry_run_training_harness_interface_registry(profile)

    assert len(df) == 15
    assert summary["total_interfaces"] == 15
    assert summary["permitted_count"] == 6
    assert summary["prohibited_count"] == 9
    assert summary["fit_prohibited"] is True
    assert summary["predict_prohibited"] is True
    assert summary["non_signal"] is True


def test_validate_interface_permission():
    res_valid = validate_interface_permission("validate_contracts")
    assert res_valid["permitted"] is True

    res_fit = validate_interface_permission("fit")
    assert res_fit["permitted"] is False
    assert res_fit["status"] == "INTERFACE_METHOD_PROHIBITED"

    res_predict = validate_interface_permission("predict")
    assert res_predict["permitted"] is False
