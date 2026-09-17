# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Readiness Scoring."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    READINESS_SCORE_DOMAIN,
    ACCEPTANCE_READY,
)
from advanced_backtest_acceptance.backtest_acceptance_models import (
    BacktestAcceptanceReadinessScore,
)


def classify_backtest_acceptance_readiness_score(score: float) -> str:
    """Classify readiness score into governance categories."""
    if not (0.0 <= score <= 1.0):
        raise ValueError(f"Score must be within [0.0, 1.0], got {score}")
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "contract_ready_with_manual_review"
    else:
        return "backtest_acceptance_contract_ready_non_production"


def calculate_backtest_acceptance_readiness_score(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> BacktestAcceptanceReadinessScore:
    """Compute diagnostic readiness score based on findings and safety boundaries."""
    active = profile or get_backtest_acceptance_profile()

    score = 1.0
    if findings_df is not None and not findings_df.empty:
        critical_count = len(findings_df[findings_df["severity_label"].isin(["CRITICAL", "BLOCKER"])])
        warning_count = len(findings_df[findings_df["severity_label"] == "WARNING"])
        score -= min(1.0, critical_count * 0.40 + warning_count * 0.05)
        score = max(0.0, score)

    classification = classify_backtest_acceptance_readiness_score(score)
    meets_threshold = score >= active.min_readiness_score

    return BacktestAcceptanceReadinessScore(
        score=score,
        classification=classification,
        meets_threshold=meets_threshold,
        current_phase=active.current_phase,
        target_final_phase=active.target_final_phase,
        next_phase=active.next_phase,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        strategy_approved=False,
        performance_guaranteed=False,
    )


def build_backtest_acceptance_readiness_score_report(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary report for backtest acceptance readiness score."""
    active = profile or get_backtest_acceptance_profile()
    score_obj = calculate_backtest_acceptance_readiness_score(findings_df=None, profile=active)

    records = [{
        "score": score_obj.score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.meets_threshold,
        "min_readiness_score": active.min_readiness_score,
        "current_phase": score_obj.current_phase,
        "target_final_phase": score_obj.target_final_phase,
        "next_phase": score_obj.next_phase,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
        "live_trading_ready": False,
        "official_approval": False,
        "strategy_approved": False,
        "performance_guaranteed": False,
        "status": ACCEPTANCE_READY,
    }]

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": READINESS_SCORE_DOMAIN,
        "active_profile": active.profile_name,
        "readiness_score": score_obj.score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.meets_threshold,
        "production_ready": False,
        "broker_ready": False,
        "strategy_approved": False,
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
