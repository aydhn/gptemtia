"""Phase 132: Macro/Event/News Regime Health Check."""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)


def build_macro_event_news_regime_health_check(
    project_root: Path,
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify ecosystem health for Phase 132 macro/event/news context expansion."""
    p = profile or get_macro_event_news_regime_profile()

    checks = [
        ("phase_131_cross_asset_available", project_root / "advanced_cross_asset_regime_context"),
        ("phase_130_transition_available", project_root / "advanced_regime_transition"),
        ("phase_129_behavior_available", project_root / "advanced_market_behavior_diagnostics"),
        ("phase_128_rule_free_available", project_root / "advanced_regime_rule_free"),
        ("phase_127_matrix_available", project_root / "advanced_regime_matrix"),
        ("phase_126_foundation_available", project_root / "advanced_regime_foundation"),
        ("phase_124_store_available", project_root / "advanced_feature_store_integration"),
        ("phase_123_quality_available", project_root / "advanced_feature_quality_drift"),
        ("phase_121_validation_available", project_root / "advanced_feature_validation"),
        ("phase_120_fusion_available", project_root / "advanced_feature_fusion"),
        ("phase_132_module_available", project_root / "advanced_macro_event_news_regime"),
        ("datalake_storage_available", project_root / "data" / "storage" / "data_lake.py"),
        ("featurestore_available", project_root / "ml" / "feature_store.py"),
        ("scripts_directory_present", project_root / "scripts"),
        ("tests_directory_present", project_root / "tests"),
        ("docs_directory_present", project_root / "docs"),
    ]

    rows = []
    for check_name, path in checks:
        exists = path.exists()
        rows.append(
            {
                "check_name": check_name,
                "target_path": str(path),
                "exists": exists,
                "status": "PASS" if exists else "FAIL",
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    passed = int((df["status"] == "PASS").sum())
    failed = len(df) - passed
    overall_status = "HEALTHY" if failed == 0 else "UNHEALTHY"

    summary = {
        "overall_status": overall_status,
        "total_checks": len(df),
        "passed_checks": passed,
        "failed_checks": failed,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_regime_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for health check DataFrame."""
    passed = int((df["status"] == "PASS").sum()) if "status" in df.columns else 0
    return {
        "total_checks": len(df),
        "passed": passed,
        "failed": len(df) - passed,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
