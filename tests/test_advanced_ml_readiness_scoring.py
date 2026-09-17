# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Readiness Scoring."""

import pytest
import pandas as pd
from advanced_ml_acceptance.advanced_ml_readiness_scoring import (
    calculate_advanced_ml_readiness_score,
    build_advanced_ml_readiness_score_report,
    classify_advanced_ml_readiness_score,
    summarize_advanced_ml_readiness_scores,
)


def test_readiness_scoring():
    df, summary = build_advanced_ml_readiness_score_report()
    assert not df.empty
    assert 0.0 <= summary["readiness_score"] <= 1.0
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["official_approval"] is False
    assert summary["non_signal"] is True

    s = summarize_advanced_ml_readiness_scores(df)
    assert s["score"] == summary["readiness_score"]
    assert s["production_ready"] is False


def test_classify_scores():
    assert classify_advanced_ml_readiness_score(0.10) == "blocked"
    assert classify_advanced_ml_readiness_score(0.40) == "incomplete"
    assert classify_advanced_ml_readiness_score(0.60) == "contract_ready_with_manual_review"
    assert classify_advanced_ml_readiness_score(0.90) == "advanced_ml_contract_acceptance_ready_non_production"

    with pytest.raises(ValueError):
        classify_advanced_ml_readiness_score(1.5)
