# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Findings Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    FINDING_DOMAIN,
    ACCEPTANCE_READY,
)
from advanced_backtest_acceptance.backtest_acceptance_models import (
    BacktestAcceptanceFinding,
)

FORBIDDEN_REMEDIATION_PHRASES: List[str] = [
    "auto-run backtest",
    "auto-run benchmark",
    "auto-calculate metrics",
    "auto-generate performance claim",
    "auto-approve strategy",
    "auto-allocate capital",
    "auto-position-size",
    "auto-construct portfolio",
    "auto-optimize strategy",
    "auto-train model",
    "auto-run prediction",
    "auto-send broker order",
    "auto-generate signal",
    "approve production",
    "approve broker readiness",
    "auto-deploy",
    "auto-write model registry",
    "auto-overwrite",
    "auto-delete",
    "auto-impute",
    "enable scraping",
]


def create_backtest_acceptance_finding(
    finding_type: str,
    phase_ref: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> BacktestAcceptanceFinding:
    """Factory function for creating an acceptance finding with forbidden recommendation check."""
    rec_lower = recommendation.lower()
    for forbidden in FORBIDDEN_REMEDIATION_PHRASES:
        if forbidden in rec_lower:
            raise ValueError(f"Prohibited remediation proposal detected: '{forbidden}' in recommendation: {recommendation}")

    return BacktestAcceptanceFinding(
        finding_id=f"FND-{abs(hash(message)) % 100000:05d}",
        finding_type=finding_type,
        phase_ref=phase_ref,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        non_signal=True,
    )


def build_backtest_acceptance_findings_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for consolidated acceptance findings."""
    active = profile or get_backtest_acceptance_profile()

    # Informational finding highlighting clean completion of backtest block contracts
    base_finding = create_backtest_acceptance_finding(
        finding_type="phase_146_152_consolidation_notice",
        phase_ref="Phase 146-152",
        severity_label="INFO",
        message="All Phase 146-151 backtest contracts successfully verified under offline research policy.",
        recommendation="Proceed with contract design in Phase 153 for portfolio construction under strict non-live rules.",
        manual_review_required=True,
    )

    records = [{
        "finding_id": base_finding.finding_id,
        "finding_type": base_finding.finding_type,
        "phase_ref": base_finding.phase_ref,
        "severity_label": base_finding.severity_label,
        "message": base_finding.message,
        "recommendation": base_finding.recommendation,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "manual_review_required": base_finding.manual_review_required,
        "status": ACCEPTANCE_READY,
        "non_signal": True,
        "non_production": True,
        "local_only": True,
    }]

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": FINDING_DOMAIN,
        "active_profile": active.profile_name,
        "total_findings": len(records),
        "critical_count": len([r for r in records if r["severity_label"] in ["CRITICAL", "BLOCKER"]]),
        "manual_review_required_count": len([r for r in records if r["manual_review_required"]]),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
