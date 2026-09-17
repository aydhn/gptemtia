# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Input Contracts."""

from advanced_ensemble_model_registry.candidate_model_input_contracts import (
    build_candidate_model_input_contracts,
    validate_candidate_model_input_contracts,
    summarize_candidate_model_input_contracts,
)


def test_candidate_model_input_contracts():
    df, summary = build_candidate_model_input_contracts()
    assert len(df) == 10
    assert summary["total_input_contracts"] == 10
    assert summary["all_no_lookahead_guaranteed"] is True
    assert summary["all_metadata_only_news_guaranteed"] is True
    assert summary["all_source_preserved"] is True
    assert summary["zero_targets_contained"] is True
    assert summary["zero_signals_contained"] is True
    assert summary["non_signal"] is True
    assert validate_candidate_model_input_contracts(df, summary) is True
