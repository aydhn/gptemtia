# -*- coding: utf-8 -*-
"""Unit tests for baseline model readiness scoring."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_readiness_scoring import (
    classify_baseline_model_readiness_score,
    calculate_baseline_model_readiness_score,
    build_baseline_model_readiness_score_report,
    summarize_baseline_model_readiness_scores,
)


def test_classify_baseline_model_readiness_score():
    assert classify_baseline_model_readiness_score(0.95) == "READY_FOR_LOCAL_DRY_RUN_HARNESS"
    assert classify_baseline_model_readiness_score(0.70) == "CONTRACT_READY_WITH_REVIEWS"
    assert classify_baseline_model_readiness_score(0.50) == "MINIMAL_CONTRACT_ACCEPTANCE"
    assert classify_baseline_model_readiness_score(0.20) == "BLOCKED_BY_SAFETY_FINDINGS"


def test_calculate_baseline_model_readiness_score_clean():
    empty_findings = pd.DataFrame(columns=["severity_label"])
    score = calculate_baseline_model_readiness_score(empty_findings)
    assert score.score == 1.0
    assert score.critical_blockers == 0
    assert score.total_findings == 0
    assert score.score_tier == "READY_FOR_LOCAL_DRY_RUN_HARNESS"
    assert score.non_signal is True
    assert score.production_ready is False
    assert score.broker_ready is False
    assert score.official_approval is False


def test_build_baseline_model_readiness_score_report():
    df, summary = build_baseline_model_readiness_score_report()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert summary["readiness_score"] == 1.0
    assert summary["is_ready_for_dry_run"] is True
    assert summary["trade_signal_certified"] is False
    assert summary["production_ready"] is False
    assert summary["non_signal"] is True
