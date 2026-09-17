# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Findings Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_FINDING_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)
from .portfolio_construction_models import PortfolioFinding

FORBIDDEN_REMEDIATION_PHRASES: List[str] = [
    "auto-run backtest",
    "auto-run benchmark",
    "auto-calculate metrics",
    "auto-generate performance claim",
    "auto-approve strategy",
    "auto-allocate capital",
    "auto-position-size",
    "auto-construct portfolio",
    "auto-optimize strategy",
    "auto-train model",
    "auto-run prediction",
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


def create_portfolio_finding(
    finding_type: str,
    domain: str,
    severity: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> PortfolioFinding:
    """Factory function for creating a portfolio finding with forbidden recommendation check."""
    rec_lower = recommendation.lower()
    for forbidden in FORBIDDEN_REMEDIATION_PHRASES:
        if forbidden in rec_lower:
            raise ValueError(
                f"Prohibited remediation proposal detected: '{forbidden}' in recommendation: {recommendation}"
            )

    return PortfolioFinding(
        finding_id=f"FND-153-{abs(hash(message)) % 100000:05d}",
        finding_type=finding_type,
        domain=domain,
        severity=severity,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        non_signal=True,
    )


def build_portfolio_findings_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for consolidated portfolio construction findings."""
    base_findings = [
        create_portfolio_finding(
            finding_type="phase_152_handoff_accepted",
            domain="upstream_governance",
            severity="INFO",
            message="Phase 152 Backtest Acceptance Report verified and accepted as input contract base.",
            recommendation="Maintain strict offline contract scope without executing backtests or optimizations.",
            manual_review_required=False,
        ),
        create_portfolio_finding(
            finding_type="portfolio_contract_layer_established",
            domain="portfolio_construction",
            severity="INFO",
            message="Portfolio construction, position sizing, and risk budgeting contracts established.",
            recommendation="Review all contract parameter specifications prior to Phase 154 handoff.",
            manual_review_required=True,
        ),
        create_portfolio_finding(
            finding_type="non_production_boundary_enforced",
            domain="safety_governance",
            severity="INFO",
            message="All real capital allocation, broker order generation, and live execution remain strictly disabled.",
            recommendation="Ensure manual review gates remain mandatory before any future execution phases.",
            manual_review_required=True,
        ),
    ]

    records = []
    for f in base_findings:
        records.append({
            "finding_id": f.finding_id,
            "finding_type": f.finding_type,
            "domain": f.domain,
            "severity": f.severity,
            "message": f.message,
            "recommendation": f.recommendation,
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "next_phase": profile.next_phase,
            "manual_review_required": f.manual_review_required,
            "status": PORTFOLIO_CONTRACT_READY,
            "contract_only": True,
            "non_production": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": PORTFOLIO_FINDING_DOMAIN,
        "active_profile": profile.profile_name,
        "total_findings": len(records),
        "critical_count": len([r for r in records if r["severity"] in ["CRITICAL", "BLOCKER"]]),
        "manual_review_required_count": len([r for r in records if r["manual_review_required"]]),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
