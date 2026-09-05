"""Phase 130: Regime Transition Health Check.

Performs offline environment, dependency, and module health inspection
for Phase 130 Regime Transition and Stability Analysis.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)


def build_regime_transition_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Inspect environment, code packages, data lake, feature store, and test readiness."""
    if profile is None:
        profile = get_default_regime_transition_profile()
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    checks = [
        {
            "check_item": "phase_129_advanced_market_behavior_diagnostics",
            "component": "upstream_package",
            "status": "PASS" if (project_root / "advanced_market_behavior_diagnostics").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "phase_128_advanced_regime_rule_free",
            "component": "upstream_package",
            "status": "PASS" if (project_root / "advanced_regime_rule_free").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "phase_127_advanced_regime_matrix",
            "component": "upstream_package",
            "status": "PASS" if (project_root / "advanced_regime_matrix").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "phase_126_advanced_regime_foundation",
            "component": "upstream_package",
            "status": "PASS" if (project_root / "advanced_regime_foundation").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "phase_125_advanced_feature_factor_acceptance",
            "component": "upstream_package",
            "status": "PASS" if (project_root / "advanced_feature_factor_acceptance").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "phase_124_advanced_feature_store_integration",
            "component": "upstream_package",
            "status": "PASS" if (project_root / "advanced_feature_store_integration").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "phase_123_advanced_feature_quality_drift",
            "component": "upstream_package",
            "status": "PASS" if (project_root / "advanced_feature_quality_drift").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "phase_121_advanced_feature_validation",
            "component": "upstream_package",
            "status": "PASS" if (project_root / "advanced_feature_validation").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "advanced_regime_transition_package",
            "component": "core_package",
            "status": "PASS" if (project_root / "advanced_regime_transition").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "data_lake_storage_layer",
            "component": "storage",
            "status": "PASS" if (project_root / "data" / "storage" / "data_lake.py").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "feature_store_layer",
            "component": "feature_store",
            "status": "PASS" if (project_root / "ml" / "feature_store.py").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "scripts_directory",
            "component": "scripts",
            "status": "PASS" if (project_root / "scripts").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "tests_directory",
            "component": "tests",
            "status": "PASS" if (project_root / "tests").exists() else "FAIL",
            "mandatory": True,
        },
        {
            "check_item": "docs_directory",
            "component": "docs",
            "status": "PASS" if (project_root / "docs").exists() else "FAIL",
            "mandatory": True,
        },
    ]

    df = pd.DataFrame(checks)
    summary = summarize_regime_transition_health(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_regime_transition_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health check results."""
    total = len(df)
    passed = int((df["status"] == "PASS").sum()) if not df.empty else 0
    is_healthy = total == passed
    return {
        "total_checks": total,
        "passed_checks": passed,
        "failed_checks": total - passed,
        "health_status": "HEALTHY" if is_healthy else "UNHEALTHY",
        "is_healthy": is_healthy,
        "non_signal": True,
        "zero_execution_clean": True,
    }
