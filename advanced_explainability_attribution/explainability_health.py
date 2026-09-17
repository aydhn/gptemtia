# -*- coding: utf-8 -*-
"""Phase 143: Explainability System Health Checks."""

import os
from typing import Any, Dict, List, Optional
from config.settings import get_settings
from config.paths import (
    advanced_explainability_attribution_reports_dir,
    advanced_explainability_attribution_contracts_dir,
    advanced_explainability_attribution_placeholders_dir,
    advanced_explainability_attribution_safeguards_dir,
    advanced_explainability_attribution_metrics_dir,
)
from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)
from advanced_explainability_attribution.explainability_pipeline import (
    run_explainability_pipeline,
)


def check_explainability_health(
    profile: Optional[ExplainabilityProfile] = None,
) -> Dict[str, Any]:
    """Check health of the explainability layer and return diagnostic report."""
    prof = profile or get_explainability_profile()
    settings = get_settings()

    checks: List[Dict[str, Any]] = []

    # 1. Directory presence checks
    dirs_to_check = [
        ("reports_dir", advanced_explainability_attribution_reports_dir),
        ("contracts_dir", advanced_explainability_attribution_contracts_dir),
        ("placeholders_dir", advanced_explainability_attribution_placeholders_dir),
        ("safeguards_dir", advanced_explainability_attribution_safeguards_dir),
        ("metrics_dir", advanced_explainability_attribution_metrics_dir),
    ]
    for dname, dpath in dirs_to_check:
        exists = os.path.isdir(str(dpath))
        checks.append({
            "check": f"directory_{dname}",
            "passed": exists,
            "path": str(dpath),
        })

    # 2. Settings check
    checks.append({
        "check": "settings_enabled",
        "passed": bool(getattr(settings, "advanced_explainability_attribution_enabled", True)),
        "detail": "advanced_explainability_attribution_enabled",
    })
    checks.append({
        "check": "dry_run_invariant",
        "passed": bool(getattr(settings, "explainability_dry_run_default", True)),
        "detail": "explainability_dry_run_default",
    })
    checks.append({
        "check": "calculation_disabled_invariant",
        "passed": not bool(getattr(settings, "explainability_allow_explainability_calculation", False)),
        "detail": "explainability_allow_explainability_calculation is False",
    })

    # 3. Pipeline execution check
    pipeline_result = run_explainability_pipeline(prof)
    checks.append({
        "check": "pipeline_execution",
        "passed": bool(pipeline_result.get("success", False)),
        "detail": "dry_run pipeline executed without error",
    })
    checks.append({
        "check": "all_execution_disabled",
        "passed": bool(pipeline_result.get("safeguards_summary", {}).get("all_execution_disabled", False)),
        "detail": "all 9 disabled execution suites verified",
    })
    checks.append({
        "check": "zero_violations",
        "passed": bool(pipeline_result.get("safeguards_summary", {}).get("zero_violations", False)),
        "detail": "zero lookahead, metadata-only news, and source preservation violations",
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "status": "healthy" if all_passed else "unhealthy",
        "is_healthy": all_passed,
        "total_checks": len(checks),
        "passed_checks": sum(1 for c in checks if c["passed"]),
        "failed_checks": sum(1 for c in checks if not c["passed"]),
        "checks": checks,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
