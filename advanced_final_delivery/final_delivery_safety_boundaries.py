# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Safety Boundaries Registry.

Builds and summarizes the comprehensive safety boundary rules for the final delivery package.
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

SAFETY_RULES = [
    ("strict_local_offline_enforcement", "Tum operasyonlar yerel diskte ve cevrimdisi ortamda gerceklesir"),
    ("strict_dry_run_enforcement", "Tum komutlar dry-run kipinde calisir ve canli etki uretmez"),
    ("strict_no_live_trading_enforcement", "Canli emir gonderimi ve borsa erisimi kesinlikle engellenmistir"),
    ("strict_no_broker_enforcement", "Broker API baglantisi ve yetkilendirmesi engellenmistir"),
    ("strict_no_investment_advice_enforcement", "Hicbir cikti yatirim tavsiyesi veya trade sinyali degildir"),
    ("strict_non_production_enforcement", "Sistem uretim ortamina dagitilamaz"),
    ("strict_manual_review_enforcement", "Kararlar ve aksiyonlar insan onay kapilarindan gecmek zorundadir"),
    ("strict_source_preservation_enforcement", "Kaynak dosyalar asla ezilemez veya silinemez"),
]


def build_final_delivery_safety_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build safety boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in SAFETY_RULES:
        rows.append({
            "safety_rule": r_name,
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
        "safety_rule_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
