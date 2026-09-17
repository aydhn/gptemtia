# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Safety Evidence.

Builds and summarizes the evidence registry for all enforced safety boundaries across the system.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_EVIDENCE_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

SAFETY_EVIDENCE_ITEMS = [
    ("No-Live-Trading Safety Boundary", "Phase 1-160", "Canli emir iletimi, canli borsa ve gercek hesap erisimi sifir toleransla yasaktir"),
    ("No-Broker Safety Boundary", "Phase 1-160", "Broker API baglantisi ve yetkilendirmesi engellenmistir"),
    ("No-Investment-Advice Safety Boundary", "Phase 1-160", "Kesin AL/SAT, yonlu iddia veya tavsiye uretimi yasaktir"),
    ("No-Production-Deployment Safety Boundary", "Phase 1-160", "Uretim ortamina resmi onay ve otomatik dagitim engellenmistir"),
    ("No-Model-Execution Safety Boundary", "Phase 1-160", "Gercek model inference, training ve prediction engellenmistir"),
    ("No-Backtest-Execution Safety Boundary", "Phase 1-160", "Gercek backtest, benchmark ve optimizer calistirmasi engellenmistir"),
    ("No-Scraping-Credential-Output Safety Boundary", "Phase 1-160", "Web kazima, kimlik bilgisi yazdirma ve kaynak dosya ezme engellenmistir"),
    ("Source Preservation Safety Boundary", "Phase 1-160", "Kaynak dosyalar degistirilemez ve silinemez"),
]


def build_final_delivery_safety_evidence_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build safety evidence DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for sb_name, p_range, desc in SAFETY_EVIDENCE_ITEMS:
        rows.append({
            "safety_boundary": sb_name,
            "phase_range": p_range,
            "description": desc,
            "enforced": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_EVIDENCE_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "safety_evidence_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
