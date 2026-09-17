# -*- coding: utf-8 -*-
"""Phase 160: Phase 101-160 Advanced Summary.

Builds and summarizes the completion status of the Advanced development block (Phases 101-160).
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

ADVANCED_MILESTONES = [
    ("Core Runtime Consolidation", "Phase 101-105", "Gelismis calisma zamani ve motor konsolidasyonu"),
    ("Data Providers, Macro & News Metadata", "Phase 106-115", "Coklu veri saglayici ve haber metaveri altyapisi"),
    ("Advanced Feature & Factor Engine", "Phase 116-125", "Momentum, volatilite, mean reversion faktorleri ve kalite denetimi"),
    ("Advanced Regime Engine", "Phase 126-135", "Volatilite, trend, likidite, makro ve capraz varlik rejim modellemesi"),
    ("Advanced ML Pipeline & Governance", "Phase 136-145", "GPU altyapisi, temel modeller, ensemble, drift, kalibrasyon ve ML kabul"),
    ("Realistic Backtest & Robustness", "Phase 146-152", "Kayma maliyetleri, walk-forward, stres testi, Monte Carlo ve backtest kabul"),
    ("Portfolio & Risk Architecture", "Phase 153-157", "Portfoy insasi, optimizasyon, risk raporlama, senaryo kontrol ve portfoy kabul"),
    ("Full-System Integration & Hardening", "Phase 158-159", "Sistem geneli entegrasyon provasi, sertlestirme ve release candidate"),
    ("Final Delivery & Plan Closure", "Phase 160", "Nihai teslimat, manifesto ve 160 fazlik plan resmi kapanisi"),
]


def build_final_delivery_phase_101_160_advanced_summary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build Phase 101-160 Advanced summary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for m_name, p_range, desc in ADVANCED_MILESTONES:
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
        "advanced_block": "Phase 101-160",
        "milestone_count": len(rows),
        "all_completed": bool(df["completed"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
