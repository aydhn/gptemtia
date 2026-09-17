# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Findings Registry.

Logs diagnostic findings and prevents automatic remediation phrases.
"""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile
from .portfolio_optimization_models import PortfolioOptimizationFinding


def create_portfolio_optimization_finding(
    finding_id: str,
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> PortfolioOptimizationFinding:
    """Create a validated PortfolioOptimizationFinding."""
    return PortfolioOptimizationFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def build_portfolio_optimization_findings_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build diagnostic findings table."""
    findings = [
        create_portfolio_optimization_finding(
            finding_id="FINDING_154_01",
            finding_type="contract_layer_active",
            domain="optimization_contract_domain",
            severity_label="INFO",
            message="Portfolio optimization contract layer instantiated in offline research mode",
            recommendation="Review contracts manually and maintain zero execution invariants",
            manual_review_required=True,
        ),
        create_portfolio_optimization_finding(
            finding_id="FINDING_154_02",
            finding_type="zero_execution_enforced",
            domain="disabled_execution_domain",
            severity_label="INFO",
            message="All real optimizer, solver, and weight generation executions are strictly locked",
            recommendation="Retain policy locks across all future research cycles",
            manual_review_required=True,
        ),
        create_portfolio_optimization_finding(
            finding_id="FINDING_154_03",
            finding_type="phase_155_handoff_ready",
            domain="phase_155_handoff_domain",
            severity_label="INFO",
            message="Phase 155 Risk Reporting prerequisites successfully sealed",
            recommendation="Proceed to Phase 155 Risk Reporting following operator sign-off",
            manual_review_required=True,
        ),
    ]
    records = [f.model_dump() for f in findings]
    df = pd.DataFrame(records)
    summary = {
        "finding_count": len(records),
        "blocker_count": 0,
        "warning_count": 0,
        "info_count": len(records),
    }
    return df, summary
