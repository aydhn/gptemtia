# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Findings Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_models import (
    GpuTrainingFinding,
)


def create_gpu_training_finding(
    finding_type: str,
    governance_domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> GpuTrainingFinding:
    """Create a validated GpuTrainingFinding instance."""
    import uuid

    return GpuTrainingFinding(
        finding_id=f"FIND_{uuid.uuid4().hex[:8]}",
        finding_type=finding_type,
        governance_domain=governance_domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        non_signal=True,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
    )


def build_gpu_training_findings_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build findings registry documenting governance posture."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    findings = [
        create_gpu_training_finding(
            finding_type="resource_policy_manual_review",
            governance_domain="resource_policy_domain",
            severity_label="INFO",
            message="GPU training resource governance boundaries are established under contract_only mode.",
            recommendation="Review device selection and memory budget limits before subsequent ML phases.",
            manual_review_required=True,
        ),
        create_gpu_training_finding(
            finding_type="real_training_request_blocked",
            governance_domain="no_real_training_domain",
            severity_label="INFO",
            message="All real model training and fit routines are permanently blocked in Phase 139.",
            recommendation="Preserve zero-training boundary until explicit model training approval phases.",
            manual_review_required=True,
        ),
        create_gpu_training_finding(
            finding_type="artifact_request_blocked",
            governance_domain="artifact_disabled_domain",
            severity_label="INFO",
            message="Model weight serialization and registry writing are disabled in Phase 139.",
            recommendation="Maintain stateless contract mode without disk artifact generation.",
            manual_review_required=True,
        ),
    ]

    rows = []
    for f in findings:
        rows.append(
            {
                "finding_id": f.finding_id,
                "finding_type": f.finding_type,
                "governance_domain": f.governance_domain,
                "severity_label": f.severity_label,
                "message": f.message,
                "recommendation": f.recommendation,
                "manual_review_required": f.manual_review_required,
                "non_signal": f.non_signal,
                "destructive_action_allowed": f.destructive_action_allowed,
                "auto_fix_allowed": f.auto_fix_allowed,
                "created_at": f.created_at,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_gpu_training_findings(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize findings DataFrame."""
    if df.empty:
        return {"total_findings": 0, "critical_count": 0, "non_signal": True}
    return {
        "total_findings": len(df),
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "critical_count": int((df["severity_label"] == "CRITICAL").sum()) if "severity_label" in df.columns else 0,
        "destructive_allowed": False,
        "auto_fix_allowed": False,
        "current_phase": 139,
        "non_signal": True,
    }
