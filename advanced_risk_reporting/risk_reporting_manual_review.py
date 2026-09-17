# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Manual Review Queue."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingManualReviewItem


DEFAULT_MANUAL_REVIEWS = [
    {
        "checkpoint_id": "MRQ-155-001",
        "domain": "risk_report_contract_domain",
        "review_target": "risk_report_contracts",
        "description": "Verify risk report contracts satisfy zero execution and offline invariants",
        "status": "PENDING_OPERATOR_REVIEW",
        "recommendation": "Operator should verify contract specifications before Phase 156.",
    },
    {
        "checkpoint_id": "MRQ-155-002",
        "domain": "exposure_attribution_domain",
        "review_target": "exposure_attribution_contracts",
        "description": "Verify exposure attribution templates remain in placeholder mode",
        "status": "PENDING_OPERATOR_REVIEW",
        "recommendation": "Confirm zero exposure calculations were executed.",
    },
    {
        "checkpoint_id": "MRQ-155-003",
        "domain": "limit_monitoring_domain",
        "review_target": "limit_monitoring_contracts",
        "description": "Verify limit monitoring contracts do not instantiate live alerting loops",
        "status": "PENDING_OPERATOR_REVIEW",
        "recommendation": "Confirm alert routing disabled policies are active.",
    },
]


def build_risk_reporting_manual_review_queue(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for manual review checkpoints."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for r in DEFAULT_MANUAL_REVIEWS:
        model = RiskReportingManualReviewItem(**r)
        data = model.model_dump()
        data["current_phase"] = profile.current_phase
        data["target_final_phase"] = profile.target_final_phase
        data["next_phase"] = profile.next_phase
        rows.append(data)

    df = pd.DataFrame(rows)
    summary = {
        "review_count": len(df),
        "all_pending": True,
        "is_safe": True,
    }
    return df, summary
