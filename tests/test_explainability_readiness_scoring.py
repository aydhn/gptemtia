# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Readiness Scoring."""

import pytest
from advanced_explainability_attribution.explainability_readiness_scoring import (
    calculate_explainability_readiness_score,
    build_explainability_readiness_dataframe,
)


def test_explainability_readiness_scoring():
    score = calculate_explainability_readiness_score()
    assert score.readiness_score == 1.0
    assert score.classification == "ready_for_phase_144_model_governance"
    assert score.meets_threshold is True
    assert score.non_signal is True

    df, summary = build_explainability_readiness_dataframe(score)
    assert len(df) == 1
    assert summary["readiness_score"] == 1.0
    assert summary["current_phase"] == 143
    assert summary["next_phase"] == 144
