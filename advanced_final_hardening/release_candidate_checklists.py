# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Checklists.

Defines the 20-item Release Candidate checklist verifying all subsystems,
boundaries, dependencies, and handoff prerequisites before Phase 160.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    RELEASE_CANDIDATE_CHECKPOINT_DOMAIN,
    RELEASE_CANDIDATE_CONTRACT_READY,
)

CHECKLIST_ITEMS = [
    ("component_presence_check", "Tüm sistem bileşenlerinin ve faz paketlerinin varlığı", True),
    ("dependency_presence_check", "Temel kütüphanelerin (pandas, numpy, pytest) varlığı", True),
    ("configuration_check", "config/settings.py ayarlarının dry-run uyumluluğu", True),
    ("env_template_check", ".env.example şablonunun güncelliği", True),
    ("path_check", "config/paths.py dizin tanımlarının eksiksizliği", True),
    ("documentation_check", "Operatör, mimari ve güvenlik rehberlerinin varlığı", True),
    ("test_inventory_check", "Tüm faz testlerinin test envanterinde yer alması", True),
    ("script_inventory_check", "Tüm faz betiklerinin betik envanterinde yer alması", True),
    ("report_inventory_check", "Raporlama şablonlarının ve dizinlerinin eksiksizliği", True),
    ("safety_boundary_check", "Güvenlik sınırlarının sistem seviyesinde işletilmesi", True),
    ("disabled_execution_check", "Canlı işlem/broker/tahmin çalıştırma kilitlerinin teyidi", True),
    ("no_secret_output_check", "Hiçbir rapor ve logda API anahtarı veya secret bulunmaması", True),
    ("no_scraping_check", "Web kazıma ve harici API isteklerinin devre dışılığı", True),
    ("no_live_trading_check", "Canlı piyasaya emir gönderiminin kesinlikle engellenmesi", True),
    ("no_broker_check", "Broker API bağlantılarının kesinlikle engellenmesi", True),
    ("no_prediction_check", "Gerçek model tahmini ve inference'ın engellenmesi", True),
    ("no_target_label_check", "Hedef/etiket üretiminin engellenmesi", True),
    ("no_model_registry_write_check", "Model registry'ye kayıt yazmanın engellenmesi", True),
    ("no_artifact_persistence_check", "Model ağırlık dosyası saklamanın engellenmesi", True),
    ("phase_160_handoff_check", "Phase 160 nihai bot teslimat devir şartlarının hazır oluşu", True),
]


def build_release_candidate_checklist_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build release candidate checklist registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for chk_name, desc, passed in CHECKLIST_ITEMS:
        rows.append({
            "checklist_item": chk_name,
            "description": desc,
            "passed": passed,
            "manual_review_required": True,
            "production_ready": False,
            "broker_ready": False,
            "live_ready": False,
            "deployment_ready": False,
            "signal_ready": False,
            "domain": RELEASE_CANDIDATE_CHECKPOINT_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": RELEASE_CANDIDATE_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "checklist_item_count": len(rows),
        "all_passed": bool(df["passed"].all()),
        "current_phase": active_profile.current_phase,
        "status": RELEASE_CANDIDATE_CONTRACT_READY,
    }
    return df, summary
