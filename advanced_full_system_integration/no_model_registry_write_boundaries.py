# -*- coding: utf-8 -*-
"""Phase 158: No Model Registry Write Boundaries.

Enforces read-only access to ML models and prohibits saving new models to the registry.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

MODEL_REGISTRY_RULES = [
    ("NMR-001", "model_registry_boundary", "no_model_weights_save", "storage", False, "Saving trained model weights or checkpoints is prohibited."),
    ("NMR-002", "model_registry_boundary", "no_model_registration_mutation", "registry", False, "Mutating model registry records is prohibited."),
    ("NMR-003", "model_registry_boundary", "read_only_model_catalog", "catalog", True, "Model registry catalog is read-only metadata."),
]


def build_no_model_registry_write_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-model-registry-write boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in MODEL_REGISTRY_RULES:
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
