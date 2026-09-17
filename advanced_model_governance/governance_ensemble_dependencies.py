# -*- coding: utf-8 -*-
"""Phase 144: Governance Ensemble Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

ENSEMBLE_DEP_SPECS: List[Dict[str, str]] = [
    {"dependency_name": "phase_140_candidate_model_registry", "source": "Phase 140", "scope": "Candidate model contracts and families", "status": "SATISFIED"},
    {"dependency_name": "phase_140_ensemble_strategy_contracts", "source": "Phase 140", "scope": "Voting, blending, and stacking specifications", "status": "SATISFIED"},
    {"dependency_name": "phase_140_eligibility_gate_registry", "source": "Phase 140", "scope": "Eligibility validation checks", "status": "SATISFIED"},
]


def build_governance_ensemble_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for ensemble dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in ENSEMBLE_DEP_SPECS:
        row = dict(spec)
        row["phase"] = prof.current_phase
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_ensemble_dependencies(df)
    return df, summary


def summarize_governance_ensemble_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ensemble dependencies."""
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
