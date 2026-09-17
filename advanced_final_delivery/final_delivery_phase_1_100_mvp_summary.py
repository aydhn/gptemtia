# -*- coding: utf-8 -*-
"""Phase 160: Phase 1-100 MVP Summary.

Builds and summarizes the completion status and achievements of the MVP block (Phases 1-100).
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

MVP_MILESTONES = [
    ("Core Architecture & Offline Pipeline", "Phase 1-20", "Temel CLI, offline mimari ve CSV veri akisi"),
    ("Indicator & Strategy Foundations", "Phase 21-40", "Temel teknik indikatorler ve strateji sablonlari"),
    ("Local Paper Trading & Simulator", "Phase 41-60", "Cevrimdisi paper trading ve emir simülasyon mantigi"),
    ("Data Lake & Storage Architecture", "Phase 61-80", "DataLake dizin yapisi ve yerel dosya yonetimi"),
    ("Validation, Reporting & MVP Acceptance", "Phase 81-100", "MVP dogrulama, raporlama ve ilk 100 faz kapanis kabul tescili"),
]


def build_final_delivery_phase_1_100_mvp_summary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build Phase 1-100 MVP summary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for m_name, p_range, desc in MVP_MILESTONES:
        rows.append({
            "milestone_name": m_name,
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
        "mvp_block": "Phase 1-100",
        "milestone_count": len(rows),
        "all_completed": bool(df["completed"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
