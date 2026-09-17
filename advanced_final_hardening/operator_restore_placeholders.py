# -*- coding: utf-8 -*-
"""Phase 159: Operator Restore Placeholders.

Defines restore placeholder contracts.
Contract and documentation only; strictly blocks destructive restore or overwrite.
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

RESTORE_POLICIES = [
    ("RESTORE-01", "dry_run_reconstruction", "Kayıp metaverileri pipeline dry-run ile sıfırdan oluşturma"),
    ("RESTORE-02", "no_source_overwrite", "Geri yükleme esnasında mevcut kaynak kodların veya verilerin asla ezilmemesi"),
    ("RESTORE-03", "manual_operator_signoff", "Herhangi bir geri yükleme öncesi insan onayının zorunlu kılınması"),
]


def build_operator_restore_placeholder_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build restore placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for r_id, name, desc in RESTORE_POLICIES:
        rows.append({
            "restore_id": r_id,
            "policy_name": name,
            "description": desc,
            "destructive_restore_allowed": False,
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
        "restore_policy_count": len(rows),
        "destructive_restore_allowed": bool(df["destructive_restore_allowed"].any()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
