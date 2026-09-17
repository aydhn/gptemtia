# -*- coding: utf-8 -*-
"""Phase 159: Operator Startup Runbook Contracts."""

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

STARTUP_STEPS = [
    ("step_1_env_check", "Sistem ortam değişkenlerinin ve Python 3.12+ çalışma zamanının kontrolü"),
    ("step_2_settings_verification", "config/settings.py ayarlarının dry-run ve local-only olduğunun teyidi"),
    ("step_3_paths_verification", "Dizinlerin (data/lake, reports/output, docs/generated) mevcut olduğunun kontrolü"),
    ("step_4_health_check_run", "python -m scripts.run_final_hardening_health_check çalıştırması"),
    ("step_5_no_live_trading_confirmation", "Canlı işlem bayraklarının kapalı (False) olduğunun teyidi"),
]


def build_operator_startup_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator startup runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for step_id, desc in STARTUP_STEPS:
        rows.append({
            "step_id": step_id,
            "step_name": step_id.replace("_", " ").title(),
            "description": desc,
            "requires_manual_inspection": True,
            "actual_bot_execution_allowed": False,
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
        "no_bot_execution": bool((~df["actual_bot_execution_allowed"]).all()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
