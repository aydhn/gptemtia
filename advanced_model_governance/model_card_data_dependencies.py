# -*- coding: utf-8 -*-
"""Phase 144: Model Card Data Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

DATA_DEPENDENCY_ITEMS: List[Dict[str, str]] = [
    {"dep_id": "DDEP-01", "name": "ml_dataset_contract_source", "phase_ref": "Phase 137", "role": "Contract schemas for dataset partitions and splits."},
    {"dep_id": "DDEP-02", "name": "time_index_policy_source", "phase_ref": "Phase 137", "role": "Point-in-time chronological time index requirements."},
    {"dep_id": "DDEP-03", "name": "purged_split_policy_source", "phase_ref": "Phase 137", "role": "Embargo and purge requirements preventing leakage."},
]


def build_model_card_data_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card data dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in DATA_DEPENDENCY_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["status"] = "SATISFIED"
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_data_dependencies(df)
    return df, summary


def summarize_model_card_data_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card data dependencies."""
    return {
        "total_data_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
