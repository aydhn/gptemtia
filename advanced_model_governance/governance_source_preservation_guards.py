# -*- coding: utf-8 -*-
"""Phase 144: Governance Source Preservation Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

DESTRUCTIVE_ACTIONS = [
    "overwrite",
    "delete",
    "truncate",
    "drop_columns",
    "auto_impute",
    "destructive_cleaning",
]


def build_governance_source_preservation_guard_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for source preservation guards."""
    prof = profile or get_model_governance_profile()
    records = [
        {"guard_name": "no_overwrite_guard", "enforcement": "Strict prohibition of overwriting raw input files.", "status": "ACTIVE"},
        {"guard_name": "no_deletion_guard", "enforcement": "File deletion and destructive trimming are blocked.", "status": "ACTIVE"},
        {"guard_name": "no_auto_drop_guard", "enforcement": "Automatic column removal or silent imputation is blocked.", "status": "ACTIVE"},
    ]
    for r in records:
        r["phase"] = prof.current_phase
        r["is_enforced"] = True

    df = pd.DataFrame(records)
    summary = summarize_governance_source_preservation_guards(df)
    return df, summary


def summarize_governance_source_preservation_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation guards."""
    return {
        "total_guards": len(df),
        "all_enforced": bool(df["is_enforced"].all()),
        "status": "SOURCE_PRESERVATION_GUARDS_ACTIVE",
    }


def validate_governance_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate action does not violate source preservation policy."""
    act_lower = str(action).lower()
    is_destructive = any(term in act_lower for term in DESTRUCTIVE_ACTIONS)
    return {
        "action": action,
        "is_allowed": not is_destructive,
        "is_destructive": is_destructive,
        "status": "PASS" if not is_destructive else "BLOCKED_BY_POLICY",
        "message": "Action preserves raw source data." if not is_destructive else "Destructive action blocked.",
    }
