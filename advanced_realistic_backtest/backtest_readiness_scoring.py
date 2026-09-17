# -*- coding: utf-8 -*-
"""Phase 146: Backtest Readiness Scoring.

Computes architectural readiness score for backtest contracts and guard layers.
Strictly non-signal and non-production.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile
from advanced_realistic_backtest.realistic_backtest_models import BacktestReadinessScore


def classify_backtest_readiness_score(score: float) -> str:
    """Classify readiness score into standard bands."""
    if score < 0.25:
        return "blocked"
    if score < 0.50:
        return "incomplete"
    if score < 0.75:
        return "contract_ready_with_manual_review"
    return "realistic_backtest_contract_ready_non_production"


def calculate_backtest_readiness_score(
    findings_df: pd.DataFrame, profile: RealisticBacktestProfile
) -> BacktestReadinessScore:
    """Calculate diagnostic readiness score based on findings and profile constraints."""
    total_findings = len(findings_df) if not findings_df.empty else 0
    critical_blockers = (
        int((findings_df["severity_label"] == "CRITICAL").sum())
        if not findings_df.empty and "severity_label" in findings_df.columns
        else 0
    )

    if critical_blockers > 0:
        score = 0.20
    else:
        # Baseline score for clean contract definitions
        score = 1.0 - min(0.50, total_findings * 0.05)
        score = max(0.50, min(1.0, score))

    classification = classify_backtest_readiness_score(score)
    meets_threshold = score >= profile.min_readiness_score

    return BacktestReadinessScore(
        score=float(score),
        classification=classification,
        total_findings=total_findings,
        critical_blockers=critical_blockers,
        meets_threshold=meets_threshold,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
    )


def build_backtest_readiness_score_report(
    profile: RealisticBacktestProfile, findings_df: pd.DataFrame | None = None
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report of backtest readiness score."""
    if findings_df is None:
        findings_df = pd.DataFrame()

    readiness = calculate_backtest_readiness_score(findings_df, profile)
    rows = [
        {
            "profile_name": profile.profile_name,
            "readiness_score": readiness.score,
            "classification": readiness.classification,
            "total_findings": readiness.total_findings,
            "critical_blockers": readiness.critical_blockers,
            "meets_threshold": readiness.meets_threshold,
            "threshold": profile.min_readiness_score,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "profile_name": profile.profile_name,
        "readiness_score": readiness.score,
        "classification": readiness.classification,
        "meets_threshold": readiness.meets_threshold,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary
