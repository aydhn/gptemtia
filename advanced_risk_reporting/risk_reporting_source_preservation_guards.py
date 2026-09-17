# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Source Preservation Guards."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingGuardItem


def build_risk_reporting_source_preservation_guard_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for source preservation guards."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingGuardItem(
            guard_name="source_preservation_guard",
            domain="preservation_guard",
            guard_rule="Prohibits overwriting raw lake data, auto-deleting files, or destructive cleaning",
            is_active=True,
            action_on_violation="BLOCK",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"guard_count": len(df), "all_active": True}


def validate_risk_reporting_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate that action does not alter or destroy source data."""
    destructive = [
        "overwrite",
        "delete",
        "drop_source",
        "purge",
        "destructive_clean",
        "truncate_table",
    ]
    blocked = any(d in action.lower() for d in destructive)
    return {
        "is_blocked": blocked,
        "is_safe": not blocked,
        "action": "BLOCK" if blocked else "ALLOW",
        "reason": "Destructive source action strictly prohibited" if blocked else "No violation",
    }
