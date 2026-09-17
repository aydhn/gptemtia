# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Phase Map.

Builds and summarizes the comprehensive 160-phase block mapping across all development phases.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_PHASE_MAP_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

PHASE_BLOCKS = [
    ("Block 1: MVP Core Build", "Phase 1-100", "Yerel/cevrimdisi MVP cekirdek, veri, feature, indikator, rapor, dogrulama ve dry-run sinirlari"),
    ("Block 2: Runtime Consolidation", "Phase 101-105", "MVP sonrasi cekirdek calisma zamani ve motor konsolidasyonu"),
    ("Block 3: Data Providers & Quality", "Phase 106-115", "Web kazima olmadan coklu veri saglayici, makro/haber metaverisi ve veri kalitesi"),
    ("Block 4: Indicator & Factor Engine", "Phase 116-125", "Gelismis teknik indikator, feature ve faktor motoru"),
    ("Block 5: Regime Engine", "Phase 126-135", "Piyasa rejimi siniflandirma, gecis teshisi ve davranis modelleme sozlesmeleri"),
    ("Block 6: Advanced ML & Governance", "Phase 136-145", "GPU, ML veri seti, temel modeller, ensemble, kalibrasyon, drift, aciklanabilirlik ve ML kabul"),
    ("Block 7: Realistic Backtest & Governance", "Phase 146-152", "Gercekci backtest, islem maliyetleri, kayma, walk-forward, stres testi, Monte Carlo ve backtest kabul"),
    ("Block 8: Portfolio & Risk Management", "Phase 153-157", "Portfoy insasi, pozisyon boyutlandirma, optimizasyon, risk raporlama, senaryo kontrol ve portfoy kabul"),
    ("Block 9: Final System Integration & Delivery", "Phase 158-160", "Sistem genelinde entegrasyon, kabul provasi, final hardening, release candidate ve final teslimat"),
]


def build_final_delivery_phase_map_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build phase map DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for b_name, p_range, desc in PHASE_BLOCKS:
        rows.append({
            "block_name": b_name,
            "phase_range": p_range,
            "description": desc,
            "completed": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_PHASE_MAP_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_blocks": len(rows),
        "total_phases": 160,
        "all_completed": bool(df["completed"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
