# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Training Disabled Report."""

from advanced_ensemble_model_registry.candidate_model_training_disabled import (
    build_candidate_model_training_disabled_report,
    validate_candidate_model_training_disabled_report,
    summarize_candidate_model_training_disabled_report,
)


def test_candidate_model_training_disabled():
    report = build_candidate_model_training_disabled_report()
    assert report["real_training_executed"] is False
    assert report["model_fit_executed"] is False
    assert report["epochs_run"] == 0
    assert report["non_signal"] is True
    assert validate_candidate_model_training_disabled_report(report) is True

    summary = summarize_candidate_model_training_disabled_report(report)
    assert summary["training_disabled"] is True
