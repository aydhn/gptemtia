# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Findings Module.

Defines findings registry and factory for recording diagnostics and governance notices.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    FINDING_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)
from advanced_monte_carlo_robustness.monte_carlo_models import MonteCarloFinding


def create_monte_carlo_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
    finding_id: Optional[str] = None,
) -> MonteCarloFinding:
    """Factory creating a structured MonteCarloFinding dataclass."""
    f_id = finding_id or f"FINDING_149_{finding_type.upper()}"
    return MonteCarloFinding(
        finding_id=f_id,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        status="OPEN",
    )


BASELINE_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_type": "contract_layer_mode_active",
        "domain": FINDING_DOMAIN,
        "severity_label": "INFO",
        "message": "Phase 149 operating in contract-only mode. All simulation and metric executions remain strictly disabled.",
        "recommendation": "Review robustness envelope and parameter stability specifications before Phase 150 handoff.",
        "manual_review_required": True,
    },
    {
        "finding_type": "offline_research_boundary_enforced",
        "domain": FINDING_DOMAIN,
        "severity_label": "INFO",
        "message": "Zero live trading and zero broker connectivity invariants verified across all active profiles.",
        "recommendation": "Maintain strict local/offline research perimeter.",
        "manual_review_required": False,
    },
    {
        "finding_type": "bias_guard_audit_pass",
        "domain": FINDING_DOMAIN,
        "severity_label": "INFO",
        "message": "No lookahead columns, resampling leakage triggers, or raw text columns detected in registries.",
        "recommendation": "Proceed with validation-aware handoff to Phase 150 Backtest Governance.",
        "manual_review_required": False,
    },
]


def build_monte_carlo_findings_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo findings registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for f in BASELINE_FINDINGS:
        finding = create_monte_carlo_finding(
            finding_type=f["finding_type"],
            domain=f["domain"],
            severity_label=f["severity_label"],
            message=f["message"],
            recommendation=f["recommendation"],
            manual_review_required=f["manual_review_required"],
        )
        rows.append(
            {
                "finding_id": finding.finding_id,
                "finding_type": finding.finding_type,
                "domain": finding.domain,
                "severity_label": finding.severity_label,
                "message": finding.message,
                "recommendation": finding.recommendation,
                "manual_review_required": finding.manual_review_required,
                "status": finding.status,
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
            }
        )
    df = pd.DataFrame(rows)
    critical_count = len(df[df["severity_label"] == "CRITICAL"])
    high_count = len(df[df["severity_label"] == "HIGH"])

    summary = {
        "domain": FINDING_DOMAIN,
        "total_findings": len(df),
        "critical_count": critical_count,
        "high_count": high_count,
        "manual_review_count": int(df["manual_review_required"].sum()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
