"""Phase 126: Regime Foundation Health Check.

Performs verification of upstream modules, core storage layers, scripts, and tests.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)


def build_regime_foundation_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Inspect and report health status of all prerequisite subsystems."""
    active_profile = profile or get_default_regime_foundation_profile()
    root = project_root or Path(__file__).resolve().parent.parent

    checks: List[Dict[str, Any]] = [
        {
            "component": "advanced_feature_factor_acceptance",
            "check_item": "Phase 125 acceptance layer importable",
            "path": str(root / "advanced_feature_factor_acceptance"),
            "status": "HEALTHY" if (root / "advanced_feature_factor_acceptance").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "advanced_feature_store_integration",
            "check_item": "Phase 124 feature store integration available",
            "path": str(root / "advanced_feature_store_integration"),
            "status": "HEALTHY" if (root / "advanced_feature_store_integration").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "advanced_feature_quality_drift",
            "check_item": "Phase 123 feature quality & drift diagnostics available",
            "path": str(root / "advanced_feature_quality_drift"),
            "status": "HEALTHY" if (root / "advanced_feature_quality_drift").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "advanced_factor_metadata",
            "check_item": "Phase 122 factor metadata layer available",
            "path": str(root / "advanced_factor_metadata"),
            "status": "HEALTHY" if (root / "advanced_factor_metadata").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "advanced_feature_validation",
            "check_item": "Phase 121 feature validation guard available",
            "path": str(root / "advanced_feature_validation"),
            "status": "HEALTHY" if (root / "advanced_feature_validation").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "advanced_regime_foundation",
            "check_item": "Phase 126 regime foundation package available",
            "path": str(root / "advanced_regime_foundation"),
            "status": "HEALTHY" if (root / "advanced_regime_foundation").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "data_lake",
            "check_item": "DataLake storage module available",
            "path": str(root / "data" / "storage" / "data_lake.py"),
            "status": "HEALTHY" if (root / "data" / "storage" / "data_lake.py").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "feature_store",
            "check_item": "ML FeatureStore module available",
            "path": str(root / "ml" / "feature_store.py"),
            "status": "HEALTHY" if (root / "ml" / "feature_store.py").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "scripts",
            "check_item": "Scripts directory available",
            "path": str(root / "scripts"),
            "status": "HEALTHY" if (root / "scripts").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "tests",
            "check_item": "Tests directory available",
            "path": str(root / "tests"),
            "status": "HEALTHY" if (root / "tests").exists() else "UNHEALTHY",
            "non_signal": True,
        },
        {
            "component": "docs",
            "check_item": "Documentation directory available",
            "path": str(root / "docs"),
            "status": "HEALTHY" if (root / "docs").exists() else "UNHEALTHY",
            "non_signal": True,
        },
    ]

    df = pd.DataFrame(checks)
    healthy_count = len(df[df["status"] == "HEALTHY"])
    unhealthy_count = len(df[df["status"] == "UNHEALTHY"])

    summary = {
        "active_profile": active_profile.profile_name,
        "total_checks": len(df),
        "healthy_checks": healthy_count,
        "unhealthy_checks": unhealthy_count,
        "health_status": "HEALTHY" if unhealthy_count == 0 else "UNHEALTHY",
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_regime_foundation_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    return {
        "total_checks": len(df),
        "all_healthy": bool((df["status"] == "HEALTHY").all()) if "status" in df.columns else False,
        "non_signal": True,
    }
