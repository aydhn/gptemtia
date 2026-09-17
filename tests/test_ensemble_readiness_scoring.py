# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Readiness Scoring."""

from advanced_ensemble_model_registry.ensemble_readiness_scoring import (
    calculate_ensemble_readiness_score,
    validate_ensemble_readiness_score,
    summarize_ensemble_readiness_score,
)


def test_ensemble_readiness_scoring():
    score = calculate_ensemble_readiness_score()
    assert 0.0 <= score.readiness_score <= 1.0
    assert score.meets_threshold is True
    assert score.classification == "READY_FOR_PHASE_141_HANDOFF"
    assert validate_ensemble_readiness_score(score) is True

    summary = summarize_ensemble_readiness_score(score)
    assert summary["meets_threshold"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
