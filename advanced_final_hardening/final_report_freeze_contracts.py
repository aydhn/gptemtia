# -*- coding: utf-8 -*-
"""Phase 159: Final Report Freeze Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    REPORT_FREEZE_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

REPORT_FREEZE_ITEMS = [
    ("report_builder_contract_freeze", "reports/report_builder.py", "Tüm text ve markdown raporlayıcı şablonları dondurması"),
    ("output_formats_freeze", "reports/output/*/csv,markdown,txt,json", "Raporlama çıktı formatları dondurması"),
    ("disclaimer_standards_freeze", "all_phase_disclaimers", "Zorunlu feragatname ve non-signal uyarı standartları dondurması"),
]


def build_final_report_freeze_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build report freeze contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for freeze_name, scope, desc in REPORT_FREEZE_ITEMS:
        rows.append({
            "freeze_name": freeze_name,
            "freeze_category": "reporting",
            "target_scope": scope,
            "description": desc,
            "frozen": True,
            "actual_lock_enacted": False,
            "modifications_allowed_without_review": False,
            "domain": REPORT_FREEZE_DOMAIN,
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
