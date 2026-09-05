"""Phase 127: Regime Matrix Source Preservation Policies.

Enforces non-destructive handling of all input data and prohibits destructive mutative actions.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

FORBIDDEN_ACTIONS: List[str] = [
    "overwrite_source",
    "delete_source",
    "move_source",
    "destructive_clean",
    "auto_impute_overwrite",
    "auto_drop_feature",
    "mutate_input_dataframe",
]

SOURCE_PRESERVATION_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "spp_no_source_overwrite",
        "name": "Zero Source Overwrite",
        "description": "Never overwrite existing files in upstream data lakes or raw directories.",
        "is_enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "spp_no_destructive_cleaning",
        "name": "Zero Destructive Cleaning",
        "description": "Never purge rows or drop columns silently; quarantine via manual review queue.",
        "is_enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "spp_no_synthetic_imputation",
        "name": "Zero Auto-Imputation",
        "description": "Missing values must remain explicit NaNs or flagged with indicators rather than synthesized.",
        "is_enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "spp_immutable_input_copies",
        "name": "Immutable Input DataFrame Protection",
        "description": "All transform functions must create df.copy() before processing.",
        "is_enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "spp_non_destructive_feature_quarantine",
        "name": "Non-Destructive Feature Quarantine",
        "description": "Anomalous or degraded features must be isolated via manual review queue, never deleted.",
        "is_enforced": True,
        "non_signal": True,
    },
]


def build_regime_matrix_source_preservation_policy_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the source preservation policy registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for pol in SOURCE_PRESERVATION_POLICIES:
        p_copy = pol.copy()
        p_copy["current_phase"] = p.current_phase
        p_copy["target_final_phase"] = p.target_final_phase
        p_copy["next_phase"] = p.next_phase
        p_copy["source_preserved"] = True
        p_copy["status"] = "matrix_ready"
        rows.append(p_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_source_preservation_policies(df)
    return df, summary


def validate_regime_matrix_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate whether an action violates non-destructive source preservation policies."""
    act_clean = action.strip().lower()
    is_forbidden = act_clean in FORBIDDEN_ACTIONS or any(fb in act_clean for fb in ["delete", "overwrite", "drop", "impute"])

    return {
        "action": action,
        "is_allowed": not is_forbidden,
        "is_forbidden": is_forbidden,
        "forbidden_actions_list": FORBIDDEN_ACTIONS,
        "source_preserved": not is_forbidden,
    }


def summarize_regime_matrix_source_preservation_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation policies."""
    return {
        "total_policies": len(df),
        "policy_ids": df["policy_id"].tolist() if not df.empty else [],
        "forbidden_actions_count": len(FORBIDDEN_ACTIONS),
        "all_enforced": bool(df["is_enforced"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_source_preservation_policies = build_regime_matrix_source_preservation_policy_registry


def is_forbidden_preservation_action(action: str) -> bool:
    """Return True if action violates non-destructive source preservation."""
    res = validate_regime_matrix_source_preservation_action(action)
    return res["is_forbidden"]


def assert_action_allowed_for_source(action: str) -> None:
    """Raise PermissionError if action violates non-destructive source preservation."""
    if is_forbidden_preservation_action(action):
        raise PermissionError(f"Action '{action}' is strictly forbidden by source preservation policy.")

