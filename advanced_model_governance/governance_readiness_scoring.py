# -*- coding: utf-8 -*-
"""Phase 144: Governance Readiness Scoring."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)
from advanced_model_governance.model_governance_models import GovernanceReadinessScore


def classify_governance_readiness_score(score: float) -> str:
    """Classify readiness score into governance category."""
    if score >= 0.85:
        return "governance_contract_ready"
    elif score >= 0.65:
        return "governance_contract_ready_with_warnings"
    elif score >= 0.45:
        return "governance_contract_placeholder_only"
    else:
        return "governance_contract_manual_review_required"


def calculate_governance_readiness_score(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[ModelGovernanceProfile] = None,
) -> GovernanceReadinessScore:
    """Calculate readiness score based on findings and profile invariants."""
    prof = profile or get_model_governance_profile()
    f_df = findings_df if findings_df is not None else pd.DataFrame()

    base_score = 1.0
    critical_count = 0
    high_count = 0

    if not f_df.empty and "severity_label" in f_df.columns:
        critical_count = int((f_df["severity_label"] == "CRITICAL").sum())
        high_count = int((f_df["severity_label"] == "HIGH").sum())
        base_score -= (critical_count * 0.25)
        base_score -= (high_count * 0.10)

    score = max(0.0, min(1.0, base_score))
    classification = classify_governance_readiness_score(score)
    meets_threshold = score >= prof.min_readiness_score

    return GovernanceReadinessScore(
        readiness_score=score,
        classification=classification,
        meets_threshold=meets_threshold,
        findings_count=len(f_df),
        manual_review_count=10,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
        release_approved=False,
        model_performance_claim=False,
    )


def build_governance_readiness_score_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for readiness score report."""
    prof = profile or get_model_governance_profile()
    res = calculate_governance_readiness_score(profile=prof)

    record = {
        "readiness_score": res.readiness_score,
        "classification": res.classification,
        "meets_threshold": res.meets_threshold,
        "findings_count": res.findings_count,
        "manual_review_count": res.manual_review_count,
        "non_signal": res.non_signal,
        "production_ready": res.production_ready,
        "broker_ready": res.broker_ready,
        "release_approved": res.release_approved,
        "model_performance_claim": res.model_performance_claim,
        "phase": prof.current_phase,
    }

    df = pd.DataFrame([record])
    summary = summarize_governance_readiness_scores(df)
    return df, summary


def summarize_governance_readiness_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize readiness scores."""
    row = df.iloc[0] if not df.empty else {}
    return {
        "readiness_score": float(row.get("readiness_score", 1.0)),
        "classification": str(row.get("classification", "governance_contract_ready")),
        "meets_threshold": bool(row.get("meets_threshold", True)),
        "production_ready": False,
        "broker_ready": False,
        "release_approved": False,
        "non_signal": True,
    }
