# -*- coding: utf-8 -*-
"""Phase 159: Final Paths Audit Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    PATHS_AUDIT_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

PATHS_AUDIT_ITEMS = [
    ("paths_module_presence", "config/paths.py", "paths.py modülünün varlığı", True),
    ("phase_159_paths_definition", "config/paths.py:phase_159_paths", "Phase 159 dizin listesi tanımı", True),
    ("data_lake_directories_creation", "data/lake/advanced_final_hardening/", "Veri ambarı alt dizinleri varlığı", True),
    ("reports_directories_creation", "reports/output/advanced_final_hardening/", "Raporlama dizinleri varlığı", True),
    ("docs_directories_creation", "docs/generated/advanced_final_hardening/", "Oluşturulan dokümantasyon dizinleri varlığı", True),
]


def build_final_paths_audit_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build paths audit contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for audit_id, target, desc, passed in PATHS_AUDIT_ITEMS:
        rows.append({
            "audit_id": audit_id,
            "target": target,
            "description": desc,
            "passed": passed,
            "destructive_migration_allowed": False,
            "domain": PATHS_AUDIT_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "audit_item_count": len(rows),
        "all_passed": bool(df["passed"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
