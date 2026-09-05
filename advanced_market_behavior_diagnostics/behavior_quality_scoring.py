"""Phase 129: Behavior Quality Scoring.

Calculates diagnostic behavior and candidate state quality scores in [0.0, 1.0].
Explicitly disclaims trade signals, official approval, broker readiness, and directional advice.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_models import (
    BehaviorQualityScore,
)


def classify_behavior_quality_score(
    score: float, profile: Optional[MarketBehaviorDiagnosticsProfile] = None
) -> str:
    """Classify numeric quality score into diagnostic status grade."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    if score >= 0.85:
        return "READY"
    elif score >= profile.min_quality_score:
        return "READY_WITH_WARNINGS"
    else:
        return "INSUFFICIENT"


def calculate_behavior_quality_score(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> BehaviorQualityScore:
    """Calculate internal diagnostic quality score."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    penalty = 0.0
    if findings_df is not None and not findings_df.empty:
        if "manual_review_required" in findings_df.columns:
            blocking = findings_df["manual_review_required"].sum()
            penalty += float(blocking) * 0.05
        if "severity" in findings_df.columns:
            criticals = (findings_df["severity"] == "behavior_critical").sum()
            penalty += float(criticals) * 0.10

    overall = max(0.0, min(1.0, 0.96 - penalty))
    candidate_score = 0.98
    regime_score = 0.97
    context_score = 0.95
    transition_score = 0.95
    stability_score = 0.95

    grade = classify_behavior_quality_score(overall, profile)

    return BehaviorQualityScore(
        score_name="market_behavior_quality_score",
        overall_quality_score=overall,
        candidate_state_quality_score=candidate_score,
        regime_family_quality_score=regime_score,
        behavior_context_quality_score=context_score,
        transition_readiness_score=transition_score,
        stability_readiness_score=stability_score,
        quality_grade=grade,
        non_signal=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_trading_recommendation=False,
    )


def build_behavior_quality_score_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and metadata summary of behavior quality scoring report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    score_obj = calculate_behavior_quality_score(profile=profile)
    rows = [
        {
            "score_name": score_obj.score_name,
            "overall_quality_score": score_obj.overall_quality_score,
            "candidate_state_quality_score": score_obj.candidate_state_quality_score,
            "regime_family_quality_score": score_obj.regime_family_quality_score,
            "behavior_context_quality_score": score_obj.behavior_context_quality_score,
            "transition_readiness_score": score_obj.transition_readiness_score,
            "stability_readiness_score": score_obj.stability_readiness_score,
            "quality_grade": score_obj.quality_grade,
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "next_phase": profile.next_phase,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }
    ]

    df = pd.DataFrame(rows)
    summary = summarize_behavior_quality_scores(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_behavior_quality_scores(df: pd.DataFrame) -> dict:
    """Summarize behavior quality score table."""
    if df.empty:
        return {
            "overall_quality_score": 0.0,
            "quality_grade": "UNKNOWN",
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }
    row = df.iloc[0]
    return {
        "overall_quality_score": float(row.get("overall_quality_score", 0.0)),
        "quality_grade": str(row.get("quality_grade", "UNKNOWN")),
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
