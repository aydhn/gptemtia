# -*- coding: utf-8 -*-
"""Phase 141: Candidate Model Dependencies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CANDIDATE_MODEL_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_name": "candidate_tree_ensemble_contract_dep",
        "source_phase": "Phase 140",
        "target_component": "candidate_model_contracts",
        "description": "Tree ensemble candidate contract dependency.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "candidate_neural_contract_dep",
        "source_phase": "Phase 140",
        "target_component": "candidate_model_contracts",
        "description": "Neural candidate contract dependency.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "candidate_linear_contract_dep",
        "source_phase": "Phase 140",
        "target_component": "candidate_model_contracts",
        "description": "Linear candidate contract dependency.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "candidate_boosting_contract_dep",
        "source_phase": "Phase 140",
        "target_component": "candidate_model_contracts",
        "description": "Boosting candidate contract dependency.",
        "status": "SATISFIED",
    },
]


def build_calibration_candidate_model_dependency_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for candidate model dependencies."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CANDIDATE_MODEL_DEPENDENCIES:
        rows.append(
            {
                "dependency_name": item["dependency_name"],
                "source_phase": item["source_phase"],
                "target_component": item["target_component"],
                "description": item["description"],
                "status": item["status"],
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_candidate_model_dependencies(df)
    return df, summary


def summarize_calibration_candidate_model_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate model dependencies DataFrame."""
    return {
        "total_dependencies": len(df),
        "dependencies": df["dependency_name"].tolist() if not df.empty else [],
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
