# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Validation Dependencies Registry.

Tracks upstream validation dependencies from Phases 121, 133, 134, 135, 136, and 137.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

VALIDATION_DEPENDENCIES = [
    {"source_phase": 121, "dependency_name": "feature_validation_no_lookahead", "status": "SATISFIED", "description": "Phase 121 no-lookahead and timestamp validation"},
    {"source_phase": 133, "dependency_name": "regime_validation_acceptance", "status": "SATISFIED", "description": "Phase 133 regime validation and no-lookahead acceptance"},
    {"source_phase": 134, "dependency_name": "regime_featurestore_validation", "status": "SATISFIED", "description": "Phase 134 validation-aware regime store contracts"},
    {"source_phase": 135, "dependency_name": "regime_acceptance_manifest", "status": "SATISFIED", "description": "Phase 135 regime block final acceptance"},
    {"source_phase": 136, "dependency_name": "gpu_ml_runtime_validation", "status": "SATISFIED", "description": "Phase 136 ML runtime foundation validation"},
    {"source_phase": 137, "dependency_name": "ml_dataset_contract_validation", "status": "SATISFIED", "description": "Phase 137 dataset contracts and experiment registry validation"},
]


def build_baseline_model_validation_dependency_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build validation dependency registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for dep in VALIDATION_DEPENDENCIES:
        rows.append({
            "source_phase": dep["source_phase"],
            "dependency_name": dep["dependency_name"],
            "status": dep["status"],
            "description": dep["description"],
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_validation_dependencies(df)
    return df, summary


def summarize_baseline_model_validation_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation dependencies."""
    all_satisfied = bool((df["status"] == "SATISFIED").all()) if not df.empty else True
    return {
        "total_dependencies": len(df),
        "all_satisfied": all_satisfied,
        "source_phases": sorted(df["source_phase"].unique().tolist()) if not df.empty else [],
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
