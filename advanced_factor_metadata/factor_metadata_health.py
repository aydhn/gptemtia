"""Phase 122 Factor Metadata Health Check.

Performs deterministic local system health checks verifying availability of
Phases 116–121 modules, scripts, tests, registries, and docs.
Strictly non-signal and research-only.
"""

from pathlib import Path
from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)

HEALTH_CHECKS: List[Dict[str, Any]] = [
    {
        "check_id": "health_phase_116_engine",
        "component": "advanced_feature_engine",
        "description": "Phase 116 Feature Engine Foundation availability.",
        "rel_path": "advanced_feature_engine",
    },
    {
        "check_id": "health_phase_117_indicators",
        "component": "advanced_technical_indicators",
        "description": "Phase 117 Technical Indicators Expansion availability.",
        "rel_path": "advanced_technical_indicators",
    },
    {
        "check_id": "health_phase_118_grid",
        "component": "advanced_feature_grid",
        "description": "Phase 118 Multi-Window Feature Grid availability.",
        "rel_path": "advanced_feature_grid",
    },
    {
        "check_id": "health_phase_119_alignment",
        "component": "advanced_cross_asset_alignment",
        "description": "Phase 119 Cross-Asset Feature Alignment availability.",
        "rel_path": "advanced_cross_asset_alignment",
    },
    {
        "check_id": "health_phase_120_fusion",
        "component": "advanced_feature_fusion",
        "description": "Phase 120 Macro/Calendar/News Feature Fusion availability.",
        "rel_path": "advanced_feature_fusion",
    },
    {
        "check_id": "health_phase_121_validation",
        "component": "advanced_feature_validation",
        "description": "Phase 121 Feature Validation and Lookahead Guard availability.",
        "rel_path": "advanced_feature_validation",
    },
    {
        "check_id": "health_phase_122_metadata",
        "component": "advanced_factor_metadata",
        "description": "Phase 122 Factor Metadata and Factor Families package.",
        "rel_path": "advanced_factor_metadata",
    },
    {
        "check_id": "health_phase_122_scripts",
        "component": "scripts.run_factor_metadata_status",
        "description": "Phase 122 Operational CLI scripts.",
        "rel_path": "scripts/run_factor_metadata_status.py",
    },
    {
        "check_id": "health_phase_122_tests",
        "component": "tests.test_factor_metadata_config",
        "description": "Phase 122 Unit and Contract Tests.",
        "rel_path": "tests/test_factor_metadata_config.py",
    },
    {
        "check_id": "health_phase_122_docs",
        "component": "docs.ARCHITECTURE",
        "description": "Documentation architecture ledger.",
        "rel_path": "docs/ARCHITECTURE.md",
    },
]


def build_factor_metadata_health_check(
    project_root: Path | None = None,
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute health checks and produce health DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()
    root = project_root or Path(".")

    results: List[Dict[str, Any]] = []
    for item in HEALTH_CHECKS:
        target_path = root / item["rel_path"]
        exists = target_path.exists()
        status = "PASS" if exists else "FAIL"

        results.append(
            {
                "check_id": item["check_id"],
                "component": item["component"],
                "description": item["description"],
                "path": str(target_path),
                "status": status,
                "passed": exists,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(results)
    passed_count = sum(1 for r in results if r["passed"])
    total_count = len(results)
    all_passed = passed_count == total_count

    summary = {
        "active_profile": active_profile.name,
        "health_status": "HEALTHY" if all_passed else "DEGRADED",
        "total_checks": total_count,
        "passed_checks": passed_count,
        "failed_checks": total_count - passed_count,
        "prerequisites_ready": all_passed,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
    }
    return df, summary


def summarize_factor_metadata_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor metadata health DataFrame."""
    total = len(df)
    passed = int((df["status"] == "PASS").sum()) if "status" in df else 0
    return {
        "total_checks": total,
        "passed_checks": passed,
        "failed_checks": total - passed,
        "is_healthy": passed == total,
        "non_signal": True,
    }
