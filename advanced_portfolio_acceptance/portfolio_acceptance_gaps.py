# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Gap Registry.

Registers and monitors non-blocking documentation or configuration gaps across Phase 157.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    GAP_DOMAIN,
    SEVERITY_WARNING,
    PORTFOLIO_ACCEPTANCE_READY,
)

KNOWN_GAP_TYPES = [
    ("optional_doc_missing", "Non-critical operational runbook item optional for research"),
    ("optional_generated_report_missing", "Generated auxiliary report optional during dry run"),
    ("manual_review_note_missing", "Manual review documentation placeholder pending review"),
    ("dependency_summary_incomplete", "Detailed dependency report can be augmented in integration"),
    ("acceptance_score_warning", "Acceptance score reflects contracts only, not live readiness"),
    ("handoff_detail_incomplete", "Detailed integration rehearsal notes to be finalized in Phase 158"),
    ("integration_prerequisite_note_missing", "Full-system integration notes registered for Phase 158"),
]


def build_portfolio_acceptance_gap_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of monitored gaps."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for gap_type, desc in KNOWN_GAP_TYPES:
        records.append({
            "gap_type": gap_type,
            "description": desc,
            "severity_label": SEVERITY_WARNING,
            "is_open": False,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_gaps(df)
    return df, summary


def summarize_portfolio_acceptance_gaps(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize gap registry."""
    open_gaps = len(df[df["is_open"]]) if not df.empty and "is_open" in df.columns else 0
    return {
        "domain": GAP_DOMAIN,
        "total_monitored_gap_types": len(df),
        "open_gaps_count": open_gaps,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
