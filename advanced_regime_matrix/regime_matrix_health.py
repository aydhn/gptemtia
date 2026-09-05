"""Phase 127: Regime Matrix Health Check.

Performs system diagnostic verification across upstream phases, storage layers,
scripts, tests, and documentation.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)


def build_regime_matrix_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute comprehensive subsystem health checks for Phase 127."""
    root = project_root or Path(__file__).resolve().parent.parent
    p = profile or get_default_regime_matrix_profile()

    checks: List[Dict[str, Any]] = [
        {
            "subsystem": "advanced_regime_foundation",
            "phase": 126,
            "check_type": "directory_and_module_presence",
            "path_target": "advanced_regime_foundation",
            "is_critical": True,
        },
        {
            "subsystem": "advanced_feature_factor_acceptance",
            "phase": 125,
            "check_type": "directory_and_module_presence",
            "path_target": "advanced_feature_factor_acceptance",
            "is_critical": True,
        },
        {
            "subsystem": "advanced_feature_store_integration",
            "phase": 124,
            "check_type": "directory_and_module_presence",
            "path_target": "advanced_feature_store_integration",
            "is_critical": True,
        },
        {
            "subsystem": "advanced_feature_quality_drift",
            "phase": 123,
            "check_type": "directory_and_module_presence",
            "path_target": "advanced_feature_quality_drift",
            "is_critical": True,
        },
        {
            "subsystem": "advanced_factor_metadata",
            "phase": 122,
            "check_type": "directory_and_module_presence",
            "path_target": "advanced_factor_metadata",
            "is_critical": True,
        },
        {
            "subsystem": "advanced_feature_validation",
            "phase": 121,
            "check_type": "directory_and_module_presence",
            "path_target": "advanced_feature_validation",
            "is_critical": True,
        },
        {
            "subsystem": "advanced_regime_matrix",
            "phase": 127,
            "check_type": "active_layer_presence",
            "path_target": "advanced_regime_matrix",
            "is_critical": True,
        },
        {
            "subsystem": "data_lake",
            "phase": 127,
            "check_type": "storage_lake_module",
            "path_target": "data/storage/data_lake.py",
            "is_critical": True,
        },
        {
            "subsystem": "feature_store",
            "phase": 127,
            "check_type": "ml_feature_store_module",
            "path_target": "ml/feature_store.py",
            "is_critical": True,
        },
        {
            "subsystem": "scripts_presence",
            "phase": 127,
            "check_type": "executable_cli_directory",
            "path_target": "scripts",
            "is_critical": True,
        },
        {
            "subsystem": "tests_presence",
            "phase": 127,
            "check_type": "test_suite_directory",
            "path_target": "tests",
            "is_critical": True,
        },
        {
            "subsystem": "docs_presence",
            "phase": 127,
            "check_type": "documentation_directory",
            "path_target": "docs",
            "is_critical": True,
        },
    ]

    rows = []
    for chk in checks:
        target_path = root / chk["path_target"]
        exists = target_path.exists()
        health_status = "HEALTHY" if exists else ("CRITICAL_MISSING" if chk["is_critical"] else "WARNING")

        rows.append(
            {
                "subsystem": chk["subsystem"],
                "phase": chk["phase"],
                "check_type": chk["check_type"],
                "path_target": chk["path_target"],
                "exists": exists,
                "health_status": health_status,
                "is_critical": chk["is_critical"],
                "non_signal": True,
                "source_preserved": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_health(df)
    return df, summary


def summarize_regime_matrix_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the health check DataFrame."""
    total_checks = len(df)
    healthy_count = int((df["health_status"] == "HEALTHY").sum()) if not df.empty else 0
    all_healthy = total_checks == healthy_count

    return {
        "total_checks": total_checks,
        "total_subsystems": total_checks,
        "healthy_count": healthy_count,
        "healthy_subsystems": healthy_count,
        "degraded_subsystems": total_checks - healthy_count,
        "all_healthy": all_healthy,
        "health_status": "HEALTHY" if all_healthy else "DEGRADED",
        "overall_health": "HEALTHY" if all_healthy else "DEGRADED",
        "model_training_executed": False,
        "non_signal": True,
        "source_preserved": True,
    }


run_regime_matrix_health_check = build_regime_matrix_health_check

