# -*- coding: utf-8 -*-
"""Phase 144: Governance Findings Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)
from advanced_model_governance.model_governance_models import GovernanceFinding

SAMPLE_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_id": "FND-144-01",
        "finding_type": "production_approval_request_blocked",
        "governance_domain": "governance_approval_boundary_domain",
        "severity_label": "INFO",
        "message": "Production approval request intercepted and safely blocked by policy.",
        "recommendation": "Inspect approval boundaries and preserve non-production state.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FND-144-02",
        "finding_type": "broker_ready_request_blocked",
        "governance_domain": "broker_ready_disabled_domain",
        "severity_label": "INFO",
        "message": "Broker-ready claim intercepted and safely blocked.",
        "recommendation": "Inspect prohibited-use registry and maintain offline research isolation.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FND-144-03",
        "finding_type": "live_trading_request_blocked",
        "governance_domain": "live_trading_disabled_domain",
        "severity_label": "INFO",
        "message": "Live trading request intercepted and safely blocked.",
        "recommendation": "Inspect live trading disabled report.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FND-144-04",
        "finding_type": "model_registry_write_request_blocked",
        "governance_domain": "model_registry_write_disabled_domain",
        "severity_label": "INFO",
        "message": "Model registry write request intercepted and safely blocked.",
        "recommendation": "Maintain contract-only representation without external registry writes.",
        "manual_review_required": True,
    },
]


def create_governance_finding(
    finding_type: str,
    governance_domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> GovernanceFinding:
    """Factory for GovernanceFinding dataclass instance."""
    finding_id = f"FND-DYN-{abs(hash(finding_type + governance_domain)) % 10000:04d}"
    return GovernanceFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        governance_domain=governance_domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def build_governance_findings_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance findings."""
    prof = profile or get_model_governance_profile()
    records = []
    for f in SAMPLE_FINDINGS:
        row = dict(f)
        row["phase"] = prof.current_phase
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_findings(df)
    return df, summary


def summarize_governance_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance findings."""
    return {
        "total_findings": len(df),
        "critical_findings": int((df["severity_label"] == "CRITICAL").sum()) if not df.empty else 0,
        "high_findings": int((df["severity_label"] == "HIGH").sum()) if not df.empty else 0,
        "info_findings": int((df["severity_label"] == "INFO").sum()) if not df.empty else 0,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "status": "FINDINGS_LOGGED",
    }
