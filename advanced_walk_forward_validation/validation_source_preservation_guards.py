# -*- coding: utf-8 -*-
"""Phase 147: Validation Source Preservation Guards.

Guards preventing source overwrite, file deletion, and destructive transformations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

FORBIDDEN_ACTIONS = [
    "overwrite",
    "delete",
    "drop",
    "destructive_cleaning",
    "auto_impute",
    "auto_feature_drop",
]


def build_validation_source_preservation_guard_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for source preservation guards."""
    rows = [
        {
            "guard_name": "source_immutability_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Ham verinin ve DataLake kaynaklarinin degistirilmesini engelleyen muhafiz.",
            "non_signal": True,
        },
        {
            "guard_name": "no_destructive_cleaning_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Otomatik deger doldurma (imputation) ve kolon silmeyi engelleyen muhafiz.",
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_guards": len(df),
        "all_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_validation_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate action against source preservation policy."""
    act_lower = action.lower().strip()
    is_blocked = any(f in act_lower for f in FORBIDDEN_ACTIONS)
    return {
        "action": action,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "message": f"Eylem engellendi: {action}" if is_blocked else "Eylem guvenli",
        "non_signal": True,
    }
