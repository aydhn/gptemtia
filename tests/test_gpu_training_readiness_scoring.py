"""Test suite for Phase 139 GPU Training Readiness Scoring."""

import pandas as pd
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_readiness_scoring import (
    build_gpu_training_readiness_score_report,
    calculate_gpu_training_readiness_score,
    classify_gpu_training_readiness_score,
    summarize_gpu_training_readiness_scores,
)


def test_classify_gpu_training_readiness_score():
    assert classify_gpu_training_readiness_score(0.90) == "READY_FOR_GPU_RESOURCE_GOVERNANCE_DRY_RUN"
    assert classify_gpu_training_readiness_score(0.75) == "READY_WITH_MONITORED_POLICIES"
    assert classify_gpu_training_readiness_score(0.50) == "READY_WITH_REVIEW_REQUIRED"
    assert classify_gpu_training_readiness_score(0.30) == "BLOCKED_BY_GOVERNANCE_GAPS"


def test_calculate_gpu_training_readiness_score():
    profile = get_default_gpu_training_governance_profile()

    # Empty findings should yield 1.0
    empty_df = pd.DataFrame()
    score_clean = calculate_gpu_training_readiness_score(empty_df, profile)
    assert score_clean.score == 1.0
    assert score_clean.meets_threshold is True
    assert score_clean.production_ready is False
    assert score_clean.real_training_approved is False

    # Deductions test
    findings_df = pd.DataFrame([
        {"severity_label": "CRITICAL"},
        {"severity_label": "HIGH"},
    ])
    score_deducted = calculate_gpu_training_readiness_score(findings_df, profile)
    assert score_deducted.score == 0.55  # 1.0 - 0.30 - 0.15


def test_build_gpu_training_readiness_score_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_readiness_score_report(profile)

    assert len(df) == 1
    assert summary["readiness_score"] >= 0.85
    assert summary["meets_threshold"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["real_training_approved"] is False
    assert summary["non_signal"] is True
