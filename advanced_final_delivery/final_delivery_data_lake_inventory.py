# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery DataLake Inventory.

Builds metadata inventory of DataLake namespaces and artifact paths.
Does not delete, move, or modify any files.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_INVENTORY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

DATA_LAKE_NAMESPACES = [
    ("advanced_final_delivery", "Phase 160", "Nihai teslimat tescilleri, envanterleri, manifestosu ve kapanis kayitlari"),
    ("advanced_final_hardening", "Phase 159", "Sistem dondurma sozlesmeleri, release candidate ve runbook kayitlari"),
    ("advanced_full_system_integration", "Phase 158", "Sistem entegrasyonu ve kabul provasi kayitlari"),
    ("advanced_portfolio_acceptance", "Phase 157", "Portfoy kabul tescilleri ve kontrol noktalari"),
    ("advanced_portfolio_scenario_control", "Phase 156", "Portfoy senaryo ve drawdown kontrol kayitlari"),
    ("advanced_risk_reporting", "Phase 155", "Risk raporlama ve maruziyet tescilleri"),
    ("advanced_portfolio_optimization", "Phase 154", "Portfoy optimizasyon ve tahsis kayitlari"),
    ("advanced_portfolio_construction", "Phase 153", "Portfoy insa ve pozisyon boyutlandirma kayitlari"),
    ("advanced_backtest_acceptance", "Phase 152", "Backtest kabul tescilleri ve guvenilirlik raporlari"),
    ("advanced_monte_carlo_robustness", "Phase 151", "Monte Carlo simulasyon ve saglamlik tescilleri"),
    ("advanced_stress_testing", "Phase 150", "Stres testi senaryo ve sonuc tescilleri"),
    ("advanced_benchmark_evaluation", "Phase 149", "Strateji karsilastirma ve benchmark tescilleri"),
    ("advanced_walk_forward_validation", "Phase 148", "Walk-forward pencere ve OOS tescilleri"),
    ("advanced_realistic_backtest", "Phase 146-147", "Islem maliyetleri ve kayma tescilleri"),
    ("advanced_ml_acceptance", "Phase 145", "ML kabul ve onay provasi tescilleri"),
]


def build_final_delivery_data_lake_inventory_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataLake inventory DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for ns_name, p_range, desc in DATA_LAKE_NAMESPACES:
        rows.append({
            "namespace": ns_name,
            "phase_range": p_range,
            "description": desc,
            "storage_formats": "CSV, JSON",
            "source_preserved": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_INVENTORY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "namespace_count": len(rows),
        "source_preserved": True,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
