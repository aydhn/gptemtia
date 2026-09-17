# -*- coding: utf-8 -*-
"""Phase 148: Stress Readiness Scoring.

Calculates diagnostic readiness score for stress testing and scenario simulation contracts.
Diagnostic metric only; non-signal invariant, zero production or broker readiness claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressReadinessScore


def classify_stress_readiness_score(score: float) -> str:
    """Classify the numeric readiness score into canonical operational categories."""
    if score < 0.25:
        return "blocked"
    if score < 0.50:
        return "incomplete"
    if score < 0.75:
        return "contract_ready_with_manual_review"
    return "stress_testing_contract_ready_non_production"


def calculate_stress_readiness_score(
    findings_df: pd.DataFrame,
    profile: StressTestingProfile,
) -> StressReadinessScore:
    """Calculate diagnostic readiness score based on findings and critical blockers."""
    if findings_df.empty:
        score = 1.0
        critical_count = 0
        total_findings = 0
    else:
        critical_count = int((findings_df["severity_label"] == "CRITICAL").sum())
        warning_count = int((findings_df["severity_label"] == "WARNING").sum())
        total_findings = len(findings_df)

        if critical_count > 0:
            score = max(0.0, 0.40 - critical_count * 0.15)
        else:
            score = max(0.50, 1.0 - warning_count * 0.05)

    classification = classify_stress_readiness_score(score)
    meets_threshold = score >= profile.min_readiness_score

    return StressReadinessScore(
        score=round(score, 2),
        classification=classification,
        total_findings=total_findings,
        critical_blockers=critical_count,
        meets_threshold=meets_threshold,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
    )


def build_stress_readiness_score_report(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame report for stress testing readiness scoring."""
    score_obj = calculate_stress_readiness_score(pd.DataFrame(), profile)
    rows = [
        {
            "score": score_obj.score,
            "classification": score_obj.classification,
            "total_findings": score_obj.total_findings,
            "critical_blockers": score_obj.critical_blockers,
            "meets_threshold": score_obj.meets_threshold,
            "min_required_threshold": profile.min_readiness_score,
            "non_signal": score_obj.non_signal,
            "production_ready": score_obj.production_ready,
            "broker_ready": score_obj.broker_ready,
            "profile_name": profile.profile_name,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "score": score_obj.score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.meets_threshold,
        "critical_blockers": score_obj.critical_blockers,
        "zero_production_ready": not score_obj.production_ready,
        "zero_broker_ready": not score_obj.broker_ready,
        "non_signal": True,
    }
    return df, summary
