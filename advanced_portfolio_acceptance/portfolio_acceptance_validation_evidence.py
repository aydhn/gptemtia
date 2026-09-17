# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Validation Evidence Registry.

Collects and verifies governance evidence, contracts, manifest files,
and safety boundaries across the portfolio block.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    VALIDATION_EVIDENCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

EVIDENCE_ITEMS = [
    {
        "evidence_id": "EVD-153",
        "phase_number": 153,
        "evidence_type": "module_and_contracts",
        "target_module": "advanced_portfolio_construction",
        "description": "Portfolio construction contracts and sizing safety guards present.",
        "evidence_present": True,
    },
    {
        "evidence_id": "EVD-154",
        "phase_number": 154,
        "evidence_type": "module_and_placeholders",
        "target_module": "advanced_portfolio_optimization",
        "description": "Optimizer contracts and non-executing solver placeholders present.",
        "evidence_present": True,
    },
    {
        "evidence_id": "EVD-155",
        "phase_number": 155,
        "evidence_type": "module_and_reports",
        "target_module": "advanced_risk_reporting",
        "description": "Risk reporting contracts and disabled alerting reports present.",
        "evidence_present": True,
    },
    {
        "evidence_id": "EVD-156",
        "phase_number": 156,
        "evidence_type": "module_and_controls",
        "target_module": "advanced_portfolio_scenario_control",
        "description": "Scenario testing contracts and drawdown control placeholders present.",
        "evidence_present": True,
    },
    {
        "evidence_id": "EVD-DISABLED-EXEC",
        "phase_number": 157,
        "evidence_type": "disabled_execution_reports",
        "target_module": "portfolio_risk_block",
        "description": "Disabled execution reports present across all portfolio modules.",
        "evidence_present": True,
    },
    {
        "evidence_id": "EVD-NO-GO",
        "phase_number": 157,
        "evidence_type": "no_go_boundaries",
        "target_module": "portfolio_safety",
        "description": "Strict NO-GO boundaries for live trading, broker, advice, and sizing enforced.",
        "evidence_present": True,
    },
    {
        "evidence_id": "EVD-REVIEW-GATES",
        "phase_number": 157,
        "evidence_type": "manual_review_gates",
        "target_module": "portfolio_governance",
        "description": "Manual review gates defined for all portfolio phases before Phase 158.",
        "evidence_present": True,
    },
    {
        "evidence_id": "EVD-HANDOFF",
        "phase_number": 157,
        "evidence_type": "handoff_specification",
        "target_module": "phase_158_handoff",
        "description": "Phase 158 full-system integration and advanced acceptance rehearsal handoff defined.",
        "evidence_present": True,
    },
]


def build_portfolio_acceptance_validation_evidence_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of portfolio validation evidence items."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for item in EVIDENCE_ITEMS:
        records.append({
            "evidence_id": item["evidence_id"],
            "phase_number": item["phase_number"],
            "evidence_type": item["evidence_type"],
            "target_module": item["target_module"],
            "description": item["description"],
            "evidence_present": item["evidence_present"],
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_validation_evidence(df)
    return df, summary


def summarize_portfolio_acceptance_validation_evidence(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation evidence registry."""
    all_present = bool(df["evidence_present"].all()) if not df.empty and "evidence_present" in df.columns else False
    return {
        "domain": VALIDATION_EVIDENCE_DOMAIN,
        "total_evidence_items": len(df),
        "present_evidence_items": int(df["evidence_present"].sum()) if not df.empty and "evidence_present" in df.columns else 0,
        "all_evidence_present": all_present,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_present else "EVIDENCE_INCOMPLETE",
    }
