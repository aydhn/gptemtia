# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Non-Production Boundaries.

Enforces non-production restrictions on all Phase 160 deliverables.
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

NON_PRODUCTION_RULES = [
    ("non_production_environment_only", "Sistem yalnizca gelistirme ve arastirma ortaminda calisabilir"),
    ("zero_production_deployments", "Uretim ortamina hicbir kod, model veya artifact yuklenemez"),
    ("zero_production_approvals", "Uretim ortami hazirlik onayi verilemez"),
    ("zero_production_claims", "Sistem icin 'production ready' iddiasinda bulunulamaz"),
]


def build_final_delivery_non_production_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build non-production boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in NON_PRODUCTION_RULES:
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
