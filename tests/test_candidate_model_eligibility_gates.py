# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Eligibility Gates."""

from advanced_ensemble_model_registry.candidate_model_eligibility_gates import (
    build_candidate_model_eligibility_gates,
    validate_candidate_model_eligibility_gates,
    validate_candidate_eligibility_request,
    summarize_candidate_model_eligibility_gates,
)


def test_candidate_model_eligibility_gates():
    df, summary = build_candidate_model_eligibility_gates()
    assert len(df) == 12
    assert summary["total_gates"] == 12
    assert summary["all_gates_passed"] is True
    assert summary["all_blocks_execution"] is True
    assert summary["non_signal"] is True
    assert validate_candidate_model_eligibility_gates(df, summary) is True


def test_validate_candidate_eligibility_request():
    safe_req = {"gate_name": "training_prohibition_gate", "action": "inspect_metadata"}
    res_safe = validate_candidate_eligibility_request(safe_req)
    assert res_safe["eligible"] is True
    assert res_safe["blocked"] is False

    unsafe_req = {"gate_name": "training_prohibition_gate", "action": "train_model"}
    res_unsafe = validate_candidate_eligibility_request(unsafe_req)
    assert res_unsafe["eligible"] is False
    assert res_unsafe["blocked"] is True
