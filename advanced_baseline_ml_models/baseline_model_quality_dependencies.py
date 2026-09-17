# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Quality Dependencies Registry.

Tracks upstream quality dependencies and manual review blockers from
Phases 123, 124, 136, and 137.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

QUALITY_DEPENDENCIES = [
    {"source_phase": 123, "dependency_name": "feature_quality_drift_diagnostics", "status": "SATISFIED", "description": "Phase 123 feature quality and drift monitoring readiness"},
    {"source_phase": 124, "dependency_name": "feature_store_quality_metadata", "status": "SATISFIED", "description": "Phase 124 catalog quality scores and namespace integrity"},
    {"source_phase": 136, "dependency_name": "gpu_ml_runtime_readiness", "status": "SATISFIED", "description": "Phase 136 hardware capabilities and snapshot health"},
    {"source_phase": 137, "dependency_name": "ml_dataset_readiness_score", "status": "SATISFIED", "description": "Phase 137 dataset contract readiness compliance"},
    {"source_phase": 138, "dependency_name": "manual_review_blocker_check", "status": "SATISFIED", "description": "Phase 138 manual inspection blockers resolved"},
]


def build_baseline_model_quality_dependency_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build quality dependency registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for dep in QUALITY_DEPENDENCIES:
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
    summary = summarize_baseline_model_quality_dependencies(df)
    return df, summary


def summarize_baseline_model_quality_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize quality dependencies."""
    all_satisfied = bool((df["status"] == "SATISFIED").all()) if not df.empty else True
    return {
        "total_dependencies": len(df),
        "all_satisfied": all_satisfied,
        "source_phases": sorted(df["source_phase"].unique().tolist()) if not df.empty else [],
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
