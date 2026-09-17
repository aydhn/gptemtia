# -*- coding: utf-8 -*-
"""Phase 160: Portfolio Block Summary.

Builds and summarizes the completion status of the Portfolio and Risk Block (Phases 153-157).
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

PORTFOLIO_COMPONENTS = [
    ("portfolio_construction_engine", "Phase 153", "Portfoy insasi, pozisyon boyutlandirma ve risk butceleme"),
    ("portfolio_optimization_engine", "Phase 154", "Kisitli optimizasyon ve tahsis motoru"),
    ("risk_reporting_engine", "Phase 155", "Risk raporlama, maruziyet ayristirma ve limit izleme"),
    ("portfolio_scenario_control_engine", "Phase 156", "Portfoy senaryo testi ve drawdown kontrol sistemi"),
    ("portfolio_acceptance_layer", "Phase 157", "Konsolide portfoy kabul ve dogrulama tescili"),
]


def build_final_delivery_portfolio_block_summary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build portfolio block summary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for c_name, p_range, desc in PORTFOLIO_COMPONENTS:
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
        "portfolio_block": "Phase 153-157",
        "component_count": len(rows),
        "all_completed": bool(df["completed"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
