# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Readiness Scoring."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingReadinessScore


def classify_risk_reporting_readiness_score(score: float) -> str:
    """Classify numeric readiness score into qualitative readiness state."""
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "contract_ready_with_manual_review"
    else:
        return "risk_reporting_contract_ready_non_production"


def calculate_risk_reporting_readiness_score(
    findings_df: pd.DataFrame,
    profile: RiskReportingProfile = None,
) -> RiskReportingReadinessScore:
    """Calculate overall readiness score based on findings and safety status."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    base_score = 1.0
    if not findings_df.empty and "severity_label" in findings_df.columns:
        blockers = int((findings_df["severity_label"] == "BLOCKER").sum())
        warnings = int((findings_df["severity_label"] == "WARNING").sum())
        deduction = (blockers * 0.40) + (warnings * 0.10)
        base_score = max(0.0, base_score - deduction)

    classification = classify_risk_reporting_readiness_score(base_score)
    is_ready = base_score >= profile.min_readiness_score

    return RiskReportingReadinessScore(
        readiness_score=round(base_score, 4),
        classification=classification,
        is_contract_ready=is_ready,
        summary_text=f"Phase 155 readiness: {base_score:.2f} ({classification})",
        current_phase=profile.current_phase,
        target_final_phase=profile.target_final_phase,
        next_phase=profile.next_phase,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
    )


def build_risk_reporting_readiness_score_report(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for readiness score report."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    empty_findings = pd.DataFrame()
    score_model = calculate_risk_reporting_readiness_score(empty_findings, profile)
    data = score_model.model_dump()
    df = pd.DataFrame([data])
    summary = {
        "readiness_score": score_model.readiness_score,
        "classification": score_model.classification,
        "is_contract_ready": score_model.is_contract_ready,
        "meets_threshold": score_model.readiness_score >= profile.min_readiness_score,
    }
    return df, summary
