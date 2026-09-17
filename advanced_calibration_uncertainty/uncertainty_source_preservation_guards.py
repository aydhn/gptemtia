# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Source Preservation Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

DESTRUCTIVE_ACTIONS_UNCERTAINTY = [
    "overwrite",
    "delete",
    "move",
    "destructive_clean",
    "auto_impute",
    "auto_drop",
    "drop_feature",
]


def build_uncertainty_source_preservation_guard_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for uncertainty source preservation guards."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = [
        {
            "guard_id": "uncert_guard_no_overwrite",
            "rule_name": "prohibit_source_file_overwrites",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "guard_id": "uncert_guard_no_destructive_cleaning",
            "rule_name": "prohibit_auto_destructive_cleaning",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
        {
            "guard_id": "uncert_guard_no_auto_drop",
            "rule_name": "prohibit_auto_imputation_and_feature_dropping",
            "blocking": True,
            "is_active": True,
            "non_signal": True,
            "phase": prof.current_phase,
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_uncertainty_source_preservation_guards(df)
    return df, summary


def validate_uncertainty_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate requested action ensuring source data immutability."""
    act_lower = action.lower()
    is_destructive = any(d in act_lower for d in DESTRUCTIVE_ACTIONS_UNCERTAINTY)
    return {
        "action_allowed": not is_destructive,
        "is_blocked": is_destructive,
        "reason": "Destructive action blocked by uncertainty source preservation policy."
        if is_destructive
        else "Safe non-destructive action.",
        "non_signal": True,
    }


def summarize_uncertainty_source_preservation_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty source preservation guards DataFrame."""
    return {
        "total_guards": len(df),
        "guards": df["guard_id"].tolist() if not df.empty else [],
        "all_active": bool(df["is_active"].all()) if not df.empty else True,
        "all_blocking": bool(df["blocking"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
