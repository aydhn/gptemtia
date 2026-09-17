# -*- coding: utf-8 -*-
"""Phase 158: No Artifact Persistence Boundaries.

Prohibits persisting binary models, neural network weights, or unapproved artifacts.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

ARTIFACT_RULES = [
    ("NAP-001", "artifact_boundary", "no_binary_model_pickle", "storage", False, "Serializing binary model objects is prohibited."),
    ("NAP-002", "artifact_boundary", "no_onnx_export", "storage", False, "Exporting ONNX models is prohibited."),
    ("NAP-003", "artifact_boundary", "allow_metadata_reporting", "reporting", True, "Persisting metadata reports in Markdown, TXT, JSON, and CSV is allowed."),
]


def build_no_artifact_persistence_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-artifact-persistence boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in ARTIFACT_RULES:
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
