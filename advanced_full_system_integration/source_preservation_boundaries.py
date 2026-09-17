# -*- coding: utf-8 -*-
"""Phase 158: Source Preservation Boundaries.

Enforces raw data preservation, immutability, and blocks destructive data operations.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

SOURCE_RULES = [
    ("SPR-001", "source_preservation", "no_source_overwrite", "storage", False, "Overwriting original raw source files is prohibited."),
    ("SPR-002", "source_preservation", "no_auto_destructive_cleaning", "pipeline", False, "Destructive row/column cleaning without backup is prohibited."),
    ("SPR-003", "source_preservation", "no_auto_imputation", "pipeline", False, "Blind auto-imputation altering raw distributions is prohibited."),
    ("SPR-004", "source_preservation", "immutable_audit_lake", "storage", True, "Raw data in DataLake is strictly append-only and immutable."),
]


def build_source_preservation_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build source preservation boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in SOURCE_RULES:
        item = SystemBoundaryItem(
            boundary_id=bid,
            boundary_type=btype,
            rule_name=rname,
            action_type=atype,
            is_allowed=is_allowed,
            reason=reason,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "prohibited_actions_count": int((df["is_allowed"] == False).sum()),
        "allowed_actions_count": int((df["is_allowed"] == True).sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
