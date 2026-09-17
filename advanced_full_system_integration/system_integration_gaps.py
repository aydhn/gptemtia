# -*- coding: utf-8 -*-
"""Phase 158: System Integration Gaps Registry.

Tracks non-blocking architectural gaps or documentation refinements.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_system_integration_gap_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system integration gap registry DataFrame and summary."""
    gap_catalog = [
        {"gap_id": "GAP-158-001", "gap_type": "optional_doc_missing", "severity": "LOW", "is_open": False, "description": "Optional operational guides for third-party extensions."},
        {"gap_id": "gap-158-002", "gap_type": "optional_report_missing", "severity": "LOW", "is_open": False, "description": "Optional secondary visualization reports."},
        {"gap_id": "gap-158-003", "gap_type": "manual_review_note_missing", "severity": "MEDIUM", "is_open": False, "description": "Human review notes pending operator signoff."},
        {"gap_id": "gap-158-004", "gap_type": "runbook_detail_incomplete", "severity": "MEDIUM", "is_open": False, "description": "Detailed operator runbook sections deferred to Phase 159."},
        {"gap_id": "gap-158-005", "gap_type": "dependency_summary_incomplete", "severity": "LOW", "is_open": False, "description": "Extended dependency edge annotations."},
        {"gap_id": "gap-158-006", "gap_type": "integration_rehearsal_note_missing", "severity": "LOW", "is_open": False, "description": "Rehearsal execution timing benchmarks."},
        {"gap_id": "gap-158-007", "gap_type": "final_hardening_prerequisite_note_missing", "severity": "MEDIUM", "is_open": False, "description": "Pre-hardening checklist items for Phase 159."},
    ]
    df = pd.DataFrame(gap_catalog)
    summary = {
        "active_profile": profile.profile_name,
        "total_monitored_gaps": len(df),
        "open_gaps_count": int((df["is_open"] == True).sum()),
        "has_open_gaps": bool((df["is_open"] == True).any()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
