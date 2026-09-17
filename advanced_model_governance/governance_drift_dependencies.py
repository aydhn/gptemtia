# -*- coding: utf-8 -*-
"""Phase 144: Governance Drift Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

DRIFT_DEP_SPECS: List[Dict[str, str]] = [
    {"dependency_name": "phase_142_model_drift_monitoring_contracts", "source": "Phase 142", "scope": "PSI, KS, Wasserstein statistical drift tests", "status": "SATISFIED"},
    {"dependency_name": "phase_142_feature_drift_linkage", "source": "Phase 142", "scope": "Data and feature drift linkage to FeatureStore", "status": "SATISFIED"},
    {"dependency_name": "phase_142_uncertainty_drift_contracts", "source": "Phase 142", "scope": "Uncertainty interval drift monitoring", "status": "SATISFIED"},
]


def build_governance_drift_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for drift dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in DRIFT_DEP_SPECS:
        row = dict(spec)
        row["phase"] = prof.current_phase
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_drift_dependencies(df)
    return df, summary


def summarize_governance_drift_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize drift dependencies."""
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
