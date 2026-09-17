# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model GPU Governance Dependencies."""

from advanced_ensemble_model_registry.candidate_model_gpu_governance_dependencies import (
    build_candidate_model_gpu_governance_dependency_registry,
    summarize_candidate_model_gpu_governance_dependencies,
)


def test_candidate_model_gpu_governance_dependencies():
    df, summary = build_candidate_model_gpu_governance_dependency_registry()
    assert len(df) == 3
    assert summary["total_dependencies"] == 3
    assert summary["all_satisfied"] is True
    assert summary["all_non_signal"] is True
