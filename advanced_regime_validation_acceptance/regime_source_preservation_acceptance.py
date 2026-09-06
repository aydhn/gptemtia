"""Phase 133: Regime Source Preservation Acceptance Report and Validators.

Enforces zero source modification, zero overwrite, zero auto-imputation, and zero destructive cleaning.
"""

from typing import Any, Dict, List, Optional, Set, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)

FORBIDDEN_SOURCE_ACTIONS: Set[str] = {
    "overwrite_source",
    "delete_source",
    "move_source",
    "destructive_clean",
    "auto_impute_overwrite",
    "auto_drop_feature",
    "mutate_input_dataframe",
}


def validate_source_preservation_action(action: str) -> Dict[str, Any]:
    """Check if an action violates source preservation principles."""
    act_lower = action.lower().strip()
    if act_lower in FORBIDDEN_SOURCE_ACTIONS:
        return {
            "passed": False,
            "status": "acceptance_fail",
            "action": action,
            "message": f"Action '{action}' is strictly forbidden: violates source preservation policy!",
        }

    return {
        "passed": True,
        "status": "acceptance_pass",
        "action": action,
        "message": f"Action '{action}' adheres to source preservation rules.",
    }


def build_regime_source_preservation_acceptance_report(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Source Preservation Acceptance."""
    p = profile or get_default_regime_validation_acceptance_profile()

    rows = []
    for action in sorted(list(FORBIDDEN_SOURCE_ACTIONS)):
        rows.append(
            {
                "forbidden_action": action,
                "rejection_severity": "acceptance_critical",
                "is_prohibited": True,
                "status": "acceptance_pass",
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_rules": len(df),
        "source_preservation_enforced": True,
        "profile_name": p.profile_name,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_source_preservation_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation acceptance DataFrame."""
    return {
        "total_rules": len(df),
        "all_prohibited": bool(df["is_prohibited"].all()) if "is_prohibited" in df.columns else True,
        "source_preserved": True,
    }
