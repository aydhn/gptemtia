# -*- coding: utf-8 -*-
"""Phase 144: Governance Decision Log Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

DECISION_LOG_ITEMS: List[Dict[str, str]] = [
    {"decision_id": "DEC-01", "topic": "non_production_boundary", "decision": "Keep all models in contract-only state with zero weight persistence.", "rationale": "Prevents unauthorized production deployment."},
    {"decision_id": "DEC-02", "topic": "prohibited_use_policy", "decision": "Strictly block all live trading, broker execution, and financial advice.", "rationale": "Enforces regulatory safety and local research mandate."},
    {"decision_id": "DEC-03", "topic": "explainability_attribution_usage", "decision": "Forbid automatic retraining or pruning based on attribution scores.", "rationale": "Prevents attribution feedback loops and instability."},
]


def build_governance_decision_log_placeholder_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance decision log placeholders."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in DECISION_LOG_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["is_placeholder"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_decision_log_placeholders(df)
    return df, summary


def summarize_governance_decision_log_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance decision log placeholders."""
    return {
        "total_decision_placeholders": len(df),
        "all_placeholders": bool(df["is_placeholder"].all()),
        "status": "PLACEHOLDER_LOG_READY",
    }
