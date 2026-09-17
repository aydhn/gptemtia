# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Baseline Dependencies."""

from advanced_ensemble_model_registry.candidate_model_baseline_dependencies import (
    build_candidate_model_baseline_dependencies,
    build_candidate_model_baseline_dependency_registry,
    summarize_candidate_model_baseline_dependencies,
)


def test_candidate_model_baseline_dependencies():
    df, summary = build_candidate_model_baseline_dependencies()
    assert len(df) == 2
    assert summary["total_dependencies"] == 2
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
