# -*- coding: utf-8 -*-
"""Phase 159: Operator Maintenance Placeholders.

Defines placeholder definitions for scheduled offline maintenance routines.
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

MAINTENANCE_TASKS = [
    ("MAINT-01", "disk_space_audit", "DataLake ve reports çıktı dizinleri boyut kontrolü", "Weekly"),
    ("MAINT-02", "test_suite_regression", "Tam pytest test takımının koşulması", "Bi-weekly"),
    ("MAINT-03", "documentation_sync", "Kod ve doküman senkronizasyonunun incelenmesi", "Monthly"),
]


def build_operator_maintenance_placeholder_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build maintenance placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for m_id, task, desc, freq in MAINTENANCE_TASKS:
        rows.append({
            "task_id": m_id,
            "task_name": task,
            "description": desc,
            "frequency": freq,
            "requires_system_downtime": False,
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
        "maintenance_task_count": len(rows),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
