# -*- coding: utf-8 -*-
"""Phase 158: System Integration Findings Registry.

Tracks findings, recommendations, and governance items requiring review.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemIntegrationFinding

FORBIDDEN_RECOMMENDATION_PHRASES = [
    "auto-run full system",
    "auto-run live bot",
    "auto-generate live signals",
    "auto-send broker order",
    "auto-run prediction",
    "auto-train model",
    "auto-run backtest",
    "auto-run optimizer",
    "auto-construct portfolio",
    "auto-run risk monitoring",
    "auto-run scenario",
    "approve production",
    "approve broker readiness",
    "auto-deploy",
    "auto-write model registry",
    "auto-overwrite",
    "auto-delete",
    "auto-impute",
    "enable scraping",
]


def create_system_integration_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
    is_blocking: bool = False,
) -> SystemIntegrationFinding:
    """Create and validate a finding against forbidden recommendations."""
    rec_lower = recommendation.lower()
    for forbidden in FORBIDDEN_RECOMMENDATION_PHRASES:
        if forbidden in rec_lower:
            raise ValueError(f"Prohibited recommendation detected: '{forbidden}'")

    fid = f"FND-158-{abs(hash((finding_type, message))) % 10000:04d}"
    return SystemIntegrationFinding(
        finding_id=fid,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        is_blocking=is_blocking,
    )


def build_system_integration_findings_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system integration findings DataFrame and summary."""
    findings = [
        create_system_integration_finding(
            finding_type="governance_review_required",
            domain="manual_review_gates",
            severity_label="LOW",
            message="Ten system manual review gates are queued for operator inspection before Phase 159 release candidate.",
            recommendation="Review the manual review gate registry and sign off documentation offline.",
            manual_review_required=True,
            is_blocking=False,
        ),
        create_system_integration_finding(
            finding_type="contract_only_notice",
            domain="system_integration",
            severity_label="INFO",
            message="Full-system integration verified at contract and acceptance rehearsal level without live execution.",
            recommendation="Maintain local/offline dry-run boundaries during Phase 159 hardening.",
            manual_review_required=True,
            is_blocking=False,
        ),
    ]

    df = pd.DataFrame([f.__dict__ for f in findings])
    summary = {
        "active_profile": profile.profile_name,
        "total_findings": len(df),
        "blocking_findings_count": int((df["is_blocking"] == True).sum()),
        "manual_review_required_count": int((df["manual_review_required"] == True).sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
