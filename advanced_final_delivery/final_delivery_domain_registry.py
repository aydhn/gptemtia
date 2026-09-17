# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Domain Registry.

Builds and summarizes the operational and validation domains for Phase 160.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_DELIVERY_DOMAIN,
    FINAL_DELIVERY_PROFILE_DOMAIN,
    FINAL_DELIVERY_SCOPE_DOMAIN,
    FINAL_PACKAGE_DOMAIN,
    FINAL_COMPONENT_DOMAIN,
    FINAL_INVENTORY_DOMAIN,
    FINAL_EVIDENCE_DOMAIN,
    FINAL_PHASE_MAP_DOMAIN,
    FINAL_PHASE_SUMMARY_DOMAIN,
    FINAL_OPERATOR_HANDOVER_DOMAIN,
    FINAL_BOUNDARY_DOMAIN,
    FINAL_DISABLED_EXECUTION_DOMAIN,
    FINAL_BLOCKER_DOMAIN,
    FINAL_GAP_DOMAIN,
    FINAL_WARNING_DOMAIN,
    FINAL_FINDING_DOMAIN,
    FINAL_READINESS_SCORE_DOMAIN,
    FINAL_MANIFEST_DOMAIN,
    FINAL_HEALTH_DOMAIN,
    FINAL_VALIDATION_DOMAIN,
    FINAL_SAFETY_DOMAIN,
    FINAL_COMPLETION_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

DOMAINS = [
    (FINAL_DELIVERY_PROFILE_DOMAIN, "Final delivery profil ve calisma kipi yonetimi"),
    (FINAL_DELIVERY_DOMAIN, "Final delivery genel kapsami"),
    (FINAL_DELIVERY_SCOPE_DOMAIN, "Final delivery kapsam ve sinir kayitlari"),
    (FINAL_PACKAGE_DOMAIN, "Nihai teslimat paket sozlesmeleri ve kontratlari"),
    (FINAL_COMPONENT_DOMAIN, "160 fazlik tum bilesenler envanter tescili"),
    (FINAL_INVENTORY_DOMAIN, "Modul, script, test, doc, rapor, DataLake ve FeatureStore envanterleri"),
    (FINAL_EVIDENCE_DOMAIN, "Faz kabul, manifesto, dogrulama ve guvenlik kanitlari tescili"),
    (FINAL_PHASE_MAP_DOMAIN, "160 fazlik plan faz haritasi ve blok siniflandirmasi"),
    (FINAL_PHASE_SUMMARY_DOMAIN, "Phase 1-100 MVP, Phase 101-160 Advanced ve blok ozetleri"),
    (FINAL_OPERATOR_HANDOVER_DOMAIN, "Operator devir teslim protokolu ve calistirma sinirlari"),
    (FINAL_BOUNDARY_DOMAIN, "No-go, go, emniyet ve uretim-disi guvenlik sinirlari"),
    (FINAL_DISABLED_EXECUTION_DOMAIN, "Devre disi birakilmis sistem/canli/broker/egitim calistirma raporlari"),
    (FINAL_BLOCKER_DOMAIN, "Kritik final teslimat engelleri denetimi"),
    (FINAL_GAP_DOMAIN, "Opsiyonel final teslimat bosluklari denetimi"),
    (FINAL_WARNING_DOMAIN, "Final teslimat uyarilari denetimi"),
    (FINAL_FINDING_DOMAIN, "Konsolide bulgular ve manuel inceleme gereksinimleri"),
    (FINAL_READINESS_SCORE_DOMAIN, "Final teslimat eksiksizlik hazirlik skoru"),
    (FINAL_MANIFEST_DOMAIN, "Full Advanced Bot Final Delivery ana manifestosu"),
    (FINAL_HEALTH_DOMAIN, "Sistem bilesenleri saglik kontrolu"),
    (FINAL_VALIDATION_DOMAIN, "Final teslimat kural dogrulama raporu"),
    (FINAL_SAFETY_DOMAIN, "Sistem genelinde katı guvenlik siniri"),
    (FINAL_COMPLETION_DOMAIN, "160 fazlik plan resmi kapanis tescili"),
]


def build_final_delivery_domain_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the final delivery domain registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for d_name, desc in DOMAINS:
        rows.append({
            "domain_name": d_name,
            "description": desc,
            "current_phase": active_profile.current_phase,
            "target_final_phase": active_profile.target_final_phase,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_DELIVERY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "current_phase": active_profile.current_phase,
        "domain_count": len(rows),
        "domains": df["domain_name"].tolist(),
        "all_non_signal": bool(df["non_signal"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
