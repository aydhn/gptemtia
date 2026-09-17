# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Gap Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    GAP_DOMAIN,
    ACCEPTANCE_READY,
)
from advanced_backtest_acceptance.backtest_acceptance_models import (
    BacktestAcceptanceFinding,
)

GAP_TYPES: List[str] = [
    "optional_doc_missing",
    "optional_generated_report_missing",
    "manual_review_note_missing",
    "dependency_summary_incomplete",
    "acceptance_score_warning",
    "handoff_detail_incomplete",
]


def create_backtest_acceptance_gap(
    gap_type: str,
    phase_ref: str,
    severity_label: str,
    message: str,
    recommendation: str,
) -> BacktestAcceptanceFinding:
    """Factory function for creating gap findings."""
    return BacktestAcceptanceFinding(
        finding_id=f"GAP-{abs(hash(message)) % 100000:05d}",
        finding_type=gap_type,
        phase_ref=phase_ref,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=True,
        non_signal=True,
    )


def build_backtest_acceptance_gap_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for registered gaps (default: 0 gaps)."""
    active = profile or get_backtest_acceptance_profile()

    records: List[Dict[str, Any]] = []

    columns = [
        "finding_id", "finding_type", "phase_ref", "severity_label",
        "message", "recommendation", "current_phase", "target_final_phase",
        "next_phase", "manual_review_required", "status", "non_signal"
    ]
    df = pd.DataFrame(records, columns=columns)
    summary: Dict[str, Any] = {
        "domain": GAP_DOMAIN,
        "active_profile": active.profile_name,
        "total_gaps": len(records),
        "has_gaps": len(records) > 0,
        "supported_gap_types": GAP_TYPES,
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
