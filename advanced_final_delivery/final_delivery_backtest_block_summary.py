# -*- coding: utf-8 -*-
"""Phase 160: Backtest Block Summary.

Builds and summarizes the completion status of the Realistic Backtest Block (Phases 146-152).
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

BACKTEST_COMPONENTS = [
    ("realistic_backtest_engine", "Phase 146-147", "Islem maliyetleri ve kayma (slippage) gercekci backtest motoru"),
    ("walk_forward_oos_validation", "Phase 148", "Pencere kaydirma ve orneklem disi (OOS) dogrulama"),
    ("benchmark_evaluation_framework", "Phase 149", "Strateji karsilastirma ve referans benchmark cercevesi"),
    ("stress_testing_engine", "Phase 150", "Tarihsel kriz senaryolari ve sok simulasyonlari"),
    ("monte_carlo_robustness_layer", "Phase 151", "Monte Carlo yol ornekleme ve parametre dayaniklilik analizi"),
    ("backtest_acceptance_layer", "Phase 152", "Konsolide backtest kabul ve guvenilirlik tescili"),
]


def build_final_delivery_backtest_block_summary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build backtest block summary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for c_name, p_range, desc in BACKTEST_COMPONENTS:
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
        "backtest_block": "Phase 146-152",
        "component_count": len(rows),
        "all_completed": bool(df["completed"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
