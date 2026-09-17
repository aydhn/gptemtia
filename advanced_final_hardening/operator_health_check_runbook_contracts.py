# -*- coding: utf-8 -*-
"""Phase 159: Operator Health Check Runbook Contracts."""

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

HEALTH_CHECK_STEPS = [
    ("check_all_phase_modules", "Phases 1-158 modüllerinin bozulmadan import edilebildiğinin doğrulanması"),
    ("check_phase_159_modules", "advanced_final_hardening paketinin import edilebilirliğinin kontrolü"),
    ("check_pipeline_dry_run", "FinalHardeningPipeline nesnesinin dry-run modunda sorunsuz başlatılabilmesi"),
    ("check_data_lake_write_read", "DataLake okuma/yazma döngüsünün test dizininde sorunsuz çalıştığının teyidi"),
]


def build_operator_health_check_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator health check runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for step_id, desc in HEALTH_CHECK_STEPS:
        rows.append({
            "step_id": step_id,
            "step_name": step_id.replace("_", " ").title(),
            "description": desc,
            "requires_manual_inspection": True,
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
