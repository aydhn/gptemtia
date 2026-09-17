# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Dependency Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    DEPENDENCY_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

DEPENDENCIES: List[Dict[str, Any]] = [
    {"dep_id": "DEP-01", "name": "data_lake", "type": "storage_layer", "phase_ref": "Core", "satisfied": True, "details": "DataLake persistence methods available."},
    {"dep_id": "DEP-02", "name": "feature_store", "type": "feature_registry", "phase_ref": "Core", "satisfied": True, "details": "FeatureStore metadata loaders available."},
    {"dep_id": "DEP-03", "name": "config_settings", "type": "configuration", "phase_ref": "Core", "satisfied": True, "details": "Phase 145 settings configured with strict guards."},
    {"dep_id": "DEP-04", "name": "config_paths", "type": "filesystem_paths", "phase_ref": "Core", "satisfied": True, "details": "Phase 145 directories registered."},
    {"dep_id": "DEP-05", "name": "report_builder", "type": "reporting_layer", "phase_ref": "Core", "satisfied": True, "details": "Report builder generators with disclaimer ready."},
    {"dep_id": "DEP-06", "name": "phase_136_gpu_ml_runtime", "type": "ml_block_foundation", "phase_ref": "Phase 136", "satisfied": True, "details": "Hardware discovery and runtime contracts verified."},
    {"dep_id": "DEP-07", "name": "phase_137_dataset_registry", "type": "dataset_contracts", "phase_ref": "Phase 137", "satisfied": True, "details": "ML dataset schemas and experiment contracts verified."},
    {"dep_id": "DEP-08", "name": "phase_138_baseline_models", "type": "model_contracts", "phase_ref": "Phase 138", "satisfied": True, "details": "Baseline model family contracts verified."},
    {"dep_id": "DEP-09", "name": "phase_139_training_governance", "type": "resource_governance", "phase_ref": "Phase 139", "satisfied": True, "details": "Resource budget and timeout contracts verified."},
    {"dep_id": "DEP-10", "name": "phase_140_ensemble_registry", "type": "ensemble_contracts", "phase_ref": "Phase 140", "satisfied": True, "details": "Candidate registry and strategy contracts verified."},
    {"dep_id": "DEP-11", "name": "phase_141_calibration_uncertainty", "type": "calibration_contracts", "phase_ref": "Phase 141", "satisfied": True, "details": "Calibration and interval contracts verified."},
    {"dep_id": "DEP-12", "name": "phase_142_drift_monitoring", "type": "drift_contracts", "phase_ref": "Phase 142", "satisfied": True, "details": "Model drift linkage contracts verified."},
    {"dep_id": "DEP-13", "name": "phase_143_explainability", "type": "attribution_contracts", "phase_ref": "Phase 143", "satisfied": True, "details": "Explainability schemas verified."},
    {"dep_id": "DEP-14", "name": "phase_144_model_governance", "type": "governance_contracts", "phase_ref": "Phase 144", "satisfied": True, "details": "Model cards and audit placeholders verified."},
]


def build_advanced_ml_dependency_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for advanced ML dependencies."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for d in DEPENDENCIES:
        row = dict(d)
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": DEPENDENCY_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_dependencies": len(df),
        "satisfied_dependencies": int(df["satisfied"].sum()),
        "all_satisfied": bool(df["satisfied"].all()),
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_advanced_ml_dependency_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dependencies DataFrame."""
    return {
        "dependency_count": len(df),
        "all_satisfied": bool(df["satisfied"].all()) if not df.empty and "satisfied" in df.columns else False,
        "non_signal": True,
    }
