# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Gap Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    GAP_DOMAIN,
    ACCEPTANCE_READY_WITH_WARNINGS,
)

GAP_TYPES = [
    "optional_doc_missing",
    "optional_generated_report_missing",
    "manual_review_note_missing",
    "dependency_summary_incomplete",
    "acceptance_score_warning",
    "handoff_detail_incomplete",
]

DEFAULT_GAPS: List[Dict[str, Any]] = [
    {
        "gap_id": "GAP-01",
        "gap_type": "manual_review_note_missing",
        "phase_ref": "Phase 136-144",
        "severity": "INFO",
        "description": "Manual review items are registered as pending human operator inspection.",
        "resolved": False,
    },
    {
        "gap_id": "GAP-02",
        "gap_type": "optional_generated_report_missing",
        "phase_ref": "Phase 145",
        "severity": "INFO",
        "description": "Historical live run logs absent by design due to offline research boundaries.",
        "resolved": True,
    },
]


def build_advanced_ml_gap_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for non-critical gap registry."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for g in DEFAULT_GAPS:
        row = dict(g)
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY_WITH_WARNINGS
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": GAP_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_gaps": len(df),
        "unresolved_gaps": int((~df["resolved"]).sum()),
        "non_signal": True,
        "status": "TRACKED",
    }
    return df, summary


def summarize_advanced_ml_gaps(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize gaps DataFrame."""
    return {
        "gap_count": len(df),
        "unresolved_count": int((~df["resolved"]).sum()) if not df.empty and "resolved" in df.columns else 0,
        "non_signal": True,
    }
