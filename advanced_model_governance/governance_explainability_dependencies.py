# -*- coding: utf-8 -*-
"""Phase 144: Governance Explainability Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

EXPLAINABILITY_DEP_SPECS: List[Dict[str, str]] = [
    {"dependency_name": "phase_143_explainability_report_contracts", "source": "Phase 143", "scope": "Global and local XAI report templates", "status": "SATISFIED"},
    {"dependency_name": "phase_143_feature_attribution_contracts", "source": "Phase 143", "scope": "SHAP/LIME attribution contract specifications", "status": "SATISFIED"},
    {"dependency_name": "phase_143_xai_safeguards", "source": "Phase 143", "scope": "Zero model action and disabled execution evidence", "status": "SATISFIED"},
]


def build_governance_explainability_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for explainability dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in EXPLAINABILITY_DEP_SPECS:
        row = dict(spec)
        row["phase"] = prof.current_phase
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_explainability_dependencies(df)
    return df, summary


def summarize_governance_explainability_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability dependencies."""
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
