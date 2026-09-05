"""Phase 128: Regime Rule-Free Health Check.

Performs system health verification of upstream phase dependencies and Phase 128 components.
"""

from pathlib import Path
from typing import Dict, Tuple
import importlib
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

HEALTH_CHECKS = [
    {"subsystem": "phase_127_regime_matrix", "check_type": "module_import", "target": "advanced_regime_matrix.regime_matrix_config"},
    {"subsystem": "phase_126_regime_foundation", "check_type": "module_import", "target": "advanced_regime_foundation.regime_foundation_config"},
    {"subsystem": "phase_125_factor_acceptance", "check_type": "module_import", "target": "advanced_feature_factor_acceptance.feature_factor_acceptance_config"},
    {"subsystem": "phase_124_feature_store_integration", "check_type": "module_import", "target": "advanced_feature_store_integration.feature_store_integration_config"},
    {"subsystem": "phase_123_quality_drift", "check_type": "module_import", "target": "advanced_feature_quality_drift.feature_quality_drift_config"},
    {"subsystem": "phase_121_feature_validation", "check_type": "module_import", "target": "advanced_feature_validation.feature_validation_config"},
    {"subsystem": "phase_128_regime_rule_free", "check_type": "module_import", "target": "advanced_regime_rule_free.regime_rule_free_config"},
    {"subsystem": "data_lake", "check_type": "module_import", "target": "data.storage.data_lake"},
    {"subsystem": "feature_store", "check_type": "module_import", "target": "ml.feature_store"},
    {"subsystem": "scripts_directory", "check_type": "path_exists", "target": "scripts"},
    {"subsystem": "tests_directory", "check_type": "path_exists", "target": "tests"},
    {"subsystem": "docs_directory", "check_type": "path_exists", "target": "docs"},
]


def build_regime_rule_free_health_check(
    project_root: Path | None = None,
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Execute Phase 128 health checks and generate status report."""
    root = project_root or Path(__file__).resolve().parent.parent
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for c in HEALTH_CHECKS:
        subsystem = c["subsystem"]
        ctype = c["check_type"]
        target = c["target"]
        passed = False
        detail = ""

        try:
            if ctype == "module_import":
                importlib.import_module(target)
                passed = True
                detail = "Module imported successfully"
            elif ctype == "path_exists":
                p = root / target
                passed = p.exists()
                detail = f"Path exists: {p.exists()}"
        except Exception as e:
            passed = False
            detail = f"Error: {str(e)}"

        rows.append({
            "subsystem": subsystem,
            "check_type": ctype,
            "target": target,
            "status": "HEALTHY" if passed else "UNHEALTHY",
            "passed": passed,
            "details": detail,
            "current_phase": active_profile.current_phase,
            "next_phase": active_profile.next_phase,
        })

    df = pd.DataFrame(rows)
    summary = summarize_regime_rule_free_health(df)
    return df, summary


def summarize_regime_rule_free_health(df: pd.DataFrame) -> Dict:
    """Summarize health check results."""
    total = len(df)
    passed_count = int(df["passed"].sum()) if not df.empty else 0
    all_healthy = (total > 0) and (passed_count == total)

    return {
        "total_checks": total,
        "passed_checks": passed_count,
        "failed_checks": total - passed_count,
        "all_healthy": all_healthy,
        "health_status": "HEALTHY" if all_healthy else "DEGRADED",
    }
