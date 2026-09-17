# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Readiness Scoring.

Calculates diagnostic readiness score for walk-forward and out-of-sample benchmark contract layer.
Score is purely diagnostic and does NOT represent trading performance or production readiness.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import WalkForwardReadinessScore


def classify_walk_forward_readiness_score(score: float) -> str:
    """Classify readiness score into standard operational bins."""
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "contract_ready_with_manual_review"
    else:
        return "walk_forward_oos_contract_ready_non_production"


def calculate_walk_forward_readiness_score(
    findings_df: pd.DataFrame, profile: WalkForwardProfile
) -> WalkForwardReadinessScore:
    """Calculate diagnostic readiness score based on findings and policy checks."""
    base_score = 1.0
    critical_count = 0
    warning_count = 0

    if not findings_df.empty:
        critical_count = len(findings_df[findings_df["severity_label"] == "CRITICAL"])
        warning_count = len(findings_df[findings_df["severity_label"] == "WARNING"])
        base_score -= critical_count * 0.30
        base_score -= warning_count * 0.05

    score = max(0.0, min(1.0, base_score))
    meets_threshold = score >= profile.min_readiness_score
    classification = classify_walk_forward_readiness_score(score)

    return WalkForwardReadinessScore(
        score=round(score, 2),
        classification=classification,
        total_findings=len(findings_df),
        critical_blockers=critical_count,
        meets_threshold=meets_threshold,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
    )


def build_walk_forward_readiness_score_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for readiness score report."""
    from advanced_walk_forward_validation.walk_forward_findings import (
        build_walk_forward_findings_registry,
    )

    findings_df, _ = build_walk_forward_findings_registry(profile)
    readiness = calculate_walk_forward_readiness_score(findings_df, profile)

    rows = [
        {
            "score": readiness.score,
            "classification": readiness.classification,
            "meets_threshold": readiness.meets_threshold,
            "min_threshold": profile.min_readiness_score,
            "total_findings": readiness.total_findings,
            "critical_blockers": readiness.critical_blockers,
            "production_ready": readiness.production_ready,
            "broker_ready": readiness.broker_ready,
            "non_signal": readiness.non_signal,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "score": readiness.score,
        "classification": readiness.classification,
        "meets_threshold": readiness.meets_threshold,
        "critical_blockers": readiness.critical_blockers,
        "production_ready": False,
        "broker_ready": False,
        "non_signal": True,
    }
    return df, summary
