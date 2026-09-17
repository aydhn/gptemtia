# -*- coding: utf-8 -*-
"""Phase 150: Backtest Source Preservation Guards.

Enforces strict prohibitions against destructive dataset modification, raw source
overwrite, auto-imputation, and automated feature dropping.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    SAFETY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

SOURCE_PRESERVATION_RULES: List[Dict[str, Any]] = [
    {
        "guard_id": "SRC_01_NO_OVERWRITE",
        "guard_name": "source_overwrite_prohibition",
        "description": "Prohibit overwriting or altering raw market data tables and original provider observations.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "guard_id": "SRC_02_NO_DESTRUCTIVE_CLEANING",
        "guard_name": "destructive_cleaning_prohibition",
        "description": "Forbid silent row deletion, silent trimming, or destructive in-place cleaning passes.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "guard_id": "SRC_03_NO_AUTO_IMPUTATION",
        "guard_name": "auto_imputation_prohibition",
        "description": "Disallow automated forward-filling or statistical imputation without explicit audit trails.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "guard_id": "SRC_04_NO_AUTO_FEATURE_DROP",
        "guard_name": "auto_feature_drop_prohibition",
        "description": "Disallow automatic silent dropping of underperforming or correlated features.",
        "enforcement": "BLOCKING_MANDATORY",
    },
]

FORBIDDEN_DESTRUCTIVE_ACTIONS = [
    "overwrite",
    "destructive_clean",
    "file_delete",
    "auto_impute",
    "auto_drop",
    "silent_drop",
    "truncate_source",
]


def validate_backtest_source_preservation_action(action: str) -> Dict[str, Any]:
    """Inspect requested action against source preservation invariants."""
    action_lower = str(action).lower()
    blocked = False
    violating_actions: List[str] = []

    for forbidden in FORBIDDEN_DESTRUCTIVE_ACTIONS:
        if forbidden in action_lower:
            blocked = True
            violating_actions.append(forbidden)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "action": action,
        "violating_actions": violating_actions,
        "decision": "BLOCKED_BY_SOURCE_PRESERVATION_GUARD" if blocked else "ALLOWED_SAFE_OPERATION",
        "policy_message": (
            f"Destructive action blocked: {violating_actions}. Raw sources must remain immutable."
            if blocked
            else "Action complies with source preservation invariants."
        ),
        "non_signal": True,
    }


def build_backtest_source_preservation_guard_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for source preservation guards."""
    rows: List[Dict[str, Any]] = []
    for r in SOURCE_PRESERVATION_RULES:
        rows.append({
            "guard_id": r["guard_id"],
            "guard_name": r["guard_name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "status": "ACTIVE",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": SAFETY_DOMAIN,
        "subdomain": "source_preservation_guards",
        "total_guards": len(df),
        "all_active": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
