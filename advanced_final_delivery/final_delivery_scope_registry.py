# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Scope Registry.

Defines in-scope and out-of-scope boundaries for Phase 160 Full Advanced Bot Final Delivery.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_DELIVERY_SCOPE_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

SCOPE_ITEMS = [
    ("local_offline_final_delivery", "IN_SCOPE", "Yerel ve cevrimdisi nihai teslimat paketi uretimi"),
    ("final_manifest_creation", "IN_SCOPE", "160 fazi kapsayan nihai sistem manifestosu olusturma"),
    ("final_system_summary_report", "IN_SCOPE", "160 fazlik gelistirme ozet raporu uretimi"),
    ("final_package_contract_registry", "IN_SCOPE", "Final paket teslimat sozlesmelerinin tescili"),
    ("final_operator_handover_report", "IN_SCOPE", "Guvenli kullanim ve operator teslim raporu uretimi"),
    ("final_manual_review_summary", "IN_SCOPE", "Insan onay kapisi ve manuel inceleme gereksinimleri ozeti"),
    ("final_safety_summary_report", "IN_SCOPE", "Sistem geneli sifir-canli sifir-broker emniyet ozeti"),
    ("160_phase_plan_closure", "IN_SCOPE", "160 fazlik planin yonetisim ve sozlesme duzeyinde resmi kapanisi"),
    ("live_trading_execution", "OUT_OF_SCOPE", "Canli emir iletimi, borsa ve gercek alim-satim islemleri"),
    ("broker_integration", "OUT_OF_SCOPE", "Gercek broker API baglantisi ve emir iletim altyapisi"),
    ("investment_advice_generation", "OUT_OF_SCOPE", "Yatirim tavsiyesi, kesin AL/SAT veya yonlu sinyal uretimi"),
    ("real_system_execution", "OUT_OF_SCOPE", "Gercek end-to-end bot calistirmasi veya model egitimi/tahmini"),
    ("backtest_optimizer_execution", "OUT_OF_SCOPE", "Gercek backtest, portfoy optimizasyonu ve risk calistirmasi"),
    ("production_deployment", "OUT_OF_SCOPE", "Uretim ortamina dagitim, resmi onay veya model registry yazimi"),
    ("web_scraping_and_credentials", "OUT_OF_SCOPE", "Web kazima, kimlik bilgisi yazdirma veya kaynak dosya ezme"),
]


def build_final_delivery_scope_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the final delivery scope registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for item_name, scope_type, desc in SCOPE_ITEMS:
        rows.append({
            "scope_item": item_name,
            "scope_type": scope_type,
            "description": desc,
            "is_in_scope": (scope_type == "IN_SCOPE"),
            "current_phase": active_profile.current_phase,
            "target_final_phase": active_profile.target_final_phase,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_DELIVERY_SCOPE_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "current_phase": active_profile.current_phase,
        "scope_item_count": len(rows),
        "in_scope_count": int((df["scope_type"] == "IN_SCOPE").sum()),
        "out_of_scope_count": int((df["scope_type"] == "OUT_OF_SCOPE").sum()),
        "all_out_of_scope_blocked": True,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
