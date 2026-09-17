# -*- coding: utf-8 -*-
"""Phase 159: Final Dependency Freeze Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    DEPENDENCY_FREEZE_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

DEPENDENCY_FREEZE_ITEMS = [
    ("python_runtime_freeze", "Python 3.12+", "Python ana çalışma zamanı sürümü dondurulması"),
    ("pandas_freeze", "pandas", "Veri manipülasyon kütüphanesi dondurulması"),
    ("numpy_freeze", "numpy", "Sayısal hesaplama kütüphanesi dondurulması"),
    ("pytest_freeze", "pytest", "Test çalıştırma altyapısı dondurulması"),
    ("offline_stdlib_freeze", "standard_library", "Standart kütüphane ve yerel offline çalışma gereksinimleri"),
]


def build_final_dependency_freeze_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build dependency freeze contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for freeze_name, scope, desc in DEPENDENCY_FREEZE_ITEMS:
        rows.append({
            "freeze_name": freeze_name,
            "freeze_category": "dependency",
            "target_scope": scope,
            "description": desc,
            "frozen": True,
            "actual_lock_enacted": False,
            "modifications_allowed_without_review": False,
            "domain": DEPENDENCY_FREEZE_DOMAIN,
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
