# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Experiment Linkage."""

from advanced_ensemble_model_registry.ensemble_experiment_linkage import (
    build_ensemble_experiment_linkage,
    validate_ensemble_experiment_linkage,
    summarize_ensemble_experiment_linkage,
)


def test_ensemble_experiment_linkage():
    linkage = build_ensemble_experiment_linkage()
    assert len(linkage) == 11
    assert "linear_candidate" in linkage
    assert "ensemble_meta_contract" in linkage
    assert validate_ensemble_experiment_linkage(linkage) is True

    summary = summarize_ensemble_experiment_linkage(linkage)
    assert summary["total_experiments_linked"] == 11
    assert summary["all_offline"] is True
    assert summary["all_non_signal"] is True
