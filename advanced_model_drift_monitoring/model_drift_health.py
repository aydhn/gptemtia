"""Model Drift Monitoring Health Checks for Phase 142.

Performs deterministic diagnostic health checks across drift monitoring contracts,
directory paths, disabled execution enforcements, and upstream linkages.
"""

from __future__ import annotations

from typing import Any, Dict, List

from advanced_model_drift_monitoring.drift_execution_disabled import (
    build_all_drift_disabled_execution_items,
)
from advanced_model_drift_monitoring.model_drift_config import get_model_drift_profile
from advanced_model_drift_monitoring.model_drift_domain_registry import (
    build_model_drift_domain_registry,
)
from advanced_model_drift_monitoring.model_drift_profile_registry import (
    build_model_drift_profile_registry,
)


def run_model_drift_health_check() -> Dict[str, Any]:
    """Runs a comprehensive health check for Phase 142 drift monitoring subsystem."""
    checks: List[Dict[str, Any]] = []

    # 1. Profile Registry Check
    try:
        profiles_df, _ = build_model_drift_profile_registry()
        checks.append({
            "check": "profile_registry_integrity",
            "status": "passed",
            "details": f"Loaded {len(profiles_df)} profiles successfully.",
        })
    except Exception as e:
        checks.append({
            "check": "profile_registry_integrity",
            "status": "failed",
            "error": str(e),
        })

    # 2. Domain Registry Check
    try:
        domains_df, _ = build_model_drift_domain_registry()
        checks.append({
            "check": "domain_registry_integrity",
            "status": "passed",
            "details": f"Loaded {len(domains_df)} drift domains successfully.",
        })
    except Exception as e:
        checks.append({
            "check": "domain_registry_integrity",
            "status": "failed",
            "error": str(e),
        })

    # 3. Disabled Execution Safeguards Check
    try:
        disabled_items = build_all_drift_disabled_execution_items()
        all_disabled = all(item.is_disabled for item in disabled_items)
        checks.append({
            "check": "disabled_execution_safeguards",
            "status": "passed" if all_disabled else "failed",
            "details": f"{len(disabled_items)} safeguards verified disabled.",
        })
    except Exception as e:
        checks.append({
            "check": "disabled_execution_safeguards",
            "status": "failed",
            "error": str(e),
        })

    # 4. Default Profile Safety Invariants
    try:
        profile = get_model_drift_profile()
        invariants_met = (
            not profile.allow_live_drift_monitoring
            and not profile.allow_drift_metric_calculation
            and not profile.allow_drift_alerting
            and not profile.allow_drift_retraining_trigger
            and not profile.allow_drift_model_actions
            and not profile.allow_prediction_distribution_drift_execution
            and profile.enforce_non_executing_drift_monitoring
        )
        checks.append({
            "check": "profile_safety_invariants",
            "status": "passed" if invariants_met else "failed",
            "details": "All non-executing safety invariants verified in default profile.",
        })
    except Exception as e:
        checks.append({
            "check": "profile_safety_invariants",
            "status": "failed",
            "error": str(e),
        })

    all_passed = all(c["status"] == "passed" for c in checks)

    return {
        "subsystem": "advanced_model_drift_monitoring",
        "phase": 142,
        "overall_health": "HEALTHY" if all_passed else "DEGRADED",
        "total_checks": len(checks),
        "all_passed": all_passed,
        "checks": checks,
    }
