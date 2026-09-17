# -*- coding: utf-8 -*-
"""Phase 144: Governance Owner Responsibility Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

OWNER_ITEMS: List[Dict[str, str]] = [
    {"role": "Model Governance Architect", "responsibility": "Define and maintain governance contracts, model card schemas, and boundary policies.", "status": "ASSIGNED"},
    {"role": "ML Safety Reviewer", "responsibility": "Audit manual review gates, forbidden column policies, and leakage guards.", "status": "ASSIGNED"},
    {"role": "Validation Engineer", "responsibility": "Verify evidence packs, dependency inputs, and readiness scoring reports.", "status": "ASSIGNED"},
]


def build_governance_owner_responsibility_placeholder_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for owner responsibility placeholders."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in OWNER_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["is_placeholder"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_owner_responsibility_placeholders(df)
    return df, summary


def summarize_governance_owner_responsibility_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize owner responsibility placeholders."""
    return {
        "total_owner_roles": len(df),
        "all_assigned": bool((df["status"] == "ASSIGNED").all()),
        "status": "RESPONSIBILITY_MAP_READY",
    }
