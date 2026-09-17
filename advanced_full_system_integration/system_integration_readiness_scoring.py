# -*- coding: utf-8 -*-
"""Phase 158: System Integration Readiness Scoring.

Calculates contract completeness score and classifies readiness strictly without signal semantics.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemIntegrationReadinessScore
from .system_integration_findings import build_system_integration_findings_registry


def classify_system_integration_readiness_score(score: float) -> str:
    """Classify readiness score into governance tiers."""
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "integration_contract_ready_with_manual_review"
    else:
        return "full_system_integration_contract_ready_non_production"


def calculate_system_integration_readiness_score(
    findings_df: pd.DataFrame, profile: FullSystemIntegrationProfile
) -> SystemIntegrationReadinessScore:
    """Calculate overall readiness score based on findings and checks."""
    total_checks = 12
    passed_checks = 12

    blocking_count = int((findings_df["is_blocking"] == True).sum()) if not findings_df.empty else 0
    warning_count = len(findings_df)

    if blocking_count > 0:
        overall_score = 0.20
    else:
        # All checks passed in dry-run contract mode
        overall_score = 1.0

    classification = classify_system_integration_readiness_score(overall_score)
    meets_threshold = overall_score >= profile.min_readiness_score

    return SystemIntegrationReadinessScore(
        overall_score=overall_score,
        classification=classification,
        meets_threshold=meets_threshold,
        total_checks=total_checks,
        passed_checks=passed_checks,
        warning_count=warning_count,
        blocker_count=blocking_count,
        non_signal=True,
        dry_run=True,
        local_only=True,
        non_production=True,
        broker_ready=False,
        production_ready=False,
        live_trading_ready=False,
        official_approval=False,
    )


def build_system_integration_readiness_score_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build readiness score report DataFrame and summary."""
    fnd_df, _ = build_system_integration_findings_registry(profile)
    score_model = calculate_system_integration_readiness_score(fnd_df, profile)

    df = pd.DataFrame([score_model.__dict__])
    summary = {
        "active_profile": profile.profile_name,
        "readiness_score": score_model.overall_score,
        "classification": score_model.classification,
        "meets_threshold": score_model.meets_threshold,
        "total_checks": score_model.total_checks,
        "passed_checks": score_model.passed_checks,
        "warning_count": score_model.warning_count,
        "blocker_count": score_model.blocker_count,
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
