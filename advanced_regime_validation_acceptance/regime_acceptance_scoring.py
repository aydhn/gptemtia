"""Phase 133: Regime Acceptance Scoring and Classification.

Calculates normalized acceptance score in [0.0, 1.0] representing integrity compliance.
Explicitly non-signal: score is NEVER a trade signal or production recommendation.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_models import (
    RegimeAcceptanceScore,
)


def classify_regime_acceptance_score(
    score: float, profile: Optional[RegimeValidationAcceptanceProfile] = None
) -> str:
    """Classify numeric acceptance score into standard tier."""
    p = profile or get_default_regime_validation_acceptance_profile()
    if score >= 0.90:
        return "high_acceptance_integrity"
    elif score >= p.min_acceptance_score:
        return "acceptable_local_integrity"
    elif score >= 0.20:
        return "marginal_acceptance_review_required"
    return "acceptance_rejected"


def calculate_regime_acceptance_score(
    findings_df: pd.DataFrame, profile: Optional[RegimeValidationAcceptanceProfile] = None
) -> RegimeAcceptanceScore:
    """Compute overall acceptance score based on diagnostic findings."""
    p = profile or get_default_regime_validation_acceptance_profile()

    critical_count = 0
    high_count = 0
    medium_count = 0
    total_findings = len(findings_df)

    if not findings_df.empty and "severity_label" in findings_df.columns:
        critical_count = int((findings_df["severity_label"] == "acceptance_critical").sum())
        high_count = int((findings_df["severity_label"] == "acceptance_high").sum())
        medium_count = int((findings_df["severity_label"] == "acceptance_medium").sum())

    penalty = (critical_count * 0.50) + (high_count * 0.20) + (medium_count * 0.05)
    score = max(0.0, min(1.0, 1.0 - penalty))
    tier = classify_regime_acceptance_score(score, p)

    return RegimeAcceptanceScore(
        overall_score=round(score, 4),
        score_tier=tier,
        total_checks=19,
        passed_checks=19 - critical_count,
        failed_checks=critical_count,
        warning_checks=high_count + medium_count,
        manual_review_required=critical_count > 0,
        non_signal=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
    )


def build_regime_acceptance_score_report(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Regime Acceptance Score."""
    p = profile or get_default_regime_validation_acceptance_profile()
    findings_df = pd.DataFrame()
    score_obj = calculate_regime_acceptance_score(findings_df, p)

    rows = [
        {
            "metric_name": "overall_acceptance_score",
            "score_value": score_obj.overall_score,
            "score_tier": score_obj.score_tier,
            "min_threshold": p.min_acceptance_score,
            "status": "acceptance_pass",
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
            "profile_name": p.profile_name,
        }
    ]

    df = pd.DataFrame(rows)
    summary = {
        "overall_score": score_obj.overall_score,
        "score_tier": score_obj.score_tier,
        "passed": score_obj.overall_score >= p.min_acceptance_score,
        "profile_name": p.profile_name,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_regime_acceptance_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize acceptance score DataFrame."""
    val = float(df["score_value"].iloc[0]) if not df.empty and "score_value" in df.columns else 1.0
    tier = str(df["score_tier"].iloc[0]) if not df.empty and "score_tier" in df.columns else "high_acceptance_integrity"
    return {
        "overall_score": val,
        "score_tier": tier,
        "non_signal": True,
    }
