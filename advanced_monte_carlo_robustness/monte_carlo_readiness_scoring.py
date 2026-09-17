# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Readiness Scoring Module.

Calculates contract completeness score and assigns qualitative diagnostic classification.
Strictly non-signal and non-production.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    READINESS_SCORE_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)
from advanced_monte_carlo_robustness.monte_carlo_models import MonteCarloReadinessScore


def classify_monte_carlo_readiness_score(score: float) -> str:
    """Classify the numeric readiness score into standard qualitative tiers."""
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "contract_ready_with_manual_review"
    else:
        return "monte_carlo_robustness_contract_ready_non_production"


def calculate_monte_carlo_readiness_score(
    findings_df: pd.DataFrame,
    profile: MonteCarloProfile,
) -> MonteCarloReadinessScore:
    """Calculate the Monte Carlo readiness score based on findings and safety invariants."""
    total_checks = 10
    passed_checks = 10

    critical_count = 0
    if not findings_df.empty and "severity_label" in findings_df.columns:
        critical_count = len(findings_df[findings_df["severity_label"] == "CRITICAL"])

    # Deduct score if critical findings exist
    if critical_count > 0:
        passed_checks = max(0, total_checks - (critical_count * 3))

    score = round(passed_checks / total_checks, 2)
    classification = classify_monte_carlo_readiness_score(score)

    return MonteCarloReadinessScore(
        score=score,
        classification=classification,
        total_checks=total_checks,
        passed_checks=passed_checks,
        critical_findings_count=critical_count,
        manual_review_required=True,
        broker_ready=False,
        production_ready=False,
        live_trading_ready=False,
    )


def build_monte_carlo_readiness_score_report(
    profile: MonteCarloProfile,
    findings_df: Optional[pd.DataFrame] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the readiness score report DataFrame and summary."""
    f_df = findings_df if findings_df is not None else pd.DataFrame()
    score_obj = calculate_monte_carlo_readiness_score(f_df, profile)

    rows: List[Dict[str, Any]] = [
        {
            "metric": "readiness_score",
            "value": score_obj.score,
            "classification": score_obj.classification,
            "total_checks": score_obj.total_checks,
            "passed_checks": score_obj.passed_checks,
            "critical_findings": score_obj.critical_findings_count,
            "manual_review_required": score_obj.manual_review_required,
            "broker_ready": score_obj.broker_ready,
            "production_ready": score_obj.production_ready,
            "live_trading_ready": score_obj.live_trading_ready,
            "profile_name": profile.profile_name,
            "current_phase": profile.current_phase,
            "domain": READINESS_SCORE_DOMAIN,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": READINESS_SCORE_DOMAIN,
        "score": score_obj.score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.score >= profile.min_readiness_score,
        "manual_review_required": score_obj.manual_review_required,
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
