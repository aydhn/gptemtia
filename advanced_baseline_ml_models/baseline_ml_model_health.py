# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Health Check.

Checks repository readiness, upstream module availability (Phases 134-137),
feature store, data lake, scripts, and tests.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)


def build_baseline_ml_model_health_check(
    project_root: Optional[Any] = None,
    profile: Optional[BaselineMlModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build health check DataFrame and summary."""
    if isinstance(project_root, BaselineMlModelProfile):
        profile = project_root
        project_root = None
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent
    if profile is None:
        profile = get_default_baseline_ml_model_profile()


    checks = [
        ("Phase 137 advanced_ml_dataset_registry available", (project_root / "advanced_ml_dataset_registry").exists()),
        ("Phase 136 advanced_gpu_ml_runtime available", (project_root / "advanced_gpu_ml_runtime").exists()),
        ("Phase 135 advanced_regime_acceptance available", (project_root / "advanced_regime_acceptance").exists()),
        ("Phase 134 advanced_regime_featurestore_integration available", (project_root / "advanced_regime_featurestore_integration").exists()),
        ("FeatureStore available", (project_root / "ml" / "feature_store.py").exists()),
        ("DataLake available", (project_root / "data" / "storage" / "data_lake.py").exists()),
        ("advanced_baseline_ml_models available", (project_root / "advanced_baseline_ml_models").exists()),
        ("scripts directory present", (project_root / "scripts").exists()),
        ("tests directory present", (project_root / "tests").exists()),
        ("docs directory present", (project_root / "docs").exists()),
        ("config present", (project_root / "config" / "settings.py").exists()),
    ]

    rows = []
    for name, is_healthy in checks:
        rows.append({
            "check_item": name,
            "status": "HEALTHY" if is_healthy else "UNHEALTHY",
            "passed": is_healthy,
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_ml_model_health(df)
    return df, summary


def summarize_baseline_ml_model_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline ML model health DataFrame."""
    all_passed = bool(df["passed"].all()) if not df.empty else True
    return {
        "healthy_count": int((df["status"] == "HEALTHY").sum()) if not df.empty else 0,
        "unhealthy_count": int((df["status"] != "HEALTHY").sum()) if not df.empty else 0,
        "all_healthy": all_passed,
        "health_status": "SYSTEM_HEALTHY" if all_passed else "SYSTEM_DEGRADED",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }


run_baseline_ml_model_health_check = build_baseline_ml_model_health_check
