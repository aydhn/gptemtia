# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Warnings Registry.

Documents operational and safety warnings accompanying the Phase 160 deliverables.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_WARNING_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    SEVERITY_INFO,
)

SYSTEM_WARNINGS = [
    ("contract_only_final_delivery", "Teslimat yalnizca sozlesme, yonetisim ve kabul duzeyindedir"),
    ("placeholder_only_evidence", "Test kanitlari kucuk sentetik/in-memory fixture kullanir"),
    ("no_real_system_execution", "Gercek sistem ve end-to-end bot calistirilamaz"),
    ("no_live_trading", "Canli emir gonderimi ve borsa erisimi kesinlikle engellenmistir"),
    ("no_broker_execution", "Broker API baglantisi ve emir iletimi engellenmistir"),
    ("no_production_deployment", "Uretim ortamina otomatik dagitim yapilamaz"),
    ("no_release_deployment", "Release candidate paketi canliya dagitilamaz"),
    ("no_model_registry_write", "Model registry'ye model agirligi persist edilemez"),
    ("no_artifact_persistence", "Buyuk model binary dosyasi kaydedilemez"),
    ("no_prediction", "Model inference ve ileriye donuk getiri tahmini uretilemez"),
    ("no_signal_generation", "Trade sinyali veya yonlu oneriler uretilemez"),
    ("manual_review_required", "Tum sonuclar insan incelemesinden gecmek zorundadir"),
    ("final_delivery_must_remain_non_live", "Nihai teslimat her zaman non-live ve yerel kalmalidir"),
]


def build_final_delivery_warning_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build warning registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for idx, (w_type, desc) in enumerate(SYSTEM_WARNINGS, 1):
        rows.append({
            "warning_id": f"WRN-160-{idx:03d}",
            "warning_type": w_type,
            "description": desc,
            "severity": SEVERITY_INFO,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_WARNING_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "warning_count": len(rows),
        "all_severity_info": True,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
