"""Phase 123 Feature Quality and Drift Health Check.

Performs health verification across upstream packages (Phase 116-122), internal modules,
scripts, tests, and documentation artifacts.
"""

from pathlib import Path
from typing import Any, Dict, List, Tuple
import importlib
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

HEALTH_CHECK_COMPONENTS: List[Dict[str, Any]] = [
    {
        "component_id": "pkg_phase_117_technical_indicators",
        "category": "upstream_package",
        "target": "advanced_technical_indicators",
        "description": "Verify Phase 117 Technical Indicators module availability.",
    },
    {
        "component_id": "pkg_phase_118_feature_grid",
        "category": "upstream_package",
        "target": "advanced_feature_grid",
        "description": "Verify Phase 118 Multi-Window Feature Grid module availability.",
    },
    {
        "component_id": "pkg_phase_119_cross_asset",
        "category": "upstream_package",
        "target": "advanced_cross_asset_alignment",
        "description": "Verify Phase 119 Cross-Asset Alignment module availability.",
    },
    {
        "component_id": "pkg_phase_120_feature_fusion",
        "category": "upstream_package",
        "target": "advanced_feature_fusion",
        "description": "Verify Phase 120 Feature Fusion module availability.",
    },
    {
        "component_id": "pkg_phase_121_feature_validation",
        "category": "upstream_package",
        "target": "advanced_feature_validation",
        "description": "Verify Phase 121 Feature Validation module availability.",
    },
    {
        "component_id": "pkg_phase_122_factor_metadata",
        "category": "upstream_package",
        "target": "advanced_factor_metadata",
        "description": "Verify Phase 122 Factor Metadata module availability.",
    },
    {
        "component_id": "pkg_phase_123_quality_drift",
        "category": "core_package",
        "target": "advanced_feature_quality_drift",
        "description": "Verify Phase 123 Feature Quality and Drift module availability.",
    },
]


def build_feature_quality_drift_health_check(
    project_root: Path | str | None = None,
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Verify health and importability of modules."""
    active_profile = profile or get_default_feature_quality_drift_profile()
    root = Path(project_root) if project_root else Path(".")

    records = []
    for comp in HEALTH_CHECK_COMPONENTS:
        target = comp["target"]
        try:
            mod = importlib.import_module(target)
            healthy = mod is not None
            details = "Module imported successfully"
        except Exception as e:
            healthy = False
            details = f"Import error: {str(e)}"

        records.append({
            "component_id": comp["component_id"],
            "category": comp["category"],
            "target": target,
            "description": comp["description"],
            "healthy": healthy,
            "status": "diagnostic_pass" if healthy else "diagnostic_fail",
            "details": details,
            "non_signal": True,
        })

    # Check documentation and paths
    docs_present = (root / "docs" / "ROADMAP.md").exists()
    records.append({
        "component_id": "doc_roadmap_present",
        "category": "documentation",
        "target": "docs/ROADMAP.md",
        "description": "Check if ROADMAP.md exists.",
        "healthy": docs_present,
        "status": "diagnostic_pass" if docs_present else "diagnostic_fail",
        "details": "Present" if docs_present else "Missing file",
        "non_signal": True,
    })

    df = pd.DataFrame(records)
    summary = summarize_feature_quality_drift_health(df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return df, summary


def summarize_feature_quality_drift_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from health check DataFrame."""
    if df.empty:
        return {
            "total_components": 0,
            "healthy_components": 0,
            "unhealthy_components": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_c = len(df)
    healthy_c = int(df["healthy"].sum()) if "healthy" in df.columns else 0
    unhealthy_c = total_c - healthy_c

    status = "diagnostic_pass" if unhealthy_c == 0 else "diagnostic_fail"

    return {
        "total_components": total_c,
        "healthy_components": healthy_c,
        "unhealthy_components": unhealthy_c,
        "status": status,
        "manual_review_required": unhealthy_c > 0,
    }
