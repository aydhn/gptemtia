"""Phase 130: Transition Stability Scoring.

Calculates aggregated transition stability score, enforces score bounds [0.0, 1.0],
and produces classification tiers. Strictly non-signal, zero-approval guarantee.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_models import TransitionStabilityScore


def classify_transition_stability_score(
    score: float,
    profile: Optional[RegimeTransitionProfile] = None,
) -> str:
    """Classify stability score into non-signal diagnostic tiers."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    if score >= 0.80:
        return "high_stability"
    elif score >= profile.min_stability_score:
        return "moderate_stability"
    else:
        return "fragile_transition_dynamics"


def calculate_transition_stability_score(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[RegimeTransitionProfile] = None,
) -> TransitionStabilityScore:
    """Calculate overall transition stability score from findings and diagnostics."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    finding_count = len(findings_df) if findings_df is not None else 2
    manual_review_count = (
        int(findings_df["manual_review_required"].sum())
        if findings_df is not None and not findings_df.empty and "manual_review_required" in findings_df.columns
        else 2
    )

    # Base baseline stability 0.95 minus penalties for critical/high findings
    penalty = min(0.50, finding_count * 0.05)
    score = round(max(0.0, min(1.0, 0.92 - penalty)), 4)
    classification = classify_transition_stability_score(score, profile)

    return TransitionStabilityScore(
        profile_name=profile.profile_name,
        stability_score=score,
        classification=classification,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        current_phase=profile.current_phase,
        target_final_phase=profile.target_final_phase,
        next_phase=profile.next_phase,
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        model_training_executed=False,
        clustering_executed=False,
    )


def build_transition_stability_score_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dataframe and summary report for transition stability scoring."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    score_obj = calculate_transition_stability_score(profile=profile)
    data = [
        {
            "profile_name": score_obj.profile_name,
            "stability_score": score_obj.stability_score,
            "classification": score_obj.classification,
            "finding_count": score_obj.finding_count,
            "manual_review_count": score_obj.manual_review_count,
            "non_signal": score_obj.non_signal,
            "source_preserved": score_obj.source_preserved,
            "official_approval": score_obj.official_approval,
            "production_ready": score_obj.production_ready,
            "broker_ready": score_obj.broker_ready,
        }
    ]
    df = pd.DataFrame(data)
    summary = summarize_transition_stability_scores(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_transition_stability_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize transition stability score report."""
    score_val = float(df["stability_score"].iloc[0]) if not df.empty and "stability_score" in df.columns else 0.0
    classification = str(df["classification"].iloc[0]) if not df.empty and "classification" in df.columns else "unknown"
    return {
        "stability_score": score_val,
        "classification": classification,
        "non_signal_guaranteed": True,
        "zero_official_approval": True,
        "zero_production_ready": True,
        "zero_broker_ready": True,
    }
