# -*- coding: utf-8 -*-
"""Phase 159: Operator Config Check Runbook Contracts."""

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

CONFIG_CHECK_STEPS = [
    ("check_default_profile", "Varsayılan profilin balanced_local_final_hardening_contracts olduğunun kontrolü"),
    ("check_dry_run_flag", "final_hardening_dry_run_default değerinin True olduğunun kontrolü"),
    ("check_no_live_trading", "Tüm allow_live_trading bayraklarının False olduğunun teyidi"),
    ("check_no_broker", "Tüm allow_broker_integration bayraklarının False olduğunun teyidi"),
    ("check_env_template", ".env.example dosyasının güncel anahtarlarla örtüştüğünün kontrolü"),
]


def build_operator_config_check_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator config check runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for step_id, desc in CONFIG_CHECK_STEPS:
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
