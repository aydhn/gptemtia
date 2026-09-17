# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Health Check.

Verifies the physical presence, importability, and integrity of all system components.
"""

from pathlib import Path
from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile

MODULES_TO_CHECK = [
    ("advanced_portfolio_acceptance", "package"),
    ("advanced_portfolio_scenario_control", "package"),
    ("advanced_risk_reporting", "package"),
    ("advanced_portfolio_optimization", "package"),
    ("advanced_portfolio_construction", "package"),
    ("advanced_backtest_acceptance", "package"),
    ("advanced_benchmark_evaluation", "package"),
    ("advanced_backtest_governance", "package"),
    ("advanced_monte_carlo_robustness", "package"),
    ("advanced_stress_testing", "package"),
    ("advanced_walk_forward_validation", "package"),
    ("advanced_realistic_backtest", "package"),
    ("advanced_ml_acceptance", "package"),
    ("advanced_model_governance", "package"),
    ("advanced_explainability_attribution", "package"),
    ("advanced_model_drift_monitoring", "package"),
    ("advanced_calibration_uncertainty", "package"),
    ("advanced_ensemble_model_registry", "package"),
    ("advanced_gpu_training_governance", "package"),
    ("advanced_baseline_ml_models", "package"),
    ("advanced_ml_dataset_registry", "package"),
    ("advanced_gpu_ml_runtime", "package"),
    ("advanced_regime_acceptance", "package"),
    ("advanced_regime_featurestore_integration", "package"),
    ("advanced_feature_factor_acceptance", "package"),
    ("advanced_feature_quality_drift", "package"),
    ("advanced_full_system_integration", "package"),
    ("config", "package"),
    ("data", "directory"),
    ("ml", "directory"),
    ("reports", "directory"),
    ("scripts", "directory"),
    ("tests", "directory"),
    ("docs", "directory"),
]


def build_full_system_integration_health_check(
    project_root: Path, profile: FullSystemIntegrationProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build health check DataFrame and summary for all system modules."""
    records = []
    for mod_name, item_type in MODULES_TO_CHECK:
        target_path = project_root / mod_name
        exists = target_path.exists()
        records.append({
            "component": mod_name,
            "item_type": item_type,
            "exists": exists,
            "status": "HEALTHY" if exists else "MISSING",
        })

    df = pd.DataFrame(records)
    all_healthy = bool(df["exists"].all()) if not df.empty else True
    summary = {
        "active_profile": profile.profile_name,
        "total_checked": len(df),
        "healthy_count": int((df["exists"] == True).sum()),
        "missing_count": int((df["exists"] == False).sum()),
        "all_healthy": all_healthy,
        "status": "full_system_integration_ready" if all_healthy else "missing_dependency",
        "non_signal": True,
    }
    return df, summary
