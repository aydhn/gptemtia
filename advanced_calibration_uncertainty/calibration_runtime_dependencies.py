# -*- coding: utf-8 -*-
"""Phase 141: Calibration Runtime Dependencies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

RUNTIME_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_name": "gpu_ml_runtime_capability_dep",
        "source_phase": "Phase 136",
        "target_component": "runtime_discovery",
        "description": "Hardware discovery and ML runtime capability foundation.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "gpu_resource_governance_dep",
        "source_phase": "Phase 139",
        "target_component": "resource_governance",
        "description": "Memory budgeting, device selection, and CPU fallback governance.",
        "status": "SATISFIED",
    },
    {
        "dependency_name": "baseline_ml_model_contracts_dep",
        "source_phase": "Phase 138",
        "target_component": "baseline_models",
        "description": "Baseline model contracts and dry-run training harness.",
        "status": "SATISFIED",
    },
]


def build_calibration_runtime_dependency_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for runtime dependencies."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in RUNTIME_DEPENDENCIES:
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
    summary = summarize_calibration_runtime_dependencies(df)
    return df, summary


def summarize_calibration_runtime_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize runtime dependencies DataFrame."""
    return {
        "total_dependencies": len(df),
        "dependencies": df["dependency_name"].tolist() if not df.empty else [],
        "all_satisfied": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
