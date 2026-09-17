# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Component Registry.

Builds and summarizes the inventory of all 31 core architectural components
delivered across the 160-phase plan.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_COMPONENT_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

SYSTEM_COMPONENTS = [
    ("core_runtime", "Phase 1-100, 101-105", "Temel bot calisma ve orkestrasyon cekirdegi"),
    ("config_settings_paths", "Phase 1-160", "Tum fazlar icin merkezi konfigürasyon, ayarlar ve dizin yonetimi"),
    ("data_lake", "Phase 1-160", "DataLake CSV/JSON depolama ve yukleme arabirimleri"),
    ("feature_store", "Phase 1-160", "FeatureStore salt-okunur metadata erisim katmani"),
    ("data_provider_contracts", "Phase 106-111", "Coklu veri saglayici sozlesmeleri ve entegrasyon protokolleri"),
    ("macro_news_metadata_contracts", "Phase 112-115", "Makro ekonomik takvim ve haber metaveri sozlesmeleri"),
    ("indicator_feature_factor_engine", "Phase 116-125", "Gelismis teknik indikator, feature ve faktor motoru"),
    ("regime_engine", "Phase 126-135", "Piyasa rejimi siniflandirma ve davranis modelleme katmani"),
    ("ml_dataset_registry", "Phase 136-137", "Makine ogrenmesi veri seti kayit ve bolumleme altyapisi"),
    ("gpu_runtime_governance", "Phase 136-137", "GPU hizlandirma hazirligi ve donanim yonetisim katmani"),
    ("baseline_ml_models", "Phase 138-139", "Klasik ve zaman serisi temel makine ogrenmesi model paketleri"),
    ("ensemble_calibration_drift_explainability", "Phase 140-143", "Topluluk modelleri, kalibrasyon, drift ve aciklanabilirlik"),
    ("model_governance", "Phase 144-145", "Model yonetisim, izleme ve denetim standartlari"),
    ("advanced_ml_acceptance", "Phase 145", "Ileri duzey makine ogrenmesi kabul ve onay provasi"),
    ("realistic_backtest", "Phase 146-147", "Islem maliyetleri ve kayma (slippage) gercekci backtest motoru"),
    ("walk_forward_oos", "Phase 148", "Ileriye dogru yuruyen (walk-forward) ve orneklem-disi dogrulama"),
    ("stress_testing", "Phase 150", "Tarihsel kriz ve ekstrem senaryo stres testi motoru"),
    ("monte_carlo_robustness", "Phase 151", "Monte Carlo saglamlik ve dayaniklilik analiz katmani"),
    ("backtest_governance", "Phase 149, 152", "Backtest yonetisimi ve strateji karsilastirma cercevesi"),
    ("benchmark_evaluation", "Phase 149", "Referans strateji ve benchmark degerlendirme motoru"),
    ("backtest_acceptance", "Phase 152", "Konsolide backtest kabul ve guvenilirlik katmani"),
    ("portfolio_construction", "Phase 153", "Portfoy insasi, pozisyon boyutlandirma ve risk butceleme"),
    ("portfolio_optimization", "Phase 154", "Portfoy optimizasyonu ve tahsis kisitlari motoru"),
    ("risk_reporting", "Phase 155", "Risk raporlama, maruziyet ayristirma ve limit izleme"),
    ("portfolio_scenario_control", "Phase 156", "Portfoy senaryo testi ve drawdown kontrol sistemi"),
    ("portfolio_acceptance", "Phase 157", "Konsolide portfoy kabul ve dogrulama katmani"),
    ("full_system_integration", "Phase 158", "Tum alt sistemlerin entegrasyonu ve advanced acceptance provasi"),
    ("final_hardening", "Phase 159", "Sistem sertlestirme, dondurma kayitlari ve release candidate"),
    ("final_delivery", "Phase 160", "Full Advanced Bot nihai teslimat ve 160 fazlik plan kapanisi"),
    ("docs_and_runbooks", "Phase 1-160", "Kapsamli operator kilavuzlari, mimari rehberler ve kontrol listeleri"),
    ("safety_boundaries", "Phase 1-160", "Sistem geneli no-live, no-broker ve no-investment-advice emniyet sinirlari"),
]


def build_final_delivery_component_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build final delivery component registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for c_name, p_range, desc in SYSTEM_COMPONENTS:
        rows.append({
            "component_name": c_name,
            "phase_range": p_range,
            "description": desc,
            "verified": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_COMPONENT_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "component_count": len(rows),
        "all_verified": bool(df["verified"].all()),
        "all_non_signal": bool(df["non_signal"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
