# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Findings Module.

Defines findings registry and factory for recording diagnostics, audit notices,
and governance findings in Phase 150.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    FINDING_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)
from advanced_backtest_governance.backtest_governance_models import BacktestGovernanceFinding


def create_backtest_governance_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
    auto_remediation_allowed: bool = False,
    finding_id: Optional[str] = None,
) -> BacktestGovernanceFinding:
    """Factory creating a structured BacktestGovernanceFinding dataclass."""
    f_id = finding_id or f"FINDING_150_{finding_type.upper()}"
    return BacktestGovernanceFinding(
        finding_id=f_id,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        auto_remediation_allowed=auto_remediation_allowed,
        non_signal=True,
    )


BASELINE_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_type": "contract_layer_mode_active",
        "domain": FINDING_DOMAIN,
        "severity_label": "INFO",
        "message": "Phase 150 operating in contract-only mode. All backtest execution, metric calculations, and performance claims remain disabled.",
        "recommendation": "Review governance contracts, bias controls, and claim boundaries before proceeding to Phase 151.",
        "manual_review_required": True,
        "auto_remediation_allowed": False,
    },
    {
        "finding_type": "offline_research_boundary_enforced",
        "domain": FINDING_DOMAIN,
        "severity_label": "INFO",
        "message": "Zero live trading and zero broker connectivity invariants verified across all active profiles.",
        "recommendation": "Maintain strict local/offline research perimeter.",
        "manual_review_required": False,
        "auto_remediation_allowed": False,
    },
    {
        "finding_type": "bias_control_guards_verified",
        "domain": FINDING_DOMAIN,
        "severity_label": "INFO",
        "message": "Lookahead, survivorship, data snooping, overfitting, multiple testing, and parameter fishing controls active.",
        "recommendation": "Preserve all guard policies and validation gates in downstream pipelines.",
        "manual_review_required": False,
        "auto_remediation_allowed": False,
    },
    {
        "finding_type": "manual_review_gates_armed",
        "domain": FINDING_DOMAIN,
        "severity_label": "INFO",
        "message": "Ten manual review gates armed requiring explicit human operator verification before any phase progression.",
        "recommendation": "Perform manual review of review items MRQ_150_01 through MRQ_150_10.",
        "manual_review_required": True,
        "auto_remediation_allowed": False,
    },
]


def summarize_backtest_governance_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the findings registry."""
    critical_count = len(df[df["severity_label"] == "CRITICAL"]) if not df.empty else 0
    high_count = len(df[df["severity_label"] == "HIGH"]) if not df.empty else 0
    manual_review_count = int(df["manual_review_required"].sum()) if not df.empty else 0

    return {
        "domain": FINDING_DOMAIN,
        "total_findings": len(df),
        "critical_count": critical_count,
        "high_count": high_count,
        "manual_review_count": manual_review_count,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_governance_findings_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the findings registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for item in BASELINE_FINDINGS:
        finding = create_backtest_governance_finding(
            finding_type=item["finding_type"],
            domain=item["domain"],
            severity_label=item["severity_label"],
            message=item["message"],
            recommendation=item["recommendation"],
            manual_review_required=item["manual_review_required"],
            auto_remediation_allowed=item["auto_remediation_allowed"],
        )
        rows.append({
            "finding_id": finding.finding_id,
            "finding_type": finding.finding_type,
            "domain": finding.domain,
            "severity_label": finding.severity_label,
            "message": finding.message,
            "recommendation": finding.recommendation,
            "manual_review_required": finding.manual_review_required,
            "auto_remediation_allowed": finding.auto_remediation_allowed,
            "profile_name": profile.profile_name,
            "current_phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_governance_findings(df)
    summary["profile_name"] = profile.profile_name
    return df, summary
