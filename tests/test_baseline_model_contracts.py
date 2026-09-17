"""Test suite for Phase 138 Baseline Model Contracts."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_contracts import (
    build_baseline_model_contract_registry,
    summarize_baseline_model_contracts,
    validate_baseline_model_contract,
)


def test_build_baseline_model_contract_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_baseline_model_contract_registry(profile)

    assert len(df) == 10
    assert summary["total_contracts"] == 10
    assert summary["all_real_training_blocked"] is True
    assert summary["all_prediction_blocked"] is True
    assert summary["all_target_label_blocked"] is True
    assert summary["all_artifact_blocked"] is True
    assert summary["all_registry_write_blocked"] is True
    assert summary["non_signal"] is True


def test_validate_baseline_model_contract():
    valid_contract = {
        "contract_id": "contract_rf",
        "real_training_allowed": False,
        "model_fit_allowed": False,
        "model_predict_allowed": False,
        "target_label_required": False,
        "artifact_persistence_allowed": False,
        "model_registry_write_allowed": False,
        "non_signal": True,
    }
    result = validate_baseline_model_contract(valid_contract)
    assert result["valid"] is True

    invalid_contract = dict(valid_contract, real_training_allowed=True)
    bad_result = validate_baseline_model_contract(invalid_contract)
    assert bad_result["valid"] is False
    assert len(bad_result["violations"]) > 0
