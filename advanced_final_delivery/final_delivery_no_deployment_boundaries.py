# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery No-Deployment Boundaries.

Prohibits production and release deployments, registry writes, and official readiness claims.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_BOUNDARY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

NO_DEPLOYMENT_RULES = [
    ("zero_production_deployments", "Uretim sunucularina veya bulut ortamlarina dagitim yasaktir"),
    ("zero_model_registry_writes", "Model kayit defterine (registry) model yazimi yasaktir"),
    ("zero_artifact_persistence", "Model binary veya artifact persist edilmesi yasaktir"),
    ("zero_official_approval_claims", "Sistem icin 'resmi onay' veya 'live ready' iddiasinda bulunulamaz"),
]


def build_final_delivery_no_deployment_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build no deployment boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in NO_DEPLOYMENT_RULES:
        rows.append({
            "rule_name": r_name,
            "description": desc,
            "enforced": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_BOUNDARY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "rule_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
