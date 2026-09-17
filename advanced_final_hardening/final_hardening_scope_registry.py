# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Scope Registry.

Defines the allowed and restricted scope for Phase 159 Final Hardening.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    FINAL_HARDENING_SCOPE_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

SCOPE_DEFINITIONS = [
    ("final_hardening_contracts", "ALLOWED", "Final hardening sözleşme tanımları ve metaveri üretimi"),
    ("operator_runbook_contracts", "ALLOWED", "Operatör prosedürleri ve kılavuz sözleşmeleri"),
    ("release_candidate_contracts", "ALLOWED", "Release candidate kontrol listeleri ve sözleşme katmanı"),
    ("freeze_audits", "ALLOWED", "Konfigürasyon, dokümantasyon, güvenlik, doğrulama ve bağımlılık dondurma denetimleri"),
    ("system_inventories", "ALLOWED", "Script, test, doküman, rapor, veri ambarı ve sistem bileşenleri envanterleri"),
    ("safety_boundaries", "ALLOWED", "No-go ve safe-go sınırlarının sistem seviyesinde işletilmesi"),
    ("phase_160_handoff", "ALLOWED", "Phase 160 Full Advanced Bot Final Delivery devir sözleşmesi"),
    ("live_trading", "BLOCKED", "Canlı piyasada emir iletimi veya işlem açma"),
    ("broker_integration", "BLOCKED", "Broker API bağlantısı veya hesap yönetimi"),
    ("signal_generation", "BLOCKED", "Kesin AL/SAT veya yönlü trade sinyali üretimi"),
    ("investment_advice", "BLOCKED", "Yatırım tavsiyesi veya portföy yönlendirmesi"),
    ("system_execution", "BLOCKED", "Gerçek full-system veya end-to-end bot çalıştırma"),
    ("model_inference", "BLOCKED", "Gerçek model eğitme, fit etme veya tahmin yürütme"),
    ("backtest_optimizer_execution", "BLOCKED", "Gerçek backtest veya portföy optimizasyonu çalıştırma"),
    ("production_deployment", "BLOCKED", "Gerçek ortama veya release sunucusuna deploy etme"),
    ("model_registry_write", "BLOCKED", "Model registry'ye yazma veya model artifact persist etme"),
    ("data_destructive_ops", "BLOCKED", "Dosya silme, kaynak veri ezme, otomatik temizleme"),
]


def build_final_hardening_scope_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build scope registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for item, permission, desc in SCOPE_DEFINITIONS:
        rows.append({
            "scope_item": item,
            "permission": permission,
            "description": desc,
            "domain": FINAL_HARDENING_SCOPE_DOMAIN,
            "current_phase": active_profile.current_phase,
            "target_final_phase": active_profile.target_final_phase,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "scope_item_count": len(rows),
        "allowed_count": int((df["permission"] == "ALLOWED").sum()),
        "blocked_count": int((df["permission"] == "BLOCKED").sum()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
