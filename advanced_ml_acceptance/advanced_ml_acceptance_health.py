# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Health Check."""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    HEALTH_DOMAIN,
    ACCEPTANCE_READY,
)

HEALTH_ITEMS: List[Dict[str, Any]] = [
    {"check_id": "HLT-136", "component": "Phase 136 advanced_gpu_ml_runtime", "target_path": "advanced_gpu_ml_runtime", "item_type": "module"},
    {"check_id": "HLT-137", "component": "Phase 137 advanced_ml_dataset_registry", "target_path": "advanced_ml_dataset_registry", "item_type": "module"},
    {"check_id": "HLT-138", "component": "Phase 138 advanced_baseline_ml_models", "target_path": "advanced_baseline_ml_models", "item_type": "module"},
    {"check_id": "HLT-139", "component": "Phase 139 advanced_gpu_training_governance", "target_path": "advanced_gpu_training_governance", "item_type": "module"},
    {"check_id": "HLT-140", "component": "Phase 140 advanced_ensemble_model_registry", "target_path": "advanced_ensemble_model_registry", "item_type": "module"},
    {"check_id": "HLT-141", "component": "Phase 141 advanced_calibration_uncertainty", "target_path": "advanced_calibration_uncertainty", "item_type": "module"},
    {"check_id": "HLT-142", "component": "Phase 142 advanced_model_drift_monitoring", "target_path": "advanced_model_drift_monitoring", "item_type": "module"},
    {"check_id": "HLT-143", "component": "Phase 143 advanced_explainability_attribution", "target_path": "advanced_explainability_attribution", "item_type": "module"},
    {"check_id": "HLT-144", "component": "Phase 144 advanced_model_governance", "target_path": "advanced_model_governance", "item_type": "module"},
    {"check_id": "HLT-135", "component": "Phase 135 advanced_regime_acceptance", "target_path": "advanced_regime_acceptance", "item_type": "module"},
    {"check_id": "HLT-134", "component": "Phase 134 advanced_regime_featurestore_integration", "target_path": "advanced_regime_featurestore_integration", "item_type": "module"},
    {"check_id": "HLT-FS", "component": "FeatureStore", "target_path": "ml/feature_store.py", "item_type": "file"},
    {"check_id": "HLT-DL", "component": "DataLake", "target_path": "data/storage/data_lake.py", "item_type": "file"},
    {"check_id": "HLT-145", "component": "advanced_ml_acceptance", "target_path": "advanced_ml_acceptance", "item_type": "module"},
    {"check_id": "HLT-SCR", "component": "Scripts Directory", "target_path": "scripts", "item_type": "directory"},
    {"check_id": "HLT-TST", "component": "Tests Directory", "target_path": "tests", "item_type": "directory"},
    {"check_id": "HLT-DOC", "component": "Docs Directory", "target_path": "docs", "item_type": "directory"},
    {"check_id": "HLT-CFG", "component": "Config Directory", "target_path": "config", "item_type": "directory"},
]


def build_advanced_ml_acceptance_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify system health by checking for the presence of all required packages and files."""
    active = profile or get_advanced_ml_acceptance_profile()
    root = project_root or Path(".")

    records = []
    for item in HEALTH_ITEMS:
        target = root / item["target_path"]
        exists = target.exists()
        records.append({
            "check_id": item["check_id"],
            "component": item["component"],
            "target_path": item["target_path"],
            "item_type": item["item_type"],
            "exists": exists,
            "status": "HEALTHY" if exists else "MISSING",
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    all_healthy = bool(df["exists"].all())
    summary: Dict[str, Any] = {
        "domain": HEALTH_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_checks": len(df),
        "healthy_checks": int(df["exists"].sum()),
        "all_healthy": all_healthy,
        "non_signal": True,
        "status": "HEALTHY" if all_healthy else "UNHEALTHY",
    }
    return df, summary


def summarize_advanced_ml_acceptance_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    return {
        "check_count": len(df),
        "all_healthy": bool(df["exists"].all()) if not df.empty and "exists" in df.columns else False,
        "non_signal": True,
    }
