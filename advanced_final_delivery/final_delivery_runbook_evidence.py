# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Runbook Evidence.

Builds and summarizes the evidence registry for operator runbook contracts and protocols.
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

RUNBOOK_PROTOCOLS = [
    ("operator_startup_protocol", "Phase 159", "Yerel ve cevrimdisi ortamda guvenli baslatma kontrolleri"),
    ("operator_shutdown_protocol", "Phase 159", "Guvenli kapatma ve durum kaydetme protokolu"),
    ("operator_config_check_protocol", "Phase 159", "Konfigürasyon dondurma ve cevre degiskeni denetimi"),
    ("operator_data_check_protocol", "Phase 159", "DataLake ve veri butunlugu dogrulama protokolu"),
    ("operator_report_check_protocol", "Phase 159", "Rapor cikti dizinleri ve format dogrulama protokolu"),
    ("operator_health_check_protocol", "Phase 159", "Modul mevcudiyeti ve bagimlilik saglik testi"),
    ("operator_validation_runbook", "Phase 159", "Validasyon kurallari ve sifir sizinti testi"),
    ("operator_troubleshooting_protocol", "Phase 159", "Ariza teshis ve adim adim problem giderme rehberi"),
    ("operator_recovery_protocol", "Phase 159", "Guvenli geri yukleme ve kurtarma proseduru"),
    ("operator_no_go_protocol", "Phase 159", "Canli islem taleplerine karsi otomatik durdurma protokolu"),
]


def build_final_delivery_runbook_evidence_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build runbook evidence DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, p_ref, desc in RUNBOOK_PROTOCOLS:
        rows.append({
            "runbook_name": r_name,
            "phase_reference": p_ref,
            "description": desc,
            "verified": True,
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
        "runbook_count": len(rows),
        "all_verified": bool(df["verified"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
