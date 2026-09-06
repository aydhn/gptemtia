"""Test suite for Phase 136 ML Runtime Readiness Scoring."""

import pytest
from advanced_gpu_ml_runtime.ml_runtime_readiness_scoring import (
    build_ml_runtime_readiness_score_report,
    calculate_ml_runtime_readiness_score,
)


def test_build_ml_runtime_readiness_score_report():
    df, summary = build_ml_runtime_readiness_score_report()
    assert not df.empty
    assert "readiness_score" in summary
    assert 0.0 <= summary["readiness_score"] <= 1.0
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False


def test_calculate_ml_runtime_readiness_score():
    score = calculate_ml_runtime_readiness_score()
    assert hasattr(score, "readiness_score")
    assert isinstance(score.readiness_score, float)
    assert 0.0 <= score.readiness_score <= 1.0
