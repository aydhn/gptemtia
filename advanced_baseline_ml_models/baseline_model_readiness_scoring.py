# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Readiness Scoring.

Computes readiness scores for baseline model contracts and dry-run harness.
Strictly disclaims trading signal status, production readiness, and training approval.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_models import BaselineModelReadinessScore


def classify_baseline_model_readiness_score(score: float) -> str:
    """Classify the numeric readiness score into a safety tier."""
    if score >= 0.85:
        return "READY_FOR_LOCAL_DRY_RUN_HARNESS"
    elif score >= 0.65:
        return "CONTRACT_READY_WITH_REVIEWS"
    elif score >= 0.45:
        return "MINIMAL_CONTRACT_ACCEPTANCE"
    else:
        return "BLOCKED_BY_SAFETY_FINDINGS"


def calculate_baseline_model_readiness_score(
    findings_df: pd.DataFrame,
    profile: BaselineMlModelProfile | None = None,
) -> BaselineModelReadinessScore:
    """Calculate overall baseline model readiness score."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    total_findings = len(findings_df)
    critical_blockers = 0
    if not findings_df.empty and "severity_label" in findings_df.columns:
        critical_blockers = int((findings_df["severity_label"] == "CRITICAL").sum())

    # Base score of 1.0, deducted for critical findings
    base_score = 1.0
    deduction = critical_blockers * 0.35 + (total_findings - critical_blockers) * 0.05
    score = max(0.0, min(1.0, base_score - deduction))

    classification = classify_baseline_model_readiness_score(score)

    return BaselineModelReadinessScore(
        score=round(score, 4),
        score_tier=classification,
        critical_blockers=critical_blockers,
        total_findings=total_findings,
        classification=classification,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
        official_approval=False,
        real_training_approved=False,
        dataset_materialization_approved=False,
    )


def build_baseline_model_readiness_score_report(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build readiness score report DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    # Default clean baseline findings
    from advanced_baseline_ml_models.baseline_model_findings import build_baseline_model_findings_registry
    findings_df, _ = build_baseline_model_findings_registry(profile)

    readiness = calculate_baseline_model_readiness_score(findings_df, profile)

    rows = [{
        "score": readiness.score,
        "score_tier": readiness.score_tier,
        "classification": readiness.classification,
        "critical_blockers": readiness.critical_blockers,
        "total_findings": readiness.total_findings,
        "non_signal": readiness.non_signal,
        "production_ready": readiness.production_ready,
        "broker_ready": readiness.broker_ready,
        "official_approval": readiness.official_approval,
        "real_training_approved": readiness.real_training_approved,
        "dataset_materialization_approved": readiness.dataset_materialization_approved,
    }]

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_readiness_scores(df)
    return df, summary


def summarize_baseline_model_readiness_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize readiness score DataFrame."""
    score = float(df["score"].iloc[0]) if not df.empty else 1.0
    tier = str(df["score_tier"].iloc[0]) if not df.empty else "READY_FOR_LOCAL_DRY_RUN_HARNESS"
    return {
        "readiness_score": score,
        "score_tier": tier,
        "is_ready_for_dry_run": score >= 0.45,
        "trade_signal_certified": False,
        "production_ready": False,
        "broker_ready": False,
        "non_signal": True,
    }
