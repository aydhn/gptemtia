"""Phase 125: Feature Factor Acceptance Health Check.

Checks importability of all Phase 116-125 modules, DataLake, FeatureStore,
and the presence of operational scripts, tests, and documentation.
"""

import importlib
from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)

HEALTH_CHECKS = [
    {"check_id": "health_phase_116", "target": "advanced_feature_engine", "type": "module_import"},
    {"check_id": "health_phase_117", "target": "advanced_technical_indicators", "type": "module_import"},
    {"check_id": "health_phase_118", "target": "advanced_feature_grid", "type": "module_import"},
    {"check_id": "health_phase_119", "target": "advanced_cross_asset_alignment", "type": "module_import"},
    {"check_id": "health_phase_120", "target": "advanced_feature_fusion", "type": "module_import"},
    {"check_id": "health_phase_121", "target": "advanced_feature_validation", "type": "module_import"},
    {"check_id": "health_phase_122", "target": "advanced_factor_metadata", "type": "module_import"},
    {"check_id": "health_phase_123", "target": "advanced_feature_quality_drift", "type": "module_import"},
    {"check_id": "health_phase_124", "target": "advanced_feature_store_integration", "type": "module_import"},
    {"check_id": "health_phase_125", "target": "advanced_feature_factor_acceptance", "type": "module_import"},
    {"check_id": "health_datalake", "target": "data.storage.data_lake", "type": "storage_import"},
    {"check_id": "health_feature_store", "target": "ml.feature_store", "type": "storage_import"},
    {"check_id": "health_scripts", "target": "scripts", "type": "directory_exists"},
    {"check_id": "health_tests", "target": "tests", "type": "directory_exists"},
    {"check_id": "health_docs", "target": "docs", "type": "directory_exists"},
]


def build_feature_factor_acceptance_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute health checks across packages, storage, and core directories."""
    root = project_root or Path(__file__).resolve().parent.parent
    rows = []
    for item in HEALTH_CHECKS:
        target = item["target"]
        ctype = item["type"]
        status = "HEALTHY"
        details = "Check passed"
        passed = True

        if ctype in ("module_import", "storage_import"):
            try:
                importlib.import_module(target)
            except Exception as exc:
                status = "FAILED"
                details = f"Import error: {exc}"
                passed = False
        elif ctype == "directory_exists":
            p = root / target
            if not p.exists() or not p.is_dir():
                status = "FAILED"
                details = f"Directory not found: {target}"
                passed = False

        rows.append({
            "check_id": item["check_id"],
            "target": target,
            "type": ctype,
            "status": status,
            "passed": passed,
            "details": details,
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    all_healthy = bool(df["passed"].all())
    summary = {
        "health_status": "HEALTHY" if all_healthy else "UNHEALTHY",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "failed_checks": int((~df["passed"]).sum()),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_factor_acceptance_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check DataFrame."""
    all_pass = bool(df["passed"].all()) if "passed" in df.columns else False
    return {
        "overall_health": "HEALTHY" if all_pass else "UNHEALTHY",
        "total_checks": len(df),
        "all_passed": all_pass,
        "non_signal": True,
    }
