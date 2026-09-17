# -*- coding: utf-8 -*-
"""Phase 159: Final Configuration Freeze Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    CONFIGURATION_FREEZE_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

CONFIG_FREEZE_ITEMS = [
    ("core_settings_freeze", "config/settings.py", "Sistem temel ayarları ve emtia/döviz parametreleri dondurulması"),
    ("phase_settings_freeze", "config/settings.py (Phase 1-159)", "Tüm faz konfigürasyon bayraklarının dondurulması"),
    ("safety_settings_freeze", "config/settings.py (Safety flags)", "Sıfır canlı işlem ve güvenlik kilitlerinin dondurulması"),
    ("paths_configuration_freeze", "config/paths.py", "Dizin hiyerarşisi ve veri yolları tanımlarının dondurulması"),
    ("env_template_freeze", ".env.example", "Ortam değişkenleri şablon parametrelerinin dondurulması"),
]


def build_final_configuration_freeze_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build configuration freeze contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for freeze_name, scope, desc in CONFIG_FREEZE_ITEMS:
        rows.append({
            "freeze_name": freeze_name,
            "freeze_category": "configuration",
            "target_scope": scope,
            "description": desc,
            "frozen": True,
            "actual_lock_enacted": False,
            "modifications_allowed_without_review": False,
            "domain": CONFIGURATION_FREEZE_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "freeze_item_count": len(rows),
        "current_phase": active_profile.current_phase,
        "all_frozen": bool(df["frozen"].all()),
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
