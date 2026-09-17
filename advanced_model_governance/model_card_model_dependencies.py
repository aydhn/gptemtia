# -*- coding: utf-8 -*-
"""Phase 144: Model Card Model Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

MODEL_DEPENDENCY_ITEMS: List[Dict[str, str]] = [
    {"mdep_id": "MDEP-01", "name": "baseline_model_contract_ref", "phase_ref": "Phase 138", "role": "Baseline linear and tree model contract interfaces."},
    {"mdep_id": "MDEP-02", "name": "candidate_model_contract_ref", "phase_ref": "Phase 140", "role": "Advanced candidate family specifications."},
    {"mdep_id": "MDEP-03", "name": "ensemble_model_contract_ref", "phase_ref": "Phase 140", "role": "Voting, blending, and stacking strategy contracts."},
]


def build_model_card_model_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card model dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in MODEL_DEPENDENCY_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["status"] = "SATISFIED"
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_model_dependencies(df)
    return df, summary


def summarize_model_card_model_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card model dependencies."""
    return {
        "total_model_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
