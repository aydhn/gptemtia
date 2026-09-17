# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Output Contracts."""

from advanced_ensemble_model_registry.candidate_model_output_contracts import (
    build_candidate_model_output_contracts,
    validate_candidate_model_output_contracts,
    summarize_candidate_model_output_contracts,
)


def test_candidate_model_output_contracts():
    df, summary = build_candidate_model_output_contracts()
    assert len(df) == 10
    assert summary["total_output_contracts"] == 10
    assert summary["all_predictions_prohibited"] is True
    assert summary["all_probabilities_prohibited"] is True
    assert summary["all_classes_prohibited"] is True
    assert summary["all_signals_prohibited"] is True
    assert summary["all_metrics_prohibited"] is True
    assert summary["non_signal"] is True
    assert validate_candidate_model_output_contracts(df, summary) is True
