# -*- coding: utf-8 -*-
"""Phase 144: Governance Change Log Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

CHANGE_LOG_ITEMS: List[Dict[str, str]] = [
    {"change_id": "CHG-01", "component": "model_card_contract", "change_type": "initial_creation", "description": "Created baseline and candidate model card contracts."},
    {"change_id": "CHG-02", "component": "approval_boundaries", "change_type": "policy_enforcement", "description": "Activated 6 approval boundaries blocking live trading."},
    {"change_id": "CHG-03", "component": "manual_review_gates", "change_type": "gate_activation", "description": "Activated 9 manual review gates for Phase 144."},
]


def build_governance_change_log_placeholder_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance change log placeholders."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in CHANGE_LOG_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["is_placeholder"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_change_log_placeholders(df)
    return df, summary


def summarize_governance_change_log_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance change log placeholders."""
    return {
        "total_change_placeholders": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()),
        "status": "CHANGE_LOG_READY",
    }
