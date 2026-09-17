# -*- coding: utf-8 -*-
"""Phase 144: Model Card Feature Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FEATURE_DEPENDENCY_ITEMS: List[Dict[str, str]] = [
    {"feat_id": "FDEP-01", "name": "technical_feature_catalog", "phase_ref": "Phase 116-125", "role": "Momentum, volatility, and trend technical indicator space."},
    {"feat_id": "FDEP-02", "name": "macro_calendar_feature_catalog", "phase_ref": "Phase 120", "role": "Macro surprise and event release timestamps."},
    {"feat_id": "FDEP-03", "name": "regime_feature_store_catalog", "phase_ref": "Phase 134", "role": "Rule-free market state and behavior diagnostic vectors."},
]


def build_model_card_feature_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card feature dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in FEATURE_DEPENDENCY_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["status"] = "SATISFIED"
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_feature_dependencies(df)
    return df, summary


def summarize_model_card_feature_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card feature dependencies."""
    return {
        "total_feature_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
