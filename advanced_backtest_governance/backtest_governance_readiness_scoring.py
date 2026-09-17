# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Readiness Scoring Module.

Calculates contract completeness score and assigns qualitative diagnostic classification.
Strictly non-signal, local-only, and non-production.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    READINESS_SCORE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)
from advanced_backtest_governance.backtest_governance_models import BacktestGovernanceReadinessScore


def classify_backtest_governance_readiness_score(score: float) -> str:
    """Classify the numeric readiness score into standard qualitative tiers."""
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "contract_ready_with_manual_review"
    else:
        return "backtest_governance_contract_ready_non_production"


def calculate_backtest_governance_readiness_score(
    findings_df: pd.DataFrame,
    profile: BacktestGovernanceProfile,
) -> BacktestGovernanceReadinessScore:
    """Calculate the backtest governance readiness score based on findings and safety invariants."""
    total_checks = 10
    passed_checks = 10

    critical_count = 0
    high_count = 0
    if not findings_df.empty and "severity_label" in findings_df.columns:
        critical_count = len(findings_df[findings_df["severity_label"] == "CRITICAL"])
        high_count = len(findings_df[findings_df["severity_label"] == "HIGH"])

    if critical_count > 0:
        passed_checks = max(0, passed_checks - (critical_count * 3))
    if high_count > 0:
        passed_checks = max(0, passed_checks - (high_count * 1))

    score = round(min(1.0, max(0.0, passed_checks / total_checks)), 2)
    classification = classify_backtest_governance_readiness_score(score)
    meets_threshold = score >= profile.min_readiness_score

    return BacktestGovernanceReadinessScore(
        score=score,
        classification=classification,
        current_phase=profile.current_phase,
        target_final_phase=profile.target_final_phase,
        meets_threshold=meets_threshold,
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


def build_backtest_governance_readiness_score_report(
    profile: BacktestGovernanceProfile,
    findings_df: Optional[pd.DataFrame] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the readiness score report DataFrame and summary."""
    f_df = findings_df if findings_df is not None else pd.DataFrame()
    score_obj = calculate_backtest_governance_readiness_score(f_df, profile)

    rows: List[Dict[str, Any]] = [
        {
            "metric": "readiness_score",
            "score": score_obj.score,
            "classification": score_obj.classification,
            "meets_threshold": score_obj.meets_threshold,
            "broker_ready": score_obj.broker_ready,
            "production_ready": score_obj.production_ready,
            "live_trading_ready": score_obj.live_trading_ready,
            "official_approval": score_obj.official_approval,
            "profile_name": profile.profile_name,
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "non_signal": True,
            "local_only": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": READINESS_SCORE_DOMAIN,
        "score": score_obj.score,
        "classification": score_obj.classification,
        "meets_threshold": score_obj.meets_threshold,
        "broker_ready": score_obj.broker_ready,
        "production_ready": score_obj.production_ready,
        "live_trading_ready": score_obj.live_trading_ready,
        "official_approval": score_obj.official_approval,
        "profile_name": profile.profile_name,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
