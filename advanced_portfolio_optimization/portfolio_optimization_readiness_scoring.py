# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Readiness Scoring.

Calculates diagnostic contract completeness score.
Strictly non-production, non-trading, non-advisory readiness metric.
"""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile
from .portfolio_optimization_models import PortfolioOptimizationReadinessScore


def classify_portfolio_optimization_readiness_score(score: float) -> str:
    """Classify readiness score."""
    if score >= 0.75:
        return "portfolio_optimization_contract_ready_non_production"
    elif score >= 0.50:
        return "contract_ready_with_manual_review"
    elif score >= 0.25:
        return "incomplete"
    else:
        return "blocked"


def calculate_portfolio_optimization_readiness_score(
    findings_df: pd.DataFrame, profile: PortfolioOptimizationProfile | None = None
) -> PortfolioOptimizationReadinessScore:
    """Calculate diagnostic readiness score based on findings."""
    prof = profile or get_default_portfolio_optimization_profile()
    blockers = 0
    if not findings_df.empty and "severity_label" in findings_df.columns:
        blockers = len(findings_df[findings_df["severity_label"] == "BLOCKER"])

    score = 1.00 if blockers == 0 else max(0.0, 1.0 - (blockers * 0.25))
    classification = classify_portfolio_optimization_readiness_score(score)
    is_ready = score >= prof.min_readiness_score

    return PortfolioOptimizationReadinessScore(
        readiness_score=score,
        classification=classification,
        is_contract_ready=is_ready,
        summary_text=f"Phase 154 Portfolio Optimization Readiness: {score:.4f} ({classification})",
        current_phase=154,
        target_final_phase=160,
        next_phase=155,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
    )


def build_portfolio_optimization_readiness_score_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build readiness score report table."""
    prof = profile or get_default_portfolio_optimization_profile()
    readiness = calculate_portfolio_optimization_readiness_score(pd.DataFrame(), prof)
    records = [{
        "metric_name": "portfolio_optimization_readiness_score",
        "score_value": readiness.readiness_score,
        "classification": readiness.classification,
        "is_contract_ready": readiness.is_contract_ready,
        "current_phase": readiness.current_phase,
        "target_final_phase": readiness.target_final_phase,
        "next_phase": readiness.next_phase,
        "production_ready": readiness.production_ready,
        "broker_ready": readiness.broker_ready,
        "live_trading_ready": readiness.live_trading_ready,
    }]
    df = pd.DataFrame(records)
    summary = {
        "readiness_score": readiness.readiness_score,
        "classification": readiness.classification,
        "is_contract_ready": readiness.is_contract_ready,
    }
    return df, summary
