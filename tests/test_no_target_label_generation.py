"""Test suite for Phase 138 and Phase 139 No Target/Label Generation."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.no_target_label_generation import (
    build_no_target_label_generation_report,
    summarize_no_target_label_generation,
    validate_no_target_label_generation_request,
)
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.no_target_label_generation import (
    build_no_target_label_generation_report as build_phase_139_no_target_label_generation_report,
    summarize_no_target_label_generation as summarize_phase_139_no_target_label_generation,
    validate_no_target_label_generation_request as validate_phase_139_no_target_label_generation_request,
)


def test_build_no_target_label_generation_report():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_no_target_label_generation_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["target_label_generated"] is False
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_validate_no_target_label_generation_request():
    assert validate_no_target_label_generation_request("read_contracts")["blocked"] is False
    assert validate_no_target_label_generation_request("compute future return target")["blocked"] is True
    assert validate_no_target_label_generation_request("generate label column")["blocked"] is True


def test_phase_139_build_no_target_label_generation_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_phase_139_no_target_label_generation_report(profile)

    assert len(df) == 3
    assert summary["all_disabled"] is True
    assert summary["target_label_generated"] is False
    assert summary["current_phase"] == 139
    assert summary["non_signal"] is True
    assert bool((df["status"] == "PASS_DISABLED").all())


def test_phase_139_validate_no_target_label_generation_request():
    assert validate_phase_139_no_target_label_generation_request("inspect_input_guards")["blocked"] is False
    assert validate_phase_139_no_target_label_generation_request("calculate shift(-1) target")["blocked"] is True
    assert validate_phase_139_no_target_label_generation_request("forward_return vector")["blocked"] is True
