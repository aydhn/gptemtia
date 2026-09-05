"""Phase 124 Feature Store Integration Health Checks."""

import importlib
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)


def build_feature_store_integration_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify system health, module availability, and Phase 116-123 prerequisite layers."""
    root = project_root or Path(".")
    prof = profile or get_default_feature_store_integration_profile()

    checks = [
        {"check_id": "CHK_001", "name": "phase_116_advanced_feature_engine", "type": "module", "target": "advanced_feature_engine"},
        {"check_id": "CHK_002", "name": "phase_117_advanced_technical_indicators", "type": "module", "target": "advanced_technical_indicators"},
        {"check_id": "CHK_003", "name": "phase_118_advanced_feature_grid", "type": "module", "target": "advanced_feature_grid"},
        {"check_id": "CHK_004", "name": "phase_119_advanced_cross_asset_alignment", "type": "module", "target": "advanced_cross_asset_alignment"},
        {"check_id": "CHK_005", "name": "phase_120_advanced_feature_fusion", "type": "module", "target": "advanced_feature_fusion"},
        {"check_id": "CHK_006", "name": "phase_121_advanced_feature_validation", "type": "module", "target": "advanced_feature_validation"},
        {"check_id": "CHK_007", "name": "phase_122_advanced_factor_metadata", "type": "module", "target": "advanced_factor_metadata"},
        {"check_id": "CHK_008", "name": "phase_123_advanced_feature_quality_drift", "type": "module", "target": "advanced_feature_quality_drift"},
        {"check_id": "CHK_009", "name": "feature_store_module", "type": "module", "target": "ml.feature_store"},
        {"check_id": "CHK_010", "name": "data_lake_module", "type": "module", "target": "data.storage.data_lake"},
        {"check_id": "CHK_011", "name": "config_settings", "type": "module", "target": "config.settings"},
        {"check_id": "CHK_012", "name": "config_paths", "type": "module", "target": "config.paths"},
    ]

    records = []
    for c in checks:
        status = "PASSED"
        details = "Module imported successfully."
        try:
            importlib.import_module(c["target"])
        except Exception as ex:
            status = "FAILED"
            details = f"Import error: {str(ex)}"

        records.append({
            "check_id": c["check_id"],
            "check_name": c["name"],
            "check_type": c["type"],
            "target": c["target"],
            "status": status,
            "details": details,
            "non_signal": True,
            "source_preserved": True,
        })

    df = pd.DataFrame(records)
    passed_count = len([r for r in records if r["status"] == "PASSED"])
    summary = {
        "status": "HEALTHY" if passed_count == len(records) else "DEGRADED",
        "total_checks": len(records),
        "passed_checks": passed_count,
        "failed_checks": len(records) - passed_count,
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
    }
    return df, summary


def summarize_feature_store_integration_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize health DataFrame."""
    if df.empty:
        return {"status": "UNKNOWN", "total_checks": 0, "passed_checks": 0}
    passed = int((df.get("status", pd.Series()) == "PASSED").sum())
    return {
        "status": "HEALTHY" if passed == len(df) else "DEGRADED",
        "total_checks": len(df),
        "passed_checks": passed,
        "failed_checks": len(df) - passed,
    }
