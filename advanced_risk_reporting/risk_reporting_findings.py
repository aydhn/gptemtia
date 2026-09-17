# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Findings Registry."""

from typing import Any, Dict, List, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingFinding


DEFAULT_FINDINGS = [
    {
        "finding_id": "FND-155-001",
        "finding_type": "contract_layer_active",
        "domain": "risk_report_contract_domain",
        "severity_label": "INFO",
        "message": "Risk reporting contracts successfully registered in contract-only mode.",
        "recommendation": "Operator should review contract specifications before Phase 156.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FND-155-002",
        "finding_type": "exposure_attribution_contracts_active",
        "domain": "exposure_attribution_domain",
        "severity_label": "INFO",
        "message": "Exposure attribution contracts initialized as non-executing placeholders.",
        "recommendation": "Operator should inspect exposure families and formulas.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FND-155-003",
        "finding_type": "limit_monitoring_contracts_active",
        "domain": "limit_monitoring_domain",
        "severity_label": "INFO",
        "message": "Limit monitoring contracts active with live alerting strictly disabled.",
        "recommendation": "Maintain disabled alerting policy in all local environments.",
        "manual_review_required": True,
    },
]


def create_risk_reporting_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> RiskReportingFinding:
    """Factory function for creating validated diagnostic findings."""
    return RiskReportingFinding(
        finding_id=f"FND-155-GEN-{abs(hash(message)) % 10000:04d}",
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def build_risk_reporting_findings_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for diagnostic findings."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for f in DEFAULT_FINDINGS:
        model = RiskReportingFinding(**f)
        data = model.model_dump()
        data["current_phase"] = profile.current_phase
        data["target_final_phase"] = profile.target_final_phase
        data["next_phase"] = profile.next_phase
        rows.append(data)

    df = pd.DataFrame(rows)
    summary = {
        "finding_count": len(df),
        "total_findings": len(df),
        "critical_count": int((df["severity_label"] == "BLOCKER").sum()) if not df.empty else 0,
        "manual_review_required_count": int((df["manual_review_required"] == True).sum()) if not df.empty else 0,
    }
    return df, summary
