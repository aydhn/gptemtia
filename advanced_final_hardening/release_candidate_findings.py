# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Findings.

Defines findings management and strictly guards against forbidden automated
trading/deployment recommendations.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    FINDING_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)
from advanced_final_hardening.final_hardening_models import ReleaseCandidateFinding

FORBIDDEN_RECOMMENDATION_KEYWORDS = [
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
    "approve live readiness",
    "auto-deploy",
    "auto-write model registry",
    "auto-save model artifact",
    "auto-overwrite",
    "auto-delete",
    "auto-impute",
    "enable scraping",
]


def create_release_candidate_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> ReleaseCandidateFinding:
    """Create a ReleaseCandidateFinding with strict validation of recommendations."""
    rec_lower = recommendation.lower()
    for forbidden in FORBIDDEN_RECOMMENDATION_KEYWORDS:
        if forbidden in rec_lower:
            raise ValueError(
                f"Forbidden recommendation detected in finding: '{forbidden}'. "
                "Automated live execution, deployment, or destructive operations are strictly disallowed."
            )

    return ReleaseCandidateFinding(
        finding_id=f"FND-{domain[:3].upper()}-{abs(hash(message)) % 10000:04d}",
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        status=FINAL_HARDENING_CONTRACT_READY,
    )


def build_release_candidate_findings_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build findings registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    f1 = create_release_candidate_finding(
        finding_type="safety_audit",
        domain=FINDING_DOMAIN,
        severity_label="INFO",
        message="All live trading, broker, and real order executions are disabled by policy.",
        recommendation="Maintain offline research flags and dry-run boundaries.",
        manual_review_required=True,
    )
    f2 = create_release_candidate_finding(
        finding_type="freeze_audit",
        domain=FINDING_DOMAIN,
        severity_label="INFO",
        message="Configuration and documentation freezes are fully documented and registered.",
        recommendation="Perform human manual review before approving Phase 160 handoff.",
        manual_review_required=True,
    )
    f3 = create_release_candidate_finding(
        finding_type="readiness_audit",
        domain=FINDING_DOMAIN,
        severity_label="INFO",
        message="Release candidate contract layer is ready for local/offline acceptance.",
        recommendation="Proceed with Phase 160 Full Advanced Bot Final Delivery under non-live constraints.",
        manual_review_required=True,
    )

    rows = []
    for f in [f1, f2, f3]:
        rows.append({
            "finding_id": f.finding_id,
            "finding_type": f.finding_type,
            "domain": f.domain,
            "severity_label": f.severity_label,
            "message": f.message,
            "recommendation": f.recommendation,
            "manual_review_required": f.manual_review_required,
            "non_signal": f.non_signal,
            "local_only": f.local_only,
            "dry_run": f.dry_run,
            "non_production": f.non_production,
            "current_phase": active_profile.current_phase,
            "status": f.status,
        })

    df = pd.DataFrame(rows)
    summary = {
        "finding_count": len(rows),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
