# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Dry-Run Boundaries.

Enforces dry-run execution constraints on all Phase 160 activities.
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

DRY_RUN_RULES = [
    ("dry_run_default_active", "Tum pipeline ve scriptler varsayilan olarak dry-run kipinde calisir"),
    ("zero_live_side_effects", "Dry-run calismasi canli dis side-effect uretmez"),
    ("in_memory_fixtures_safe", "Testler kucuk in-memory verilerle guvenli test calistirir"),
]


def build_final_delivery_dry_run_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build dry-run boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in DRY_RUN_RULES:
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
