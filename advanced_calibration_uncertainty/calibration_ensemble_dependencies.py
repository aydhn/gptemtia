# -*- coding: utf-8 -*-
"""Phase 141: Ensemble Dependencies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

ENSEMBLE_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_name": "voting_ensemble_strategy_dep",
        "source_phase": "Phase 140",
        "target_component": "ensemble_strategy_contracts",
        "description": "Voting ensemble strategy contract dependency.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "blending_ensemble_strategy_dep",
        "source_phase": "Phase 140",
        "target_component": "ensemble_strategy_contracts",
        "description": "Blending ensemble strategy contract dependency.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "stacking_ensemble_strategy_dep",
        "source_phase": "Phase 140",
        "target_component": "ensemble_strategy_contracts",
        "description": "Stacking ensemble strategy contract dependency.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "dynamic_weighting_strategy_dep",
        "source_phase": "Phase 140",
        "target_component": "ensemble_strategy_contracts",
        "description": "Dynamic weighting ensemble strategy contract dependency.",
        "status": "SATISFIED",
    },
]


def build_calibration_ensemble_dependency_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for ensemble dependencies."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in ENSEMBLE_DEPENDENCIES:
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
    summary = summarize_calibration_ensemble_dependencies(df)
    return df, summary


def summarize_calibration_ensemble_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ensemble dependencies DataFrame."""
    return {
        "total_dependencies": len(df),
        "dependencies": df["dependency_name"].tolist() if not df.empty else [],
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
