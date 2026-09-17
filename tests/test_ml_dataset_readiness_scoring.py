"""Test suite for Phase 137 ML Dataset Readiness Scoring."""

import pytest
import pandas as pd
from advanced_ml_dataset_registry.ml_dataset_readiness_scoring import (
    calculate_ml_dataset_readiness_score,
    build_ml_dataset_readiness_score_report,
    classify_ml_dataset_readiness_score,
    summarize_ml_dataset_readiness_scores,
)


def test_build_readiness_score_report():
    df, summary = build_ml_dataset_readiness_score_report()
    assert not df.empty
    assert 0.0 <= summary["readiness_score"] <= 1.0
    assert summary["training_approved"] is False
    assert summary["dataset_materialization_approved"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["non_signal"] is True


def test_classify_scores():
    assert classify_ml_dataset_readiness_score(0.90) == "READY_FOR_LOCAL_ML_CONTRACTS"
    assert classify_ml_dataset_readiness_score(0.70) == "CONTRACT_READY_WITH_WARNINGS"
    assert classify_ml_dataset_readiness_score(0.50) == "PLACEHOLDER_CONTRACTS_ACTIVE"
    assert classify_ml_dataset_readiness_score(0.20) == "BLOCKED_BY_SAFETY_CONTRACTS"
