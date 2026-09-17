# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Source Preservation Guards.

Enforces immutability of raw and upstream data sources. Strictly prohibits
overwriting, deleting, destructive cleaning, auto-imputation, or auto-dropping features.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

DESTRUCTIVE_ACTIONS = [
    "overwrite", "delete", "remove", "drop", "purge", "auto_impute",
    "auto_drop", "destructive_clean", "truncate", "modify_in_place",
]

SOURCE_PRESERVATION_GUARDS = [
    {"guard_id": "guard_no_source_overwrite", "scope": "storage_integrity", "enforced": True, "description": "Strictly prohibits modifying or overwriting source files"},
    {"guard_id": "guard_no_file_deletion", "scope": "storage_integrity", "enforced": True, "description": "Strictly prohibits deleting data lake or catalog files"},
    {"guard_id": "guard_no_auto_imputation", "scope": "data_quality", "enforced": True, "description": "Prohibits automated filling of missing values without explicit audit"},
    {"guard_id": "guard_no_auto_feature_drop", "scope": "feature_governance", "enforced": True, "description": "Prohibits automated dropping of features during ingestion"},
]


def build_baseline_model_source_preservation_guard_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build source preservation guards registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for g in SOURCE_PRESERVATION_GUARDS:
        rows.append({
            "guard_id": g["guard_id"],
            "scope": g["scope"],
            "enforced": g["enforced"],
            "description": g["description"],
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_source_preservation_guards(df)
    return df, summary


def validate_baseline_model_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate requested action against destructive operations."""
    act_lower = action.lower()
    is_destructive = any(d in act_lower for d in DESTRUCTIVE_ACTIONS)

    return {
        "valid": not is_destructive,
        "action": action,
        "status": "ACTION_PERMITTED_NON_DESTRUCTIVE" if not is_destructive else "DESTRUCTIVE_ACTION_PROHIBITED",
        "non_signal": True,
    }


def summarize_baseline_model_source_preservation_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation guards."""
    return {
        "total_guards": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
