# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Readiness Scoring.

Calculates contract completeness and documentation readiness score for Phase 160.
Strictly disclaims that this score is NOT a trading signal, NOT production readiness,
and NOT official approval.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_READINESS_SCORE_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)
from advanced_final_delivery.final_delivery_models import FinalDeliveryReadinessScore


def classify_final_delivery_readiness_score(score: float) -> str:
    """Classify readiness score into descriptive non-production tiers."""
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "final_delivery_contract_ready_with_manual_review"
    else:
        return "full_advanced_bot_final_delivery_ready_non_production"


def calculate_final_delivery_readiness_score(
    findings_df: pd.DataFrame | None = None,
    profile: FinalDeliveryProfile | None = None,
) -> FinalDeliveryReadinessScore:
    """Calculate the readiness score based on findings and safety profile."""
    active_profile = profile or get_default_final_delivery_profile()

    # Base completeness score for 160 phases
    base_score = 1.00
    if findings_df is not None and not findings_df.empty:
        critical_count = int((findings_df.get("severity_label", "") == "CRITICAL").sum())
        high_count = int((findings_df.get("severity_label", "") == "HIGH").sum())
        base_score -= (critical_count * 0.25 + high_count * 0.10)
    score_val = max(0.0, min(1.0, base_score))

    classification = classify_final_delivery_readiness_score(score_val)
    threshold_met = score_val >= active_profile.min_readiness_score

    return FinalDeliveryReadinessScore(
        readiness_score=score_val,
        classification=classification,
        min_readiness_score=active_profile.min_readiness_score,
        threshold_met=threshold_met,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        broker_ready=False,
        production_ready=False,
        live_trading_ready=False,
        official_approval=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        domain=FINAL_READINESS_SCORE_DOMAIN,
        status=FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    )


def build_final_delivery_readiness_score_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build readiness score report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()
    readiness = calculate_final_delivery_readiness_score(profile=active_profile)

    rows = [{
        "readiness_score": readiness.readiness_score,
        "classification": readiness.classification,
        "min_readiness_score": readiness.min_readiness_score,
        "threshold_met": readiness.threshold_met,
        "non_signal": readiness.non_signal,
        "local_only": readiness.local_only,
        "dry_run": readiness.dry_run,
        "non_production": readiness.non_production,
        "broker_ready": readiness.broker_ready,
        "production_ready": readiness.production_ready,
        "live_trading_ready": readiness.live_trading_ready,
        "official_approval": readiness.official_approval,
        "domain": FINAL_READINESS_SCORE_DOMAIN,
        "status": readiness.status,
    }]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "readiness_score": readiness.readiness_score,
        "classification": readiness.classification,
        "threshold_met": readiness.threshold_met,
        "is_trading_signal": False,
        "is_investment_advice": False,
        "is_production_ready": False,
        "is_broker_ready": False,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
