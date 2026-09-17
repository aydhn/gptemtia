# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Domain Registry.

Defines all core domains operating in the Final Hardening and Release Candidate phase.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    FINAL_HARDENING_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
    FINAL_HARDENING_PROFILE_DOMAIN,
    FINAL_HARDENING_SCOPE_DOMAIN,
    FINAL_HARDENING_CONTRACT_DOMAIN,
    OPERATOR_RUNBOOK_DOMAIN,
    RELEASE_CANDIDATE_DOMAIN,
    CONFIGURATION_FREEZE_DOMAIN,
    DOCUMENTATION_FREEZE_DOMAIN,
    SAFETY_FREEZE_DOMAIN,
    VALIDATION_FREEZE_DOMAIN,
    DEPENDENCY_FREEZE_DOMAIN,
    MANIFEST_FREEZE_DOMAIN,
    REPORT_FREEZE_DOMAIN,
    SETTINGS_AUDIT_DOMAIN,
    ENV_TEMPLATE_AUDIT_DOMAIN,
    PATHS_AUDIT_DOMAIN,
    INVENTORY_DOMAIN,
    OPERATOR_PROTOCOL_DOMAIN,
    TROUBLESHOOTING_DOMAIN,
    RECOVERY_DOMAIN,
    NO_GO_PROTOCOL_DOMAIN,
    SAFE_USAGE_PROTOCOL_DOMAIN,
    RELEASE_CANDIDATE_CHECKPOINT_DOMAIN,
    RELEASE_CANDIDATE_BOUNDARY_DOMAIN,
    BLOCKER_DOMAIN,
    GAP_DOMAIN,
    WARNING_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_160_HANDOFF_DOMAIN,
)

DOMAINS_LIST = [
    (FINAL_HARDENING_PROFILE_DOMAIN, "Final hardening profilleri ve çalışma modları"),
    (FINAL_HARDENING_DOMAIN, "Genel final hardening ana alanı"),
    (FINAL_HARDENING_SCOPE_DOMAIN, "Final hardening kapsam ve sınır tanımı"),
    (FINAL_HARDENING_CONTRACT_DOMAIN, "Hardening sözleşmeleri ve kural setleri"),
    (OPERATOR_RUNBOOK_DOMAIN, "Operatör kılavuzu ve runbook sözleşmeleri"),
    (RELEASE_CANDIDATE_DOMAIN, "Release candidate sözleşmesi ve kontrolleri"),
    (CONFIGURATION_FREEZE_DOMAIN, "Konfigürasyon dondurma sözleşmesi"),
    (DOCUMENTATION_FREEZE_DOMAIN, "Dokümantasyon dondurma sözleşmesi"),
    (SAFETY_FREEZE_DOMAIN, "Güvenlik sınırları dondurma sözleşmesi"),
    (VALIDATION_FREEZE_DOMAIN, "Doğrulama kuralları dondurma sözleşmesi"),
    (DEPENDENCY_FREEZE_DOMAIN, "Bağımlılık dondurma sözleşmesi"),
    (MANIFEST_FREEZE_DOMAIN, "Manifest dondurma sözleşmesi"),
    (REPORT_FREEZE_DOMAIN, "Raporlama yapısı dondurma sözleşmesi"),
    (SETTINGS_AUDIT_DOMAIN, "Ayarlar (settings.py) denetim sözleşmesi"),
    (ENV_TEMPLATE_AUDIT_DOMAIN, "Ortam şablonu (.env.example) denetimi"),
    (PATHS_AUDIT_DOMAIN, "Dizin yolları (paths.py) denetim sözleşmesi"),
    (INVENTORY_DOMAIN, "Sistem envanterleri genel alanı"),
    (OPERATOR_PROTOCOL_DOMAIN, "Operatör güvenlik ve operasyon protokolleri"),
    (TROUBLESHOOTING_DOMAIN, "Hata teşhis ve sorun giderme protokolleri"),
    (RECOVERY_DOMAIN, "Kurtarma ve yedekleme prosedürleri"),
    (NO_GO_PROTOCOL_DOMAIN, "Operatör NO-GO ve yasaklı eylem protokolleri"),
    (SAFE_USAGE_PROTOCOL_DOMAIN, "Güvenli kullanım sınırları ve kuralları"),
    (RELEASE_CANDIDATE_CHECKPOINT_DOMAIN, "Release candidate kontrol noktaları"),
    (RELEASE_CANDIDATE_BOUNDARY_DOMAIN, "Release candidate güvenlik ve sınır tanımları"),
    (BLOCKER_DOMAIN, "Kritik engelleyiciler kayıt alanı"),
    (GAP_DOMAIN, "Eksiklik ve boşluklar kayıt alanı"),
    (WARNING_DOMAIN, "Uyarılar ve dikkat notları kayıt alanı"),
    (FINDING_DOMAIN, "Bulgular ve tespitler kayıt alanı"),
    (READINESS_SCORE_DOMAIN, "Sözleşme hazır oluş skoru alanı"),
    (MANIFEST_DOMAIN, "Release candidate manifest alanı"),
    (HEALTH_DOMAIN, "Sistem sağlık kontrolü alanı"),
    (VALIDATION_DOMAIN, "Sistem doğrulama kuralları alanı"),
    (SAFETY_DOMAIN, "Güvenlik sınırları ve koruma alanı"),
    (PHASE_160_HANDOFF_DOMAIN, "Phase 160 nihai teslim devir alanı"),
]


def build_final_hardening_domain_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build domain registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for domain_name, desc in DOMAINS_LIST:
        rows.append({
            "domain_name": domain_name,
            "description": desc,
            "current_phase": active_profile.current_phase,
            "target_final_phase": active_profile.target_final_phase,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain_count": len(rows),
        "current_phase": active_profile.current_phase,
        "all_domains_ready": True,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
