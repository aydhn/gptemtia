# -*- coding: utf-8 -*-
"""Phase 144: Governance Baseline Model Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

BASELINE_DEP_SPECS: List[Dict[str, str]] = [
    {"dependency_name": "phase_138_linear_baseline_contract", "source": "Phase 138", "model_family": "linear_ridge", "status": "SATISFIED"},
    {"dependency_name": "phase_138_tree_baseline_contract", "source": "Phase 138", "model_family": "random_forest_regressor", "status": "SATISFIED"},
    {"dependency_name": "phase_138_training_harness_disabled", "source": "Phase 138", "model_family": "all_baselines", "status": "SATISFIED"},
]


def build_governance_baseline_model_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for baseline model dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in BASELINE_DEP_SPECS:
        row = dict(spec)
        row["phase"] = prof.current_phase
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_baseline_model_dependencies(df)
    return df, summary


def summarize_governance_baseline_model_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline model dependencies."""
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
