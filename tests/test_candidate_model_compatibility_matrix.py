# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Compatibility Matrix."""

from advanced_ensemble_model_registry.candidate_model_compatibility_matrix import (
    build_candidate_compatibility_matrix,
    validate_candidate_compatibility_matrix,
    summarize_candidate_compatibility_matrix,
)


def test_candidate_model_compatibility_matrix():
    df, summary = build_candidate_compatibility_matrix()
    assert len(df) == 10
    assert summary["total_compatibility_records"] == 10
    assert summary["all_scores_non_signal"] is True
    assert summary["all_scores_non_performance"] is True
    assert summary["non_signal"] is True
    assert validate_candidate_compatibility_matrix(df, summary) is True
