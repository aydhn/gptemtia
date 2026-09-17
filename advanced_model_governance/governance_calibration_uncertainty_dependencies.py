# -*- coding: utf-8 -*-
"""Phase 144: Governance Calibration & Uncertainty Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

CALIBRATION_DEP_SPECS: List[Dict[str, str]] = [
    {"dependency_name": "phase_141_probability_calibration_contracts", "source": "Phase 141", "scope": "Platt scaling and isotonic calibration contracts", "status": "SATISFIED"},
    {"dependency_name": "phase_141_uncertainty_estimation_contracts", "source": "Phase 141", "scope": "Conformal and quantile uncertainty bounds", "status": "SATISFIED"},
    {"dependency_name": "phase_141_reliability_placeholders", "source": "Phase 141", "scope": "Reliability diagram and Brier score tracking", "status": "SATISFIED"},
]


def build_governance_calibration_uncertainty_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration & uncertainty dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in CALIBRATION_DEP_SPECS:
        row = dict(spec)
        row["phase"] = prof.current_phase
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_calibration_uncertainty_dependencies(df)
    return df, summary


def summarize_governance_calibration_uncertainty_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration & uncertainty dependencies."""
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
