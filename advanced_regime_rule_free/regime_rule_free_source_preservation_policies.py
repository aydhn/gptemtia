"""Phase 128: Regime Rule-Free Source Preservation Policies.

Enforces zero-mutation, zero-deletion, and zero-overwrite rules on source datasets.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

FORBIDDEN_SOURCE_ACTIONS = [
    "overwrite_source",
    "delete_source",
    "move_source",
    "destructive_clean",
    "auto_impute_overwrite",
    "auto_drop_feature",
    "mutate_input_dataframe",
]

SOURCE_PRESERVATION_RULES = [
    {
        "rule_id": "sp_no_source_overwrite",
        "description": "Never overwrite existing raw or lake artifacts. All outputs write to new dedicated Phase 128 paths.",
        "enforced": True,
    },
    {
        "rule_id": "sp_no_file_deletion",
        "description": "Automated file or row deletion is strictly forbidden.",
        "enforced": True,
    },
    {
        "rule_id": "sp_copy_before_transform",
        "description": "Any DataFrame operation must work on an explicit copy (.copy()), preserving the caller's DataFrame.",
        "enforced": True,
    },
    {
        "rule_id": "sp_no_destructive_imputation",
        "description": "NaN values must not be blindly imputed or overwritten; missingness must be preserved as diagnostics.",
        "enforced": True,
    },
    {
        "rule_id": "sp_no_auto_drop",
        "description": "Low-variance or missing features must never be automatically dropped without researcher manual review.",
        "enforced": True,
    },
]


def validate_regime_rule_free_source_preservation_action(action: str) -> Dict:
    """Validate whether an attempted action violates source preservation."""
    action_clean = action.strip().lower()
    is_forbidden = action_clean in FORBIDDEN_SOURCE_ACTIONS

    return {
        "action": action,
        "is_permitted": not is_forbidden,
        "violation_reason": f"Action '{action}' is strictly forbidden by source preservation policies" if is_forbidden else None,
    }


def build_regime_rule_free_source_preservation_policy_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for source preservation rules."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for r in SOURCE_PRESERVATION_RULES:
        row = r.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_regime_rule_free_source_preservation_policies(df)
    return df, summary


def summarize_regime_rule_free_source_preservation_policies(df: pd.DataFrame) -> Dict:
    """Summarize source preservation rules."""
    total = len(df)
    all_enforced = bool(df["enforced"].all()) if not df.empty else True

    return {
        "total_source_preservation_rules": total,
        "all_rules_enforced": all_enforced,
        "forbidden_actions_count": len(FORBIDDEN_SOURCE_ACTIONS),
        "preservation_status": "SECURE" if all_enforced else "UNSAFE",
    }
