# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Families."""

from advanced_ensemble_model_registry.candidate_model_families import (
    build_candidate_model_families,
    validate_candidate_model_families,
    summarize_candidate_model_families,
    CANDIDATE_MODEL_FAMILIES,
)


def test_candidate_model_families():
    assert len(CANDIDATE_MODEL_FAMILIES) == 10
    df, summary = build_candidate_model_families()
    assert len(df) == 10
    assert summary["total_families"] == 10
    assert summary["all_placeholders"] is True
    assert summary["zero_models_instantiated"] is True
    assert summary["zero_training_executed"] is True
    assert summary["non_signal"] is True
    assert validate_candidate_model_families(df, summary) is True
