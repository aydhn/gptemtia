"""Phase 131: Cross-Asset Regime Health Check.

Performs subsystem health diagnostics verifying directory presence, upstream phase integration,
DataLake/FeatureStore connectivity, scripts, tests, and documentation availability.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)


def build_cross_asset_regime_health_check(
    project_root: Optional[Path] = None,
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute subsystem health audit for Cross-Asset Regime Context layer."""
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    checks: List[Dict[str, Any]] = [
        {
            "subsystem": "phase_130_advanced_regime_transition",
            "required_path": project_root / "advanced_regime_transition",
            "description": "Phase 130 Regime Transition and Stability Analysis module availability",
        },
        {
            "subsystem": "phase_129_advanced_market_behavior_diagnostics",
            "required_path": project_root / "advanced_market_behavior_diagnostics",
            "description": "Phase 129 Market Behavior Diagnostics module availability",
        },
        {
            "subsystem": "phase_128_advanced_regime_rule_free",
            "required_path": project_root / "advanced_regime_rule_free",
            "description": "Phase 128 Regime Rule-Free Labeling module availability",
        },
        {
            "subsystem": "phase_127_advanced_regime_matrix",
            "required_path": project_root / "advanced_regime_matrix",
            "description": "Phase 127 Regime Feature Matrix module availability",
        },
        {
            "subsystem": "phase_126_advanced_regime_foundation",
            "required_path": project_root / "advanced_regime_foundation",
            "description": "Phase 126 Regime Classification Foundation module availability",
        },
        {
            "subsystem": "phase_124_advanced_feature_store_integration",
            "required_path": project_root / "advanced_feature_store_integration",
            "description": "Phase 124 Feature Store Integration module availability",
        },
        {
            "subsystem": "phase_123_advanced_feature_quality_drift",
            "required_path": project_root / "advanced_feature_quality_drift",
            "description": "Phase 123 Feature Quality and Drift module availability",
        },
        {
            "subsystem": "phase_121_advanced_feature_validation",
            "required_path": project_root / "advanced_feature_validation",
            "description": "Phase 121 Feature Validation and No-Lookahead module availability",
        },
        {
            "subsystem": "phase_119_advanced_cross_asset_alignment",
            "required_path": project_root / "advanced_cross_asset_alignment",
            "description": "Phase 119 Cross-Asset Alignment module availability",
        },
        {
            "subsystem": "advanced_cross_asset_regime_context",
            "required_path": project_root / "advanced_cross_asset_regime_context",
            "description": "Phase 131 Cross-Asset Regime Context core package availability",
        },
        {
            "subsystem": "data_lake",
            "required_path": project_root / "data" / "storage" / "data_lake.py",
            "description": "DataLake storage integration module availability",
        },
        {
            "subsystem": "feature_store",
            "required_path": project_root / "ml" / "feature_store.py",
            "description": "FeatureStore access module availability",
        },
        {
            "subsystem": "scripts",
            "required_path": project_root / "scripts",
            "description": "CLI operations script directory availability",
        },
        {
            "subsystem": "tests",
            "required_path": project_root / "tests",
            "description": "Pytest test directory availability",
        },
        {
            "subsystem": "docs",
            "required_path": project_root / "docs",
            "description": "Documentation directory availability",
        },
    ]

    rows = []
    for c in checks:
        exists = c["required_path"].exists()
        rows.append(
            {
                "subsystem": c["subsystem"],
                "path": str(c["required_path"]),
                "description": c["description"],
                "exists": exists,
                "status": "HEALTHY" if exists else "DEGRADED",
                "non_signal": True,
                "source_preserved": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_regime_health(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_regime_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize subsystem health check results."""
    total = len(df)
    healthy = int((df["status"] == "HEALTHY").sum()) if not df.empty else 0
    degraded = total - healthy
    overall_status = "HEALTHY" if degraded == 0 else "DEGRADED"

    return {
        "total_checks": total,
        "healthy_checks": healthy,
        "degraded_checks": degraded,
        "overall_status": overall_status,
        "all_healthy": degraded == 0,
        "non_signal": True,
        "source_preserved": True,
    }
