# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Contracts."""

from advanced_ensemble_model_registry.candidate_model_contracts import (
    build_candidate_model_contracts,
    validate_candidate_model_contracts,
    validate_candidate_model_contract,
    summarize_candidate_model_contracts,
)


def test_candidate_model_contracts():
    df, summary = build_candidate_model_contracts()
    assert len(df) == 10
    assert summary["total_contracts"] == 10
    assert summary["all_training_disabled"] is True
    assert summary["all_prediction_disabled"] is True
    assert summary["all_ensemble_disabled"] is True
    assert summary["all_non_signal_required"] is True
    assert validate_candidate_model_contracts(df, summary) is True


def test_validate_candidate_model_contract():
    valid_c = {
        "contract_name": "test_contract",
        "real_training_allowed": False,
        "model_fit_allowed": False,
        "model_predict_allowed": False,
        "inference_allowed": False,
        "ensemble_execution_allowed": False,
        "calibration_allowed": False,
        "target_label_generation_allowed": False,
        "artifact_persistence_allowed": False,
        "model_registry_write_allowed": False,
        "non_signal_required": True,
    }
    res = validate_candidate_model_contract(valid_c)
    assert res["is_valid"] is True

    bad_c = dict(valid_c, real_training_allowed=True)
    res_bad = validate_candidate_model_contract(bad_c)
    assert res_bad["is_valid"] is False
