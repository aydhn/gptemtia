# -*- coding: utf-8 -*-
"""Phase 144: Model Card Limitations Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

LIMITATION_ITEMS: List[Dict[str, str]] = [
    {
        "limitation_id": "LIM-001",
        "category": "dry_run_contract_only",
        "description": "Models are registered as interface contracts without weights, checkpoints, or persistence.",
        "impact": "No inference or real evaluation possible from this contract.",
    },
    {
        "limitation_id": "LIM-002",
        "category": "non_signal_guarantee",
        "description": "Outputs contain zero directional market signals, position sizing, or trading recommendations.",
        "impact": "Must never be consumed by execution or order routing layers.",
    },
    {
        "limitation_id": "LIM-003",
        "category": "offline_research_scope",
        "description": "Contracts are scoped exclusively for offline research and governance simulation.",
        "impact": "Real-time streaming feeds or order books are completely unsupported.",
    },
    {
        "limitation_id": "LIM-004",
        "category": "no_production_readiness",
        "description": "Model card presence does NOT confer production readiness or official compliance sign-off.",
        "impact": "Cannot be used as justification for live deployment.",
    },
    {
        "limitation_id": "LIM-005",
        "category": "metadata_only_news",
        "description": "Textual information is constrained to schema metadata and timestamps with zero raw article body text.",
        "impact": "Natural language sentiment or LLM embeddings are intentionally unavailable.",
    },
    {
        "limitation_id": "LIM-006",
        "category": "no_lookahead_enforced",
        "description": "Time indices and joins are strictly point-in-time and forbid future data or shift(-1).",
        "impact": "Backtest overfitting or future leakage is structurally prevented.",
    },
]


def build_model_card_limitation_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card limitations."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in LIMITATION_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["is_enforced"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_limitations(df)
    return df, summary


def summarize_model_card_limitations(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card limitations."""
    return {
        "total_limitations": len(df),
        "all_enforced": bool(df["is_enforced"].all()),
        "non_signal_enforced": bool(df["non_signal"].all()),
    }
