# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Readiness Scoring.

Calculates contract completeness and governance readiness scores strictly
as an internal audit metric, without granting trading or production approvals.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    READINESS_SCORE_DOMAIN,
    SEVERITY_CRITICAL,
    SEVERITY_WARNING,
    PORTFOLIO_ACCEPTANCE_READY,
)
from .portfolio_acceptance_models import PortfolioAcceptanceReadinessScore
from .portfolio_acceptance_findings import build_portfolio_acceptance_findings_registry


def classify_portfolio_acceptance_readiness_score(score: float) -> str:
    """Classify readiness score into governance tiers."""
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "contract_ready_with_manual_review"
    else:
        return "portfolio_acceptance_contract_ready_non_production"


def calculate_portfolio_acceptance_readiness_score(
    findings_df: pd.DataFrame,
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> PortfolioAcceptanceReadinessScore:
    """Calculate readiness score based on contract compliance and absence of blockers."""
    active = profile or get_portfolio_acceptance_profile()

    blockers = 0
    warnings = 0
    if not findings_df.empty and "is_blocking" in findings_df.columns:
        blockers = int(findings_df["is_blocking"].sum())
        if "severity_label" in findings_df.columns:
            warnings = int((findings_df["severity_label"] == SEVERITY_WARNING).sum())

    total_checks = 10
    if blockers > 0:
        overall_score = 0.0
        passed_checks = 0
    else:
        # Deduct small penalty for open warnings
        score = 1.0 - (0.05 * min(warnings, 4))
        overall_score = max(score, 0.0)
        passed_checks = total_checks - min(warnings, total_checks)

    classification = classify_portfolio_acceptance_readiness_score(overall_score)
    meets_threshold = (overall_score >= active.min_readiness_score)

    return PortfolioAcceptanceReadinessScore(
        overall_score=overall_score,
        classification=classification,
        meets_threshold=meets_threshold,
        total_checks=total_checks,
        passed_checks=passed_checks,
        warning_count=warnings,
        blocker_count=blockers,
        non_signal=True,
        dry_run=True,
        local_only=True,
        non_production=True,
        broker_ready=False,
        production_ready=False,
        live_trading_ready=False,
        official_approval=False,
    )


def build_portfolio_acceptance_readiness_score_report(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build readiness score report DataFrame and summary."""
    active = profile or get_portfolio_acceptance_profile()
    findings_df, _ = build_portfolio_acceptance_findings_registry(active)
    readiness = calculate_portfolio_acceptance_readiness_score(findings_df, active)

    records = [{
        "profile_name": active.profile_name,
        "readiness_score": readiness.overall_score,
        "classification": readiness.classification,
        "meets_threshold": readiness.meets_threshold,
        "min_threshold": active.min_readiness_score,
        "total_checks": readiness.total_checks,
        "passed_checks": readiness.passed_checks,
        "warning_count": readiness.warning_count,
        "blocker_count": readiness.blocker_count,
        "non_signal": True,
        "dry_run": True,
        "local_only": True,
        "non_production": True,
        "broker_ready": False,
        "production_ready": False,
        "live_trading_ready": False,
        "current_phase": active.current_phase,
        "status": PORTFOLIO_ACCEPTANCE_READY if readiness.meets_threshold else "BELOW_THRESHOLD",
    }]

    df = pd.DataFrame(records)
    summary = {
        "domain": READINESS_SCORE_DOMAIN,
        "readiness_score": readiness.overall_score,
        "classification": readiness.classification,
        "meets_threshold": readiness.meets_threshold,
        "total_checks": readiness.total_checks,
        "passed_checks": readiness.passed_checks,
        "warning_count": readiness.warning_count,
        "blocker_count": readiness.blocker_count,
        "is_signal": False,
        "is_investment_advice": False,
        "is_portfolio_approval": False,
        "is_production_ready": False,
        "is_broker_ready": False,
        "status": PORTFOLIO_ACCEPTANCE_READY if readiness.meets_threshold else "BELOW_THRESHOLD",
    }
    return df, summary
