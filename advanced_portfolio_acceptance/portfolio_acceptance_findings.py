# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Findings Registry.

Consolidates all acceptance findings, warnings, and review notes while
strictly prohibiting unsafe automated remediation actions.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    FINDING_DOMAIN,
    SEVERITY_INFO,
    SEVERITY_WARNING,
    SEVERITY_CRITICAL,
    PORTFOLIO_ACCEPTANCE_READY,
)
from .portfolio_acceptance_models import PortfolioAcceptanceFinding

FORBIDDEN_RECOMMENDATIONS = [
    "auto-construct portfolio",
    "auto-position-size",
    "auto-optimize portfolio",
    "auto-generate weights",
    "auto-generate allocation",
    "auto-rebalance",
    "auto-generate orders",
    "auto-run risk report",
    "auto-calculate exposure",
    "auto-monitor limits",
    "auto-run scenario",
    "auto-calculate drawdown",
    "auto-trigger drawdown control",
    "auto-hedge",
    "auto-de-risk",
    "auto-send alert",
    "auto-generate dashboard",
    "auto-send broker order",
    "auto-generate signal",
    "approve production",
    "approve broker readiness",
    "auto-deploy",
    "auto-write model registry",
    "auto-overwrite",
    "auto-delete",
    "auto-impute",
    "enable scraping",
]


def create_portfolio_acceptance_finding(
    finding_type: str,
    phase_ref: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> PortfolioAcceptanceFinding:
    """Create a structured finding while validating against forbidden recommendations."""
    rec_lower = recommendation.lower()
    for forbidden in FORBIDDEN_RECOMMENDATIONS:
        if forbidden in rec_lower:
            raise ValueError(
                f"Prohibited remediation '{forbidden}' requested in finding recommendation."
            )

    return PortfolioAcceptanceFinding(
        finding_id=f"FND-{phase_ref.replace(' ', '')}-{finding_type.upper()[:8]}",
        finding_type=finding_type,
        phase_ref=phase_ref,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        is_blocking=(severity_label == SEVERITY_CRITICAL),
    )


DEFAULT_FINDINGS = [
    create_portfolio_acceptance_finding(
        finding_type="contract_only_verification",
        phase_ref="Phase 153-157",
        severity_label=SEVERITY_INFO,
        message="Portfolio and risk contracts verified in contract-only and placeholder mode.",
        recommendation="Maintain contract-only boundary into Phase 158 integration rehearsal.",
        manual_review_required=True,
    ),
    create_portfolio_acceptance_finding(
        finding_type="non_production_assurance",
        phase_ref="Phase 157",
        severity_label=SEVERITY_WARNING,
        message="Acceptance readiness score does not approve live trading or production deployment.",
        recommendation="Perform thorough manual governance review before Phase 158 rehearsal.",
        manual_review_required=True,
    ),
]


def build_portfolio_acceptance_findings_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
    extra_findings: Optional[List[PortfolioAcceptanceFinding]] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of portfolio acceptance findings."""
    active = profile or get_portfolio_acceptance_profile()
    findings_list = list(DEFAULT_FINDINGS)
    if extra_findings:
        findings_list.extend(extra_findings)

    records = []
    for f in findings_list:
        records.append({
            "finding_id": f.finding_id,
            "finding_type": f.finding_type,
            "phase_ref": f.phase_ref,
            "severity_label": f.severity_label,
            "message": f.message,
            "recommendation": f.recommendation,
            "manual_review_required": f.manual_review_required,
            "is_blocking": f.is_blocking,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_findings(df)
    return df, summary


def summarize_portfolio_acceptance_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize findings registry."""
    blocking_count = len(df[df["is_blocking"]]) if not df.empty and "is_blocking" in df.columns else 0
    review_count = len(df[df["manual_review_required"]]) if not df.empty and "manual_review_required" in df.columns else 0
    return {
        "domain": FINDING_DOMAIN,
        "total_findings": len(df),
        "blocking_findings_count": blocking_count,
        "manual_review_required_count": review_count,
        "status": PORTFOLIO_ACCEPTANCE_READY if blocking_count == 0 else "BLOCKERS_PRESENT",
    }
