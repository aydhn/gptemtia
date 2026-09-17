# -*- coding: utf-8 -*-
"""Phase 160: Full-System Block Summary.

Builds and summarizes the completion status of the Full-System Closing Block (Phases 158-160).
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_PHASE_SUMMARY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

SYSTEM_CLOSING_COMPONENTS = [
    ("full_system_integration", "Phase 158", "Tum alt sistemlerin entegrasyonu ve kabul provasi"),
    ("final_hardening_and_release_candidate", "Phase 159", "Sistem sertlestirme, runbook protokolleri ve release candidate"),
    ("full_advanced_bot_final_delivery", "Phase 160", "Nihai teslimat paketi, final manifest ve 160 faz kapanisi"),
]


def build_final_delivery_full_system_block_summary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build full-system block summary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for c_name, p_range, desc in SYSTEM_CLOSING_COMPONENTS:
        rows.append({
            "component_name": c_name,
            "phase_range": p_range,
            "description": desc,
            "completed": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_PHASE_SUMMARY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "full_system_block": "Phase 158-160",
        "component_count": len(rows),
        "all_completed": bool(df["completed"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
