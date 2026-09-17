# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Findings Registry.

Consolidates audit findings and enforces safe recommendation standards.
Strictly prohibits automated execution, auto-deployment, or live readiness recommendations.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_FINDING_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    SEVERITY_INFO,
)
from advanced_final_delivery.final_delivery_models import FinalDeliveryFinding

AUDIT_FINDINGS = [
    (
        "FND-160-001",
        "final_delivery_contract_completeness",
        "Final delivery package contracts verified complete and frozen.",
        "Maintain frozen local delivery contracts; do not attempt live trading or broker integration.",
    ),
    (
        "FND-160-002",
        "final_manifest_verification",
        "Final delivery master manifest reflects 160-phase completion without side-effects.",
        "Archive manifest for regulatory compliance and maintain offline boundary.",
    ),
    (
        "FND-160-003",
        "safety_boundaries_enforcement",
        "All 25 NO-GO boundary rules verified active and strictly blocking execution.",
        "Ensure safety boundaries remain enabled indefinitely in non-production environments.",
    ),
    (
        "FND-160-004",
        "operator_handover_readiness",
        "Operator handover protocols and runbooks verified for safe offline usage.",
        "Require manual sign-off on operator handover before running offline inspections.",
    ),
]


def create_final_delivery_finding(
    finding_id: str,
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> FinalDeliveryFinding:
    """Create a validated FinalDeliveryFinding instance."""
    # Ensure safe recommendation
    rec_lower = recommendation.lower()
    unsafe_patterns = [
        "auto-run", "live bot", "live signal", "broker order", "prediction",
        "train model", "backtest", "optimizer", "construct portfolio",
        "approve production", "approve broker", "approve live", "auto-deploy",
        "auto-write", "auto-save", "auto-overwrite", "auto-delete", "auto-impute", "scraping"
    ]
    for p in unsafe_patterns:
        if p in rec_lower:
            recommendation = "Review offline documentation and maintain strict local safety boundary."
            break

    return FinalDeliveryFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def build_final_delivery_findings_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build findings registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for f_id, f_type, msg, rec in AUDIT_FINDINGS:
        f = create_final_delivery_finding(
            finding_id=f_id,
            finding_type=f_type,
            domain=FINAL_FINDING_DOMAIN,
            severity_label=SEVERITY_INFO,
            message=msg,
            recommendation=rec,
            manual_review_required=True,
        )
        rows.append({
            "finding_id": f.finding_id,
            "finding_type": f.finding_type,
            "severity_label": f.severity_label,
            "message": f.message,
            "recommendation": f.recommendation,
            "manual_review_required": f.manual_review_required,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_FINDING_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "finding_count": len(rows),
        "all_manual_review_required": True,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
