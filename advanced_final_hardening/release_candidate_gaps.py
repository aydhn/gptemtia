# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Gaps."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    GAP_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

POTENTIAL_GAPS = [
    ("GAP-01", "optional_doc_missing", "İsteğe bağlı dokümantasyon notu", False),
    ("GAP-02", "optional_report_missing", "İsteğe bağlı ek rapor notu", False),
    ("GAP-03", "runbook_detail_incomplete", "Runbook detay tamamlama notu", False),
    ("GAP-04", "manual_review_note_missing", "Manuel inceleme notu", False),
    ("GAP-05", "final_inventory_incomplete", "Envanter listesi notu", False),
    ("GAP-06", "release_candidate_note_missing", "Release candidate genel notu", False),
    ("GAP-07", "final_delivery_prerequisite_note_missing", "Phase 160 nihai teslim önşart notu", False),
]


def build_release_candidate_gap_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build gap registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for g_id, name, desc, is_open in POTENTIAL_GAPS:
        rows.append({
            "gap_id": g_id,
            "gap_name": name,
            "description": desc,
            "is_open": is_open,
            "domain": GAP_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "gap_count": len(rows),
        "open_gap_count": int(df["is_open"].sum()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
