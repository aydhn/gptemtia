# -*- coding: utf-8 -*-
"""Phase 141: Calibration Dataset Dependencies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

DATASET_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_name": "dataset_contract_commodity_fx_dep",
        "source_phase": "Phase 137",
        "target_component": "dataset_contracts",
        "description": "Commodity/FX temporal partition dataset contracts.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "dataset_contract_macro_event_dep",
        "source_phase": "Phase 137",
        "target_component": "dataset_contracts",
        "description": "Macro event partition dataset contracts.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "featurestore_catalog_dep",
        "source_phase": "Phase 134",
        "target_component": "feature_catalog",
        "description": "Validation-aware feature store catalog.",
        "status": "SATISFIED",
    },
]


def build_calibration_dataset_dependency_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for dataset dependencies."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in DATASET_DEPENDENCIES:
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
    summary = summarize_calibration_dataset_dependencies(df)
    return df, summary


def summarize_calibration_dataset_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dataset dependencies DataFrame."""
    return {
        "total_dependencies": len(df),
        "dependencies": df["dependency_name"].tolist() if not df.empty else [],
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
