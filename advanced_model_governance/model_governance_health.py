# -*- coding: utf-8 -*-
"""Phase 144: Model Governance Health Check."""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)


def build_model_governance_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for system health check."""
    root = project_root or Path(".")
    prof = profile or get_model_governance_profile()

    checks = [
        {"component": "Phase 143 Explainability Attribution", "path": root / "advanced_explainability_attribution", "status": "AVAILABLE"},
        {"component": "Phase 142 Model Drift Monitoring", "path": root / "advanced_model_drift_monitoring", "status": "AVAILABLE"},
        {"component": "Phase 141 Calibration Uncertainty", "path": root / "advanced_calibration_uncertainty", "status": "AVAILABLE"},
        {"component": "Phase 140 Ensemble Model Registry", "path": root / "advanced_ensemble_model_registry", "status": "AVAILABLE"},
        {"component": "Phase 139 GPU Training Governance", "path": root / "advanced_gpu_training_governance", "status": "AVAILABLE"},
        {"component": "Phase 138 Baseline ML Models", "path": root / "advanced_baseline_ml_models", "status": "AVAILABLE"},
        {"component": "Phase 137 ML Dataset Registry", "path": root / "advanced_ml_dataset_registry", "status": "AVAILABLE"},
        {"component": "Phase 136 GPU ML Runtime", "path": root / "advanced_gpu_ml_runtime", "status": "AVAILABLE"},
        {"component": "Phase 135 Regime Acceptance", "path": root / "advanced_regime_acceptance", "status": "AVAILABLE"},
        {"component": "Phase 134 FeatureStore Integration", "path": root / "advanced_regime_featurestore_integration", "status": "AVAILABLE"},
        {"component": "FeatureStore Module", "path": root / "ml" / "feature_store.py", "status": "AVAILABLE"},
        {"component": "DataLake Module", "path": root / "data" / "storage" / "data_lake.py", "status": "AVAILABLE"},
        {"component": "Model Governance Package", "path": root / "advanced_model_governance", "status": "AVAILABLE"},
        {"component": "Scripts Directory", "path": root / "scripts", "status": "AVAILABLE"},
        {"component": "Tests Directory", "path": root / "tests", "status": "AVAILABLE"},
        {"component": "Docs Directory", "path": root / "docs", "status": "AVAILABLE"},
        {"component": "Config Directory", "path": root / "config", "status": "AVAILABLE"},
    ]

    records = []
    for c in checks:
        exists = Path(c["path"]).exists()
        records.append({
            "component": c["component"],
            "target_path": str(c["path"]),
            "exists": exists,
            "status": "HEALTHY" if exists else "MISSING",
            "phase": prof.current_phase,
        })

    df = pd.DataFrame(records)
    summary = summarize_model_governance_health(df)
    return df, summary


def summarize_model_governance_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check results."""
    all_healthy = bool(df["exists"].all())
    return {
        "total_checks": len(df),
        "all_components_healthy": all_healthy,
        "healthy_count": int(df["exists"].sum()),
        "status": "ALL_SYSTEMS_OPERATIONAL" if all_healthy else "WARNING_COMPONENTS_MISSING",
    }
