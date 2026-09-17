# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Health Check."""

import importlib
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

HEALTH_CHECK_COMPONENTS: List[Dict[str, str]] = [
    {"component": "Phase 140 advanced_ensemble_model_registry", "module": "advanced_ensemble_model_registry"},
    {"component": "Phase 139 advanced_gpu_training_governance", "module": "advanced_gpu_training_governance"},
    {"component": "Phase 138 advanced_baseline_ml_models", "module": "advanced_baseline_ml_models"},
    {"component": "Phase 137 advanced_ml_dataset_registry", "module": "advanced_ml_dataset_registry"},
    {"component": "Phase 136 advanced_gpu_ml_runtime", "module": "advanced_gpu_ml_runtime"},
    {"component": "Phase 135 advanced_regime_acceptance", "module": "advanced_regime_acceptance"},
    {"component": "Phase 134 advanced_regime_featurestore_integration", "module": "advanced_regime_featurestore_integration"},
    {"component": "FeatureStore", "module": "ml.feature_store"},
    {"component": "DataLake", "module": "data.storage.data_lake"},
    {"component": "advanced_calibration_uncertainty", "module": "advanced_calibration_uncertainty"},
    {"component": "config", "module": "config.settings"},
    {"component": "reports", "module": "reports.report_builder"},
]


def check_calibration_uncertainty_health(
    project_root: Optional[Path] = None,
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Dict[str, Any]:
    """Execute health checks and return consolidated summary."""
    df, summary = build_calibration_uncertainty_health_check(project_root, profile)
    return summary


def build_calibration_uncertainty_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for health check."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in HEALTH_CHECK_COMPONENTS:
        mod_name = item["module"]
        status = "HEALTHY"
        details = "Module importable and functional."
        try:
            importlib.import_module(mod_name)
        except Exception as e:
            status = "ERROR"
            details = f"Failed to import {mod_name}: {str(e)}"

        rows.append(
            {
                "component": item["component"],
                "module": mod_name,
                "status": status,
                "details": details,
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_health(df)
    return df, summary


def summarize_calibration_uncertainty_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    total = len(df)
    passed = int((df["status"] == "HEALTHY").sum()) if not df.empty else 0
    all_healthy = (passed == total) and total > 0
    return {
        "status": "HEALTHY" if all_healthy else "UNHEALTHY",
        "total_checks": total,
        "passed_checks": passed,
        "failed_checks": total - passed,
        "all_passed": all_healthy,
        "non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
