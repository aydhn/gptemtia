# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Readiness Scoring."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    READINESS_SCORE_DOMAIN,
    ACCEPTANCE_READY,
)
from advanced_ml_acceptance.advanced_ml_acceptance_models import AdvancedMlReadinessScore


def classify_advanced_ml_readiness_score(score: float) -> str:
    """Classify readiness score into strict governance tiers."""
    if not (0.0 <= score <= 1.0):
        raise ValueError(f"Score must be within [0.0, 1.0], got {score}")
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "contract_ready_with_manual_review"
    else:
        return "advanced_ml_contract_acceptance_ready_non_production"


def calculate_advanced_ml_readiness_score(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> AdvancedMlReadinessScore:
    """Calculate the readiness score based on findings and profile constraints."""
    active = profile or get_advanced_ml_acceptance_profile()

    score = 1.0
    if findings_df is not None and not findings_df.empty:
        # Deduct for blockers
        if "severity_label" in findings_df.columns:
            blocker_count = int((findings_df["severity_label"] == "CRITICAL").sum())
            if blocker_count > 0:
                score -= min(1.0, blocker_count * 0.50)

            high_count = int((findings_df["severity_label"] == "HIGH").sum())
            if high_count > 0:
                score -= min(0.40, high_count * 0.15)

    score = max(0.0, min(1.0, score))
    classification = classify_advanced_ml_readiness_score(score)
    meets_threshold = score >= active.min_readiness_score

    return AdvancedMlReadinessScore(
        score=score,
        classification=classification,
        meets_threshold=meets_threshold,
        current_phase=active.current_phase,
        target_final_phase=active.target_final_phase,
        next_phase=active.next_phase,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
        official_approval=False,
    )


def build_advanced_ml_readiness_score_report(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for readiness score."""
    active = profile or get_advanced_ml_acceptance_profile()
    score_obj = calculate_advanced_ml_readiness_score(None, active)

    records = [{
        "score": score_obj.score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.meets_threshold,
        "min_threshold": active.min_readiness_score,
        "current_phase": score_obj.current_phase,
        "target_final_phase": score_obj.target_final_phase,
        "next_phase": score_obj.next_phase,
        "status": ACCEPTANCE_READY,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
        "official_approval": False,
    }]

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": READINESS_SCORE_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "readiness_score": score_obj.score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.meets_threshold,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
        "official_approval": False,
        "status": "CALCULATED",
    }
    return df, summary


def summarize_advanced_ml_readiness_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize readiness score DataFrame."""
    if df.empty:
        return {"score": 0.0, "classification": "unknown", "meets_threshold": False, "non_signal": True}
    row = df.iloc[0]
    return {
        "score": float(row.get("score", 0.0)),
        "classification": str(row.get("classification", "unknown")),
        "meets_threshold": bool(row.get("meets_threshold", False)),
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
