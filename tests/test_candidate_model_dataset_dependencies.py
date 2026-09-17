# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Dataset Dependencies."""

from advanced_ensemble_model_registry.candidate_model_dataset_dependencies import (
    build_candidate_model_dataset_dependency_registry,
    summarize_candidate_model_dataset_dependencies,
)


def test_candidate_model_dataset_dependencies():
    df, summary = build_candidate_model_dataset_dependency_registry()
    assert len(df) == 2
    assert summary["total_dependencies"] == 2
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
