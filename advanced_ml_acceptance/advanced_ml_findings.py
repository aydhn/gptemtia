# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Findings Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    FINDING_DOMAIN,
    ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
)
from advanced_ml_acceptance.advanced_ml_acceptance_models import AdvancedMlFinding

FORBIDDEN_RECOMMENDATION_PHRASES = [
    "approve production",
    "approve broker readiness",
    "approve live trading",
    "auto-deploy model",
    "auto-write model registry",
    "auto-save model artifact",
    "auto-run prediction",
    "auto-run backtest",
    "auto-calculate slippage",
    "auto-generate signal",
    "auto-run optimizer",
    "auto-delete",
    "auto-overwrite",
    "auto-impute",
    "enable scraping",
    "download article body",
    "generate sentiment",
    "generate embedding",
]


def create_advanced_ml_finding(
    finding_type: str,
    phase_ref: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> AdvancedMlFinding:
    """Create an advanced ML finding and validate against forbidden recommendations."""
    rec_lower = recommendation.lower()
    for forbidden in FORBIDDEN_RECOMMENDATION_PHRASES:
        if forbidden in rec_lower:
            raise ValueError(f"Forbidden recommendation detected: '{forbidden}' in recommendation: '{recommendation}'")

    return AdvancedMlFinding(
        finding_id=f"FND-{finding_type[:6].upper()}",
        finding_type=finding_type,
        phase_ref=phase_ref,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        non_signal=True,
    )


def build_advanced_ml_findings_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build consolidated findings DataFrame and summary."""
    active = profile or get_advanced_ml_acceptance_profile()

    sample_findings = [
        create_advanced_ml_finding(
            finding_type="contract_only_audit",
            phase_ref="Phase 136-144",
            severity_label="INFO",
            message="Phase 136-144 components verified at contract and schema level.",
            recommendation="Retain contract-only status until formal execution gates are designed.",
            manual_review_required=True,
        ),
        create_advanced_ml_finding(
            finding_type="manual_review_audit",
            phase_ref="Phase 144",
            severity_label="LOW",
            message="Model cards and risk disclosures await human committee inspection.",
            recommendation="Perform manual inspection of model card limitations.",
            manual_review_required=True,
        ),
        create_advanced_ml_finding(
            finding_type="handoff_readiness_audit",
            phase_ref="Phase 145",
            severity_label="INFO",
            message="Readiness scores computed without granting live or broker permissions.",
            recommendation="Proceed to Phase 146 realistic backtest contract planning.",
            manual_review_required=False,
        ),
    ]

    records = []
    for f in sample_findings:
        records.append({
            "finding_id": f.finding_id,
            "finding_type": f.finding_type,
            "phase_ref": f.phase_ref,
            "severity_label": f.severity_label,
            "message": f.message,
            "recommendation": f.recommendation,
            "manual_review_required": f.manual_review_required,
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status_label": ACCEPTANCE_MANUAL_REVIEW_REQUIRED if f.manual_review_required else "RESOLVED",
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": FINDING_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_findings": len(df),
        "manual_review_findings": int(df["manual_review_required"].sum()),
        "non_signal": True,
        "status": "RECORDED",
    }
    return df, summary


def summarize_advanced_ml_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize findings DataFrame."""
    return {
        "finding_count": len(df),
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "non_signal": True,
    }
