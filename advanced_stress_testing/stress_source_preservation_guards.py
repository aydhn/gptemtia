# -*- coding: utf-8 -*-
"""Phase 148: Stress Source Preservation Guards.

Enforces source data immutability during stress scenario testing.
Strictly blocks destructive cleaning, in-place overwrites, auto-imputation, and file deletion.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem

PROHIBITED_ACTIONS = [
    "overwrite",
    "source_overwrite",
    "auto_impute",
    "auto_imputation",
    "auto_feature_drop",
    "drop_columns",
    "delete_file",
    "destructive_clean",
]


def build_stress_source_preservation_guard_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of source preservation guards."""
    guard = StressGuardItem(
        guard_name="stress_source_preservation_guard",
        guard_type="SOURCE_PRESERVATION",
        description="Kaynak verilerin üzerine yazılmasını, otomatik imputasyonu veya dosya silinmesini engeller.",
        enforcement_level="STRICT",
        active=True,
    )
    rows = [
        {
            "guard_name": guard.guard_name,
            "guard_type": guard.guard_type,
            "description": guard.description,
            "enforcement_level": guard.enforcement_level,
            "active": guard.active,
            "non_signal": True,
            "local_only": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "guard_active": guard.active,
        "enforcement_level": guard.enforcement_level,
        "non_signal": True,
    }
    return df, summary


def validate_stress_source_preservation_action(action: str) -> Dict[str, Any]:
    """Inspect an action name to guarantee no destructive modification occurs."""
    act_norm = action.lower().strip()
    is_violating = any(p in act_norm for p in PROHIBITED_ACTIONS)
    return {
        "action": action,
        "is_safe": not is_violating,
        "action_taken": "BLOCKED" if is_violating else "PASSED",
        "non_signal": True,
    }
