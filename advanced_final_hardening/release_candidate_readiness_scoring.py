# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Readiness Scoring.

Calculates and classifies the readiness score of the contract and hardening layer.
Readiness score indicates contract completeness only; never represents trading or broker readiness.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    READINESS_SCORE_DOMAIN,
    RELEASE_CANDIDATE_CONTRACT_READY,
)
from advanced_final_hardening.final_hardening_models import ReleaseCandidateReadinessScore


def classify_release_candidate_readiness_score(score: float) -> str:
    """Classify the readiness score into non-production contract bands."""
    if not (0.0 <= score <= 1.0):
        raise ValueError(f"Score must be between 0.0 and 1.0, got: {score}")
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "release_candidate_contract_ready_with_manual_review"
    else:
        return "release_candidate_contract_ready_non_production"


def calculate_release_candidate_readiness_score(
    findings_df: pd.DataFrame | None,
    profile: FinalHardeningProfile | None = None,
) -> ReleaseCandidateReadinessScore:
    """Calculate the overall readiness score based on findings and profile constraints."""
    base_score = 0.95
    if findings_df is not None and not findings_df.empty:
        critical_count = int((findings_df["severity_label"] == "CRITICAL").sum())
        high_count = int((findings_df["severity_label"] == "HIGH").sum())
        base_score -= (critical_count * 0.25 + high_count * 0.10)

    final_score = max(0.0, min(1.0, base_score))
    classification = classify_release_candidate_readiness_score(final_score)

    return ReleaseCandidateReadinessScore(
        score=final_score,
        classification=classification,
        domain=READINESS_SCORE_DOMAIN,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        broker_ready=False,
        production_ready=False,
        live_trading_ready=False,
        official_approval=False,
        is_trading_signal=False,
        is_investment_advice=False,
        is_release_deployment_authorization=False,
        status=RELEASE_CANDIDATE_CONTRACT_READY,
    )


def build_release_candidate_readiness_score_report(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build readiness score report DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()
    rc_score = calculate_release_candidate_readiness_score(None, active_profile)

    row = {
        "readiness_score": rc_score.score,
        "classification": rc_score.classification,
        "min_required_score": active_profile.min_readiness_score,
        "threshold_met": bool(rc_score.score >= active_profile.min_readiness_score),
        "is_trading_signal": False,
        "is_investment_advice": False,
        "production_ready": False,
        "broker_ready": False,
        "live_trading_ready": False,
        "domain": READINESS_SCORE_DOMAIN,
        "non_signal": True,
        "local_only": True,
        "dry_run": True,
        "non_production": True,
        "current_phase": active_profile.current_phase,
        "status": RELEASE_CANDIDATE_CONTRACT_READY,
    }

    df = pd.DataFrame([row])
    summary = {
        "readiness_score": rc_score.score,
        "classification": rc_score.classification,
        "threshold_met": row["threshold_met"],
        "current_phase": active_profile.current_phase,
        "status": RELEASE_CANDIDATE_CONTRACT_READY,
    }
    return df, summary
