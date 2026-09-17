# -*- coding: utf-8 -*-
"""Phase 159: Operator Recovery Runbook Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    RECOVERY_DOMAIN,
    OPERATOR_RUNBOOK_CONTRACT_READY,
)

RECOVERY_PROCEDURES = [
    ("safe_reinit", "Güvenli Yeniden Başlatma", "Python sürecini kapatıp `python -m scripts.run_final_hardening_health_check` ile yeniden başlatın.", False),
    ("manifest_rebuild", "Manifest Yeniden Oluşturma", "Tüm registry'leri pipeline üzerinden save=True ile yeniden oluşturun; kaynak veriye dokunulmaz.", False),
    ("docs_rebuild", "Dokümantasyon Yeniden Derleme", "Dokümantasyon çıktılarını betikler üzerinden yeniden üretin.", False),
]


def build_operator_recovery_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator recovery runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for proc_id, title, steps, destructive in RECOVERY_PROCEDURES:
        rows.append({
            "procedure_id": proc_id,
            "title": title,
            "steps": steps,
            "destructive": destructive,
            "domain": RECOVERY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": OPERATOR_RUNBOOK_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "procedure_count": len(rows),
        "all_non_destructive": bool((~df["destructive"]).all()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
