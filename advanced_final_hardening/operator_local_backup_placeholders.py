# -*- coding: utf-8 -*-
"""Phase 159: Operator Local Backup Placeholders.

Defines placeholder contracts for local artifact backups.
Metadata and contract only; does not perform filesystem copies or overwrites.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    OPERATOR_PROTOCOL_DOMAIN,
    OPERATOR_RUNBOOK_CONTRACT_READY,
)

BACKUP_TARGETS = [
    ("BACKUP-01", "reports_output", "reports/output/", "Yerel araştırma raporları arşivleme hedefi"),
    ("BACKUP-02", "data_lake_manifests", "data/lake/*/manifest/", "Tüm faz manifest ve devir kayıtları hedefi"),
    ("BACKUP-03", "docs_generated", "docs/generated/", "Üretilen dokümantasyon dosyaları hedefi"),
]


def build_operator_local_backup_placeholder_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build local backup placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for b_id, name, path, desc in BACKUP_TARGETS:
        rows.append({
            "backup_id": b_id,
            "backup_target": name,
            "source_path": path,
            "description": desc,
            "actual_copy_executed": False,
            "overwrite_allowed": False,
            "domain": OPERATOR_PROTOCOL_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": OPERATOR_RUNBOOK_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "backup_target_count": len(rows),
        "actual_copy_executed": bool(df["actual_copy_executed"].any()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
