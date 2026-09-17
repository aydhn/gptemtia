# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Candidate Model Prediction Disabled Report."""

from advanced_ensemble_model_registry.candidate_model_prediction_disabled import (
    build_candidate_model_prediction_disabled_report,
    validate_candidate_model_prediction_disabled_report,
    summarize_candidate_model_prediction_disabled_report,
)


def test_candidate_model_prediction_disabled():
    report = build_candidate_model_prediction_disabled_report()
    assert report["model_predict_executed"] is False
    assert report["predictions_generated"] == 0
    assert report["probabilities_generated"] == 0
    assert report["non_signal"] is True
    assert validate_candidate_model_prediction_disabled_report(report) is True

    summary = summarize_candidate_model_prediction_disabled_report(report)
    assert summary["prediction_disabled"] is True
