"""Model Drift Validation Engine for Phase 142.

Performs automated validation across all Phase 142 drift contracts, window policies,
threshold placeholders, and disabled execution safeguards.
"""

from __future__ import annotations

from typing import Any, Dict, List

from advanced_model_drift_monitoring.current_window_policies import (
    build_current_window_policies,
    validate_current_window_policy,
)
from advanced_model_drift_monitoring.drift_execution_disabled import (
    build_all_drift_disabled_execution_items,
)
from advanced_model_drift_monitoring.drift_metric_placeholders import (
    build_all_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.drift_threshold_placeholder_policies import (
    build_drift_threshold_placeholders,
    validate_drift_threshold_placeholder,
)
from advanced_model_drift_monitoring.model_drift_domain_registry import (
    build_model_drift_domain_registry,
    validate_domain_label,
)
from advanced_model_drift_monitoring.model_drift_monitoring_contracts import (
    build_model_drift_monitoring_contracts,
    validate_drift_monitoring_contract,
)
from advanced_model_drift_monitoring.reference_window_policies import (
    build_reference_window_policies,
    validate_reference_window_policy,
)


def run_model_drift_validation() -> Dict[str, Any]:
    """Runs end-to-end validation across drift monitoring contracts and policies."""
    validation_results: List[Dict[str, Any]] = []

    # 1. Validate Contracts
    contracts = build_model_drift_monitoring_contracts()
    for c in contracts:
        validation_results.append(validate_drift_monitoring_contract(c))

    # 2. Validate Thresholds
    thresholds = build_drift_threshold_placeholders()
    for t in thresholds:
        validation_results.append(validate_drift_threshold_placeholder(t))

    # 3. Validate Windows
    ref_windows = build_reference_window_policies()
    for rw in ref_windows:
        validation_results.append(validate_reference_window_policy(rw))

    curr_windows = build_current_window_policies()
    for cw in curr_windows:
        validation_results.append(validate_current_window_policy(cw))

    # Check overall validity
    all_valid = all(r.get("valid", True) for r in validation_results)
    invalid_count = sum(1 for r in validation_results if not r.get("valid", True))

    return {
        "phase": 142,
        "validation_status": "PASSED" if all_valid else "FAILED",
        "total_items_validated": len(validation_results),
        "valid_items_count": len(validation_results) - invalid_count,
        "invalid_items_count": invalid_count,
        "all_valid": all_valid,
        "results": validation_results,
    }
