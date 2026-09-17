# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Health Check."""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_governance_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build health check verifying filesystem components and upstream module availability."""
    active_profile = profile or get_default_gpu_training_governance_profile()
    root = project_root or Path(__file__).resolve().parent.parent

    checks = [
        {"component": "Phase 138 advanced_baseline_ml_models", "path": root / "advanced_baseline_ml_models"},
        {"component": "Phase 137 advanced_ml_dataset_registry", "path": root / "advanced_ml_dataset_registry"},
        {"component": "Phase 136 advanced_gpu_ml_runtime", "path": root / "advanced_gpu_ml_runtime"},
        {"component": "Phase 135 advanced_regime_acceptance", "path": root / "data" / "lake" / "advanced_regime_acceptance"},
        {"component": "Phase 134 advanced_regime_featurestore_integration", "path": root / "data" / "lake" / "advanced_regime_featurestore_integration"},
        {"component": "FeatureStore", "path": root / "ml" / "feature_store.py"},
        {"component": "DataLake", "path": root / "data" / "storage" / "data_lake.py"},
        {"component": "advanced_gpu_training_governance", "path": root / "advanced_gpu_training_governance"},
        {"component": "scripts", "path": root / "scripts"},
        {"component": "tests", "path": root / "tests"},
        {"component": "docs", "path": root / "docs"},
        {"component": "config", "path": root / "config" / "settings.py"},
    ]

    rows = []
    for c in checks:
        exists = c["path"].exists()
        rows.append(
            {
                "component": c["component"],
                "path": str(c["path"]),
                "status": "HEALTHY" if exists else "MISSING",
                "exists": exists,
                "non_signal": True,
                "current_phase": 139,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_gpu_training_governance_health(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_governance_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    if df.empty:
        return {"total_checks": 0, "health_status": "UNKNOWN", "non_signal": True}
    all_healthy = bool((df["status"] == "HEALTHY").all())
    return {
        "total_checks": len(df),
        "healthy_count": int((df["status"] == "HEALTHY").sum()),
        "health_status": "SYSTEM_HEALTHY" if all_healthy else "DEGRADED",
        "all_healthy": all_healthy,
        "current_phase": 139,
        "non_signal": True,
    }
