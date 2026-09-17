# -*- coding: utf-8 -*-
"""Phase 159: Operator Shutdown Runbook Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    OPERATOR_RUNBOOK_DOMAIN,
    OPERATOR_RUNBOOK_CONTRACT_READY,
)

SHUTDOWN_STEPS = [
    ("step_1_verify_no_lingering_tasks", "Arka planda çalışan asenkron veya daemonic görev olmadığının kontrolü"),
    ("step_2_verify_report_flush", "Tüm markdown ve text raporların diske yazıldığının teyidi"),
    ("step_3_data_lake_sync_check", "DataLake CSV ve JSON kayıtlarının bütünlüğünün kontrolü"),
    ("step_4_session_closure", "Yerel operatör araştırma oturumunun güvenli biçimde sonlandırılması"),
]


def build_operator_shutdown_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator shutdown runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for step_id, desc in SHUTDOWN_STEPS:
        rows.append({
            "step_id": step_id,
            "step_name": step_id.replace("_", " ").title(),
            "description": desc,
            "requires_manual_inspection": True,
            "destructive_termination_allowed": False,
            "domain": OPERATOR_RUNBOOK_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": OPERATOR_RUNBOOK_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "step_count": len(rows),
        "all_manual_inspection": bool(df["requires_manual_inspection"].all()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
