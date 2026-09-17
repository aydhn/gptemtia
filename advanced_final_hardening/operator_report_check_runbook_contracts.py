# -*- coding: utf-8 -*-
"""Phase 159: Operator Report Check Runbook Contracts."""

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

REPORT_CHECK_STEPS = [
    ("check_disclaimer_presence", "Tüm üretilen raporlarda zorunlu yasal/araştırma feragatnamesinin kontrolü"),
    ("check_no_signal_claims", "Raporlarda kesin AL/SAT veya yatırım tavsiyesi yer almadığının kontrolü"),
    ("check_report_formats", "Markdown (.md) ve text (.txt) formatlarının eşzamanlı üretildiğinin teyidi"),
    ("check_reports_dir_structure", "reports/output/advanced_final_hardening alt dizinlerinin kontrolü"),
]


def build_operator_report_check_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator report check runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for step_id, desc in REPORT_CHECK_STEPS:
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
