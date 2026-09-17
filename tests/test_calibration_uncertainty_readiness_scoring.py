# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Readiness Scoring."""

from advanced_calibration_uncertainty.calibration_uncertainty_readiness_scoring import (
    calculate_calibration_uncertainty_readiness_score,
    build_calibration_uncertainty_readiness_score_report,
    summarize_calibration_uncertainty_readiness_scores,
)


def test_calibration_uncertainty_readiness_scoring():
    score_obj = calculate_calibration_uncertainty_readiness_score()
    assert score_obj.readiness_score >= 0.85
    assert score_obj.non_signal is True
    assert score_obj.production_ready is False
    assert score_obj.broker_ready is False

    df, summary = build_calibration_uncertainty_readiness_score_report()
    assert summary["readiness_score"] >= 0.85
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
