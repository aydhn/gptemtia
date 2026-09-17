# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Readiness Scoring."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_construction_config import (
    PortfolioConstructionProfile,
    get_default_portfolio_construction_profile,
)
from .portfolio_construction_labels import (
    PORTFOLIO_READINESS_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
    READINESS_BLOCKED,
    READINESS_INCOMPLETE,
    READINESS_CONTRACT_READY_WITH_MANUAL_REVIEW,
    READINESS_CONTRACT_READY_NON_PRODUCTION,
)
from .portfolio_construction_models import PortfolioReadinessScore


def classify_portfolio_readiness_score(score: float) -> str:
    """Classify readiness score into Phase 153 governance tiers."""
    if not (0.0 <= score <= 1.0):
        raise ValueError(f"Score must be within [0.0, 1.0], got {score}")
    if score < 0.25:
        return READINESS_BLOCKED
    elif score < 0.50:
        return READINESS_INCOMPLETE
    elif score < 0.75:
        return READINESS_CONTRACT_READY_WITH_MANUAL_REVIEW
    else:
        return READINESS_CONTRACT_READY_NON_PRODUCTION


def calculate_portfolio_readiness_score(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[PortfolioConstructionProfile] = None,
) -> PortfolioReadinessScore:
    """Compute diagnostic readiness score based on findings and safety boundaries."""
    active = profile or get_default_portfolio_construction_profile()

    score = 1.0
    findings_count = 0
    critical_count = 0
    if findings_df is not None and not findings_df.empty:
        findings_count = len(findings_df)
        critical_count = len(findings_df[findings_df["severity"].isin(["CRITICAL", "BLOCKER"])])
        warning_count = len(findings_df[findings_df["severity"] == "WARNING"])
        score -= min(1.0, critical_count * 0.40 + warning_count * 0.05)
        score = max(0.0, score)

    classification = classify_portfolio_readiness_score(score)
    meets_threshold = score >= active.min_readiness_score

    return PortfolioReadinessScore(
        overall_score=round(score, 4),
        classification=classification,
        meets_threshold=meets_threshold,
        findings_count=findings_count,
        critical_count=critical_count,
        current_phase=active.current_phase,
        target_final_phase=active.target_final_phase,
        next_phase=active.next_phase,
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
    )


def build_portfolio_readiness_score_report(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[PortfolioConstructionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary report for portfolio construction readiness score."""
    active = profile or get_default_portfolio_construction_profile()
    score_obj = calculate_portfolio_readiness_score(findings_df=findings_df, profile=active)

    records = [{
        "overall_score": score_obj.overall_score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.meets_threshold,
        "min_readiness_score": active.min_readiness_score,
        "findings_count": score_obj.findings_count,
        "critical_count": score_obj.critical_count,
        "current_phase": score_obj.current_phase,
        "target_final_phase": score_obj.target_final_phase,
        "next_phase": score_obj.next_phase,
        "contract_only": True,
        "non_production": True,
        "broker_ready": False,
        "live_trading_ready": False,
        "status": PORTFOLIO_CONTRACT_READY,
    }]

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": PORTFOLIO_READINESS_DOMAIN,
        "active_profile": active.profile_name,
        "overall_score": score_obj.overall_score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.meets_threshold,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
