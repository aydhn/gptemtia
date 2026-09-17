# -*- coding: utf-8 -*-
"""Phase 159: Operator Manual Review Protocols."""

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

MANUAL_REVIEWS = [
    ("config_review", "Konfigürasyon dondurma insan doğrulaması"),
    ("safety_review", "Güvenlik sınırları ve no-go teyidi"),
    ("readiness_score_review", "Hazır oluş skoru ve bulguların gözden geçirilmesi"),
    ("manifest_review", "Release candidate manifest onay incelemesi"),
    ("handoff_review", "Phase 160 devir şartlarının eksiksizliğinin incelenmesi"),
]


def build_operator_manual_review_protocol_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator manual review protocol registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for rev_id, desc in MANUAL_REVIEWS:
        rows.append({
            "review_id": rev_id,
            "title": rev_id.replace("_", " ").title(),
            "description": desc,
            "mandatory": True,
            "auto_approval_allowed": False,
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
        "review_count": len(rows),
        "all_mandatory": bool(df["mandatory"].all()),
        "no_auto_approval": bool((~df["auto_approval_allowed"]).all()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
