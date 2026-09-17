# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Operator Handover Registry.

Builds and summarizes the operator handover protocols and operational boundaries
for Phase 160 Full Advanced Bot Final Delivery.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_OPERATOR_HANDOVER_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

HANDOVER_ITEMS = [
    ("local_offline_usage_only", "Sistem yalnizca yerel ve cevrimdisi arastirma amaclidir"),
    ("dry_run_default_enforced", "Tum calistirmalar dry-run modunda gerceklestirilmelidir"),
    ("no_live_trading_enforced", "Canli emir gonderimi, canli borsa erisimi kesinlikle yasaktir"),
    ("no_broker_integration_enforced", "Gercek broker API baglantisi engellenmistir"),
    ("no_investment_advice_enforced", "Ciktilar kesinlikle yatirim tavsiyesi veya trade sinyali degildir"),
    ("no_production_deployment_enforced", "Sistem uretim ortamina dagitilamaz veya canliya alinamaz"),
    ("manual_review_required_enforced", "Herhangi bir karar oncesi insan incelemesi zorunludur"),
    ("validation_reports_must_be_reviewed", "Tum dogrulama raporlari ve bulgulari incelenmelidir"),
    ("safety_boundaries_remain_active", "Guvenlik sinirlari hicbir kosulda devre disi birakilamaz"),
    ("contract_acceptance_package_only", "Bu teslimat yalnizca sozlesme, dokumantasyon ve kabul paketidir"),
]


def build_final_delivery_operator_handover_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator handover DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for h_name, desc in HANDOVER_ITEMS:
        rows.append({
            "handover_rule": h_name,
            "description": desc,
            "enforced": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_OPERATOR_HANDOVER_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "handover_item_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "notice": "Final delivery is contract/documentation/acceptance package only; live trading and broker integration are strictly prohibited.",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
