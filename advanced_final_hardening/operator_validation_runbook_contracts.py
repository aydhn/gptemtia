# -*- coding: utf-8 -*-
"""Phase 159: Operator Validation Runbook Contracts."""

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

VALIDATION_STEPS = [
    ("run_pytest_suite", "pytest komutu ile tüm testlerin başarıyla geçtiğinin teyidi"),
    ("validate_no_forbidden_claims", "Metin ve rapor çıktılarında yasaklı iddiaların taranması ve doğrulanması"),
    ("validate_release_candidate_readiness", "Readiness score'un eşik değer üzerinde olduğunun doğrulanması"),
    ("validate_manifest_flags", "Manifest dosyasındaki tüm güvenlik ve non-execution bayraklarının doğrulanması"),
]


def build_operator_validation_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator validation runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for step_id, desc in VALIDATION_STEPS:
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
